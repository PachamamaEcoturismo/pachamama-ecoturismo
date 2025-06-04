from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, session, g
import requests # For InfinityPay API call
import json # For creating the items JSON for InfinityPay
import urllib.parse # For URL encoding parameters
from src.models import db
from src.models.service import Service
from src.models.booking import Booking
from datetime import datetime
from flask_babel import gettext as _

main_bp = Blueprint("main", __name__)

# TODO: Move to config or environment variables
INFINITEPAY_HANDLE = "pachamama1234" # IMPORTANT: User needs to provide this
SITE_BASE_URL = "http://localhost:5000" # Adjust for production

@main_bp.before_request
def before_request():
    # Make language code available in templates
    g.lang_code = session.get('language', 'pt')

@main_bp.route("/change_language/<language>")
def change_language(language):
    if language in ['pt', 'en', 'es']:
        session['language'] = language
    
    # Redirect back to the referring page or home if not available
    return_to = request.referrer or url_for('main.index')
    return redirect(return_to)

@main_bp.route("/")
def index():
    return render_template("public/index.html")

@main_bp.route("/servicos")
def list_services():
    services = Service.query.filter_by(is_active=True).all()
    return render_template("public/services.html", services=services)

@main_bp.route("/servicos/<int:service_id>")
def service_detail(service_id):
    service = Service.query.get_or_404(service_id)
    return render_template("public/service_detail.html", service=service)

@main_bp.route("/reservar/<int:service_id>", methods=["GET", "POST"])
def book_service(service_id):
    service = Service.query.get_or_404(service_id)
    if request.method == "POST":
        customer_name = request.form.get("customer_name")
        customer_cpf = request.form.get("customer_cpf")
        customer_birth_date_str = request.form.get("customer_birth_date")
        customer_address = request.form.get("customer_address")
        customer_email = request.form.get("customer_email")
        customer_phone = request.form.get("customer_phone")
        start_date_str = request.form.get("start_date")
        end_date_str = request.form.get("end_date")
        num_adults = int(request.form.get("num_adults", 1))
        num_children = int(request.form.get("num_children", 0))

        if not all([customer_name, customer_cpf, customer_birth_date_str, customer_address, customer_email, start_date_str]):
            flash(_("Todos os campos obrigatórios devem ser preenchidos."), "danger")
            return render_template("public/booking_form.html", service=service)

        try:
            # Tenta primeiro o formato yyyy-mm-dd (padrão HTML5)
            try:
                start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            except ValueError:
                # Tenta o formato dd/mm/yyyy como alternativa
                start_date = datetime.strptime(start_date_str, "%d/%m/%Y")
                
            # Tenta primeiro o formato yyyy-mm-dd (padrão HTML5)
            try:
                customer_birth_date = datetime.strptime(customer_birth_date_str, "%Y-%m-%d").date()
            except ValueError:
                # Tenta o formato dd/mm/yyyy como alternativa
                customer_birth_date = datetime.strptime(customer_birth_date_str, "%d/%m/%Y").date()
                
            end_date = None
            if end_date_str:
                try:
                    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
                except ValueError:
                    end_date = datetime.strptime(end_date_str, "%d/%m/%Y")
        except ValueError:
            flash(_("Formato de data inválido. Use o formato AAAA-MM-DD ou DD/MM/AAAA."), "danger")
            return render_template("public/booking_form.html", service=service)

        total_price = service.price * num_adults
        if service.category == "hospedagem" and end_date and start_date:
            num_days = (end_date - start_date).days
            if num_days <= 0:
                flash(_("Data final deve ser após a data inicial."), "danger")
                return render_template("public/booking_form.html", service=service)
            total_price = service.price * num_adults * num_days

        new_booking = Booking(
            service_id=service.id,
            start_date=start_date,
            end_date=end_date,
            num_adults=num_adults,
            num_children=num_children,
            total_price=total_price,
            status="Pendente",
            customer_name=customer_name,
            customer_cpf=customer_cpf,
            customer_birth_date=customer_birth_date,
            customer_address=customer_address,
            customer_email=customer_email,
            customer_phone=customer_phone
        )
        db.session.add(new_booking)
        db.session.commit() # Commit to get the new_booking.id

        # Prepare for InfinityPay
        # IMPORTANT: User must configure their INFINITEPAY_HANDLE
        if INFINITEPAY_HANDLE == "SEU_HANDLE_INFINITEPAY":
            flash(_("Integração com pagamento não configurada pelo administrador."), "danger")
            # Log this issue for the admin
            current_app.logger.error("InfinityPay Handle não configurado.")
            return redirect(url_for("main.booking_confirmation", booking_id=new_booking.id))

        items_json = json.dumps([{"name": service.name, "price": int(total_price * 100), "quantity": 1}])
        order_nsu = str(new_booking.id) # Use booking ID as order_nsu
        redirect_url_infinity = url_for("main.payment_return", _external=True)
        
        params = {
            "items": items_json,
            "order_nsu": order_nsu,
            "redirect_url": redirect_url_infinity,
            "customer_name": customer_name,
            "customer_email": customer_email,
            # Add other customer details if desired and supported by InfinityPay link
        }
        
        infinity_pay_url_base = f"https://checkout.infinitepay.io/{INFINITEPAY_HANDLE}"
        infinity_pay_checkout_url = f"{infinity_pay_url_base}?{urllib.parse.urlencode(params)}"
        
        # Instead of redirecting to local confirmation, redirect to InfinityPay
        return redirect(infinity_pay_checkout_url)

    return render_template("public/booking_form.html", service=service)

@main_bp.route("/reserva/confirmacao_pendente/<int:booking_id>") # Renamed for clarity
def booking_confirmation(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    return render_template("public/booking_confirmation.html", booking=booking)

@main_bp.route("/reserva/pagamento/retorno")
def payment_return():
    # Parameters from InfinityPay
    order_nsu = request.args.get("order_nsu")
    transaction_id = request.args.get("transaction_id") # This is the NSU from InfinityPay
    invoice_id = request.args.get("invoice_id")
    # proof = request.args.get("proof")
    # payment_method_infinity = request.args.get("payment_method")

    if not order_nsu or not transaction_id or not invoice_id:
        flash(_("Retorno de pagamento inválido da InfinityPay."), "danger")
        return redirect(url_for("main.index"))

    booking = Booking.query.get(order_nsu) # order_nsu is our booking.id
    if not booking:
        flash(_("Reserva não encontrada para este retorno de pagamento."), "danger")
        return redirect(url_for("main.index"))

    if booking.status != "Pendente":
        flash(_("Esta reserva (ID: {}) já foi processada.").format(booking.id), "info")
        return redirect(url_for("main.booking_status_page", booking_id=booking.id)) # A new page to show final status

    # Verify payment with InfinityPay API
    # IMPORTANT: User must configure their INFINITEPAY_HANDLE
    if INFINITEPAY_HANDLE == "SEU_HANDLE_INFINITEPAY":
        flash(_("Erro na verificação: Integração com pagamento não configurada pelo administrador."), "danger")
        current_app.logger.error("InfinityPay Handle não configurado para verificação.")
        return redirect(url_for("main.booking_confirmation", booking_id=booking.id))
        
    verification_url = f"https://api.infinitepay.io/invoices/public/checkout/payment_check/{INFINITEPAY_HANDLE}"
    verification_params = {
        "handle": INFINITEPAY_HANDLE,
        "transaction_id": transaction_id,
        "invoice_id": invoice_id
    }

    try:
        response = requests.get(verification_url, params=verification_params, timeout=10)
        response.raise_for_status() # Raise an exception for HTTP errors
        payment_data = response.json()

        if payment_data.get("success") and payment_data.get("paid"):
            booking.status = "Confirmado"
            booking.payment_id = transaction_id # Store InfinityPay's transaction_id
            db.session.commit()
            flash(_("Pagamento confirmado e reserva efetivada com sucesso!"), "success")
            # TODO: Send confirmation email
            return redirect(url_for("main.booking_status_page", booking_id=booking.id))
        else:
            booking.status = "Falha no Pagamento"
            db.session.commit()
            flash(_("O pagamento não pôde ser confirmado. Status: {}. Por favor, tente novamente ou entre em contato.").format(payment_data), "danger")
            return redirect(url_for("main.booking_status_page", booking_id=booking.id))

    except requests.exceptions.RequestException as e:
        current_app.logger.error(f"Erro ao verificar pagamento com InfinityPay: {e}")
        flash(_("Ocorreu um erro ao verificar seu pagamento. Por favor, entre em contato conosco."), "danger")
        # Keep status as Pendente, or set to a specific error status
        return redirect(url_for("main.booking_confirmation", booking_id=booking.id))

@main_bp.route("/reserva/status/<int:booking_id>")
def booking_status_page(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    # This page will show the final status of the booking after payment attempt
    return render_template("public/booking_status.html", booking=booking)

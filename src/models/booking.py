from . import db
from datetime import datetime

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=True) # Pode ser nulo para serviços de um dia
    num_adults = db.Column(db.Integer, nullable=False, default=1)
    num_children = db.Column(db.Integer, nullable=False, default=0)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='Pendente') # Ex: Pendente, Confirmado, Cancelado, Concluído
    payment_id = db.Column(db.String(100), nullable=True) # ID da transação do InfinityPay
    customer_name = db.Column(db.String(150), nullable=False)
    customer_cpf = db.Column(db.String(14), nullable=False) # Formato XXX.XXX.XXX-XX
    customer_birth_date = db.Column(db.Date, nullable=False)
    customer_address = db.Column(db.Text, nullable=False)
    customer_email = db.Column(db.String(120), nullable=False)
    customer_phone = db.Column(db.String(20), nullable=True)
    additional_guest_details = db.Column(db.Text, nullable=True) # Para detalhes dos outros hóspedes, se necessário
    notes = db.Column(db.Text, nullable=True) # Observações adicionais
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relacionamento (user já está em Service.bookings via backref)
    # user = db.relationship('User', backref=db.backref('bookings', lazy=True))

    def __repr__(self):
        return f'<Booking {self.id} for Service {self.service_id} by User {self.user_id}>'

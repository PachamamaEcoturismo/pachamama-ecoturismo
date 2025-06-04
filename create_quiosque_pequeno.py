from src.models import db
from src.models.service import Service
from src.main import app

with app.app_context():
    # Criar o novo serviço Quiosque Pequeno
    quiosque_pequeno = Service(
        name='Quiosque Pequeno',
        description='O quisoque pequeno Pachamama possui churrasqueira, fogao a lenha, geladeira, mesa, cadeiras, bancos e rede, além de alguns utensilios, tais como, copos, talheres e pratos.',
        category='aluguel',
        price=150.00,
        price_description='diária + R$ 40,00 por pessoa',
        capacity=10,
        included_items='Churrasqueira, Fogão a lenha, Geladeira, Mesa, Cadeiras, Bancos, Rede, Utensílios básicos (copos, talheres, pratos)',
        additional_info='Observação: caso esteja acampado na área de camping, ou hospedado na cabana, não será cobrado adicional de 40,00 reais por pessoa para os hóspedes.',
        is_active=True
    )
    
    db.session.add(quiosque_pequeno)
    db.session.commit()
    
    print(f"Serviço Quiosque Pequeno criado com sucesso! ID: {quiosque_pequeno.id}")

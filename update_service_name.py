from src.models import db
from src.models.service import Service
from src.main import app

with app.app_context():
    # Buscar o serviço pelo nome atual
    service = Service.query.filter_by(name='Aluguel de Quiosque do Camping').first()
    
    if service:
        print(f"Serviço encontrado - ID: {service.id}, Nome atual: {service.name}, Categoria: {service.category}")
        
        # Atualizar o nome
        service.name = 'Quiosque Grande'
        db.session.commit()
        
        print(f"Nome atualizado para: {service.name}")
    else:
        print("Serviço 'Aluguel de Quiosque do Camping' não encontrado")

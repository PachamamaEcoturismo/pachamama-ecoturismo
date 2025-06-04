from . import db
from datetime import datetime

class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # Ex: 'hospedagem', 'passeio', 'expedicao', 'quiosque', 'experiencia'
    price = db.Column(db.Float, nullable=False)
    price_description = db.Column(db.String(100), nullable=True) # Ex: 'por pessoa', 'por dia por pessoa', 'valor único'
    duration = db.Column(db.String(100), nullable=True) # Ex: '2 horas', 'diária', '3 dias'
    capacity = db.Column(db.Integer, nullable=True) # Lotação máxima ou vagas
    included_items = db.Column(db.Text, nullable=True) # Itens inclusos, separados por vírgula ou similar
    what_to_bring = db.Column(db.Text, nullable=True) # O que levar, separado por vírgula ou similar
    additional_info = db.Column(db.Text, nullable=True) # Informações adicionais
    images_urls = db.Column(db.Text, nullable=True) # URLs das imagens, separadas por vírgula (temporário até ter o upload)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    bookings = db.relationship('Booking', backref='service', lazy=True)

    def __repr__(self):
        return f'<Service {self.name}>'

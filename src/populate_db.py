import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # DON'T CHANGE THIS !!!

from src.main import app, db
from src.models.service import Service
from src.models.user import User
from werkzeug.security import generate_password_hash

# Criar contexto de aplicação
with app.app_context():
    # Recriar todas as tabelas
    db.drop_all()
    db.create_all()
    
    # Criar usuário administrador
    admin = User(
        username="admin",
        email="admin@pachamama.com.br",
        password_hash=generate_password_hash("admin123"),
        is_admin=True
    )
    db.session.add(admin)
    
    # Criar serviços baseados nos textos fornecidos pelo cliente
    services = [
        Service(
            name="Passeio de Caiaque Pachamama",
            category="passeio",
            description="Venha conhecer as belezas naturais de Naviraí-MS com um surpreendente passeio de caiaque pelo rio Laranjaí. O rio Laranjaí não possui corredeiras e, por isso, o passeio de caiaque é de contemplação e pode ser feito por qualquer pessoa, inclusive por crianças.\n\nInformações adicionais: o horário de saída é às 8 da manhã, mínimo de 6 pessoas para a realização da atividade. O passeio tem cerca de duas horas de duração e, ao terminar, os participantes podem desfrutar da piscina em nossa sede.",
            price=150.00,
            price_description="por pessoa",
            duration="Aproximadamente 2 horas",
            capacity=15,
            included_items="- Transporte\n- Equipamentos\n- Colete salva-vidas\n- Lanche ao final do passeio",
            what_to_bring="- Repelente\n- Protetor solar\n- Roupa de banho\n- Toalha\n- Chapéu/boné",
            additional_info="Após o passeio, os participantes podem desfrutar da piscina em nossa sede."
        ),
        Service(
            name="Passeio de Caiaque no Parque Estadual das Várzeas do Rio Ivinhema",
            category="passeio",
            description="Passeio de caiaque maravilhoso, no Parque Estadual das Várzeas do Rio Ivinhema (PEVRI), uma das áreas de conservação mais preservadas do Mato Grosso do Sul. Uma experiência única de contato com a natureza em sua forma mais pura.",
            price=200.00,
            price_description="por pessoa",
            duration="Dia inteiro",
            capacity=10,
            included_items="- Transporte\n- Equipamentos\n- Colete salva-vidas\n- Alimentação durante o passeio",
            what_to_bring="- Repelente\n- Protetor solar\n- Roupa de banho\n- Toalha\n- Chapéu/boné\n- Binóculos (opcional para observação de aves)",
            additional_info="O Parque Estadual das Várzeas do Rio Ivinhema é uma área de conservação com rica biodiversidade. É comum avistar diversas espécies de aves e, com sorte, outros animais silvestres."
        ),
        Service(
            name="Hospedagem em Cabana",
            category="hospedagem",
            description="A cabana possui banheiro, ar condicionado, fogão, geladeira e utensílios necessários para o preparo de refeições. Também possui churrasqueira portátil e local para fogueira, além de ser um cantinho super aconchegante que convida à boa conversa e contemplação da natureza.\n\nOs hóspedes da cabana Pachamama também podem usufruir da piscina, espaço, trilhas e do uso dos caiaques no rio Laranjaí, com todos os equipamentos de segurança necessários.",
            price=150.00,
            price_description="por dia por pessoa",
            capacity=4,
            included_items="- Acesso à piscina\n- Uso de caiaques no rio Laranjaí (com equipamentos de segurança)\n- Acesso às trilhas",
            additional_info="Check-in: 13h00\nCheck-out: 12h00 do dia seguinte"
        ),
        Service(
            name="Hospedagem em Camping",
            category="hospedagem",
            description="O camping do Pachamama oferece núcleos nivelados (local plano) para armar as barracas, além de contar com energia elétrica, tomada e banheiro próximo, com chuveiro quente.\n\nCaso você não tenha barraca, o Pachamama possui barracas para alugar, com o valor adicional de R$ 40,00.",
            price=80.00,
            price_description="por dia por pessoa",
            capacity=20,
            included_items="- Acesso a banheiros com chuveiro quente\n- Energia elétrica\n- Tomadas",
            what_to_bring="- Barraca (ou alugar por R$ 40,00 adicionais)\n- Itens pessoais de camping",
            additional_info="Check-in: 13h00\nCheck-out: 17h00 do dia seguinte"
        ),
        Service(
            name="Aluguel de Quiosque do Camping",
            category="aluguel",
            description="O quiosque do camping Pachamama possui churrasqueira, fogão a lenha, geladeira, mesa, cadeiras, bancos e rede, além de alguns utensílios, tais como, copos, talheres e pratos.",
            price=150.00,
            price_description="diária",
            capacity=15,
            included_items="- Churrasqueira\n- Fogão a lenha\n- Geladeira\n- Mesa e cadeiras\n- Utensílios básicos (copos, talheres, pratos)",
            additional_info="Ideal para reuniões familiares, churrascos e confraternizações."
        )
    ]
    
    for service in services:
        db.session.add(service)
    
    # Commit das alterações
    db.session.commit()
    
    print("Banco de dados populado com sucesso!")
    print(f"Criado usuário admin: admin@pachamama.com.br / senha: admin123")
    print(f"Criados {len(services)} serviços")

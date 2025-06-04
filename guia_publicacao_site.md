# Guia de Publicação - Site Pachamama Ecoturismo

Este documento contém instruções detalhadas para a publicação do site Pachamama Ecoturismo em um servidor web.

## Estrutura do Projeto

O site Pachamama Ecoturismo é uma aplicação Flask com as seguintes características:
- Framework Flask (3.1.0)
- Banco de dados SQLite
- Sistema de internacionalização (PT, EN, ES)
- Painel administrativo
- Templates e arquivos estáticos

## Requisitos de Hospedagem

Para hospedar este site, você precisará de:

1. **Servidor com suporte a Python 3.8+**
2. **Suporte a WSGI** (Web Server Gateway Interface)
3. **Acesso SSH** para configuração e manutenção
4. **Pelo menos 512MB de RAM** para operação adequada
5. **Pelo menos 1GB de espaço em disco**

## Opções de Hospedagem Recomendadas

### 1. PythonAnywhere
- Plataforma especializada em hospedagem Python
- Configuração simples para aplicações Flask
- Painel de controle intuitivo
- Planos gratuitos disponíveis para testes

### 2. Heroku
- Plataforma como serviço (PaaS)
- Integração com Git para deploy
- Escalabilidade automática
- Bom para projetos em crescimento

### 3. DigitalOcean
- Servidores VPS (Virtual Private Server)
- Controle total sobre o ambiente
- Droplets pré-configurados para Python/Flask
- Mais flexibilidade, mas requer mais conhecimento técnico

### 4. AWS Elastic Beanstalk
- Serviço gerenciado da Amazon
- Escalabilidade robusta
- Bom para projetos que podem crescer rapidamente
- Interface de gerenciamento completa

## Preparação para Deploy

### 1. Ajustes no arquivo main.py

Antes de publicar, é necessário modificar o arquivo `main.py` para ambiente de produção:

```python
if __name__ == '__main__':
    # Modo de desenvolvimento
    # app.run(host='0.0.0.0', port=5000, debug=True)
    
    # Modo de produção
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### 2. Configuração do Banco de Dados

O site atualmente usa SQLite, que é adequado para sites com tráfego moderado. Para maior escala, considere migrar para MySQL ou PostgreSQL.

### 3. Arquivos Estáticos

Certifique-se de que todos os arquivos estáticos (imagens, CSS, JavaScript) estão na pasta `static` e são referenciados corretamente nos templates.

### 4. Variáveis de Ambiente

Para maior segurança, mova informações sensíveis para variáveis de ambiente:

```python
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY', 'chave_padrao_para_desenvolvimento')
```

## Processo de Deploy

### Usando PythonAnywhere (Recomendado para iniciantes)

1. Crie uma conta em pythonanywhere.com
2. Faça upload do pacote do projeto (ZIP)
3. Descompacte no servidor
4. Crie um ambiente virtual:
   ```
   mkvirtualenv --python=python3.8 pachamama_env
   ```
5. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
6. Configure um novo aplicativo web:
   - Framework: Flask
   - Python Version: 3.8
   - Path to WSGI file: /home/yourusername/pachamama_ecoturismo/wsgi.py
7. Edite o arquivo WSGI para apontar para sua aplicação

### Usando Heroku

1. Instale o Heroku CLI
2. Crie um arquivo `Procfile` na raiz do projeto:
   ```
   web: gunicorn wsgi:app
   ```
3. Adicione `gunicorn` ao requirements.txt
4. Crie um arquivo `wsgi.py` na raiz:
   ```python
   from src.main import app
   
   if __name__ == "__main__":
       app.run()
   ```
5. Inicialize um repositório Git:
   ```
   git init
   git add .
   git commit -m "Initial commit"
   ```
6. Crie e faça deploy no Heroku:
   ```
   heroku create pachamama-ecoturismo
   git push heroku master
   ```

## Domínio e DNS

Após configurar a hospedagem, você precisará:

1. Registrar um domínio (ex: pachamama-ecoturismo.com.br)
2. Configurar os registros DNS para apontar para seu servidor
3. Configurar HTTPS para segurança (muitos provedores oferecem Let's Encrypt gratuitamente)

## Manutenção

Após a publicação, lembre-se de:

1. Configurar backups regulares do banco de dados
2. Monitorar o desempenho do site
3. Manter as dependências atualizadas
4. Verificar regularmente os logs do servidor

## Suporte

Em caso de dúvidas ou problemas durante o processo de publicação, entre em contato com o suporte técnico.

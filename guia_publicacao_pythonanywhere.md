# Guia de Publicação no PythonAnywhere - Pachamama Ecoturismo

Este documento contém instruções detalhadas para publicar o site Pachamama Ecoturismo no PythonAnywhere e configurar o domínio pachamamanavirai.com.br.

## 1. Preparação do Pacote para Upload

Antes de fazer o upload para o PythonAnywhere, vamos preparar o pacote do projeto:

1. **Ajustar o arquivo main.py para produção**
   - Remover o modo debug
   - Garantir configurações seguras

2. **Criar arquivo WSGI para PythonAnywhere**
   - Este arquivo será necessário para a configuração no servidor

3. **Verificar requirements.txt**
   - Garantir que todas as dependências estão listadas

## 2. Criação de Conta no PythonAnywhere

1. Acesse [pythonanywhere.com](https://www.pythonanywhere.com/)
2. Clique em "Pricing and signup"
3. Escolha o plano "Hacker" (ou superior, dependendo das necessidades)
4. Complete o processo de registro
5. Faça login na sua nova conta

## 3. Upload do Projeto

### Via Interface Web:
1. No painel do PythonAnywhere, clique em "Files"
2. Crie uma nova pasta: `mkdir pachamama_ecoturismo`
3. Navegue para a pasta criada
4. Clique em "Upload a file" para cada arquivo do projeto
   - Alternativa: Compacte o projeto em um arquivo ZIP e faça upload do ZIP

### Via Git (alternativa mais eficiente):
1. No painel do PythonAnywhere, abra um console Bash
2. Execute:
   ```bash
   git clone https://github.com/seu-usuario/pachamama_ecoturismo.git
   ```
   (Substitua pela URL do seu repositório, se disponível)

## 4. Configuração do Ambiente Virtual

1. No painel do PythonAnywhere, abra um console Bash
2. Execute os seguintes comandos:
   ```bash
   mkvirtualenv --python=python3.8 pachamama_env
   cd ~/pachamama_ecoturismo
   pip install -r requirements.txt
   ```
3. Verifique se todas as dependências foram instaladas corretamente

## 5. Configuração da Aplicação Web

1. No painel do PythonAnywhere, clique em "Web"
2. Clique em "Add a new web app"
3. Escolha o domínio temporário oferecido (você poderá mudar para seu domínio personalizado depois)
4. Na tela "Select a Python Web framework", escolha "Flask"
5. Selecione a versão Python 3.8
6. No campo "Path to your Flask app", insira o caminho para o arquivo principal:
   ```
   /home/seuusuario/pachamama_ecoturismo/src/main.py
   ```
7. Clique em "Next" para concluir o assistente

## 6. Configuração do Arquivo WSGI

1. No painel do PythonAnywhere, clique em "Web"
2. Procure por "WSGI configuration file" e clique no link para editar
3. Substitua o conteúdo pelo seguinte:

```python
import sys
import os

# Adicionar o diretório do projeto ao path
path = '/home/seuusuario/pachamama_ecoturismo'
if path not in sys.path:
    sys.path.append(path)

# Importar a aplicação Flask
from src.main import app as application

# Configurações de produção
application.config['DEBUG'] = False
application.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'chave_segura_para_producao')
```

4. Salve o arquivo

## 7. Configuração de Variáveis de Ambiente

1. No painel do PythonAnywhere, clique em "Web"
2. Procure por "Environment variables" e adicione:
   - `SECRET_KEY`: uma chave secreta longa e aleatória
   - Outras variáveis de ambiente necessárias para o projeto

## 8. Configuração de Arquivos Estáticos

1. No painel do PythonAnywhere, clique em "Web"
2. Procure por "Static files"
3. Adicione uma entrada:
   - URL: `/static/`
   - Directory: `/home/seuusuario/pachamama_ecoturismo/src/static/`

## 9. Reiniciar a Aplicação

1. No painel do PythonAnywhere, clique em "Web"
2. Clique no botão "Reload" para reiniciar a aplicação
3. Verifique se o site está funcionando no domínio temporário fornecido

## 10. Registro do Domínio

1. Acesse [registro.br](https://registro.br/)
2. Pesquise por "pachamamanavirai.com.br" para verificar disponibilidade
3. Complete o processo de registro:
   - Forneça informações de contato
   - Realize o pagamento (aproximadamente R$40/ano)
   - Aguarde a confirmação do registro (pode levar algumas horas)

## 11. Configuração do Domínio no PythonAnywhere

1. No painel do PythonAnywhere, clique em "Web"
2. Procure por "Add a new domain"
3. Digite seu domínio: `pachamamanavirai.com.br`
4. Siga as instruções para verificação de propriedade

## 12. Configuração DNS

1. No painel do Registro.br, acesse as configurações de DNS do seu domínio
2. Adicione os seguintes registros:
   - Tipo: CNAME
   - Nome: www
   - Valor: seu-usuario.pythonanywhere.com
   (Substitua "seu-usuario" pelo seu nome de usuário no PythonAnywhere)

3. Para o domínio raiz (sem www), adicione:
   - Tipo: A
   - Nome: @
   - Valor: Endereço IP fornecido pelo PythonAnywhere

## 13. Configuração HTTPS

1. No painel do PythonAnywhere, clique em "Web"
2. Procure por "HTTPS/SSL" na seção do seu domínio personalizado
3. Clique em "Enable HTTPS" para gerar um certificado Let's Encrypt gratuito
4. Aguarde a configuração do certificado (pode levar alguns minutos)

## 14. Teste Final

1. Acesse seu site pelo domínio personalizado: `https://pachamamanavirai.com.br`
2. Verifique se todas as páginas estão carregando corretamente
3. Teste o painel administrativo
4. Verifique se as imagens e arquivos estáticos estão sendo exibidos
5. Teste a funcionalidade de internacionalização

## 15. Manutenção Contínua

1. Configure backups regulares do banco de dados
2. Monitore o desempenho do site
3. Mantenha as dependências atualizadas
4. Verifique regularmente os logs do servidor

## Suporte

Em caso de dúvidas ou problemas durante o processo de publicação, entre em contato com o suporte técnico.

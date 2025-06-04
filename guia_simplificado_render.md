# Guia Simplificado: Publicação do Site Pachamama Ecoturismo no Render.com

Este guia simplificado explica como publicar o site Pachamama Ecoturismo no Render.com usando o pacote otimizado que preparamos para você.

## Passo 1: Criar uma Conta no Render.com

1. Acesse [render.com](https://render.com/)
2. Clique em "Sign Up" no canto superior direito
3. Recomendamos usar a opção "Continue with GitHub" para facilitar a conexão

## Passo 2: Criar um Repositório no GitHub

1. Acesse [github.com](https://github.com) e faça login
2. Clique no botão "+" no canto superior direito e selecione "New repository"
3. Nome: `pachamama-ecoturismo`
4. Visibilidade: "Public"
5. Clique em "Create repository"

## Passo 3: Enviar o Pacote para o GitHub

1. Descompacte o arquivo `pacote_render.zip` em seu computador
2. Abra o terminal ou prompt de comando
3. Navegue até a pasta descompactada:
   ```
   cd caminho/para/pacote_render
   ```
4. Execute os seguintes comandos:
   ```
   git init
   git add .
   git commit -m "Versão inicial do site Pachamama Ecoturismo"
   git branch -M main
   git remote add origin https://github.com/seu-usuario/pachamama-ecoturismo.git
   git push -u origin main
   ```

## Passo 4: Criar o Serviço Web no Render.com

1. No Dashboard do Render, clique em "New +" e selecione "Web Service"
2. Conecte ao GitHub e selecione o repositório `pachamama-ecoturismo`
3. Configure o serviço:
   - Nome: `pachamama-ecoturismo`
   - Região: `Ohio (US East)` (ou a mais próxima de você)
   - Branch: `main`
   - Runtime: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn src.main:app`
   - Instance Type: `Free`
4. Clique em "Create Web Service"

## Passo 5: Configurar Variáveis de Ambiente

1. Na página do serviço, vá para a aba "Environment"
2. Adicione as seguintes variáveis:
   - `SECRET_KEY`: `sua-chave-secreta-aqui` (use qualquer texto longo e aleatório)
   - `FLASK_ENV`: `production`
3. Clique em "Save Changes"

## Passo 6: Testar o Site

1. Aguarde o deploy (acompanhe na aba "Logs")
2. Quando concluído, acesse a URL fornecida (ex: `https://pachamama-ecoturismo.onrender.com`)
3. Teste o painel administrativo em `/admin`

## Observações Importantes

- O pacote já está otimizado para o Render.com com todas as configurações necessárias
- O site "adormece" após 15 minutos sem tráfego no plano gratuito
- Para evitar hibernação, configure um serviço como UptimeRobot para "pingar" o site a cada 5 minutos
- Para atualizar o site, faça as alterações localmente, commit e push para o GitHub

## Solução de Problemas

Se o site não carregar após o deploy:
1. Verifique os logs no Render.com (aba "Logs")
2. Certifique-se de que as variáveis de ambiente estão configuradas corretamente
3. Verifique se o repositório no GitHub contém todos os arquivos do pacote

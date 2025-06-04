mkdir -p translations/en/LC_MESSAGES translations/es/LC_MESSAGES

# Extrair strings para tradução
pybabel extract -F babel.cfg -o messages.pot .

# Inicializar arquivos de tradução para inglês e espanhol
pybabel init -i messages.pot -d translations -l en
pybabel init -i messages.pot -d translations -l es

# Editar os arquivos .po em translations/en/LC_MESSAGES/messages.po e translations/es/LC_MESSAGES/messages.po
# para adicionar as traduções

# Compilar os arquivos de tradução
pybabel compile -d translations

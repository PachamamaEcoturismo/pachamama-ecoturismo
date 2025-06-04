# Guia de Internacionalização - Pachamama Ecoturismo

Este documento explica como o sistema multilíngue do site Pachamama Ecoturismo foi implementado e como gerenciar as traduções em português, inglês e espanhol.

## Visão Geral

O site Pachamama Ecoturismo agora suporta três idiomas:
- Português (padrão)
- Inglês
- Espanhol

A implementação utiliza Flask-Babel para gerenciar as traduções e permitir que os visitantes alternem facilmente entre os idiomas disponíveis.

## Estrutura do Sistema Multilíngue

### Arquivos e Diretórios Principais

- **babel.cfg**: Arquivo de configuração que define quais arquivos devem ser analisados para extração de strings traduzíveis.
- **babel_config.py**: Configurações do Flask-Babel para detecção de idioma e localização.
- **translations/**: Diretório que contém as traduções para cada idioma:
  - **en/LC_MESSAGES/**: Traduções para inglês
  - **es/LC_MESSAGES/**: Traduções para espanhol
  - Cada pasta contém arquivos `.po` (editáveis) e `.mo` (compilados)

### Como Funciona

1. O sistema detecta o idioma preferido do usuário com base na seleção explícita (botões PT/EN/ES)
2. A seleção de idioma é armazenada na sessão do usuário para persistir durante a navegação
3. Todos os textos marcados para tradução são exibidos no idioma selecionado
4. O idioma padrão é português (pt) quando nenhuma seleção é feita

## Como Gerenciar Traduções

### Adicionar Novas Strings para Tradução

Quando você adicionar novos textos ao site, marque-os para tradução usando a função `_()`:

```html
<!-- Em templates HTML -->
<h1>{{ _('Título em português') }}</h1>
<p>{{ _('Texto em português que será traduzido') }}</p>
```

```python
# Em arquivos Python
from flask_babel import gettext as _

@app.route('/exemplo')
def exemplo():
    mensagem = _('Esta mensagem será traduzida')
    return render_template('exemplo.html', mensagem=mensagem)
```

### Atualizar Arquivos de Tradução

Quando novos textos forem adicionados ao site, você precisará atualizar os arquivos de tradução:

1. **Extrair novas strings**:
   ```bash
   pybabel extract -F babel.cfg -o messages.pot .
   ```

2. **Atualizar arquivos de tradução existentes**:
   ```bash
   pybabel update -i messages.pot -d translations
   ```

3. **Editar as traduções**:
   Abra os arquivos `.po` em `translations/en/LC_MESSAGES/messages.po` e `translations/es/LC_MESSAGES/messages.po` e adicione as traduções para as novas strings.

4. **Compilar as traduções**:
   ```bash
   pybabel compile -d translations
   ```

### Adicionar um Novo Idioma

Para adicionar suporte a um novo idioma (por exemplo, francês):

1. **Inicializar arquivos de tradução para o novo idioma**:
   ```bash
   pybabel init -i messages.pot -d translations -l fr
   ```

2. **Editar o arquivo de tradução**:
   Edite `translations/fr/LC_MESSAGES/messages.po` com as traduções para francês.

3. **Compilar as traduções**:
   ```bash
   pybabel compile -d translations
   ```

4. **Adicionar o idioma ao seletor**:
   Edite o arquivo `src/templates/public/base.html` para adicionar o novo idioma ao seletor.

## Boas Práticas

1. **Mantenha as traduções consistentes**: Use os mesmos termos para conceitos similares em todos os idiomas.
2. **Teste após atualizar traduções**: Verifique se todas as páginas estão exibindo corretamente os textos traduzidos.
3. **Considere o contexto cultural**: Algumas expressões podem precisar de adaptação cultural, não apenas tradução literal.
4. **Mantenha os arquivos de tradução organizados**: Adicione comentários nos arquivos `.po` para explicar o contexto quando necessário.
5. **Faça backup dos arquivos de tradução**: Antes de fazer grandes alterações, crie cópias de segurança.

## Solução de Problemas

### Textos não estão sendo traduzidos

- Verifique se o texto está envolvido pela função `_()` no código
- Certifique-se de que os arquivos de tradução foram compilados (`pybabel compile -d translations`)
- Verifique se a tradução existe no arquivo `.po` correspondente

### Erros ao compilar traduções

- Verifique a sintaxe dos arquivos `.po`
- Certifique-se de que não há caracteres especiais ou formatação incorreta

### Problemas com a detecção de idioma

- Verifique se a sessão está funcionando corretamente
- Teste limpar os cookies do navegador e selecionar o idioma novamente

## Conclusão

O sistema multilíngue implementado no site Pachamama Ecoturismo permite uma experiência personalizada para visitantes de diferentes nacionalidades. Com a manutenção adequada das traduções, o site continuará acessível e amigável para um público internacional.

Para qualquer dúvida adicional ou suporte técnico, entre em contato com a equipe de desenvolvimento.

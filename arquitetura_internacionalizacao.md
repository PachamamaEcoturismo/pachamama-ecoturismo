# Arquitetura de Internacionalização - Pachamama Ecoturismo

## Visão Geral

Este documento descreve a arquitetura de internacionalização para o site Pachamama Ecoturismo, permitindo suporte a três idiomas: português (padrão), inglês e espanhol.

## Componentes Principais

### 1. Gerenciamento de Idiomas (Flask-Babel)

- **Detecção de idioma**: Implementada em ordem de prioridade:
  1. Parâmetro de sessão (`session['language']`)
  2. Parâmetro de URL (`?lang=en`)
  3. Cabeçalho HTTP Accept-Language
  4. Padrão: português ('pt')

- **Configuração do Babel**:
  - Idioma padrão: português ('pt')
  - Idiomas suportados: português ('pt'), inglês ('en'), espanhol ('es')
  - Diretório de traduções: '/translations'

### 2. Estrutura de Arquivos de Tradução

```
/translations
  /en
    /LC_MESSAGES
      messages.po
      messages.mo
  /es
    /LC_MESSAGES
      messages.po
      messages.mo
```

### 3. Adaptação de Templates

- Todos os textos estáticos serão envolvidos com a função `gettext` (ou seu alias `_`)
- Exemplo: `{{ _('Bem-vindo ao Pachamama Ecoturismo') }}`

### 4. Textos Dinâmicos do Banco de Dados

Para conteúdos dinâmicos como descrições de serviços, duas abordagens serão implementadas:

1. **Tabelas de tradução**: Para cada entidade que precisa de tradução (Service, etc.)
   ```
   ServiceTranslation:
     - service_id (FK)
     - language_code (pt, en, es)
     - name
     - description
     - etc.
   ```

2. **Função auxiliar**: Para recuperar o texto no idioma atual
   ```python
   def get_translated_field(entity, field_name, language=None):
       if not language:
           language = get_locale()
       
       translation = entity.translations.filter_by(language_code=language).first()
       if translation and getattr(translation, field_name, None):
           return getattr(translation, field_name)
       
       # Fallback para o idioma padrão (português)
       return getattr(entity, field_name)
   ```

### 5. Interface de Seleção de Idioma

- Seletor de idioma no cabeçalho do site
- Ícones de bandeira ou códigos de idioma (PT/EN/ES)
- Manutenção do idioma selecionado via sessão
- Redirecionamento para a mesma página após troca de idioma

### 6. Fluxo de Tradução

1. Extração de strings: `pybabel extract -F babel.cfg -o messages.pot .`
2. Inicialização de traduções: `pybabel init -i messages.pot -d translations -l [LANG]`
3. Compilação: `pybabel compile -d translations`
4. Atualização: `pybabel update -i messages.pot -d translations`

### 7. Considerações Especiais

- **URLs**: Manter URLs independentes de idioma, usando parâmetro `?lang=` quando necessário
- **Formatação de números e datas**: Usar funções específicas do Babel para formatação conforme o locale
- **SEO**: Implementar tags hreflang para indicar versões alternativas de idioma

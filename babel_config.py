from flask import Flask, request, session, g
from flask_babel import Babel

def get_locale():
    # Primeiro tenta obter o idioma da sessão
    if 'language' in session:
        return session['language']
    
    # Depois tenta obter do parâmetro de URL
    lang = request.args.get('lang')
    if lang in ['pt', 'en', 'es']:
        session['language'] = lang
        return lang
    
    # Por último, tenta detectar do cabeçalho Accept-Language
    return request.accept_languages.best_match(['pt', 'en', 'es'], default='pt')

def configure_babel(app):
    babel = Babel(app)
    app.config['BABEL_DEFAULT_LOCALE'] = 'pt'
    app.config['BABEL_SUPPORTED_LOCALES'] = ['pt', 'en', 'es']
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'
    babel.init_app(app, locale_selector=get_locale)
    return babel

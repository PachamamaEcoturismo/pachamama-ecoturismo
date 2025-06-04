import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from flask import Flask, send_from_directory, request, session, g, redirect
from src.models import db
from src.models.user import User
from src.models.service import Service
from src.models.booking import Booking
from src.routes.main_routes import main_bp # Import the main_bp
from flask_babel import Babel

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'), template_folder='templates') # Added template_folder
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "asdf#FGSgvasgf$5$WGT")

# Babel configuration for internationalization
app.config['BABEL_DEFAULT_LOCALE'] = 'pt'
app.config['BABEL_SUPPORTED_LOCALES'] = ['pt', 'en', 'es']
app.config['BABEL_TRANSLATION_DIRECTORIES'] = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'translations')

def get_locale():
    # First try to get language from session
    if 'language' in session:
        return session['language']
    
    # Then try to get from URL parameter
    lang = request.args.get('lang')
    if lang in ['pt', 'en', 'es']:
        session['language'] = lang
        return lang
    
    # Finally, try to detect from Accept-Language header
    return request.accept_languages.best_match(['pt', 'en', 'es'], default='pt')

babel = Babel(app, locale_selector=get_locale)
app.register_blueprint(main_bp) # Register the blueprint

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'pachamama.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()

# Serve static files and index.html (current placeholder)
@app.route('/static/<path:filename>') # Route for static files if not handled by Flask default
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

# Route to change language
@app.route('/change_language/<language>')
def change_language(language):
    if language in ['pt', 'en', 'es']:
        session['language'] = language
    
    # Redirect back to the referring page or home if not available
    return_to = request.referrer or '/'
    return redirect(return_to)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

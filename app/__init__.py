import os
import sys
from pathlib import Path
from flask import Flask
from flask_mail import Mail
from dotenv import load_dotenv

# Load environment variables from .env file (if it exists)
try:
    env_path = Path(__file__).parent.parent / '.env'
    if env_path.exists():
        load_dotenv(env_path, verbose=False)
except Exception as e:
    pass  # Silently fail if .env doesn't exist

mail = Mail()

def create_app():
    # Get absolute path to app directory
    app_dir = os.path.dirname(os.path.abspath(__file__))
    static_folder = os.path.join(app_dir, 'static')
    
    print(f"[APP] Initializing Flask app", file=sys.stderr)
    print(f"[APP] App dir: {app_dir}", file=sys.stderr)
    print(f"[APP] Static folder: {static_folder}", file=sys.stderr)
    
    # Create Flask app
    app = Flask(__name__, static_folder=static_folder, static_url_path='/static')
    
    # Configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Email Configuration (from .env file or environment variables)
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER', 'noreply@portfolio.com')
    
    print(f"[APP] Mail configured: {bool(app.config['MAIL_USERNAME'])}", file=sys.stderr)
    
    mail.init_app(app)
    
    # Register blueprints
    try:
        from app.routes import main_bp
        app.register_blueprint(main_bp)
        print(f"[APP] Routes registered successfully", file=sys.stderr)
    except Exception as e:
        print(f"[APP] ERROR registering routes: {e}", file=sys.stderr)
        raise
    
    return app

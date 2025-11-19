"""WSGI entry point for production servers like Gunicorn."""
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create and configure the Flask app
from app import create_app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)

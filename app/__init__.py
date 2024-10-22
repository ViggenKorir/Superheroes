from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Load configuration from config.py
    app.config.from_object('app.config.Config')

    # Initialize the database
    db.init_app(app)

    return app

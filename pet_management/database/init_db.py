from flask import Flask
from database.models import db

def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pet_management.db'  # Cấu hình URI cơ sở dữ liệu (ở đây dùng SQLite)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

def create_tables():
    from database.models import db
    db.create_all()

from flaskcomercialsp import database, login_manager
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, Email
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(80), unique=True, nullable=False)
    password = database.Column(database.String(80), nullable=False)  # Para simplificar; use hashing na vida real.

class Cliente(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(120), unique=True, nullable=False)
    telefone = database.Column(database.String(15), nullable=False)
    nome = database.Column(database.String(80), nullable=False)
    sobrenome = database.Column(database.String(80), nullable=False)
    genero = database.Column(database.String(10), nullable=False)
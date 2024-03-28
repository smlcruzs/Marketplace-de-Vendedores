from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required
from flask_bcrypt import Bcrypt
import os
import sqlalchemy
#Criando um app ( Site )

app = Flask(__name__)
app.config['SECRET_KEY'] = '444529d5f8ba707b7da4e4e0c58a7703'

if os.getenv("DATABASE_URL"): 
    URL_DB = os.getenv('DATABASE_URL')
    nova_URL = URL_DB.replace('postgres://', 'postgresql://')
    app.config['SQLALCHEMY_DATABASE_URI'] = nova_URL
else: 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comercialcm.db'
database  = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"

from flaskcomercialsp import models
engine=sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspector=sqlalchemy.inspect(engine)
if not inspector.has_table("user"):
    with app.app_context():
        database.drop_all()
        database.create_all()

else:

    pass





from flaskcomercialsp import routes, models
from flaskcomercialsp import database
from flaskcomercialsp.models import User, Cliente

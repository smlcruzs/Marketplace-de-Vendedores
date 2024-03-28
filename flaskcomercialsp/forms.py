from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms import RadioField

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')

class ClienteForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    nome = StringField('Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    genero = RadioField('Gênero', choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

class EmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Entrar')
from flask import render_template, url_for, redirect, request, session
from flaskcomercialsp import app
#from flaskcomercialsp import login_required, login_user, logout_user, current_user
#from flaskcomercialsp.forms import  FormLogin, FormCriarConta, FormFoto
#from flaskcomercialsp.models import Usuario, Foto
import os
from werkzeug.utils import secure_filename
from flaskcomercialsp.forms import LoginForm, ClienteForm, EmailForm
from flaskcomercialsp.models import User, Cliente
from flaskcomercialsp import database

from flask_login import login_user, current_user, login_required

@app.route('/', methods=['GET', 'POST'])
def homepage():
    formlogin = LoginForm()
    error_message = None 
    if formlogin.validate_on_submit():
        email = formlogin.email.data
        senha = formlogin.senha.data
        user = User.query.filter_by(username=email).first()  # Supondo que o campo username armazene o email
        if user and user.password == senha:
            login_user(user)
            # Aqui você deve implementar a lógica de autenticação, por exemplo, usando Flask-Login
            return redirect(url_for('cadastros', id_usuario=user.id))
        else:
            error_message = "Login ou senha errados. Por favor, tente novamente."
    
    return render_template('login_admin.html', formlogin=formlogin,  error_message= error_message)


@app.route('/cadastros', methods=['GET', 'POST'])
@login_required
def cadastros():
    form = ClienteForm()
    if form.validate_on_submit():
        # Criar uma nova instância do modelo Cliente e preencher com os dados do formulário
        cliente = Cliente(
            email=form.email.data,
            telefone=form.telefone.data,
            nome=form.nome.data,
            sobrenome=form.sobrenome.data,
            genero=form.genero.data
        )
        print(cliente )
        # Adicionar o novo cliente ao banco de dados
        database.session.add(cliente)
        database.session.commit()
        # Redirecionar para a página de acesso após o cadastro
    return render_template('cadastro_de_clientes.html', form=form)

@app.route('/links')
def links():
    if session.get('email_redirecionado'):
        return render_template('index.html')
    return redirect(url_for('acesso'))

@app.route('/acesso', methods=['GET', 'POST'])
def acesso():
    form = EmailForm()  # Instancie o formulário Flask-WTF
    if form.validate_on_submit():
        email = form.email.data
        cliente = Cliente.query.filter_by(email=email).first()
        if cliente:
            session['email_redirecionado'] = email
            return redirect(url_for('links'))
    return render_template('pag_entrada_cliente.html', form=form)
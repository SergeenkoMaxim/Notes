from flask import Flask, render_template, redirect, request, flash, url_for, session
from forms import LoginForm, RegForm
from functions import hash_password, is_email
from Database import db
import os


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/login/', methods=['GET', 'POST'])
def login():
    logform = LoginForm()

    if 'userLogged' in session:  # переадресация пользователя на страницу профиля, если вход уже выполнен

        return redirect(url_for('profile', username=session['userLogged']))

    if request.method == 'POST':

        name = logform.login.data  #Получение данных из форм
        email = request.form['email']
        password = logform.password.data

        if hash_password(password) == db.get_password(name) and db.is_user_exist(email):
            session['userLogged'] = name

            return redirect(url_for('profile', username=session['userLogged']))     #отправление на страницу profile

    else:

        flash('Неверный логин или пароль', category='error')

    return render_template('authorization.html',  logform=logform)


@app.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegForm()

    if request.method == 'POST':

        login = form.login.data  #Получение данных из форм
        email = request.form['email']
        password = form.password.data
        hashed_password = hash_password(password)

        if is_email(email):

            db.add_user(login, email, hashed_password)  #Добавление данных в бд

        else:

            flash('Данная почта не существует', category='error')   #категории используются для оформления стилей

    return render_template('registration.html', form=form)


@app.route('/profile/<username>')
def profile(username):

    return f"Hello {username}"


@app.errorhandler(404)  #отлавдивание ошибок при неверном URL'е, 404 - код ошибки
def pagenotfound(error):
    return "Страница не найдена"


if __name__ == '__main__':
    app.run(debug=True, port=5555)

#Для выхода из учетной записи необходимо удалить userLogged из сессии

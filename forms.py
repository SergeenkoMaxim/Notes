from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    login = StringField('Имя: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль: ', validators=[DataRequired(), Length(min=8, max=30)])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegForm(FlaskForm):
    login = StringField('Имя: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль: ', validators=[DataRequired(), Length(min=8, max=30)])
    password_to_confirm = PasswordField('Подтвердить: ', validators=[DataRequired(), Length(min=8, max=30)])
    submit = SubmitField('Зарегистрироваться')

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, BooleanField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"placeholder": 'Имя'})
    email = EmailField('Почта', validators=[DataRequired()], render_kw={"placeholder": 'Почта'})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"placeholder": 'Пароль'})
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()], render_kw={"placeholder": 'Повторите пароль'})
    submit = SubmitField('Войти')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()], render_kw={"placeholder": 'Почта'})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"placeholder": 'Пароль'})
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
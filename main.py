from flask import Flask, url_for, request, render_template, redirect, jsonify
from data import db_session
import configs_api
import flask
from flask_login import login_user, LoginManager, login_required, logout_user
from forms.user import RegisterForm, LoginForm
from data.users import User
from data.configurations import Configuration
from forms.configuration import AddConfigurationForm
from flask_login import LoginManager, current_user
from flask_restful import reqparse, abort, Api, Resource
from data import configs_api


app = Flask(__name__)
app.config['SECRET_KEY'] = 'pchub_secret_key'
api = Api(app)
login_manager = LoginManager()
login_manager.init_app(app)


def main():
    api.add_resource(configs_api.ConfigurationList, '/api/') 
    api.add_resource(configs_api.ConfigurationResourse, '/api/<int:config_id>')
    db_session.global_init("db/data.sqlite3")
    app.run(port=8080, host='127.0.0.1')


@app.route('/')
def index():
    db_sess = db_session.create_session()
    configurations = db_sess.query(Configuration)
    return render_template('index.html', title='Главная страница', configurations=configurations)


@app.route('/add_configuration', methods=['GET', 'POST'])
@login_required
def add_configuration():
    form = AddConfigurationForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        summ =int(form.cooler_price.data) + int(form.ram_price.data) + int(form.cpu_price.data) + int(form.frame_price.data) + int(form.ssd_price.data) + int(form.power_price.data) + int(form.motherboard_price.data) + int(form.gpu_price.data)
        config = Configuration(
            name=form.name.data,
            
            cooler=form.cooler.data,
            cooler_link=form.cooler_link.data,
            cooler_price=form.cooler_price.data,
            
            ram=form.ram.data,
            ram_link=form.ram_link.data,
            ram_price=form.ram_price.data,
            
            cpu=form.cpu.data,
            cpu_link=form.cpu_link.data,
            cpu_price=form.cpu_price.data,
            
            frame=form.frame.data,
            frame_link=form.frame_link.data,
            frame_price=form.frame_price.data,
            
            ssd=form.ssd.data,
            ssd_link=form.ssd_link.data,
            ssd_price=form.ssd_price.data,


            power=form.power.data,
            power_link=form.power_link.data,
            power_price=form.power_price.data,
            
            motherboard=form.motherboard.data,
            motherboard_link=form.motherboard_link.data,
            motherboard_price=form.motherboard_price.data,
            
            gpu=form.gpu.data,
            gpu_link=form.gpu_link.data,
            gpu_price=form.gpu_price.data,
            
            comment=form.comment.data,
            
            total_price=summ,
        )
        current_user.configurations.append(config)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('add_configuration.html', title='Добавление кофигурации', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой адрес электронной почты уже используется")
        user = User(
            username=form.username.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/show')
def show():
    return render_template('show_config.html')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


if __name__ == "__main__":
    main()
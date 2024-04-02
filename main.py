from flask import Flask, url_for, request, render_template, redirect
from data import db_session
from flask_login import login_user, LoginManager, login_required, logout_user
from forms.user import RegisterForm, LoginForm
from data.users import User
from data.configurations import Configuration
from forms.configuration import AddConfigurationForm
from flask_login import LoginManager, current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'pchub_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


def main():
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
        config = Configuration(
            name=form.name.data,
            
            cooler=form.cooler.data,
            cooler_link=form.cooler_link.data,
            
            ram=form.ram.data,
            ram_link=form.ram_link.data,
            
            cpu=form.cpu.data,
            cpu_link=form.cpu_link.data,
            
            frame=form.frame.data,
            frame_link=form.frame_link.data,
            
            ssd=form.ssd.data,
            ssd_link=form.ssd_link.data,

            power=form.power.data,
            power_link=form.power_link.data,
            
            motherboard=form.motherboard.data,
            motherboard_link=form.motherboard_link.data,
            
            gpu=form.gpu.data,
            gpu_link=form.gpu_link.data,
            
            comment=form.comment.data
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


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


if __name__ == "__main__":
    main()
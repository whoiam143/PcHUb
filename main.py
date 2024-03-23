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
    return render_template('index.html', title='Главная страница')


@app.route('/add_configuration', methods=['GET', 'POST'])
@login_required
def add_configuration():
    form = AddConfigurationForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        config = Configuration(
            cooler=form.cooler.data,
            cooler_link=form.cooler_link.data,
            
            ram=form.cooler.data,
            ram_link=form.cooler_link.data,
            
            cpu=form.cooler.data,
            cpu_link=form.cooler_link.data,
            
            frame=form.cooler.data,
            frame_link=form.cooler_link.data,
            
            ssd=form.cooler.data,
            ssd_link=form.cooler_link.data,

            power=form.cooler.data,
            power_link=form.cooler_link.data,
            
            motherboard=form.cooler.data,
            motherboard_link=form.cooler_link.data,
            
            gpu=form.cooler.data,
            gpu_link=form.cooler_link.data,
            
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
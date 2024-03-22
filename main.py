from flask import Flask, url_for, request, render_template, redirect
from data import db_session
from flask_login import login_user, LoginManager, login_required, logout_user


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init("db/data.sqlite3")
    app.run(port=8080, host='127.0.0.1')


@app.route('/')
def index():
    return render_template('base.html', title='Главная страница')




if __name__ == "__main__":
    main()
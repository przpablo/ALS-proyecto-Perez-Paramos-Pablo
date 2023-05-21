import os
import flask
import sirope
import flask_login
from flask import render_template, redirect, url_for, request
from flask_login import login_manager
from views.auth.auth import auth_blueprint
from views.search.home import home_blueprint
from model.usuario import Usuario


def create_app():
    lmanager = login_manager.LoginManager()
    aplicacion = flask.Flask(__name__, instance_relative_config=True)
    syrp = sirope.Sirope()

    # aplicacion.config.from_json("config.json")
    aplicacion.secret_key = "1e44b3a45067431da85bfe4259f5a15e"
    lmanager.init_app(aplicacion)
    aplicacion.register_blueprint(auth_blueprint, url_prefix='/auth')
    aplicacion.register_blueprint(home_blueprint, url_prefix='/home')

    return aplicacion, lmanager, syrp


app, lm, srp = create_app()


@lm.user_loader
def user_loader(email):
    return Usuario.find(srp, email)


@app.route('/logout')
def logout():
    flask_login.logout_user()
    flask.flash("User logged out")
    return flask.redirect("/")


@lm.unauthorized_handler
def unauthorized_handler():
    flask.flash("Unauthorized")
    return flask.redirect("/")


# IGUAL PUEDO ELIMINARLO
def guardar_usuario(user):
    srp.save(user)


# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if not email:
            flask.flash("El email está vacío")
            return flask.redirect("/")
        else:
            user = Usuario.find(srp, email)
            if not password:
                flask.flash("El password está vacío")
                return flask.redirect("/")
            elif not user:
                flask.flash("El usuario no existe")
                return flask.redirect("/")
            elif not user.chk_password(password):
                flask.flash("El password es incorrecto")
                return flask.redirect("/")

            flask_login.login_user(user)
            return redirect(url_for('home.home_route'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run()

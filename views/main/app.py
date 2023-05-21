import os
import flask
import sirope
import flask_login
from flask import Flask, render_template, redirect, url_for, request
from flask_login import login_manager
from views.auth.auth import auth_blueprint
from views.search.home import home_blueprint
from model.usuario import Usuario


def create_app():
    lmanager = login_manager.LoginManager()
    aplicacion = flask.Flask(__name__, instance_relative_config=True)
    syrp = sirope.Sirope()

    # aplicacion.config.from_json("config.json")
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


def guardar_usuario(user):
    srp.save(user)


# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Aquí se realizaría la lógica de autenticación
        # Si la autenticación es exitosa, redirigir a la página home
        return redirect(url_for('home.home_route'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run()

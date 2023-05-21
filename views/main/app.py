import flask
import sirope
import flask_login
from flask import render_template, request
from flask_login import login_manager
from views.auth.auth import auth_blueprint
from views.search.home import home_blueprint, publicar_blueprint
from views.car.car import car_blueprint
from model.usuario import Usuario
from model.viaje import Viaje


def create_app():
    lmanager = login_manager.LoginManager()
    aplicacion = flask.Flask(__name__, instance_relative_config=True)
    syrp = sirope.Sirope()

    # aplicacion.config.from_json("config.json")
    aplicacion.secret_key = "1e44b3a45067431da85bfe4259f5a15e"
    lmanager.init_app(aplicacion)
    aplicacion.register_blueprint(auth_blueprint, url_prefix='/auth')
    aplicacion.register_blueprint(home_blueprint, url_prefix='/home')
    aplicacion.register_blueprint(publicar_blueprint, url_prefix='/publicar')
    aplicacion.register_blueprint(car_blueprint, url_prefix='/car')

    return aplicacion, lmanager, syrp


app, lm, srp = create_app()


@lm.user_loader
def user_loader(email):
    return Usuario.find(srp, email)


@app.route('/logout')
@flask_login.login_required
def logout():
    flask_login.logout_user()
    flask.flash("User logged out")
    return flask.redirect("/")


@lm.unauthorized_handler
def unauthorized_handler():
    flask.flash("Debes iniciar sesión para acceder a esta página", "error")
    return flask.redirect("/")


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

            lista_viajes = srp.load_all(Viaje)
            datos = {
                "lista_viajes": reversed(list(lista_viajes))
            }
            return render_template('home.html', **datos)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()

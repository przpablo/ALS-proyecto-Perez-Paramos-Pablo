import flask
import sirope
from model.usuario import Usuario
from flask import render_template, request


def get_blprint():
    auth = flask.blueprints.Blueprint("auth", __name__,template_folder="templates",static_folder="static")
    syrp = sirope.Sirope()

    return auth, syrp


auth_blueprint, srp = get_blprint()


@auth_blueprint.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['name']
        email = request.form['email']
        tlf = request.form['phone']
        passwd = request.form['password']

        if not nombre:
            flask.flash("Nombre no puede estar vacío")
            return flask.redirect("/registro")
        elif not email:
            flask.flash("Email no puede estar vacío")
            return flask.redirect("/registro")
        elif not tlf or len(tlf) != 9:
            flask.flash("Teléfono no es válido")
            return flask.redirect("/registro")
        elif not passwd:
            flask.flash("Contraseña no puede estar vacía")
            return flask.redirect("/registro")
        else:
            user = Usuario(nombre, email, tlf, passwd)
            srp.save(user)
            return render_template('index.html')

    return render_template('registro.html')
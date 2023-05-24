import flask
import sirope
from model.usuario import Usuario
from flask import render_template, request, url_for
from flask_login import login_required


def get_blprint():
    auth = flask.blueprints.Blueprint("auth", __name__, template_folder="templates", static_folder="static")
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

        if not nombre or not nombre.isalpha():
            flask.flash("Nombre no puede estar vacío")
            return flask.redirect("/auth/registro")
        if not email:
            flask.flash("Email no puede estar vacío")
            return flask.redirect("/auth/registro")
        if not tlf or len(tlf) != 9 or not tlf.isdigit():
            flask.flash("Teléfono no es válido")
            return flask.redirect("/auth/registro")
        if not passwd:
            flask.flash("Contraseña no puede estar vacía")
            return flask.redirect("/auth/registro")
        else:
            user = Usuario(nombre, email, tlf, passwd)
            srp.save(user)
            return render_template('index.html')

    return render_template('registro.html')


@auth_blueprint.route('/modperfil', methods=['GET', 'POST'])
@login_required
def mod_perfil():
    usuario = Usuario.current_user()

    if request.method == 'POST':
        modnombre = request.form['name']
        tlf = request.form['phone']
        passwd = request.form['password']
        confirm_password = request.form['confirm_password']

        if not modnombre or not modnombre.isalpha():
            flask.flash("Nombre no puede estar vacío")
            return flask.redirect("/auth/registro")
        if not tlf or len(tlf) != 9 or not tlf.isdigit():
            flask.flash("Teléfono no es válido")
            return flask.redirect("/auth/registro")
        if not passwd:
            flask.flash("Contraseña no puede estar vacía")
            return flask.redirect("/auth/registro")
        if passwd != confirm_password or not confirm_password:
            flask.flash("Las contraseñas no coinciden")
            return flask.redirect(url_for('auth.mod_perfil'))
        else:
            user = Usuario(modnombre, usuario.email, tlf, passwd)
            srp.save(user)
            return flask.redirect(url_for('home.home_route'))

    return render_template('modperfil.html', usuario=usuario)

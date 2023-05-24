import flask
import sirope
from flask_login import login_required
from model.coche import Coche
from flask import render_template, request, url_for
from model.usuario import Usuario


def get_blprint():
    car = flask.blueprints.Blueprint("car", __name__, template_folder="templates", static_folder="static")
    syrp = sirope.Sirope()

    return car, syrp


car_blueprint, srp = get_blprint()
usuario = Usuario.current_user()


def comprobaciones():
    marca = request.form['marca']
    modelo = request.form['modelo']
    color = request.form['color']
    anno = request.form['anno']

    if not marca or not marca.isalpha():
        flask.flash("El formato de la marca no es válido")
        return False
    if not modelo:
        flask.flash("El formato del modelo no es válido")
        return False
    if not color or not color.isalpha():
        flask.flash("El formato del color no es válido")
        return False
    if not anno or not anno.isdigit() or int(anno) < 1900 or int(anno) > 2023:
        flask.flash("El formato del año no es válido")
        return False
    else:
        car = Coche(marca, modelo, color, anno)
        usuario.coche = car
        srp.save(car)
        srp.save(usuario)
        return True


@car_blueprint.route('/car', methods=['GET', 'POST'])
@login_required
def add_car():
    if usuario.coche is not None:
        flask.flash("El usuario ya tiene un coche. No puedes añadir otro, pero sí modificarlo.")
        return flask.redirect(url_for('home.home_route'))

    if request.method == 'POST':
        if not comprobaciones():
            return flask.redirect("/car/car")
        else:
            return flask.redirect(url_for('home.home_route'))

    return render_template('addcar.html')


@car_blueprint.route('/modcar', methods=['GET', 'POST'])
@login_required
def mod_car():
    if usuario.coche is None:
        flask.flash("El usuario no tiene un coche, no puedes modificarlo")
        return flask.redirect(url_for('home.home_route'))

    if request.method == 'POST':
        if not comprobaciones():
            return flask.redirect(url_for('car.mod_car'))
        else:
            return flask.redirect(url_for('home.home_route'))

    return render_template('modcar.html', coche=usuario.coche)


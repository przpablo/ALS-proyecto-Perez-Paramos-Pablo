import flask
import sirope
from flask_login import login_required
from model.coche import Coche
from flask import render_template, request
from model.usuario import Usuario


def get_blprint():
    car = flask.blueprints.Blueprint("car", __name__, template_folder="templates", static_folder="static")
    syrp = sirope.Sirope()

    return car, syrp


car_blueprint, srp = get_blprint()


@car_blueprint.route('/car', methods=['GET', 'POST'])
@login_required
def add_car():
    if request.method == 'POST':
        marca = request.form['marca']
        modelo = request.form['modelo']
        color = request.form['color']
        anno = request.form['anno']

        if not marca or not marca.isalpha():
            flask.flash("El formato de la marca no es válido")
            return flask.redirect("/car/addcar")
        if not modelo or not modelo.isalpha():
            flask.flash("El formato del modelo no es válido")
            return flask.redirect("/car/addcar")
        if not color or not color.isalpha():
            flask.flash("El formato del color no es válido")
            return flask.redirect("/car/addcar")
        if not anno or not anno.isdigit() or int(anno) < 1900 or int(anno) > 2023:
            flask.flash("El formato del año no es válido")
            return flask.redirect("/car/addcar")
        else:
            car = Coche(marca, modelo, color, anno)
            usuario = Usuario.current_user()
            usuario.coche = car
            srp.save(car)
            srp.save(usuario)
            return render_template('/home.html')

    return render_template('addcar.html')

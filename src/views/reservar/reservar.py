import flask
import sirope
from flask import render_template, request, url_for
from flask_login import login_required
from model.viaje import Viaje
from datetime import date, datetime
from model.usuario import Usuario


def get_blprint():
    reserva_bprt = flask.blueprints.Blueprint("reservar", __name__, template_folder="templates", static_folder="static")
    syrp = sirope.Sirope()
    return reserva_bprt, syrp


reservar_blueprint, srp = get_blprint()


@reservar_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def reservar_route():
    if request.method == 'POST':
        viaje_id = request.form.get('viaje_id')
        viaje = Viaje.obtener_viaje_por_id(srp.load_all(Viaje), viaje_id)

        if not viaje:
            flask.flash("No existe el viaje")
            return flask.redirect(url_for('home.home_route'))

        return render_template('reserva.html', viaje=viaje)

    return flask.redirect(url_for('home.home_route'))


@reservar_blueprint.route('/actualizar', methods=['POST'])
@login_required
def actualizar_viaje():
    viaje_id = request.form.get('viaje_id')
    viaje = Viaje.obtener_viaje_por_id(srp.load_all(Viaje), viaje_id)
    if request.method == 'POST':
        usuario = Usuario.current_user()
        if not viaje:
            flask.flash("No existe el viaje")
            return flask.redirect(url_for('home.home_route'))
        if viaje.plazas <= 0:
            flask.flash("No quedan plazas")
            return flask.redirect(url_for('home.home_route'))
        if usuario.email == viaje.conductor['email']:
            flask.flash("No puedes reservar tu propio viaje")
            return flask.redirect(url_for('home.home_route'))
        else:
            viaje.add_pasajero(usuario.to_dict())
            srp.save(viaje)
            return flask.redirect(url_for('valorar.misviajes_route'))

    return render_template('reserva.html', viaje=viaje)

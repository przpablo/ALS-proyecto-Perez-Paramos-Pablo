import flask
from flask import render_template, request, url_for
from flask_login import login_required
from model.viaje import Viaje
from datetime import date, datetime
from model.usuario import Usuario
import sirope


def get_blprint():
    valora_bprt = flask.blueprints.Blueprint("valorar", __name__, template_folder="templates", static_folder="static")
    syrp = sirope.Sirope()
    return valora_bprt, syrp


valorar_blueprint, srp = get_blprint()


@valorar_blueprint.route('/', methods=['GET'])
@login_required
def misviajes_route():
    lista = srp.load_all(Viaje)
    lista_viajes = []

    for viaje in lista:
        for pasajero in viaje.pasajeros:
            if pasajero['email'] == Usuario.current_user().email:
                lista_viajes.append(viaje)

    datos = {
        "lista_viajes": reversed(list(lista_viajes))
    }

    return render_template('misviajes.html', **datos)


@valorar_blueprint.route('/viaje', methods=['GET', 'POST'])
@login_required
def valorar_route():
    if request.method == 'POST':
        viaje_id = request.form.get('viaje_id')
        viaje = Viaje.obtener_viaje_por_id(srp.load_all(Viaje), viaje_id)
        return render_template('valorar.html', viaje=viaje)

    return flask.redirect(url_for('home.home_route'))

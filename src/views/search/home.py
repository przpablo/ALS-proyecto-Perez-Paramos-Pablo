import flask
from flask import render_template, request, url_for
from flask_login import login_required
from model.viaje import Viaje
from datetime import date, datetime
from model.usuario import Usuario
import sirope


def get_blprint():
    home_bprt = flask.blueprints.Blueprint("home", __name__, template_folder="templates", static_folder="static")
    publica_bprt = flask.blueprints.Blueprint("publicar", __name__, template_folder="templates", static_folder="static")
    syrp = sirope.Sirope()
    return home_bprt, publica_bprt, syrp


home_blueprint, publicar_blueprint, srp = get_blprint()


@home_blueprint.route('/', methods=['GET'])
@login_required
def home_route():
    lista_viajes = srp.load_all(Viaje)
    datos = {
        "lista_viajes": reversed(list(lista_viajes))
    }

    flask.flash("Viaje publicado con éxito", "success")
    # return flask.redirect("/home/home")
    return render_template('home.html', **datos)


@publicar_blueprint.route('/publicar', methods=['GET', 'POST'])
@login_required
def publicar_route():
    if request.method == "POST":
        origen = request.form['origen']
        destino = request.form['destino']
        fecha = request.form['fecha']
        hora = request.form['hora']
        tiempo = request.form['tiempo']
        tarifa = request.form['tarifa']
        plazas = request.form['plazas']

        if not origen or not origen.isalpha():
            flask.flash("Formato origen no válido")
            return flask.redirect("/publicar/publicar")
        if not destino or not destino.isalpha():
            flask.flash("Formato destino no válido")
            return flask.redirect("/publicar/publicar")
        if not fecha or datetime.strptime(fecha, "%Y-%m-%d").date() < date.today():
            flask.flash("Formato fecha no válido")
            return flask.redirect("/publicar/publicar")
        if not hora:
            flask.flash("La hora está vacía")
            return flask.redirect("/publicar/publicar")
        if not tiempo:
            flask.flash("El tiempo está vacío")
            return flask.redirect("/publicar/publicar")
        if not tarifa:
            flask.flash("Formato tarifa no válido")
            return flask.redirect("/publicar/publicar")
        if not plazas:
            flask.flash("Formato plazas no válido")
            return flask.redirect("/publicar/publicar")
        else:
            viaje = Viaje(origen, destino, fecha, hora, int(tiempo), int(tarifa), int(plazas), Usuario.current_user())
            srp.save(viaje)

            flask.flash("Viaje publicado con éxito", "success")
            return flask.redirect(url_for('home.home_route'))

    return render_template('publicar.html')

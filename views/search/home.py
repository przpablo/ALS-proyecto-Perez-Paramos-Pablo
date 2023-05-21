import flask
from flask import render_template
import sirope


def get_blprint():
    home_bprt = flask.blueprints.Blueprint("home", __name__, template_folder="templates", static_folder="static")
    publica_bprt = flask.blueprints.Blueprint("publicar", __name__, template_folder="templates", static_folder="static")
    syrp = sirope.Sirope()
    return home_bprt, publica_bprt, syrp


home_blueprint, publicar_blueprint, srp = get_blprint()


@home_blueprint.route('/home', methods=['GET'])
def home_route():
    return render_template('home.html')


@publicar_blueprint.route('/publicar', methods=['GET', 'POST'])
def publicar_route():
    return render_template('publicar.html')

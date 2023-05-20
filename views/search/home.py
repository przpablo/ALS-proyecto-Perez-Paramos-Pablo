import flask
from flask import render_template
import sirope


def get_blprint():
    home_bprt = flask.blueprints.Blueprint("home", __name__, url_prefix="/home", template_folder="templates",
                                      static_folder="static")
    syrp = sirope.Sirope()
    return home_bprt, syrp


home_blueprint, srp = get_blprint()


@home_blueprint.route('/home', methods=['GET'])
def home_route():
    return render_template('home.html')

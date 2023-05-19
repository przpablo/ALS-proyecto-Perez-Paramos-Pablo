from flask import render_template, Blueprint

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')


@auth_blueprint.route('/registro', methods=['GET'])
def registro():
    return render_template('registro.html')

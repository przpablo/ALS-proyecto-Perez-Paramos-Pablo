import json
import flask
import flask_login
import sirope
# from model.usuario import Usuario

"""
def create_app():
    lmanager = flask_login.login_manager.LoginManager()
    fapp = flask.Flask(__name__)
    syrp = sirope.Sirope()

    fapp.config.from_file("../../instance/config.json", load=json.load)
    lmanager.init_app(fapp)
    return fapp, lmanager, syrp


app, lm, srp = create_app()


@lm.user_loader
def user_loader(email):
   return Usuario.find(srp, email)


@lm.unauthorized_handler
def unauthorized_handler():
    flask.flash("Unauthorized")
    return flask.redirect("/")


if __name__ == '__main__':
    app.run() """

import flask


app = flask.Flask(__name__)


@app.route("/")
def get_index():
    return flask.send_from_directory(app.static_folder, "index.html")


@app.route("/hi", methods=["POST"])
def post_answer():
    nombre = flask.request.form["edName"]
    return ("<html><body>"
    + f"<b>Hola, {nombre}</b><form>"
    + "<INPUT Type='button'"
    + "VALUE='<<' onClick="
    + "'history.go(-1);"
    + "return true;'/>"
    + "</form></body></html>")

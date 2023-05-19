from flask import Flask, render_template
from views.auth.auth import auth_blueprint

app = Flask(__name__)

# Registrar el blueprint con la ruta correcta
app.register_blueprint(auth_blueprint, url_prefix='/auth')


# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

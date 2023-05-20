from flask import Flask, render_template, redirect, url_for, request
from views.auth.auth import auth_blueprint
from views.search.home import home_blueprint

app = Flask(__name__)

# Registrar el blueprint con la ruta correcta
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(home_blueprint, url_prefix='/home')


# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Aquí se realizaría la lógica de autenticación
        # Si la autenticación es exitosa, redirigir a la página home
        return redirect(url_for('home.home_route'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run()

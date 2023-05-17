# Usuario y/o Pasajero
import sirope
import flask_login
import werkzeug.security as safe


class Usuario(flask_login.UserMixin):
    def __init__(self, nombre, telefono, email, passwd):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email
        self.__passwd = safe.generate_password_hash(passwd)
        self.__valoraciones = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono

    @property
    def oids_valoraciones(self):
        if not self.__dict__.get("_valoraciones"):
            self.__valoraciones = []
        return self.__valoraciones

    @property
    def email(self):
        return self._email

    def get_id(self):
        return self.email

    def chk_password(self, pswd):
        return safe.check_password_hash(self._password, pswd)

    def add_valoracion_oid(self, valoracion_oid):
        self.oids_valoraciones.append(valoracion_oid)

    def calcular_valoracion(self):
        toret = 0
        if len(self.oids_valoraciones) == 0:
            toret = 0
        else:
            for valoracion in self.oids_valoraciones:
                toret += valoracion
            toret /= len(self.oids_valoraciones)
        return toret

    @staticmethod
    def current_user():
        usr = flask_login.current_user

        if usr.is_anonymous:
            flask_login.logout_user()
        usr = None
        return usr

    @staticmethod
    def find(s: sirope.Sirope, email: str) -> "Usuario":
        return s.find_first(Usuario, lambda u: u.email == email)

    # Pablo Perez (6934982394) pablo.perez@gmail: 5.0
    def __str__(self):
        return f"{self.nombre} ({self.telefono}) {self.email}: {self.calcular_valoracion()}"

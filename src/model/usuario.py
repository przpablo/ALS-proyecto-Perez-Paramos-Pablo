# Usuario y/o Pasajero
import sirope
import flask_login
import werkzeug.security as safe
from model.coche import Coche


class Usuario(flask_login.UserMixin):
    def __init__(self, nombre, email, telefono, passwd):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email
        self.__passwd = safe.generate_password_hash(passwd)
        self.__valoraciones = []
        self.__valoracionmedia = 0.0
        self.__coche = None

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
    def valoraciones(self):
        return list(self.__valoraciones)

    @property
    def email(self):
        return self.__email

    @property
    def coche(self) -> Coche:
        return self.__coche

    @coche.setter
    def coche(self, coche: Coche):
        self.__coche = coche.to_dict()

    @property
    def valoracionmedia(self) -> float:
        return self.__valoracionmedia

    @valoracionmedia.setter
    def valoracionmedia(self, valoracionmedia: float):
        self.__valoracionmedia = valoracionmedia

    def to_dict(self):
        return {
            'nombre': self.__nombre,
            'email': self.__email,
            'telefono': self.__telefono,
            'valoraciones': self.__valoraciones,
            'valoracion_media': self.__valoracionmedia,
            'coche': self.__coche if self.__coche else None
        }

    def get_id(self):
        return self.email

    def chk_password(self, pswd):
        return safe.check_password_hash(self.__passwd, pswd)

    def add_valoracion(self, valoracion: int):
        self.__valoraciones.append(valoracion)
        self.valoracion_media = self.calcular_valoracion()

    def calcular_valoracion(self):
        toret = 0.0
        if len(self.valoraciones) == 0:
            toret = 0.0
        else:
            for valoracion in self.valoraciones:
                toret += float(valoracion)
            toret /= len(self.valoraciones)
        return toret

    @staticmethod
    def current_user():
        return flask_login.current_user

    @staticmethod
    def find(s: sirope.Sirope, email: str) -> "Usuario":
        return s.find_first(Usuario, lambda u: u.email == email)

    def publica(self, origen, destino, fecha, hora, tiempo, tarifa, plazas):
        from viaje import Viaje
        return Viaje(origen, destino, fecha, hora, tiempo, tarifa, plazas, self)

    # Pablo Perez (6934982394) pablo.perez@gmail: 5.0
    def __str__(self):
        return f"{self.nombre} ({self.telefono}) {self.email}: {self.calcular_valoracion()}"

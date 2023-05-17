# Conductor

from coche import Coche
from usuario import Usuario


class Conductor(Usuario):
    def __init__(self, nombre, telefono, email, passwd, coche: Coche, carnet: bool):
        super().__init__(nombre, telefono, email, passwd)
        self.__coche = coche
        self.__carnet = carnet

    @property
    def coche(self):
        return self.__coche

    @coche.setter
    def coche(self, coche):
        self.__coche = coche

    @property
    def carnet(self):
        return self.__carnet

    @carnet.setter
    def carnet(self, carnet):
        self.__carnet = carnet

    def publica(self, origen, destino, fecha, hora, tiempo, tarifa, plazas):
        from viaje import Viaje
        return Viaje(origen, destino, fecha, hora, tiempo, tarifa, plazas, self)

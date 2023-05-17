# Viaje

from conductor import Conductor


class Viaje:
    def __init__(self, id_viaje, origen, destino, fecha, hora, tiempo, tarifa, plazas, conductor: Conductor):
        self.__id_viaje = id_viaje
        self.__origen = origen
        self.__destino = destino
        self.__fecha = fecha
        self.__hora = hora
        self.__tiempo = tiempo
        self.__tarifa = tarifa
        self.__plazas = plazas
        self.__condutor = conductor

    @property
    def id_viaje(self):
        return self.__id_viaje

    @property
    def origen(self):
        return self.__origen

    @origen.setter
    def origen(self, origen):
        self.__origen = origen

    @property
    def destino(self):
        return self.__destino

    @destino.setter
    def destino(self, destino):
        self.__destino = destino

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @property
    def hora(self):
        return self.__hora

    @hora.setter
    def hora(self, hora):
        self.__hora = hora

    @property
    def tiempo(self):
        return self.__tiempo

    @tiempo.setter
    def tiempo(self, tiempo):
        self.__tiempo = tiempo

    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa.setter
    def tarifa(self, tarifa):
        self.__tarifa = tarifa

    @property
    def plazas(self):
        return self.__plazas

    @plazas.setter
    def plazas(self, plazas):
        self.__plazas = plazas

    @property
    def conductor(self):
        return self.__condutor


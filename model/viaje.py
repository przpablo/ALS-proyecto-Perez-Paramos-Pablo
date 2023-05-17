# Viaje

from conductor import Conductor


class Viaje:
    def __init__(self, origen, destino, fecha, hora, tiempo, tarifa, plazas, conductor: Conductor):
        self.__origen = origen
        self.__destino = destino
        self.__fecha = fecha
        self.__hora = hora
        self.__tiempo = tiempo
        self.__tarifa = tarifa
        self.__plazas = plazas
        self.__condutor = conductor
        self.__pasajeros = []

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

    @property
    def pasajeros(self):
        return list(self.__pasajeros)

    def add_pasajero(self, pasajero):
        if self.plazas > 0:
            self.__pasajeros.append(pasajero)
            self.__plazas -= 1
        else:
            raise Exception("No hay plazas disponibles")

    def add_pasajeros(self, pasajeros: list):
        if self.plazas >= len(pasajeros):
            self.__pasajeros.extend(pasajeros)
            self.__plazas -= len(pasajeros)
        else:
            raise Exception("No hay plazas disponibles")

    def __str__(self):
        return f"{self.origen} - {self.destino} ({self.fecha} {self.hora}): {self.tarifa}€ por: {self.conductor.nombre}"

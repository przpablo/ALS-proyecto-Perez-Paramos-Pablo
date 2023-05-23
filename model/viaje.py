# Viaje
import uuid
from model.usuario import Usuario
from datetime import date


class Viaje:
    def __init__(self, origen, destino, fecha: date, hora, tiempo: int, tarifa: int, plazas: int, conductor: Usuario):
        self.__id = str(uuid.uuid4())
        self.__origen = origen
        self.__destino = destino
        self.__fecha = fecha
        self.__hora = hora
        self.__tiempo = tiempo
        self.__tarifa = tarifa
        self.__plazas = plazas
        self.__conductor = conductor.to_dict()
        self.__pasajeros = []
        self.__estado = False  # False = no realizado, True = realizado

    @property
    def id(self):
        return self.__id

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
    def plazas(self) -> int:
        return int(self.__plazas)

    @plazas.setter
    def plazas(self, plazas: int):
        self.__plazas = plazas

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, value):
        self.__estado = value

    @property
    def conductor(self):
        return self.__conductor

    @conductor.setter
    def conductor(self, conductor: Usuario):
        self.__conductor = conductor.to_dict()

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

    @staticmethod
    def obtener_viaje_por_id(viajes, viaje_id):
        for viaje in viajes:
            if viaje.id == viaje_id:
                return viaje
        return None

    def to_dict(self):
        return {
            'id': self.__id,
            'origen': self.__origen,
            'destino': self.__destino,
            'fecha': str(self.__fecha),
            'hora': self.__hora,
            'tiempo': self.__tiempo,
            'tarifa': self.__tarifa,
            'plazas': self.__plazas,
            'conductor': self.conductor,
            'pasajeros': self.__pasajeros,
            'estado': self.__estado
        }

    def __str__(self):
        return f"{self.origen} - {self.destino} ({self.fecha} {self.hora}): {self.tarifa}€ por: {self.conductor.nombre}"

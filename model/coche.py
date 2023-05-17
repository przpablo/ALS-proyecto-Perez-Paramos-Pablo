# Coche

class Coche:
    def __init__(self, marca, modelo, color, anno):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__anno = anno

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def anno(self):
        return self.__anno

    @anno.setter
    def anno(self, anno):
        self.__anno = anno

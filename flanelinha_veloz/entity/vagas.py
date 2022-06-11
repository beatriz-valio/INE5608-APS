# In English:: car_spot
# data, horario_inicio, horario_fim

from datetime import datetime, timedelta


class Vagas:
    def __init__(self, vaga:int, data: datetime, horario_inicio: timedelta, horario_fim: timedelta):
        if isinstance(vaga, int):
            self.__vaga = vaga
        if isinstance(data, datetime):
            self.__data = data
        if isinstance(horario_inicio, int):
            self.__horario_inicio = horario_inicio
        if isinstance(horario_fim, int):
            self.__horario_fim = horario_fim

    @property
    def vaga(self) -> int:
        return self.__vaga

    @vaga.setter
    def vaga(self, vaga: int):
        if isinstance(vaga, int):
            self.__vaga = vaga

    @property
    def data(self) -> datetime:
        return self.__data

    @data.setter
    def data(self, data: datetime):
        if isinstance(data, datetime):
            self.__livres = data

    @property
    def horario_inicio(self) -> timedelta:
        return self.__horario_inicio

    @horario_inicio.setter
    def horario_inicio(self, horario_inicio: timedelta):
        if isinstance(horario_inicio, timedelta):
            self.__horario_inicio = horario_inicio

    @property
    def horario_fim(self) -> timedelta:
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, horario_fim: timedelta):
        if isinstance(horario_fim, timedelta):
            self.__horario_fim = horario_fim

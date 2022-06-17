from datetime import timedelta, datetime


class Vaga:
    def __init__(self, data: datetime, horario_inicio: timedelta, horario_fim: timedelta):
        if isinstance(data, datetime):
            self.__data = data
        if isinstance(horario_inicio, timedelta):
            self.__horario_inicio = horario_inicio
        if isinstance(horario_fim, timedelta):
            self.__horario_fim = horario_fim

    @property
    def data(self) -> datetime:
        return self.__data

    @data.setter
    def data(self, data: datetime):
        if isinstance(data, datetime):
            self.data = data

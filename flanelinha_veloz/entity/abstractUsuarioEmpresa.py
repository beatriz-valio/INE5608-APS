from abc import abstractmethod
from flanelinha_veloz.entity.abstractUsuario import Usuario
from datetime import datetime as dt, timedelta

class UsuarioEmpresa(Usuario):
    @abstractmethod
    def __init__(self, cpf: str, data_nascimento: dt, email: str, genero: str, nome: str, senha: str, sobrenome: str, cargo: str, turno: list, dias_trabalhados: list):
        super().__init__(cpf, data_nascimento, email, genero, nome, senha, sobrenome)
        if isinstance(cargo, str):
            self.__cargo = cargo
        if isinstance(turno, list):
            self.__turno = turno

    @property
    def cargo(self) -> str:
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo: str):
        if isinstance(cargo, str):
            self.__cargo = cargo

    @property
    def turno(self) -> list:
        return self.__turno

    @turno.setter
    def turno(self, turno: list):
        if isinstance(turno, list):
            self.__turno = turno

    @property
    def dias_trabalhados(self) -> list:
        return self.__dias_trabalhados

    @dias_trabalhados.setter
    def dias_trabalhados(self, dias_trabalhados: list):
        if isinstance(dias_trabalhados, list):
            self.__dias_trabalhados = dias_trabalhados

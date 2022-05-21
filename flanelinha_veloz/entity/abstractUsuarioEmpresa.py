from abc import abstractmethod
from flanelinha_veloz.entity.abstractUsuario import Usuario
from datetime import datetime as dt, timedelta

class UsuarioEmpresa(Usuario):
    @abstractmethod
    def __init__(self, cpf: str, data_nacimento: dt, email: str, genero: str, nome: str, senha: str, sobrenome: str, cargo: str): #, turno: timedelta, turnos: turno[]):
        super().__init__(cpf, data_nacimento, email, genero, nome, senha, sobrenome)
        if isinstance(cargo, str):
            self.__cargo = cargo

    @property
    def cargo(self) -> str:
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo: str):
        if isinstance(cargo, str):
            self.__cargo = cargo

from abc import ABC
from datetime import datetime as dt

class Usuario(ABC):

    def __init__(self, cpf: str, data_nacimento: dt, email: str, genero: str, nome: str, senha: str, sobrenome: str):
        if isinstance(cpf, str):
            self.__cpf = cpf
        if isinstance(data_nacimento, dt):
            self.__data_nacimento = data_nacimento
        if isinstance(email, str):
            self.__email = email
        if isinstance(genero, str):
            self.__genero = genero
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(senha, str):
            self.__senha = senha
        if isinstance(sobrenome, str):
            self.__sobrenome = sobrenome

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        if isinstance(cpf, str):
            self.__cpf = cpf

    @property
    def data_nacimento(self) -> dt:
        return self.__data_nacimento

    @data_nacimento.setter
    def data_nacimento(self, data_nacimento: dt):
        if isinstance(data_nacimento, dt):
            self.__data_nacimento = data_nacimento

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        if isinstance(email, str):
            self.__email = email
    
    @property
    def genero(self) -> str:
        return self.__genero

    @genero.setter
    def genero(self, genero: str):
        if isinstance(genero, str):
            self.__genero = genero
    
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
    
    @property
    def senha(self) -> str:
        return self.__senha

    @senha.setter
    def senha(self, senha: str):
        if isinstance(senha, str):
            self.__senha = senha
    
    @property
    def sobrenome(self) -> str:
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome: str):
        if isinstance(sobrenome, str):
            self.__sobrenome = sobrenome
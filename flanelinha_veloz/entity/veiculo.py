from datetime import timedelta


class Veiculo:
    def __init__(self, codigo: int, duracao: timedelta, nome: str,
                 preco: float):
        if isinstance(codigo, int):
            self.__codigo = codigo
        if isinstance(duracao, timedelta):
            self.__duracao = duracao
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(preco, float):
            self.__preco = preco

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def duracao(self) -> timedelta:
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao: timedelta):
        if isinstance(duracao, timedelta):
            self.__duracao = duracao

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, preco: float):
        if isinstance(preco, float):
            self.__preco = preco

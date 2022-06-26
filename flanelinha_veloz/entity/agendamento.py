from datetime import timedelta

from flanelinha_veloz.entity.cliente import Cliente
from flanelinha_veloz.entity.funcionario import Funcionario
from flanelinha_veloz.entity.servico import Servico
from flanelinha_veloz.entity.vaga import Vaga
from flanelinha_veloz.entity.veiculo import Veiculo


class Agendamento:
    def __init__(self, cliente: Cliente, duracao: timedelta,
                 funcionario: Funcionario, placa: str, servico: Servico,
                 vaga: Vaga, valor: float, veiculo: Veiculo):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        if isinstance(duracao, timedelta):
            self.__duracao = duracao
        if isinstance(funcionario, Funcionario):
            self.__funcionario = funcionario
        if isinstance(placa, str):
            self.__placa = placa
        if isinstance(servico, Servico):
            self.__servico = servico
        if isinstance(vaga, Vaga):
            self.__vaga = vaga
        if isinstance(valor, float):
            self.__valor = valor
        if isinstance(veiculo, Veiculo):
            self.__veiculo = veiculo

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.cliente = cliente

    @property
    def duracao(self) -> timedelta:
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao: timedelta):
        if isinstance(duracao, timedelta):
            self.duracao = duracao

    @property
    def funcionario(self) -> Funcionario:
        return self.__funcionario

    @funcionario.setter
    def funcionario(self, funcionario: Funcionario):
        if isinstance(funcionario, Funcionario):
            self.funcionario = funcionario

    @property
    def placa(self) -> str:
        return self.__placa

    @placa.setter
    def placa(self, placa: str):
        if isinstance(placa, str):
            self.placa = placa

    @property
    def servico(self) -> Servico:
        return self.__servico

    @servico.setter
    def servico(self, servico: Servico):
        self.servico = servico

    @property
    def valor(self) -> float:
        return self.__valor

    @valor.setter
    def valor(self, valor: float):
        if isinstance(valor, float):
            self.valor = valor

    @property
    def vaga(self) -> Vaga:
        return self.__vaga

    @vaga.setter
    def vaga(self, vaga: Vaga):
        if isinstance(vaga, Vaga):
            self.vaga = vaga

    @property
    def veiculo(self) -> Veiculo:
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, veiculo: Veiculo):
        if isinstance(veiculo, Veiculo):
            self.veiculo = veiculo

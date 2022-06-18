from flanelinha_veloz.entity.agendamento import Agendamento
from flanelinha_veloz.entity.cliente import Cliente
from flanelinha_veloz.persistence.abstractDAO import DAO


class ScheduleDAO(DAO):
    def __init__(self):
        super().__init__('/schedule_list.pkl')

    def add(self, schedule: Agendamento):
        if (schedule is not None) and \
                isinstance(schedule, Agendamento):
            data = str(schedule.vaga.data.day) + '/' + str(
                schedule.vaga.data.month) + '/' + str(
                schedule.vaga.data.year)
            super().add(self.generate_key(schedule.cliente, data), schedule)

    def get(self, cliente: Cliente, data: str):
        if isinstance(cliente, Cliente) and isinstance(data, str):
            return super().get(self.generate_key(cliente, data))

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

    def generate_key(self, cliente: Cliente, data: str):
        return str(cliente.cpf) + data

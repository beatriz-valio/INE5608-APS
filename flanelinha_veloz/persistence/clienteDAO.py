from flanelinha_veloz.entity.cliente import Cliente
from flanelinha_veloz.persistence.abstractDAO import DAO


class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('/clients_list.pkl')

    def add(self, client: Cliente):
        if isinstance(client.cpf, int) and \
                (client is not None) and \
                isinstance(client, Cliente):
            super().add(client.cpf, client)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

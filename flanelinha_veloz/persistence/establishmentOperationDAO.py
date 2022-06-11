from flanelinha_veloz.persistence.abstractDAO import DAO
from flanelinha_veloz.entity.estabelecimento import Estabelecimento


class EstablishmentOperationDAO(DAO):
    def __init__(self):
        super().__init__('/establishment_operation_list.pkl')

    def add(self, establishment_operation: Estabelecimento):

        if isinstance(establishment_operation.total_vagas, int) and \
                (establishment_operation is not None) and \
                isinstance(establishment_operation, Vagas):
            super().add(establishment_operation.total_vagas, establishment_operation)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

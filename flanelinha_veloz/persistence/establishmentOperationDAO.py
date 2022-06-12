from flanelinha_veloz.persistence.abstractDAO import DAO
from flanelinha_veloz.entity.estabelecimento import Estabelecimento


class EstablishmentOperationDAO(DAO):
    def __init__(self):
        super().__init__('/establishment_operation_list.pkl')

    def add(self, establishment_operation: Estabelecimento):
        if isinstance(establishment_operation.total_de_vagas, int) and \
                (establishment_operation is not None) and \
                isinstance(establishment_operation, Estabelecimento):
            super().add(0, establishment_operation)

    def get(self):
        return super().get(0)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

from flanelinha_veloz.entity.servico import Servico
from flanelinha_veloz.persistence.abstractDAO import DAO


class TypesOfServicesDAO(DAO):
    def __init__(self):
        super().__init__('/types_of_services_list.pkl')

    def add(self, types_of_services: Servico):
        if (isinstance(types_of_services.codigo, int)) and \
                (types_of_services is not None) and \
                isinstance(types_of_services, Servico):
            super().add(types_of_services.codigo, types_of_services)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

from flanelinha_veloz.entity.veiculo import Veiculo
from flanelinha_veloz.persistence.abstractDAO import DAO


class VehicleTypesDAO(DAO):
    def __init__(self):
        super().__init__('/vehicle_types_list.pkl')

    def add(self, vehicle_types: Veiculo):
        if (isinstance(vehicle_types.codigo, int)) and \
                (vehicle_types is not None) and \
                isinstance(vehicle_types, Veiculo):
            super().add(vehicle_types.codigo, vehicle_types)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

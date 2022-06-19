from flanelinha_veloz.persistence.abstractDAO import DAO
from flanelinha_veloz.entity.vaga import Vaga


class CarSpotDAO(DAO):
    def __init__(self):
        super().__init__('/car_spot_list.pkl')

    def add(self, car_spot: Vaga, key: int):
        if isinstance(key, int) and \
                isinstance(car_spot, Vaga):
            super().add(key, car_spot)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

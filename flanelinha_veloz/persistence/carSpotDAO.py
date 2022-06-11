from flanelinha_veloz.persistence.abstractDAO import DAO
from flanelinha_veloz.entity.vagas import Vagas


class CarSpotDAO(DAO):
    def __init__(self):
        super().__init__('/car_spot_list.pkl')

    def add(self, car_spot: Vagas):
        if isinstance(car_spot.vaga, int) and \
                (car_spot is not None) and \
                isinstance(car_spot, Vagas):
            super().add(car_spot.vaga, car_spot)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)

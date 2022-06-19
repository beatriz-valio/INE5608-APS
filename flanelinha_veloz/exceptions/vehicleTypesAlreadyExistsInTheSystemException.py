class VehicleTypesAlreadyExistsInTheSystemException(Exception):
    def __init__(self):
        super().__init__('Tipo de veículo já cadastrado!')

class TypesOfServicesAlreadyExistsInTheSystemException(Exception):
    def __init__(self):
        super().__init__('Tipo de serviço já cadastrado!')

class MissingSpotCarException(Exception):
    def __init__(self):
        super().__init__('É necessário inserir um valor!')

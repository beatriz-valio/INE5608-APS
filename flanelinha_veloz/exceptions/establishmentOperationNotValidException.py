class EstablishmentOperationNotValidException(Exception):
    def __init__(self):
        super().__init__('É necessário alterar pelo menos um valor para confirmar alterações!')

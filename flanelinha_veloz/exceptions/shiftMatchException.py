class ShiftMatchException(Exception):
    def __init__(self):
        super().__init__('Não é possível cadastrar esses turnos! Favor verificar!')

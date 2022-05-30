class EmployeesNotWritedException(Exception):
    def __init__(self):
        super().__init__('Por favor, digite um CPF.')

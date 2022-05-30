class EmployeesNotWritedException(Exception):
    def __init__(self):
        super().__init__('\033[91m \Por favor, digite um CPF.\n\033[0m')

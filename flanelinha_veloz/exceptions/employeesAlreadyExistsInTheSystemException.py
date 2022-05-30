class EmployeesAlreadyExistsInTheSystemException(Exception):
    def __init__(self):
        super().__init__('O funcionário informado já existe no sistema!')

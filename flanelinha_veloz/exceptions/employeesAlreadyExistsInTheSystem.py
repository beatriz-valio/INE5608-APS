class EmployeesAlreadyExistsInTheSystem(Exception):
    def __init__(self):
        super().__init__("\033[91m \nO funcionário informado já existe no sistema\n\033[0m")

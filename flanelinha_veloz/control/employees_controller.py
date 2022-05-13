from entity.employees import Employees
from view.employees_boundary import EmployeesBoundary

class EmployeesController:
    def __init__(self, system_controller) -> None:
        self.__system_controller = system_controller
        self.__boundary = EmployeesBoundary()

    def add_employee(self) -> Employees:
        pass

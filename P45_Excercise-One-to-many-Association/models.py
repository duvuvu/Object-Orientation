# Department 1 -------> 0..n Employee
import models_da

class Employee:
    def __init__(self, number, first_name, surname, birth_date, department): # department: call by object reference
        self.__number = number
        self.__first_name = first_name
        self.__surname = surname
        self.__birth_date = birth_date
        #-------------------------------------------
        self.__department = department # relation - link attribute
        #-------------------------------------------

    @property
    def number(self):
        return self.__number
    
    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def surname(self):
        return self.__surname
    
    @property
    def birth_date(self):
        return self.__birth_date

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @birth_date.setter
    def birth_date(self, birth_date):
        self.__birth_date = birth_date

     #-----------------------------------------------------
    @property # Association management methods
    def department(self):
        return self.__department
    
    @department.setter # Association management methods
    def department(self, department):
        self.__department = department
     #-----------------------------------------------------

class Department:
    def __init__(self, number, name):
        self.__number = number
        self.__name = name
        #-------------------------------------------
        self.__employees = None # relation - link attribute
        #-------------------------------------------

    @property
    def number(self):
        return self.__number
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

     #-Lazy loading----------------------------------------------------
    @property # Association management methods
    def employees(self):
        if self.__employees is None:
            self.employees = models_da.EmployeeDA().find_by_department(self)
    
    def add_employee(self, employee): # Association management methods
        self.__employees.append(employee)

    def remove_employee(self, employee): # Association management methods
        self.__employees.remove(employee)
     #-----------------------------------------------------
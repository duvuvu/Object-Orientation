# Employee 1 <-------> 0..1 Company Car

class Employee:
    def __init__(self, number, first_name, surname):
        self.__number = number
        self.__first_name = first_name
        self.__surname = surname
        #-Link attribute----------------------------
        self.__company_car = None
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
    
    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def naam(self):
        return self.__first_name + " " + self.__surname

    #-Association management methods----------------------
    @property
    def company_car(self):
        return self.company_car
    
    @company_car.setter
    def company_car(self, company_car):
        self.__company_car = company_car
    #-----------------------------------------------------

class CompanyCar:
    def __init__(self, registration, license_plate, employee):
        self.__registration = registration
        self.__license_plate = license_plate
        #-Link attribute----------------------------
        self.__employee = employee
        employee.company_car = self
        #-------------------------------------------

    @property
    def registration(self):
        return self.__registration
    
    @property
    def license_plate(self):
        return self.__license_plate
    
    @license_plate.setter
    def license_plate(self, new_license_plate):
        self.__license_plate = new_license_plate

    #-Association management methods----------------------
    @property
    def employee(self):
        return self.__employee
    
    @employee.setter
    def employee(self, employee):
        self.__employee = employee
        employee.company_car = self
    #-----------------------------------------------------
class Employee:
    def __init__(self, number, first_name, surname):
        self.__number = number
        self.__first_name = first_name
        self.__surname = surname
        self.__company_car = None # relation - link attribute

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
    def first_name(self, new_first_name):
        self.__first_name = new_first_name

    @surname.setter
    def surname(self, new_surname):
        self.__surname = new_surname

class CompanyCar:
    def __init__(self, registration, license_plate, employee):
        self.__registration = registration
        self.__license_plate = license_plate
        self.__employee = employee

    @property
    def registration(self):
        return self.__registration
    
    @property
    def license_plate(self):
        return self.__license_plate
    
    @license_plate.setter
    def license_plate(self, new_license_plate):
        self.__license_plate = new_license_plate
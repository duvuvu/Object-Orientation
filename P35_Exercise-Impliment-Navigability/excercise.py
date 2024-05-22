class Adress:
    def __init__(self, street, town):
        self.__street = street
        self.__town = town

class Department:
    def __init__(self, address, name):
        self.menbers = [] # relation
        self.__adrdress = address # relation
        self.__name = name
    
    # getters and setters
        
    def add_member(self, member):
        self.members.append(member)
    
    def show_members(self):
        pass

class StaffMember:
    def __init__(self, department, first_name, surname):
        self.__department = department # relation
        self.__department.add_member(self) # relation
        self.__first_name = first_name
        self.__surname = surname
    
    # getters and setters
        
    def show_data(self):
        pass

adressTAC = Adress("Grote markt 32", "Antwerpen")
departmentMKT = Department(adressTAC, "Marketing")
jozef = StaffMember(departmentMKT, "Jozef", "Goosens")
class Department:
    def __init__(self, name):
        #-Link attribute----------------------------
        self.members = []
        #-------------------------------------------
        self.name = name
    
    # getters and setters
        
    def add_staff_member(self, member):
        self.members.append(member)

    def show_members(self):
        pass

class StaffMember:
    def __init__(self, department, first_name, surname):
        #-Link attribute----------------------------
        self.__department = department
        self.__department.add_staff_member(self)
        #-------------------------------------------
        self.__firstname = first_name
        self.__surname = surname

    def show_data(self):
        pass

departmentMKT = Department("Marketing")
jozef = StaffMember(departmentMKT, "Jozef", "Goossens")
peter = StaffMember(departmentMKT, "Peter", "De Grootte")
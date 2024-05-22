class Patient:
    def __init__(self, new_name, new_length, new_weight):
        self.__name = new_name
        self.__length = new_length
        self.__weight = new_weight

    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    # Other getters and setters...

peter = Patient("Peter Martens", 1.90, 92.5)
peter.weight = 94
print("Peter weighs", peter.weight, "kg")
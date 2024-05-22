class Patient:
    def __init__(self, new_name, new_length, new_weight):
        self.name = new_name
        self.length = new_length
        self.weight = new_weight

    def show_bmi(self): # Method of class - definition
        bmi = self.weight / self.length ** 2
        print("The BMI of", self.name, " is:", round(bmi, 2))

jan = Patient("Jan De Vos", 1.75, 70.0)
peter = Patient("Peter Martens", 1.90, 92.5)

jan.show_bmi() # Method of class - call: self = objecct (jan or peter)
peter.show_bmi() # Method of class - call
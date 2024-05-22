class Patient:
    def __init__(self, new_name, new_length, new_weight):
        self.name = new_name
        self.length = new_length
        self.weight = new_weight

    def calculate_bmi(self): # Private Method - cannot be called from outside
        return self.weight / self.length ** 2

    def show_bmi(self):
        print("The BMI of", self.name, " is:", round(self.calculate_bmi(), 2))

jan = Patient("Jan De Vos", 1.75, 70.0)
peter = Patient("Peter Martens", 1.90, 92.5)

jan.show_bmi() 
peter.show_bmi() 
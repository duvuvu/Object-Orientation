# Object-Orientation

## Table of Contents  


## Classes and Objects

- **Object**: a representation of a "thing", often from the real world (anthropomorphism) with specific characteristics

- **Class**: group objects with the same characteristics: attributes (data), and operations (behaviour). An object is and is an *instance* of a class

- **Hint**: "Car" is a class, **a** car is an instance/object

- **Informational cohesion: data belongs to one object, which data is determined by the class

- **Anthropomorphism**: a class often represents a thing of the real world, the attributes and properties of that thing

- Remark
  - Use the Python notation in illustrating UML diagrams
  - A constructor is necessary in Python

## Classes with attributes in Python

- Keyword **class** with name of class
  - Recommended **naming convention**: PascalCase: e.g. ***class*** **Patient** or ***class*** **PatientFile**
- **Object attributes** (also: **instance-attributes**): e.g. ***self***.weight
  - Recommended naming convention: snake_case
  - ***self*** refers to the **instance**, not the class
  - Most program languages define attributes on class level
  - In Python: only initialized in the ***constructor*** method of a class. During object creation, the constructor method will be called automatically. Class attributes in Python are static

  ![image](https://github.com/duvuvu/Object-Orientation/assets/128236962/7359388c-83db-4f85-bbea-9ab121508923)

## Example Python: Patient

```python
class Patient:
    def __init__(self, new_name, new_length, new_weight):
        # Declaration/initialization object attributes
        self.name = new_name
        self.length = new_length
        self.weight = new_weight

# Instaces/objects
jan = Patient("Jan De Vos", 1.75, 70.0)
peter = Patient("Peter Martens", 1.9, 92.5)

print("Weight of Peter:", peter.weight) # peter.weight: read object attribute

bmi = round(jan.weight / jan.length ** 2, 1)
print("The BMI of Jan De Vos is:", bmi)

bmi = round(peter.weight / peter.length ** 2, 1)
print("The BMI of Peter Martens is:", bmi)
```

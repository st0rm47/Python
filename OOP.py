#--->OOP

###--->Classes and Objects
class Student:  #class
    occupation = "Student" #default value
    #Constructor function
    def __init__(self,name,house):
        #instance variables
        self.name = name
        self.house = house
   
    #Methods function
    def study(self,book):
        self.book = book
        print(f"{self.name} is studying {self.book}")

def main():
    #create object
    student1 = Student("Subodh","Kathmandu")
    student2 = Student("Priyanka", "Itahari")
    
    #access instance variables
    print(student1.name, student1.house)
    print(student2.name, student2.house)
    
    #access methods
    student1.study("ML")
    student2.study("AI")
    
    #access class variable
    print(student2.occupation)  
    
if __name__ == "__main__":
    main()
    

###--->Inheritance

#Base Class
class Father:
    def __init__(self,hairline,height):
        self.hairline = hairline
        self.height = height
    
    def display(self):
        print(f"Father has {self.hairline} hairline and {self.height} height")

# Derived Class
class Son(Father):
    def __init__(self,weight,hairline,height):
        super().__init__(hairline,height)
        self.weight = weight
            
    def display(self):
        super().display()
        print(f"Son has {self.hairline} hairline, {self.height} height, and {self.weight} weight")

def main():
    # Create objects
    son1 = Son("70","Straight","5.8")
    # Access instance variables
    son1.display()

if __name__ == "__main__":
    main()

#Method Overriding
class Father:
    def __init__(self, hairline, height):
        self.hairline = hairline
        self.height = height
       
    def display(self):
        print(f"Father has {self.hairline} hairline and {self.height} height")

class Son(Father):
    def __init__(self, hairline, height, weight):
        super().__init__(hairline, height)
        self.weight = weight
        
    def display(self):
        super().display()

def main():
    father1 = Father("Curly", "5.5")
    son1 = Son("Straight", "5.8", "70")
       
    father1.display()
    son1.display()

if __name__ == "__main__":
    main()
    
#Multiple Inheritance
class Father:
    def __init__(self, hairline, height):
        self.hairline = hairline
        self.height = height
       
    def display(self):
        print(f"Father has {self.hairline} hairline and {self.height} height")

class Mother:
    def __init__(self, haircolor, skincolor):
        self.haircolor = haircolor
        self.skincolor = skincolor
       
    def display(self):
        print(f"Mother has {self.haircolor} haircolor and {self.skincolor} skincolor")

class Son(Father, Mother):
    def __init__(self, hairline, height, haircolor, skincolor):
        Father.__init__(self, hairline, height)
        Mother.__init__(self, haircolor, skincolor)
        
    def display(self):
        Father.display(self)
        Mother.display(self)

def main():
    son1 = Son("Curly", "5.5", "Black", "White")
    son1.display()

if __name__ == "__main__":
    main()



###--->Polymorphism
    #Method Overriding
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display(self):
        pass

class Car(Vehicle):
    def display(self):
        print(f"Car brand is {self.brand} and model is {self.model}")

class Bike(Vehicle):
    def display(self):
        print(f"Bike brand is {self.brand} and model is {self.model}")

def main():
    car1 = Car("Toyota","Corolla")
    bike1 = Bike("Honda","CBR")
    
    for vehicle in (car1, bike1):
        print(vehicle.brand)
        print(vehicle.model)
        vehicle.display()
    
if __name__ == "__main__":
    main()
 

   
###--->Encapsulation
# Demonstrating private and protected access specifiers
class Employee:
    def __init__(self, name, salary):
        self._name = name  # protected attribute
        self.__salary = salary  # private attribute

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary

def main():
    emp1 = Employee("Alice", 50000)
    
    # Accessing protected attribute
    print("Employee name:", emp1.get_name())
    emp1.set_name("Bob")
    print("Updated employee name:", emp1.get_name())
    
    # Accessing private attribute (will not work)
    # print("Employee salary:", emp1.__salary)  # This line will cause an AttributeError
    
    # Updating private attribute (will not work)
    # emp1.__salary = 60000  # This line will not update the salary
    
    # Accessing private attribute through getter method
    print("Employee salary:", emp1.get_salary())
    emp1.set_salary(60000)
    print("Updated employee salary:", emp1.get_salary())

if __name__ == "__main__":
    main()


###--->Abstraction

from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Concrete classes
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Function to make animals speak
def make_animal_speak(animal):
    print(animal.make_sound())

def main():
    animals = [Dog(), Cat()]
    for animal in animals:
        make_animal_speak(animal)

if __name__ == "__main__":
    main()


































# #Raise
# class Student:  #class
#     #Constructor function
#     def __init__(self,name,house):
#         if not name or not house:
#             raise ValueError("Name and House are required")
#         #instance variables
#         self.name = name
#         self.house = house
    
# def main():
#     #create object
#     student1 = Student("","")
#     #access instance variables
#     print(student1.name, student1.house)

# if __name__ == "__main__":
#     main()


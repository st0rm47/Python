#--->OOP

#Classes and Objects
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
    
#-->Inheritance
#Base Class
class Father:
    def __init__(self, hairline, height):
        self.hairline = hairline
        self.height = height
    
    def display(self):
        print(f"Father has {self.hairline} hairline and {self.height} height")

#Derived Class        
class Son(Father):
    def __init__(self, hairline, height, weight):
        super().__init__(hairline, height)
        self.weight = weight
    
    def display(self):
        print(f"Son has {self.hairline} hairline, {self.height} height and {self.weight} weight")

def main():
    #create object
    father1 = Father("Curly", "5.5")
    son1 = Son("Straight", "5.8", "70")
    
    #access instance variables
    father1.display()
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


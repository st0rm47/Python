# #--->OOP

# #Classes and Objects
# class Student:  #class
#     #Constructor function
#     def __init__(self,name,house):
#         #instance variables
#         self.name = name
#         self.house = house
    
#     #Methods fucntion
#     def study(self,book):
#         self.book = book
#         print(f"{self.name} is studying {self.book}")

# def main():
#     #create object
#     student1 = Student("Subodh","Kathmandu")
#     #access instance variables
#     print(student1.name, student1.house)
    
#     #access methods
#     student1.study("ML")
    
# if __name__ == "__main__":
#     main()
    

#Raise
class Student:  #class
    #Constructor function
    def __init__(self,name,house):
        if not name or not house:
            raise ValueError("Name and House are required")
        #instance variables
        self.name = name
        self.house = house
    
def main():
    #create object
    student1 = Student("","")
    #access instance variables
    print(student1.name, student1.house)

if __name__ == "__main__":
    main()


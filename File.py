#-->File handling

#-->Writing a file
file = open("Testing.txt","w")
# w stands for writing mode and will create a file if not exist
file.write("Hello World \nHello Nepal \nHello Sir")
#writes into a new file
file.close()
    #When a file is opened in write mode, exisiting the content is deleted


#-->Reading a file
file = open("Testing.txt","r")
# r stands for reading mode
print(file.read(2))
# argument takes 1 character as 1 byte and prints it
print(file.read())
# after 2 characters are printed it prints the remaining characters


#-->Reading each line in a file
for line in file:
    print(line)
    #OR we can use file.readlines() function
file.close()


#Example:
file1 = open("Testing.txt","r")
n = int(input())
results = file1.readlines()
#reads all lines from file
print(results[n])
#prints only the line given as argument

#Example:
names = ["John", "Hari", "Osama"]
file = open("names.txt", "w+")
for i in names:
    file.write(i+"\n")
file.close()
file = open("names.txt","r")
print(file.read())
file.close()


#-->Appending in a file
file = open("names.txt", "a")
file.write("Ram")
file.close()


#-->WITH
with open("names.txt") as f:
    print(f.read())
    #automate the closing of a file
    
#Example:
file = open("Testing.txt", "r")
s = file.readlines()
    #Reads every lines and stores in s 
for line in s:  
    # Iterates throuugh every line and strip() removes the spaces
    s1 = line.strip()
    print(line[0]+str(len(s1)))
    #Line(0) prints 1st letter and len prints the length after spaces removed   
file.close()


#-->CSV 
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")
for student in sorted(students):
    print(student)

students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name":name, "house":house}
        students.append(student)
def get_name(student):
    return student["name"]      
for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")
    

#Same using Lambda
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name":name, "house":house}
        students.append(student)
        
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
    
    
#-->CSV Library
import csv
students=[]
with open("students1.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name":row[0], "house":row[2]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
   
   
#DictReader
import csv
students = []
with open("students1.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
 
  
#DictWriter
import csv
name = input("Name: ")
home = input("Home: ")
with open("students2.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames= ["name","home"])
    writer.writerow({"name":name, "home":home})
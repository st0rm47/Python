#Basics Day 1

print(2+3) #"+" --> addition
#ans-->5 
print(11/2) #"/" --> division
#ans-->5.5
print(2*5) #"*" --> multiply
#ans-->10 
print(2**5) #"**" --> power
#ans-->32 
print(21//5) #"//" --> quotient
#ans-->4
print(30 % 5) #"%" --> remainder
#ans-->0


#--->String
print("Hello")
print('Hello')
print('"I\'m a good person"')


#--->New Lines
print("One \n Two")
print("Name \t Age \t Contact")
print("""He is a good 
      boy father 
      son""")


#--->String Concatenate
print('Hello ' + "Ma'am")
print("2"+'2')
print("World " * 2)


#--->Variables
msg="Hello"
name="Ma'am"
print(msg+" "+name)


#--->Type Conversion
x="5"
y="9"
print(int(x)+int(y))


# #--->User Inputs
# name=input("Enter your Name: ")
# print("His name is " + name)

# age=int(input("Enter your age: "))
# print("His age is " + str(age))     #Making integer to string to concatenate

age=input()
print(type(age))    #displays the data type of age

#--->Operators
a=10
print(a)            #10
print(a<5)          #False
print(a>5)          #True
print(a>=10)        #True
print(a<10)         #False
print(a!=5)         #True


#--->Control Flow
#If statements
num=10
if num >4:
    print("Number is greater than 4")
    if num <15:
        print("Number is less than 15")
        if num==10:
            print("Number is equals to 10")
            
#Else statements
if num>4:
    print("True")
else:
    print("False")          

#Elif statements
num = 15;
if num==1:
    print("One")
elif num==2:           #Else if written as elif
    print("Two")
elif num==3:
    print("Three")
else:
    print("Fifteen")


#--->Boolean Logic
a=10
b=20
print(a==a and b==b)        #True
print(a==b or b==b)         #True
print(not a==b)             #True

if not True:
    print("1")
elif not(1+1==2):
    print("2")
else:
    print("Anything")
    
    
#--->Loops
#while loop
a = 10
while a >=0:
    print("Hello")
    a=a-1
    
#break and continue
    total=0
    i=0
    while i<5:
        age=int(input("Enter your age: "))
        i+=1
        if age <3:
            continue
        total+=100
        if age >5:
            break
    print(total)
    

    
#--->Functions
#def refers to defining a function
def pretty():
    print("You are pretty")
    
pretty()

#Function with arguments
def print_word(x):
    print("My name is " + x)
print_word("World")

def operations(x,y):
    print(x+y)
    print(x*y)
    print(x/y)
operations(4,2)

#EX:Feet into inches
feet=int(input("Enter feet: "))
def convert(x):
    print(str(feet)+ " feet is " + str(x*12) + " inches")
convert(feet)
    
#Returning from a Function
def maxi(x,y):
    if x>y:
        return x
    else:
        return y
    print("Any code written after return is not printed")
print(maxi(5,8))
print(maxi(7,9))


#Example: Write a function that takes a string and a letter as its arguments 
#And returns the count of the letter in the string.
x=input("Enter a string: ")
y=input("Enter a letter: ")

def letter(x,y):
    c=0
    for a in x:
        if a==y:
            c+=1
    return c

print(letter(x,y))



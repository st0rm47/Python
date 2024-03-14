###--->Making a Simple Calculator

def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

print("Select Operands: \n"
      "1. Addition \n"
      "2. Subtraction \n"
      "3. Multiplication \n"
      "4. Division \n")

#Taking input from the user about the operations and numbers
operand=int(input("Select Operations: "))
a=int(input("Enter 1st Number: "))
b=int(input("Enter 2nd Number: "))

#Conditions on which operand willbe performed
if operand == 1:
    print(a,"+", b, "=", addition(a,b))
elif operand == 2:
    print(a,"-", b, "=", subtraction(a,b))
elif operand == 3:
    print(a,"*", b, "=", multiplication(a,b))
elif operand == 4:
    print(a,"/", b, "=", division(a,b))
else:
    print("Invalid Operand")
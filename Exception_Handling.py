#--->Exception Handling

try:
    variable = 10
    print(10/2)
except:
    print("Error")
else:
    print("Code Executed")

#Example:
try:
    x=0
    print("hello"+x)
except ZeroDivisionError:
    print("Divided by Zero")
except TypeError:
    print("Typing Mistake")
except ValueError:
    print("Wrong Value")
else:
    print("Code Executed")
#else runs when there is no exception
    
#Example:   
pin = input()
try:
	int(pin)
	print("PIN code is created")
except ValueError:
	print("Please enter a number")


# Raising Exceptions and Pass
try:
    print(1/0)
except ZeroDivisionError:
    raise ValueError
    pass
# raise creates another error
# pass doesnot warns the user about the error
    
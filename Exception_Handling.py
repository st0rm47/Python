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
    
    
#Example:
while True:
    frac=input("Fraction: ")
    try:
        x, y =frac.split("/")
        x=int(x)
        y=int(y)
        fuel=x/y
        if fuel<=1:
            break
    except(ValueError,ZeroDivisionError):
        pass
p=int(fuel*100)
if p<=1:
    print("E")
elif p>=99:
    print("F")
else:
    print(f"{p}%")
    

#Example:
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()
    try:
        if "/" in date:
            month, day, year = date.split("/")
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                print(f"{year}-{int(month):02}-{int(day):02}")
                break

        if "," in date:
            month_str, day_str, year = date.split(" ")
            if month_str in months:
                day = day_str.replace(",", "")
                day = int(day)
                month = months.index(month_str) + 1
                if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                    print(f"{year}-{int(month):02}-{int(day):02}")
                    break

    except(ValueError, IndexError):
        pass



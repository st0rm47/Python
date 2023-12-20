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


#Tip Calculator
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    dollars = d.removeprefix("$")
    return float(dollars)

def percent_to_float(p):
    percent = p.removesuffix("%")
    percentage = float(percent) / 100
    return float(percentage)

main()



#Meal Time Converter
def main():
    time_input=input("What time is it? ")
    time, am_pm= time_input.split(" ")
    x=convert(time,am_pm)

    if 7<= x <=8:
        print("breakfast time")
    elif 12<= x <=13:
        print("lunch time")
    elif 18<= x <=19:
        print("dinner time")

def convert(time,am_pm):
    hours, minutes=time.split(":")
    if am_pm.lower()=="pm":
        hours=float(hours)+12
    minutes=float(minutes)/60
    hours=float(hours)+float(minutes)
    return hours


if __name__ == "__main__":
    main()
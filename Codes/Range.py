#--->Range

#range() can be used to create a number sequence
#list() can be used to output a range of numbers
numbers=list(range(15))
print(numbers)

numbers=list(range(10,15))
print(numbers)

#range(20)=0 to 19
#range(3,7)=3 to 6

numbers=list(range(4,20,2))
print(numbers)

numbers=list(range(4,-20,-2))
print(numbers)


#For loop in Range
for i in range(5):
    print ("Namaste")
    
n=int(input("Enter a number"))
for x in range(2,n,2):
    print(x)
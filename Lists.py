#--->Lists
#indexing always starts from 0
names=["Subodh", "Priyanka" ,"Firoj" ,"Rohan" ,"Ram"]
names[4]="Melin"
print(names[4][2])


#String as a list
x="Ramesh"
print(x[5])


#Rows and Column
seats =[['a', 'b', 'c'],
        ['d', 'e', 'f'],
        ['g', 'h', 'i'],
        ['j', 'k', 'l']]
row=int(input())
column=int(input())
print(seats[row][column]) 


#Operations in List
print(x+" "+"Basnet")

y=[1,2,3,4,5]
y+=[6,7,8,9,10]
print(y[7])

num=[1,2,3,4,5,6,7,8,9,10]
num[5]-=num[4]
print(num)
if 1 in num:
    print(num[5])
else:
    print("Not Available")


#--->For Loop in Lists
name=["Subodh", "Priyanka" ,"Firoj" ,"Rohan" ,"Ram"]
for n in name:
    print(n+ ", ")
#Here n represents name of people in the list

nums=[4,7,3,1]
for x in nums:
    print(x*2)
    
    
# #Shopping Market
# cart=[120,42,15,9,5,380]
# d=int(input()) #takes integer as an input
# total=0
# for c in cart: #c represnts each item in cart in loop
#     dis=c-(c*d/100) #Formula to find discount on each product
#     total+=dis
# print(total)


#List Slices
numbers_squares=[0,1,4,9,16,25,36,49,64,81,100,121,144,169]
print(numbers_squares[0:2])      #Prints from index 0 to index 2
print(numbers_squares[:3])       #Prints upto index 3
print(numbers_squares[3:])       #Prints from index 3 to all
print(numbers_squares[:13:2])    #Prints from index 0 to index 13 with gap of 1
print(numbers_squares[::-2])     #Prints reversely with gap of 1


#Reverse a String
x="Hello World"
print(x[::-1])


#List Functions
num=[1,2,3,4,5,1,8,5,2,3,5]
num[6]=2
num[8]=8
print(num)
print(len(num))         #count the total numbers
num.append(10)          #add an item to the list
print(num)
num.insert(5,6)         #insert an item to desired location
print(num)
print(num.index(5))     #to find the first occurence
print(max(num))         #maximum value
print(min(num))         #minimum value
print(num.count(5))     #counts the number of times it is repeated
(num.reverse())         #reverse whole list
print(num)
print(num[8:5:-1])

if all([i>5 for i in num]):
    print("All numbers larger than 5")
    #prints only if all numbers > 5
if any(i%2 == 0 for i in num):
    print("At least one is even")
    #prints if any number is even
for v in enumerate(num):
    print(v)
    #enumerate function makes indices of a list


#--->String Functions
print(", ".join(["USA","UK","China","Japan"]))
#prints (USA, UK, China, Japan)

print("Namaste Nepal".replace("Nepal", "Kathmandu"))
#prints (Namaste Kathmandu)

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("world".upper())
#Uppercase

print("WORLD".lower())
#Lowercase

print('China,Aus,Uk, US'.split(" "))
#Split by searching ,



#File Extensions
file_extensions = [
    ('.gif', 'image/gif'),
    ('.jpg', 'image/jpeg'),
    ('.jpeg', 'image/jpeg'),
    ('.png', 'image/png'),
    ('.pdf', 'application/pdf'),
    ('.txt', 'text/plain'),
    ('.zip', 'application/zip')
]

x = input("Enter the name of a file: ")
y = x.lower().strip()

found = False
for ext, content_type in file_extensions:
    if y.endswith(ext):
        print(content_type)
        found = True
        break
else:
    print("application/octet-stream")



#--->List Comprehensions
#Creating a list
cubes=[i**3 for i in range(10)]
print(cubes)

evens=[i for i in range(10) if i%2 ==0]
print(evens)
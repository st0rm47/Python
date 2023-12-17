#--->Lists
#indexing always starts from 0
names=["Subodh", "Priyanka" ,"Firoj" ,"Rohan" ,"Ram"]
print(names[1][6])


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


#Shopping Market
cart=[120,42,15,9,5,380]
d=int(input()) #takes integer as an input
total=0
for c in cart: #c represnts each item in cart in loop
    dis=c-(c*d/100) #Formula to find discount on each product
    total+=dis
print(total)
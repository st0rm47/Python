##---> Functional Programming

#Bases around functions
def test(func, arg):
    return func(func(arg))
def mult(x):
    return x*x
print(test(mult,2))
    #Here it prints value 16
    #x=2 and the mult function returns it as 4
    #Then x=4 and again the test func recalls to do mult function which returns 16
    
###---> Lambdas
    # Anonymous Functions
    # Keyword : lambda
def polynomial(x):
    return x**2 + 5*x +4
print(polynomial(4))

#Same using lambda
result = (lambda x : x**2 +5*x +4) (4)
print(result)
"""
x ==> input argument
x**2 +5*x +4 ==> return value
4 ==> argument value
"""
product = (lambda x,y : x*y) (3,4)
print(product)

triple = lambda x: x * 3
add = lambda x, y: x + y
print(add(triple(3), 4))
    # sends x =3 in triple function
    # sends value from triple and 4 to add function
    
    
###---> MAP
    # Takes two arguments: function and iterables(list,tuple etc)
def add(x):
    return x + 5
nums = [1,2,3,4,5]
result = list(map(add,nums))
print(result)
    # add ==> function
    # nums ==> iterables

#Map using lambda
nums = [12,13,14,15]
print(list(map(lambda x : x+5, nums)))

numbers1 = (1,2,3)
numbers2 = (4,5,6)
result = map(lambda x,y :x+y, numbers1, numbers2)
print(tuple(result))

#String Modification using Map
l = ['sat', 'bat']
test = tuple(map(list, l))
print(test)



###---> Filter
    # Removes items that dont match a function
    
nums = [11,22,33,44,55]
result = list(filter(lambda x : x%2==0, nums))
print(result)
    # prints even numbers only

names = ['Subodh', 'Priyanka', 'Firoj', 'Melin']
result = list(filter(lambda x : len(x)> 5, names))
print(result)



###---> Generators
    # can be created using functions and yield statements
    # yield ==> replaces return
    
def countdown():
    i = 5
    while i >0:
        yield i
        # returns data one at a time
        i-=1
for i in countdown():
    print(i)

txt = input()
def words(txt):
   for word in txt.split(" "):
        yield word

print(list(words(txt)))


###---> Decorators
    # function that takes a function and returns by adding some functionality
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
def ordinary():
    print("I am ordinary")
decorated_func = make_pretty(ordinary)
decorated_func()

# @ Symbol with Decorators 
@make_pretty
def handsome():
    print("He's handsome")
handsome()


###---> Enumerate

names = ("Subodh", "Priyanka", "Melin", "Firoj", "Nikita" , "Saugat")
print(list(enumerate(names)))

for i, names in enumerate(names):
    print(i+1, names)
    
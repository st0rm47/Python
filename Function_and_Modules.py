#-->Function and Modules

#Code Reuse
#--> Follows DRY - Dont Repeat Yourself
#--> Avoid WET - Write Everyting Twice

#-->Module
#import module_name at the top of your code
#module_name.var to acess functions

#-->Random
import random
output = random.choice(["HEAD", "TAIL"])
print(output)

value= random.randint(1,5)
print(value)

values = random.randrange(1,10,2)
print(values)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
    
#-->Statistics
import statistics
values=statistics.mean([100,110])
print(values)

value=statistics.mode([1,2,3,4,6,5,1,1,2,3])
print(value)

#-->Math
import math
print(math.sqrt(64))

#Only imports pi from math module
from math import pi
print(pi)

from math import sqrt as square_root
print(square_root(100))

#-->Sys
import sys
print("Hello my name is", sys.argv[0])

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)


#-->APIs
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())

#-->Date and Time
import datetime
x=datetime.datetime.now()
print(x.year)

#-->Packages
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
    
    
    
import emoji
var=str(input("Input:")).strip().lower()
z=emoji.emojize(var)
print(z)


#Example:
import random
while True:
    try:
        x=int(input("Level:"))
        x=int(x)
        if x >0:
            break
    except ValueError:
        pass

value=random.randint(1,x)
while True:
    try:
        y=int(input("Guess:"))
        y=int(y)
        if y>0:
            if y==value:
                print("Just right!")
                break
            elif y> value:
                print("Too large!")
            else:
                print("Too small!")
    except ValueError:
        pass


#Math Problem
import random
def main():
    count= 0
    n = get_level()
    for i in range(10):
        x, y = generate_integer(n)
        for j in range(3):
            try:
                answer = int(input(f"{x} + {y} ="))
            except ValueError:
                pass
            else:
                if answer == x + y:
                    count = count + 1
                    break
                else:
                    print("EEE")
                    if j == 2:
                        print(f"{x} + {y} = {x+y}")
    print("Score: ", count)

def get_level():
    while True:
        try:
            z = int(input())
            if 0 < z < 4:
                return z
            else:
                raise ValueError
        except ValueError:
            pass

def generate_integer(level):
        min = 10**(level-1)
        max = 10**level-1
        x = random.randint(min,max)
        y = random.randint(min,max)
        return x,y


if __name__ == "__main__":
    main()

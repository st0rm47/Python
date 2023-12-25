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
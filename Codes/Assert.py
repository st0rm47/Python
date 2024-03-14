#--> Assertions
print("Hello")
assert 2+2==4
print ("True")


temp = -10
assert (temp >= 0), "Colder than absolute zero!"
print(temp)
#If the argument is true the program continues
#If the argument is false it raises exception


try:
    assert 2*2==5
except AssertionError:
    print("2*2 is 4")
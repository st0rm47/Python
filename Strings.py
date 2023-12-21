#--->String
print("Hello")
print('Hello')
print('"I\'m a good person"', end=".\n")

#Formatting Strings
name = input("What's your name? ")
name=name.strip().title()
print(f"hello, {name}")
#strip removes whitespace
#title capitalize the letter of each word
# f treats the string in a special way


x=input("camelCase: ")
print("snake_case: ",end="")
for c in x:
    if c.isupper():
        print("_"+c.lower(),end="")
    else:
        print(c,end="")
#isupper() checks whether there is uppercase or not
#lower() lower cases the text
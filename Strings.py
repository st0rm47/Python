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


#Example:
x=input("camelCase: ")
print("snake_case: ",end="")
for c in x:
    if c.isupper():
        print("_"+c.lower(),end="")
    else:
        print(c,end="")
#isupper() checks whether there is uppercase or not
#lower() lower cases the text

#Twitter
x=str(input("Input: "))
print("Output: ",end="")
for c in x:
    if c.lower() not in ['a','e','i','o','u']:
        print(c,end="")


#Number Plates
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 6 >= len(s) >=2 and s[0:2].isalpha() and s.isalnum():
        for c in s:
            if c.isdigit():
                index=s.index(c)
                if s[index:].isdigit() and c!= '0':
                    return True
                else:
                    return False
        return True

main()

#isalpha() checks whether it is alphabets or not
#isalnuma() checks whether it is alphabets and numbers only or not
#isdigit() checks whether it is digits only or not

#format function enables us to place values in the placeholders
msg="{3}{1}{2}{0}".format("Subodh ","Priyanka ","Nikita ","Melin ")
print(msg)
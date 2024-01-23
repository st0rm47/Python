#--->Regular Expressions
#Helps us to examine patterns

#Simple Example:
email= input("Email:").strip()
username, domain = email.split("@")
if username and "." in domain:
    print("Valid")
else:
    print("Invalid")


#Same using RegEX
import re
email= input("Email:").strip()
if re.search(r"^[^@]+@[^@]+\.edu$", email):
    # "." refers any character except a new line
    # "+" refers repitions of characters 1 or more time
    # "\" refers to escape character which used to introduce string
    # "$" refers to the end of string 
    # "^" refers to the start of string
    # "r" refers to treat the string as raw string
    # "[^@]+" refers to any character except an @
    print("Valid")
else:
    print("Invalid")
    
    
#Checking that the email should be alphanumeric
import re
email= input("Email:").strip()
if re.search(r"^\w+@[a-zA-Z0-9_]+\.(com|edu|gov|net|co|org)$",email):
    # "[a-zA-Z0-9_]" tells the validation of characters
    # "\w" refers to the validation of characters
    # "|" refers to OR
    print("Valid")
else:
    print("Invalid")
    
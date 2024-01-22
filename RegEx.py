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
if re.search(".+@.+\.gmail", email):
    print("Valid")
else:
    print("Invalid")
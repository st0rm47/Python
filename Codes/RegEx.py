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


#Case-Sensitive Check
import re
email= input("Email:").strip()
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    # re.IGNORECASE ignores the sensitive cases
    # (\w+\.) refers to a new expression and can be there once or not at all
    # ? matches zero or one occurrence of the pattern left to it.
    print("Valid")
else:
    print("Invalid")
 
    
#Extracting User Input
import re
url = input("URL: ").strip()
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
    # sub is used to replace the string [sub(pattern, repl, string)]
print(f"Username: {username}")

import re
url = input("URL: ").strip()
if matches := re.search(r"^(https?://)?(www\.)?twitter\.com/([a-zA-Z0-9_]+)$", url, re.IGNORECASE):
    # ([a-zA-Z0-9_]) refers to the group of characters
    # + indicates the repetition of characters
    # search value is stored in matches
    print(f"Username:", matches.group(3))
    

#Examples:
import re
def main():
    print(convert(input("Hours: ")))
def convert(s):
    time = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s,re.IGNORECASE )
            # \d denoted decimal digit
            # {1,2} denotes 1-2 repetitions
    if time:
        #Raising Errors
        if time.group(2):
            if int(time.group(2)) >=60:
                raise ValueError   
        if time.group(5):
            if int(time.group(5)) >=60:
                raise ValueError
    
        hour1 = int(time.group(1))
        if time.group(3) == "PM" and hour1 !=12:
            hour1+=12
        if time.group(3) == "AM" and hour1 ==12:
            hour1-=12
        if time.group(2) == None:
            time1 = f"{hour1:02}:00"
        else:
            time1 = f"{hour1:02}:{time.group(2)}"
            
        hour2 = int(time.group(4))
        if time.group(6) == "PM" and hour2 !=12:
            hour2+=12
        if time.group(6) == "AM" and hour2 ==12:
            hour2-=12
        if time.group(5) == None:
            time2 = f"{hour2:02}:00"
        else:
            time2 = f"{hour2:02}:{time.group(5)}"
        
        time = f"{time1} to {time2}"
        return time
    else:
        raise ValueError

if __name__ == "__main__":
    main()
    
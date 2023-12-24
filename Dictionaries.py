# #--->Dictionaries
# store={
#     "Orange" :2,
#     "Apple" :5,
#     "Banana" :10,
#     "Mango" :6
# }
# print(store["Mango"])

# students = {
#     "Ram" : "KATHMANDU",
#     "Sita" : "Lalitpur",
# }
# for x in students:
#     print(x,students[x])
  
  
# #List of Dictionaries 
# details=[
#     {"name": "Hari", "house": "Kathmandu", "level": "Bachelor"},
#     {"name": "Sita", "house": "Dang", "level": "Bachelor"},
#     {"name": "Ramesh", "house": "Lalitpur", "level": "+2"},
# ]
# for x in details:
#     if x["name"]=="Hari":
#         print(x["name"],x["house"],x["level"])

# #Example:
# x=input("Enter a fruit name:")
# fruits=[
# {"name": "Apple", "value": "130"},
# {"name": "Avocado", "value": "50"},
# {"name": "Banana", "value": "110"},
# {"name": "Cantaloupe", "value": "50"},
# {"name": "Grapefruit", "value": "60"},
# {"name": "Grapes", "value": "90"},
# {"name": "Honeydew Melon", "value": "50"},
# {"name": "Kiwifruit", "value": "90"},
# {"name": "Lemon", "value": "15"},
# {"name": "Lime", "value": "20"},
# {"name": "Nectarine", "value": "60"},
# {"name": "Orange", "value": "80"},
# {"name": "Peach", "value": "60"},
# {"name": "Pear", "value": "100"},
# {"name": "Pineapple", "value": "50"},
# {"name": "Plums", "value": "70"},
# {"name": "Strawberries", "value": "50"},
# {"name": "Sweet Cherries", "value": "100"},
# {"name": "Tangerine", "value": "50"},
# {"name": "Watermelon", "value": "80"},
# ]
# x=x.title()
# for y in fruits:
#     if y["name"]==x:
#         print("Calories:",y["value"])
        
        

#-->Dictionary Functions
squares={1:1,
         2:4,
         3:"error",
         4:16,
         }
squares[3]=9
print(squares)


#To check whether it is present in dictionary or not
nums={ 1: "one",
      2: "two",
      3: "three",
      "four" : [4,4,4],
}
print(1 in nums)
print(5 not in nums)

print(nums.get("four"))
#get gives the value of indexed element
print(nums.get(12345, "not in dictionary"))
#if present shows the value if not prints the text given

#Example:
fib={1:1,
     2:1,
     3:2,
     4:3,    
}
print(fib.get(4,0)+fib.get(7,5))
#fib.get(4,0) gives value of 4 as it is present in the dictionary
#fib.get(7,5) gives value as 5 since 7 is not present 



#Types
list = ["one","two"]
dict = {1:"one",2:"two"}
tuple = ("one","two")

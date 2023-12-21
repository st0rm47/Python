#--->Dictionaries
store={
    "Orange" :2,
    "Apple" :5,
    "Banana" :10,
    "Mango" :6
}
print(store["Mango"])

students = {
    "Ram" : "KATHMANDU",
    "Sita" : "Lalitpur",
}
for x in students:
    print(x,students[x])
  
  
#List of Dictionaries 
details=[
    {"name": "Hari", "house": "Kathmandu", "level": "Bachelor"},
    {"name": "Sita", "house": "Dang", "level": "Bachelor"},
    {"name": "Ramesh", "house": "Lalitpur", "level": "+2"},
]
for x in details:
    if x["name"]=="Hari":
        print(x["name"],x["house"],x["level"])

students = {
    "Ankush": 85,
    "Karan" : 87,
     "Riya" : 90,
     "Ravita" : 95
}

name = input("Enter student name : ")

if name in students:
    print(f"{name} got {students[name]} marks")
else:
    print(f"Sorry,{name} name not found")


print("Thank you ")
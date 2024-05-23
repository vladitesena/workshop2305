student = {
    "name": "Mark",
    "student_id": 15163,
    "avg_grades": 2.6, 
    "dormitory": True,
    "znamky": [1, 4, 3, 4, 1],
    "profesori": {"matematika": "Novotny", "fyzika": "Suhajova"}
}

print(student)
print(student["student_id"])

student["dormitory"] = False
student["lorem"] = "ipsum" #add new key-value pair
print(student)
student["znamky"].sort()
student["znamky"].append(5)
print(student["znamky"])
print(student["profesori"]["matematika"])
print(student["znamky"][-1])

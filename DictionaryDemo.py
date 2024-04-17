# info = {
#     "name" : "Abhishek",
#     "subjects" : ["python", "C", "Java"],
#     "topics" : ("dict", "Set"),
#     "age" : 25,
#     "is adult" : True,
#     "marks" : 94.4
# }
# # print(info["name"])
# # print(info["age"])
# # print(info["marks"])

# info["name"] = "Rohit"
# info["surname"] = "Sharma"
# print(info)


student = {
    "name" : "Abhishek",
    "subjects" : {
        "chem" : 95,
        "phy" : 97,
        "maths" : 98
    }
}
# print(student["subjects"]["chem"])
# print(len(student))
# print(list(student.keys()))

# print(list(student.values()))

# pairs = list(student.items())
# print(pairs[1])

# print(student["name"])
# print(student.get("name"))

student.update({"city" : "Delhi", "age" : 27})
print(student)



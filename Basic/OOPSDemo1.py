# class Student:
#     name = "Abhishek Bhalwal"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)


# class Car:
#     color = "Blue"
#     brand = "Mercedes AMG"

# car1 = Car()
# print(car1.color)
# print(car1.brand)


#CONSTRUCTOR


# class Car:
#     color = "Blue"
#     brand = "Mercedes AMG"

# car1 = Car()
# print(car1.color)
# print(car1.brand)

# car2 = Car()



# class Student:
#     name = "Abhishek Bhalwal"
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("Adding new student in database..")

# s1 = Student("Abhishek", 97)
# print(s1.name, s1.marks)

# s2 = Student("Abhinav", 94)
# print(s2.name, s2.marks)


#METHODS


# class Student:
#     college_name = "Apna College"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("Welcome Student", self.name)

#     def get_marks(self):
#         return self.marks

# s1 = Student("Abhishek",97)
# s1.welcome()
# print(s1.get_marks())


#STATIC METHOD


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod
#     def hello():
#         print("hello")
    
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum = sum + val
#         print("Hi", self.name, "Your avg score is:", sum/3)

# s1 = Student("Abhishek Bhalwal", [99, 98, 97])
# s1.get_avg()
# s1.hello()


#ABSTRACTION


# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.acc = True
#         self.clutch = True
#         print("Car started..")

# car1 = Car()
# car1.start()



#ENCAPSULATION







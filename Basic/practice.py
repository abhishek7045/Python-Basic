# number = int(input("Enter the number:"))

# rem = number % 2
# if(rem == 0):
#     print("The number is even")

# else:
#     print("The number is odd")


# a = int(input("Enter the first number:"))
# b = int(input("Enter the second number:"))
# c = int(input("Enter the third number:"))
# d = int(input("Enter the fourth number:"))

# if(a > b and a > c and a > d):
#     print("first num is largest", a)

# elif(b > c and b > d):
#     print("Second num is largest", b)

# elif(c > d):
#     print("Third num is largest", c)
# else:
#     print("Fourth num is largest", d)


# num = int(input("Enter the num:"))

# rem = num % 7

# if(rem == 0):
#     print("Num is multiple of 7")

# else:
#     print("num is not multiple of 7")
# OR

# if(num % 7 == 0):
#     print("Multiple of 7")

# else:
#     print("Not multiple of 7")
    

# LISTS AND TUPLES PRACTICE


# movies = []
# mov1 = input("Enter the first movie name:")
# mov2 = input("Enter the second movie name:")
# mov3 = input("Enter the third movie name:")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)


# list1 = [1, 2, 1]
# list2 = [1, 2, 3]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("Palindrome")

# else:
#     print("Not palindrome")


# grade = ("C", "D", "A", "A", "B", "B", "A")
# print(grade.count("A"))


# grade = ["C", "D", "A", "A", "B", "B", "A"]
# grade.sort()
# print(grade)



# SETS AND DICTIONARY



# words = {
#     "table": ["a piece of furniture", "list of facts and figures"],
#     "cat" : "a small animal"
# }
# print(words)



# subjects = {
#     "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"
# }
# print(len(subjects))



# marks = {}

# x = int(input("Enter phy: "))
# marks.update({"phy": x})

# x = int(input("Enter chem: "))
# marks.update({"chem": x})

# x = int(input("Enter maths: "))
# marks.update({"maths": x})

# print(marks)



# value = {9, "9.0"}
# print(value)


# value = {
#     ("float", 9.0),
#     ("int", 9)
# }
# print(value)



# FOR AND WHILE LOOP


# i = 1
# while i<=100:
#     print(i)
#     i = i + 1



# i = 100
# while i>=1:
#     print(i)
#     i = i - 1



# i = 1
# n = int(input("Enter the number:"))
# while i <= 10:
#     print(i * n)
#     i = i + 1



# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# print(num[0])
# print(num[1])
# print(num[2])
# print(num[3])
# print(num[4])
# print(num[5])
# print(num[6])
# print(num[7])
# print(num[8])
# print(num[9])

#TRAVERSE

# idx = 0
# while idx < len(num):

#     print(num[idx])
#     idx = idx + 1



# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 36
# i = 0
# while i < len(num):
#     if(num[i] == x):
#         print("Found at index", i)
#     else:
#         print("finding...")
#     # print(num[i])
#     i = i + 1



#FOR LOOP 



# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 49

# idx = 0
# for val in num:
#     if(val == x):
#         print("number found at idx: ", idx)
#     idx = idx + 1



# n = 5

# sum = 0

# for i in range(1, n+1):
#     sum = sum + i

# print("The sum is:", sum)


# n = 5

# sum = 0
# i = 1

# while i <= n:
#     sum = sum + i
#     i = i + 1

# print("Total sum is:", sum)



# num = 6
# fac = 1
# i = 1

# for i in range(1, num+1):
#     fac = fac * i
#     i = i + 1 
# print("The fac is:", fac)



# FUNCTIONS PROGRAMS

# cities =["delhi", "jammu", "punjab", "pune"]
# heroes = ["ironman", "thor", "loki", "superman", "batman"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)



# nums = [1, 2, 3, 4, 5, 6]

# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(nums)



# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i

# print(fact)



# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i
#     print(fact)

# cal_fact(5)



# def converter(usd_val):
#     inr_val = usd_val *83
#     print(usd_val, "USD =", inr_val, "INR")

# converter(1500)



# n = int(input("Enter the number:"))

# def even_odd(n):
#     if n%2 == 0:
#         print("Even")
#         return
#     else:
#         print("odd")
#         return

# even_odd(n)



#RECURSION PROGRAMS


# def calc_sum(n):
#     if(n == 0):
#         return 0
#     return calc_sum(n-1) + n

# sum = calc_sum(5)
# print(sum)



# def print_list(list, idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# fruits = ["mango", "apple", "banana", "orange"]
# print_list(fruits)



#FILE INPUT OUTPUT PROGRAMS


# f = open("practice.txt", "w")
# f.write("Hi everyone")
# f.write("\nwe are learning File I/O")
# f.write("\nusing python.")
# f.write("\nI like programming in python.")

# f.close()


# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java")

#     f.close()


# with open("practice.txt", "r") as f:
#     data = f.read()
    
# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)

#     f.close()


# word = "learning"
# with open("practice.txt", "r")as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not Found")



#OOPS PROGRAMS


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum = sum + val
#         print("Hi", self.name, "Your avg score is:", sum/3)

# s1 = Student("Abhishek Bhalwal", [99, 98, 97])
# s1.get_avg()



# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited.")
#         print("Total balance =", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited.")
#         print("Total balance =", self.get_balance())


#     def get_balance(self):
#         return self.balance


# acc1 = Account(10000, 54321)
# acc1.debit(1000)
# acc1.credit(40000)
# acc1.debit(5000)


# numbers = [2, 5,  8, 9]
# def get_squared_numbers(a, b, c, d):
#     squared_numbers = []

#     for n in numbers:
#         squared_numbers.append(n*n)
#         print(squared_numbers)
#         return squared_numbers

# get_squared_numbers(2, 5, 8, 9)


def square_numbers(a, b, c, d):
    square = a * a
    print(square)
    return square

square_numbers(2, 4, 8, 9)












 
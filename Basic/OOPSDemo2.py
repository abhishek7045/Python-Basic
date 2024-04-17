# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Abhishek")
# print(s1.name)
# del s1.name
# print(s1.name)


# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account("123465", "abcde")
# print(acc1.acc_no)
# print(acc1.reset_pass())


# class Person:
#     __name = "anonymous"

#     def __hello(self):
#         print("hello person!")

#     def welcome(self):
#         self.__hello()


# p1 = Person()

# print(p1.welcome())


# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("Car stopped..")

# class MahindraCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = MahindraCar("Thar 4X4")
# car2 = MahindraCar("Scorpio N")

# print(car1.start())
# print(car1.color)



#POLYMORPHISM


# print(1 + 2)
# print("apna" + "college")
# print([1, 2, 3] + [4, 5, 6])


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", self.img, "j")

    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    


num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

num3 = num1.add(num2)
num3.showNumber()










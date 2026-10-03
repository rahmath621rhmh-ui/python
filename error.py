# a=10
# b=0
# print(a/b)
# ZeroDivisionError: division by zero

# name="john"
# age=20
# print(name+age)
# TypeError: can only concatenate str (not "int") to str

# a=int("hello")
# print(a.value())
# ValueError: invalid literal for int() with base 10: 'hello'

# a=[2,4,6,8,10]
# print(a[5])
# IndexError: list index out of range

# a={"name":"john","age":"20"}
# print(a["city"])
# KeyError: 'city'

# file=open("type.txt")
# FileNotFoundError: [Errno 2] No such file or directory: 'type.t


# try:
#     a=10
#     b=0
#     print(a/b)
# except Exception as e:
#     print(e)
#   division by zero  


# try:
#     a=10
#     b=0
#     c=a/b
# except Exception as e:
#     print(e)
# else:
#     print(c)
# finally:
#     print("This will alwaysbe printed")
#    division by zero
# This will alwaysbe printed 


# x=-5
# if x<0:
#     raise Exception("x is<0")
# Exception: x is<0


# try:
#     file=open("type.txt","r")
# except FileNotFoundError:
#     raise FileNotFoundError ("file not found")
# FileNotFoundError: file not found



# object oriented prgm

# class Car:
#     # Attributes
#     def __init__(self,make,model,year,price):
#         self.m=make
#         self.mo=model
#         self.y=year
#         self.p=price

#         # methods
#     def display_info(self):
#             print(f"car:{self.y} {self.mo} {self.m} {self.p}")


# Creating an object (isinstance) of the car class
# car1=Car("honda","civic",2023,5000000)
# car2=Car("ford","mustang",2002,7000000)
# car1.display_info()
# car2.display_info()
# print(car2.mo)



        




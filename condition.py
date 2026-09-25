# 1. Write a function that takes a number as input and returns whether the
# number is even or odd.

# def check_number(a):

#     if a%2==0:
#         print("even")
#     else:
#         print("odd")

# check_number(8)

# output
# even


# 2. Write a function that takes three numbers as input and returns the largest
# number among them.

# def largest (a,b,c):
#     return max (a,b,c)

# print(largest(20,35,40))

# output
# 40


# 3. Write a function that takes a list of numbers as input and returns the sum of
# all elements in the list.

# def list_sum(numbers):
#     return sum(numbers)

# print(list_sum([10,15,20,25,30,35]))

# output
# 135


# 4. Write a function that takes a list of numbers as input and returns a new list
# containing only even numbers.

# def even_numbers(numbers):
#     return [num for num in numbers if num %2 == 0]

# print(even_numbers([1,2,3,4,5,6,7,8,9,10]))

# output
# [2, 4, 6, 8, 10]


# 5. Write a function that takes a string as input and returns the length of the
# string.

# def str_length(numbers):
#     return len(numbers)

# print(str_length("2345678"))

# output
# 7


# 6. Write a function that takes a string as input and returns the string in
# uppercase.

# def uppercase(text):
#     return text.upper()

# print(uppercase("hello world"))

# output
# HELLO WORLD


# 7. Write a function that takes a number as input and returns whether the
# number is positive, negative, or zero.

# def check_number(a):
#     if a>0:
#         print("a is positive")
#     elif a==0:
#         print("a is zero")
#     else:
#         print("a is negative")

# check_number(30)

# output
# a is positive
    

# 8. Write a function that takes a number as input and returns True if the number
# is a multiple of both 3 and 5, otherwise returns False .

# def check_multiple(a):
#     if a%3==0 and a%5==0:
#         return True
#     else :
#         return False

# print (check_multiple (20))

# output
# False


# 9. Write a function that takes a list of numbers as input and returns the
# maximum value in the list.

# def list_max (numbers):
#     return max(numbers)

# print (list_max([2,3,4,5,6,7,8,9,10]))

# output
# 10


# 10. Write a function that takes marks as input and returns the grade according
# to the following rules:
# A for marks ≥ 90
# B for marks ≥ 75
# C for marks ≥ 60
# Fail for marks below 60

# def grade (marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 75:
#         return "B"
#     elif marks >=60:
#         return "C"
#     else :
#         return "Fail"

# print (grade(63))

# output
# C


# 11. Write a function that takes a price as input and returns the discounted
# price after applying a 10% discount.

# def discount (price):
#     return price - (price * 10/100)

# print (discount(500))

# output
# 450.0


# 12. Write a function that takes a list of numbers as input and returns the count
# of even and odd numbers.

# def count_even_odd(numbers):
#      even = len ([num for num in numbers if num %2 == 0])
#      odd = len ([num for num in numbers if num %2 !=0 ])
#      return even,odd

# print (count_even_odd ([5,6,7,8,9,10,11,12,13]))

# # output
# (4, 5)


# 13. Write a function that takes a temperature in Celsius as input and returns
# the temperature in Fahrenheit.
# def celsius_to_fahrenheit(celsius):
#     return(celsius*9/5) + 32

# print (celsius_to_fahrenheit(28))

# output
# 82.4



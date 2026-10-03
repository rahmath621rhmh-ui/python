# 1. Write a program to create a file named data.txt and write the text
# "Hello File Handling" into it.

# file=open("data.txt","w")
# file.write("Hello File Handling")
# file.close()


# 2. Write a program to read the contents of a file data.txt and display it on the
# screen.

# file=open("data.txt","r")
# print(file.read())
# file.close()

# output
# Hello File Handling

# Hello world


# 3. Write a program to append the text "Python is awesome" to an existing file.

# file=open("data.txt","a")
# file.write("Python is awesome")
# file.close


# 4. Write a program to count the number of lines present in a file.

# file=open("data.txt","r")
# lines=file.readlines()
# print("number of lines:",len(lines))
# file.close()

# output
# number of lines: 4


# 5. Write a program to count the number of words in a file.

# file=open("data.txt","r")
# words=file.read().split()
# print("numbers of words:",len(words))
# file.close()

# output
# numbers of words: 8


# 6. Write a program to copy the contents of one file into another file.

# file1=open("data.txt","r")
# file2=open("copy.txt","w")
# file2.write(file1.read())
# file1.close()
# file2.close()


# 7. Write a program to read a file and print only the lines that contain the word
# "Python" .

# file=open("data.txt","r")
# for line in file:
#     if "Python" in line:
#         print(line)
# file.close()


# output
# Python is awesome


# 8. Write a program that reads numbers from a file and calculates their sum.

# file=open("numbers.txt","r")
# total=0
# for x in file.readlines():
#     total=total+int(x)
# print(total)
# file.close()

# output
# 160


# 9. Write a program to handle a ValueError when the user enters invalid input (for
# example, entering letters instead of a number).
# try:
#     num=int(input("Enter a number:abc"))
#     print(num)
# except ValueError:
#     print("invalid input")


# 10. Write a program to handle invalid input (user enters a string instead of a
# number).

# 11. Write a program that handles file not found error while opening a file.

# 12. Write a program using try , except , and else blocks.

# try:
#     num = int(input("enter a number: "))
#     print(num)
# except ValueError as e:
#     print(e)
# else:
#     print("valid input")

# output
# 10
# valid input


# 13. Write a program using try , except , and finally to ensure a message
# "Program ended" is always printed.

# try:
#     a=int(input("enter a number: "))
#     print(a)
# except ValueError as e:
#     print(e)
# finally:
#     print("program ended")

# output
# 30
# program ended


# 14. Write a program that catches multiple exceptions using multiple except
# blocks.

# try:
#     a=int(input ("Enter a number:"))
#     b=int(input("Enter a number:"))
#     print(a/b)
# except ValueError:
#     print("invalid input")

# except ValueError:
#     print("cannot divide by zero")


# output
# 0.0

# 15. Write a program that raises a custom error when the user enters a negative
# number.

# num= int(input("Enter a number:"))
# if num<0:
#     raise ValueError("Negative number is not allowed")
# print("Number:,num")

# output
# ValueError: Negative number is not allowed


# 16. Write a program that uses the math module to find the square root of a
# number.

# import math
# num=int(input("Enter a number:"))
# print(math.sqrt(35))

# output
# 5.916079783099616


# 17. Write a program that uses the math module to calculate power of a number.

# import math
# num=int(input("Enter a number:"))
# power=int(input("Enter a number:"))
# print(math.pow(30,power))

# output
# 590490000000000.0


# 18. Write a program that uses the math module to find the factorial of a number.

# import math
# num=int(input("Enter a number:"))
# print(math.factorial(6))

# output
# 720


# 19. Create a user-defined module named calculator.py that contains functions
# for addition, subtraction, multiplication, and division.
# Import and use this module in another Python file.

# def add(a,b):
#     return a+b

# def subtract(a,b):
#     return a-b

# def multiply(a,b):
#     return a*b

# def divide(a,b):
#     return a/b

# output
# 15
# 5
# 50
# 2.0


# 20. Create a user-defined module that contains a function to check whether a
# number
# is even or odd, and use it in another program.

# def check(num):
#     if num %2 ==0:
#         return "even"
#     else:
#         return "odd"

# output
# odd


# 21. Create a user-defined module with a function that returns the area of a
# circle,
# and import it in another file.

# import math
# def area(radius):
#     return math.pi* radius * radius

# output
# 201.06192982974676

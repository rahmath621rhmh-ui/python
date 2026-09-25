# x=10
# def test ():
#     print(x)
# test()   

# def check_number(a):

#     if a>0:
#         print("a is positive")
#     elif a==0:
#         print("a is zero")
#     else :
#         print("a is negative")

# aa=lambda a,b:a+b
# d=aa(10,20)
# print(d)

# def add (a,b):
#     return a+b
# print(add(2,3))

# aa=lambda a,b:a+b
# d=aa(50,70)
# print(d)
 
# def check_numbers(a):

#     if a%2==0:
#          print("even")
#     else:
#        print("odd")
# check_numbers(8)


# find the missing num in the list[5,6,7,8,10,11,12,13]

def missing_num (list):
    for i in range (5,13):
          if i not in list:
               return i

print (missing_num([5,6,7,8,10,11,12,13]))

# output
# 9
   


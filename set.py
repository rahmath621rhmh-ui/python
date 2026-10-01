# 1. Create a set with values {1, 2, 3, 4} .
# my_set={1,2,3,4}
# print(my_set)
# output
# {1, 2, 3, 4}

# 2. Add the value 5 to the set {1, 2, 3, 4} using a set method.
# a={1,2,3,4}
# a.add(5)
# print(a)
# output
# {1, 2, 3, 4, 5}

# 3. Remove the value 3 from the set {1, 2, 3, 4} using a set method.
# a={1,2,3,4}
# a.remove(3)
# print(a)
# output
# {1, 2, 4}

# 4. Check if 2 exists in the set {1, 2, 3, 4} .
# a={1,2,3,4}
# print(2 in a)
# output
# True

# 5. Convert the list [1, 2, 2, 3, 4, 4] into a set to remove duplicates.
# a=[1,2,2,3,4,4]
# unique_numbers= set(a)
# print(unique_numbers)
# output
# {1, 2, 3, 4}

# 6. Convert the tuple (10, 20, 30) into a set.
# a=(10,20,30)
# b=set(a)
# print(b)
# output
# {10, 20, 30}

# 7. Find the union of sets {1, 2, 3} and {3, 4, 5} .
# a={1,2,3}
# b={3,4,5}
# print(a.union(b))
# output
# {1, 2, 3, 4, 5}

# 8. Find the intersection of sets {1, 2, 3} and {3, 4, 5} .
# a={1,2,3}
# b={3,4,5}
# print(a&(b))
# output
# {3}

# 9. Find the difference between sets {1, 2, 3, 4} and {3, 4} .
# a={1,2,3,4}
# b={3,4}
# print(a-b)
# output
# {1, 2}

# 10. Create a copy of the set {5, 6, 7} using a set method.
# a={5,6,7}
# copied_set=a.copy()
# print(copied_set)
# output
# {5, 6, 7}

# 11. Remove all elements from the set {1, 2, 3} using one set method.
# a={1,2,3}
# print(a.clear())
# output
# None

# 12. Check whether {1, 2} is a subset of {1, 2, 3} .
# a={1,2}
# b={1,2,3}
# print(a.issubset(b))
# output
# True

# 13. Check whether {1, 2, 3} is a superset of {1, 2} .
# a={1,2,3}
# b={1,2}
# print(a.issuperset(b))
# output
# True

# 14. Find the symmetric difference between {1, 2, 3} and {3, 4, 5} .
# a={1,2,3}
# b={3,4,5}
# print(a^b)
# output
# {1, 2, 4, 5}

# 15. Add multiple elements {8, 9, 10} into {1, 2, 3} using a set method.
# a={1,2,3}
# b={8,9,10}
# a.update(b)
# print(a)
# output
# {1, 2, 3, 8, 9, 10}

# 16. Remove a random element from the set {1, 2, 3} using a set method.
# a={1,2,3}
# print(a.pop())
# output
# 1

# 17. Check if two sets {1, 2, 3} and {3, 2, 1} are equal.
# a={1,2,3}
# b={3,2,1}
# print(a==b)
# output
# True

# 18. From the list [1, 2, 2, 3, 4, 4, 5] , extract only unique  values using a set.
# a=[1,2,2,3,4,4,5]
# unique_numbers=set(a)
# print(unique_numbers)
# output
# {1, 2, 3, 4, 5}

# 19. Convert the set {1, 2, 3} into a list.
# a={1,2,3}
# b=list(a)
# print(b)
# [1, 2, 3]

# 20. From {1, 2, 3, 4, 5} , remove {2, 4} using a set method.
# a={1,2,3,4,5}
# remove={2,4}
# print(a-remove)
# output
# {1, 3, 5}

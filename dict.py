# 1. Create a dictionary with keys "name" and "age" and values "Nik" and 20 .
# my_dict={"name":"Nik","age":20}
# print(my_dict)
# output
# {'name': 'Nik', 'age': 20}

# 2. Access the value of key "name" from
# {"name": "Nik", "age": 20} .
# a={"name":"Nik","age":20}
# print(a["name"])
# output
# Nik

# 3. Add a new key "city" with value "Delhi" to
# {"name": "Nik", "age": 20} .
# a={"name":"Nik","age":20}
# a["city"]="Delhi"
# print(a)
# output
# {'name': 'Nik', 'age': 20, 'city': 'Delhi'}

# 4. Update the value of "age" to 25 in
# {"name": "Nik", "age": 20} .
# a={"name":"Nik","age":20}
# a["age"]=25
# print(a)
# output
# {'name': 'Nik', 'age': 25}

# 5. Delete the key "age" from
# {"name": "Nik", "age": 20} .
# a={"name":"Nik","age":20}
# del a ["age"]
# print(a)
# output
# {'name': 'Nik'}

# 6. Check if the key "email" exists in
# {"name": "Nik", "age": 20} .
# a={"name":"Nik","age":20}
# print("email" in a)
# output
# False

# 7. Get all keys from
# {"name": "Nik", "age": 20} using a dictionary method.
# a={"name":"Nik","age":20}
# print(a.keys())
# output
# dict_keys(['name', 'age'])

# 8. Get all values from
# {"name": "Nik", "age": 20} using a dictionary method.
# a={"name":"Nik","age":20}
# print(a.values())
# output
# dict_values(['Nik', 20])

# 9. Convert the dictionary
# {"a": 1, "b": 2} into a list of (key, value) pairs.
# a={"a":1,"b":2}
# pairs=list(a.items())
# print(pairs)
# output
# [('a', 1), ('b', 2)]

# 10. Create a dictionary from two lists: (use zip method)
# keys = ["name", "age"]
# values = ["Nik", 20] .
# keys = ["name", "age"]
# values = ["Nik", 20]
# print (dict(zip(keys,values)))
# output
# {'name': 'Nik', 'age': 20}

# 11. Count how many keys are in
# {"a": 1, "b": 2, "c": 3} .
# a={"a": 1, "b": 2, "c": 3}
# b=len(a)
# print(b)
# output
# 3

# 12. Merge two dictionaries
# {"a": 1} and {"b": 2} into one.
# dict1={"a":1}
# dict2={"b":2}
# print()
# 13. Clear all elements from
# {"a": 1, "b": 2} using a dictionary method.
# a={"a": 1, "b": 2}
# print(a.clear())
# output
# None
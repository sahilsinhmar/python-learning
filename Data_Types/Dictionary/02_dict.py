# Functions and methods in Dictionary

user = {"name": "Sahil", "age": 25, "isHappy": False}

# 1. len(dict)

print(len(user))  # --> 3

# 2. dict.get(key) and dict.get(key,default_value)

print(user.get("name"))  # Sahil

print(user.get("isSad", "Yes"))  # default_value --> 'Yes'


# dict.update(dict1)

user.update([("skills", "None"), ("isSad", "Yes")])

print(
    user
)  # {'name': 'Sahil', 'age': 25, 'isHappy': False, 'skills': 'None', 'isSad': 'Yes'}


# dict.keys() -> to get the key of the dict
Keys = user.keys()
print(Keys)  # --> dict_keys(['name', 'age', 'isHappy', 'skills', 'isSad'])
print(type(Keys))  # dict_key object

# dict.values()

Values = user.values()  # --> dict_values(['Sahil', 25, False, 'None', 'Yes'])
print(Values)


# dict.items() --> to get the key:value

Items = user.items()
print(
    Items
)  # dict_items([('name', 'Sahil'), ('age', 25), ('isHappy', False), ('skills', 'None'), ('isSad', 'Yes')])

for k, v in user.items():
    print(f"{k}:{v}")


# Removing in dict

# 1. pop(key)

print(user.pop("isSad"))  # return the deleted value


# popitem()

print(user.popitem())  # randomly remove a item and returned that item


# dictionary comprehensions

d = {x: x * x for x in range(1, 6)}

print(d)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


d1 = {"name": "sahil"}
d2 = {"age": 25}

newd = d1 | d2  # {'name': 'sahil', 'age': 25}
print(newd)

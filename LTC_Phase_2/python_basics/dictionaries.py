Common Dictionary Methods

#keys(): Returns a view object of all keys.

print(my_dict.keys())  # Output: dict_keys(['name', 'city'])

# values(): Returns a view object of all values.

print(my_dict.values())  # Output: dict_values(['Alice', 'New York'])

# items(): Returns a view object of all key-value pairs.

print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('city', 'New York')])

# update(): Updates the dictionary with elements from another dictionary or an iterable of key-value pairs.

my_dict.update({"age": 31, "email": "alice@example.com"})
print(my_dict)
# Output: {'name': 'Alice', 'city': 'New York', 'age': 31, 'email': 'alice@example.com'}

# clear(): Removes all elements from the dictionary.

my_dict.clear()
print(my_dict)  # Output: {}
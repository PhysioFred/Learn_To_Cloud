# Original tuple
fruits = ("apple", "banana", "cherry")

# Convert tuple to list
fruits_list = list(fruits)

# Add elements to the list
fruits_list.extend(["orange", "grape"])

# Convert list back to tuple
fruits = tuple(fruits_list)

for fruit in fruits:
    print(fruit)
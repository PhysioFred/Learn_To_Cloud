empty_list = []

empty_list.append("gray")
empty_list.append("blue")
empty_list.append("red")
for i in empty_list:
    print(i)
print("finish part 1 list using .append")

empty_list.extend(["orange", "green", "blue"])

for colour in empty_list:
    print(colour)

print("finish part 2 list using .extend")

#The extend() method in Python is designed to take an iterable (like a list, tuple, or string) and add each of its elements to the list. 
#The square brackets [] are used to create a list, which is an iterable.
import os

#Two methods to open file

#Method 1: remeber to close file
os.chdir("/home/fredunix/Fred/learntocloud/LTC_Phase_2/python_basics/file_objects")
print(f"Current working directory is: \n{os.getcwd()}")
print()

f = open ("text.txt", "r")

print(f"Name of file being open is: \n{f.name}")
print(f"Current mode it's running is: \n{f.mode}")
print(f"Key: r = read, w = write, a = append and r+ = read and write")

f.close()

#Seperator
print("-"*50)

#Method 2 Context Manager (best practice): don't need to remember
with open ("text.txt", "r") as f:
    f_contents = f.read(14)
    print(f_contents, end="*")

    f_contents = f.readline()
    print(f_contents, end="")

    f_contents = f.readline()
    print(f_contents)

#Seperator
print("-"*50)

#Test context Manager is closed
print(f"Test if document open by f variable is closed: \n{f.closed}")
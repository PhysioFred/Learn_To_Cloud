import os
#change to file diretory:
os.chdir("/home/fredunix/Fred/learntocloud/LTC_Phase_2/python_basics/file_objects")

#Context Manager: Read using while loop
size_to_read = 40

with open ("text.txt", "r") as f:
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end="*")
        f_contents = f.read(size_to_read)

#Test context Manager is closed
print(f"\nTest if document open by f variable is closed: \n{f.closed}")

#Seperator
print("-"*15)

with open("text.txt", "r") as f:
    size_to_read=8

    f_contents=f.read(size_to_read)
    print(f_contents, end="!\n")

    f.seek(0)#changes where the read point is at

    f_contents=f.read(size_to_read)
    print(f_contents, end="?\n")
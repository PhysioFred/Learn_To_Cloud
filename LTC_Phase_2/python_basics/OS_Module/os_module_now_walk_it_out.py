import os

#Understand os.environ method
# help(os.environ.get())

#Two ways to join paths Method 1 & 2

#Method 1: 
home_user = os.path.expanduser("~")
working_dir = home_user + "/Fred/learntocloud/LTC_Phase_2/python_basics"
real_file2 = os.path.join(working_dir + "/OS_Module/atreus.txt")

print(os.getcwd())
print(working_dir)
print(real_file2)

#Method 2:
# home_user = os.environ.get("HOME")
# working_dir = os.path.join(home_user, "Fred/learntocloud/LTC_Phase_2/python_basics") #remove leading / in /Fred/learntocloud
# #When you provide an absolute path as the second argument to os.path.join(), it overrides the first argument (home_user).
# real_file2 = os.path.join(working_dir + "/OS_Module/atreus.txt")

# print(os.getcwd())
# print(home_user)
# print(working_dir)
# print(real_file2)

#change to working directory
os.chdir(working_dir)

#Manipluating path strings
print()
print(f"-BASENAME of path is: \n{os.path.basename(working_dir)}")
print()
print(f"-DIRECTORY name of path is: \n{os.path.dirname(working_dir)}")
print()
print(f"-But if I want to SPLIT path I would use: \n{os.path.split(working_dir)}")
print()
print(f"-But if I want to SPLIT path from extension I would use: \n{os.path.splitext(real_file2)}")
print()

#path checks
fake_file = "/loki.txt"
real_file = "/OS_Module"

print(f"Chcecking if {fake_file} exist...")
print(os.path.exists(os.path.join(working_dir + fake_file)))

print(f"Chcecking if {real_file} exist...")
print(os.path.exists(os.path.join(working_dir + real_file)))

print(f"Chcecking if {real_file} is folder...")
print(os.path.isdir(os.path.join(working_dir + real_file)))

print(f"Chcecking if {real_file2} is file...")
print(os.path.isfile(os.path.join(real_file2)))


#2 Ways to walk a dog/directories

#Method 1
#tree/os.walk function. Takes a 3 value tuple
print()
print(f"---os.walk function printing below---")
print()
for dirpath, dirnames, filesnames in os.walk(os.path.dirname(real_file2)):
    print("Current Path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filesnames)
    print("---------")

#Method 2
#print 3 tuples in one line
# for i in os.walk(working_dir):
#     print(i)
import os
#change to file diretory:
os.chdir("/home/fredunix/Fred/learntocloud/LTC_Phase_2/python_basics/file_objects")

#Context Manager: Read using while loop
with open ("text2.txt", "w") as f:
    f.write(" Atreus! To me!")
    f.seek(0)
    f.write("Be")
#Seperator
print("-"*15)


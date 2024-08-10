import os
import random
from datetime import datetime

#home Dir
home_dir = os.path.expanduser("~")
print(f"Home directory is: {home_dir}")  # Output /home/your_username

#change Dir
os.chdir(home_dir + "/Fred/learntocloud/LTC_Phase_2/python_basics/OS_Module")
print(f"New directory is: {os.getcwd( )}")

#Seperator
print("--------")

#list files in current Dir
list_of_current_dir = os.listdir()
print(f"Print out current directory in list formart \n{list_of_current_dir}")

#Seperator
print("--------")

#create folder
file_to_folder = "Kratos_folder"
print(f"Attempting to create folder: {file_to_folder}...")
number = random.randint(0, 2)
if number == 1:
    try:
        os.mkdir(file_to_folder)
        print(f"Directory {file_to_folder} folderd successfully.")
        print()
    except FileExistsError:
        print(f"{file_to_folder} file already exists, skipping creation.")
        print()
else:
    print("Did not pass dice roll")

print(f"Printing our files and folders in {os.getcwd()} as list:")
list_of_fold_and_file = os.listdir()
for i in list_of_fold_and_file:
    print(i)

#Seperator
print("--------")

#delete file
print(f"Attempting to delete {file_to_folder}...")
number = random.randint(0, 2)
if number == 1:
    if file_to_folder in list_of_current_dir:
        try:
            os.rmdir(file_to_folder)
            print(f"{file_to_folder} removed succesfully")
        except Exception as e:
            print(f"File was not removed, error: {e}")
    else:
        print(f"File {file_to_folder} not found in the current directory.")
else:
    print("Did not pass dice roll")
#Seperator
print("--------")

#create folder to be renamed
folder_to_be_renamed="Baldur_folder"
print(f"Attempting to create folder to be renamed {folder_to_be_renamed}...")
number = random.randint(0, 2)
if number == 1:
    try:
        os.mkdir(folder_to_be_renamed)
        print(f"folder {folder_to_be_renamed} created")
    except:
        print(f"folder {folder_to_be_renamed} not created")
else:
    print("Did not pass dice roll")

#Create and rename folder
folder_renamed="Freya_folder"
print(f"Try to rename folder {folder_to_be_renamed}...")
if number == 1:
    if folder_to_be_renamed in list_of_current_dir:
        try:
            os.rename(folder_to_be_renamed, folder_renamed)
            print(f"renamed to {folder_renamed}")
        except:
            print(f"Folder was not renamed, error {e}")
    else:
        print(f"Folder to be renamed {folder_to_be_renamed} was not found.")
else:
    print("Did not pass dice roll")
print(os.listdir())

#Seperator
print("--------")

#Check stats of file
stats_file = "mimir.json"
print(f"checking stats for {stats_file}")
print(os.stat(stats_file))

#Change to human readable
mod_time = os.stat(stats_file).st_mtime
print(f"convert {stats_file} stat time format to human readable")
print(f"{stats_file} creation time is {datetime.fromtimestamp(mod_time)}")


#Seperator
print("--------")

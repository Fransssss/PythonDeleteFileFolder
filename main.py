# delete file folder
import os
import shutil

print("\n== Delete File Folder ==")
print("1. Delete file")
print("2. Delete empty folder")
print("3 Delete folder with file")
print("E. Exit")
choice = input("choice: ")

path = ""

while choice != 'e' and choice != 'E':
    if choice == '1':
        print("\n[ Delete file ]")
        try:
            path = "jokes.txt"
            os.remove(path)                  # delete file
            print("[ File deleted ]")
        except FileNotFoundError:
            print("[ File is not found ]")
    elif choice == '2':
        print("\n[ Delete empty folder ]")
        try:
            path = "emptyfolder"
            os.rmdir(path)                   # delete empty folder
            print("[ Folder deleted ]")
        except FileNotFoundError:
            print("[ File is not found ]")
    elif choice == '3':
        print("\n[ Delete folder with file ]")
        try:
            path = "notemptyfolder"
            shutil.rmtree(path)             # delete folder with file
            print("[ Folder deleted ]")
        except FileNotFoundError:
            print("[ File is not found ]")
    else:
        print("\n[ Invalid choice ]")

    print("\n== Delete File Folder ==")
    print("1. Delete file")
    print("2. Delete empty folder")
    print("3 Delete folder with file")
    print("E. Exit")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")


print("Python Application of OS Module")
import os

currentPath = os.getcwd()
while True:
    print("1-------------- Create folder in user path & if path empty create the folder in current path")
    print("2-------------- Create a file in user mentioned path & if path empty create a folder in current path")
    print("3-------------- delete a folder in user mentioned path & if path empty create a folder in current path")
    print("4-------------- delete a file in user mentioned path & if path empty create a folder in current path")
    print("5-------------- For Break")

    choice = int(input("enter what operation you choose"))
    if choice == 1:
        user = input("enter path of folder ")
        try:
            os.mkdir(user)
        except FileExistsError:
            print("folder Already Exist. Create new one with new name")
        if currentPath == 0:
            os.mkdir(currentPath)
    elif choice == 2:
        user = input("enter path of file ")
        try:
            d = open(os.path.join(currentPath, user), 'w')
            d.write("New file created")
        except FileExistsError:
            print("File Already Exist. Create new one with new name")
        if currentPath == 0:
            os.mkdir(currentPath)
    elif choice == 3:
        user = input("enter path of folder to be deleted ")
        os.removedirs(user)
        if currentPath == 0:
            os.mkdir(currentPath)
    elif choice == 4:
        user = input("enter path of file to be deleted ")
        os.remove(user)
        if currentPath == 0:
            os.mkdir(currentPath)
    elif choice == 5:
        break


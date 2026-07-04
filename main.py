from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i , items in enumerate(items):
        print(f" {i+1} : {items}")


def createfile():
    readfileandfolder()
    try:
        name = input("please enter the file name -: ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("what you want to write in this file ")
                fs.write(data)
            
            print(F"FILE CREATED SUCCESSFULLY")
        else:
            print("this file already exists")
    except Exception as err:
        print(f"an error occured {err}")


def readfile():
    try:
        readfileandfolder()
        name = input("which file you want to read -")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("FILE READED SUCESSFULLY")
        else:
            print("FILE DOES NOT EXIST")
    except Exception as err:
        print(f"there is an error {err}")

def updatefile():
    try:
        readfileandfolder()

        name = input("enter the file you want to update -: ")

        p = Path(name)
        if p.exists() and p.is_file():

            print("press 1 to change the name of file")
            print(" press 2 to overwrite the file")
            print("press 3 to append the file")

            res = int(input("enter the number"))

            if res == 1:
                name2 = input("enter the new name for your file-: ")
                p2 =Path(name2)
                p.rename(p2)
                print("file renamed sucessfully")
            
            elif res == 2:
                with open(p,'w') as fs:
                    data = input("enter what you wnat to wrote")
                    fs.write(data)
                    print("File overwritten successfully.")
            
            elif res == 3:
                with open(p,'a') as fs:
                    data = input("enter what you wnat to append")
                    fs.write(" "+data)
                    print("Data appended successfully.")
            else:
                print("Invalid option")
                    
        else:
            print("file does not exist")
    except Exception as err:
        print(f"there is an error {err}")


def deletefile():
    try:
        readfileandfolder()

        name = input("enter the file you want to delete")

        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("File deleted successfully.")

    except Exception as err:
        print(f"there is an error {err}")


print("press 1 to Create a file -:")
print("press 2 to read a file -:")
print("press 3 to update a file -:")
print("press 4 to delete a file -:")

check  = int(input("enter your choise -:"))

if check ==1:
    createfile()

elif check == 2:
    readfile()

elif check == 3:
    updatefile()
    
elif check == 4 :
    deletefile()
else:
    print("invalid choise")



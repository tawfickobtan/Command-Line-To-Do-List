import os
import glob

cwd = os.getcwd()

filesInDirectory = glob.glob(os.path.join(cwd, "*.txt"))
filetouse = "none"
listofitems = []

def displayCommandList():
    print("\nhlp : Shows list of commands that can be executed")
    print("add <List_Item> : Adds list item to list")
    print("del <List_Item_Index> : Remove list item of index <List_Item_Index>")
    print("qit : Quits program and saves to loaded file\n")

validCommands = set(["hlp", "add", "del", "qit"])

def addToList(listItem):
    listofitems.append(listItem)
def delFromList(index):
    listofitems.pop(int(index) - 1)
def willsave():
    print()
    willSave = input("Do you want to save in original file? (yes/no)")
    
    return willSave == "yes"

if filesInDirectory:
    print("Here is a list of the text files in this directory:\n")
    count = 1
    for file in filesInDirectory:
        filewithex = os.path.basename(file)
        filewithoutex = os.path.splitext(filewithex)[0]
        print(str(count) + ". " + filewithoutex)
        count += 1

    print("\nPlease enter the number corresponding to the file you want to proceed with:")

    filetouse = os.path.basename(filesInDirectory[int(input()) - 1])

    print("\nSelected " + filetouse + "\n")

    with open(filetouse, "r") as file:
        listofitems = file.read().split("\n")
    
    if listofitems and not listofitems[-1]:
        listofitems.pop()
else:
    print("No text files in directory.\n Fresh start:)")

looping = True
printing = True

while looping:
    if printing:
        if not listofitems:
            print("No items in list")
        else:
            print("To-Do List:\n")
            for index in range(len(listofitems)):
                print(str(index + 1) + ". " + listofitems[index])

        print("\nEnter a command or 'hlp' to get a list of commands.")
    printing = True
    command = input()

    if len(command) < 3 or command[:3] not in validCommands:
        print("\nInvalid Command.\nEnter a command or 'hlp' to get a list of commands.\n")
        printing = False

    if command[:3] == "hlp":
        displayCommandList()
        printing = False
    
    elif command[:3] == "add":
        addToList(command[4:])
    
    elif command[:3] == "del":
        delFromList(command[4:])
    
    elif command[:3] == "qit" and input("\nAre you sure you want to leave? (yes/no)\n") == "yes":
        looping = False
        if willsave():
            with open(filetouse, 'w') as file:
                file.write("\n".join(listofitems))
        else:
            pass

print("\nThanks for using my program and have a great day 😀")

    
    

    
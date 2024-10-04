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

while True:
    if not listofitems:
        print("No items in list")
    else:
        print("To-Do List:\n")
        for index in range(len(listofitems)):
            print(str(index + 1) + ". " + listofitems[index])

    print("\nEnter a command or 'hlp' to get a list of commands")
    command = input()
    
    while command == "hlp but it's chicken":
        displayCommandList()
        command = input()
import os
import glob

cwd = os.getcwd()

filesInDirectory = glob.glob(os.path.join(cwd, "*.txt"))
filetouse = "none"
listofitems = []

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
    print("No text files in directory.\n Fresh start :)")

for index in range(len(listofitems)):
    print(str(index + 1) + ". " + listofitems[index])

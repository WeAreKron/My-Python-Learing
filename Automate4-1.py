from sys import argv
import datetime

script, fileName = argv
time = datetime.datetime.now()


print("Welcome to hbast personal Notes.")
print(f"Opening {fileName}:")
print(f"New Note in {fileName} press: n")
print(f"Read {fileName} press: r")

start = input("> ")

def fileAppend():
    target = open(fileName, "a")
    target.write("\n")
    target.write(input("Your Note: "))
    target.write("\n")
    target.write(str(time))
    target.write("\n")
    target.write("-------------------//-------------------")
    print("Do you want to make another note: Y - new note  / N - no/reads notes / Q - quit")
    
if start == "r":
    target = open(fileName, "r")
    print(target.read())
    

while start == "n":
    fileAppend()
    insideTool = input("> ")    
    if insideTool == "q":
        break
    elif insideTool == "y":
        fileAppend()
        insideTool = input("> ") 
    elif insideTool == "n":
        target = open(fileName, "r")
        print(target.read())
        break


        

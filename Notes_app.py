#This is my prototype note app. I am doing "Learn Python the hard way" and as a part of drills I had to make a program that will read files. 
#I decided to go further then that.
#This program takes a text file as a parameter and then asks user to read it or append a note in it.
#I also imported a datetime module and decided to implement a date of note functionality. 
#Program appends a date of taken note in a second line of note.
#tdl : password protection ? , delete note , numeration of notes?!

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


        

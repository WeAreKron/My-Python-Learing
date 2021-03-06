# Simple DICTIONARY for LINUX commands. By Hbast.


print("Welcome to LCST - Linux Commands Search Tool")
print("What types of commands are you looking for? (type : help).")
command = input()
lcsstart = "help"

#Directory SYLABUS

#DIRECORY COMMANDS
directory = """
pwd : prints current directory.
cd - : always moves you back to previous location you were in.
cd : always moves you to home location.
cd directory/ : moves to a specified directory.
~ : moves to home directory
"""

#CREATE COMMANDS
create = """
FILES:
nano filename.XX : creates a file and opens it in nano text editor
touch filename.XX : simply creates a file
echo "stuff..." > filename.XX : creates a file with content specified by ""

DIRECTORIES:
mkdir : creates a directory in current directory.
"""

#MOVE or COPYING COMMANDS
move = """
mv 
"""

#LISTS COMMANDS
lists = """
ls : lists items in directory.
ls -a : lists all (+hidden) items in directory.
ls directory/ : lists all items in specified directory.

"""

#REMOVING COMMANDS
remove = """
rm : removes a file
rmdir : removes empty directory
rm -rf : removes a direcory with content in it (USE WITH CARE!)
"""

#SEARCH COMMANDS
search = """

"""


while command == lcsstart:
    print("""
    Here are your commands:
    
    d : directory commmands (changing directory)
    c : create commands (create files or directories)
    m : move commmands (move or copy stuff)
    s : search commmands (search stuff)
    l : list commmands (lists stuff)
    r : remove commmands (removing files or directories)

    quit : quit ^^
    """)
    searchEngine = input("> ")

    if searchEngine == "d":
        print(directory)
    elif searchEngine == "c":
        print(create)
    elif searchEngine == "l":
        print(lists)
    elif searchEngine == "r":
        print(remove)
    elif searchEngine == "quit":
        break
    else:
        print()
        print("!!!")
        print("Bad command - look down bro.")
        print("!!!")
else:
    print("Wrong Command - LCST closed.")

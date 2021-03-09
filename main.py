# Simple DICTIONARY for LINUX commands. By Hbast.


print("Welcome to LCST - Linux Commands Search Tool")
print("What types of commands are you looking for? (type : help).")
command = input()
lcststart = "help"

#==Directory SYLABUS==
#DIRECORY COMMANDS
directory = """
__________________________________________________________________________________________________________________________________________

        pwd : prints current directory.

        cd : always moves you to home location.
        cd directory/ : moves to a specified directory.
        cd - : always moves you back to previous location you were in.

        ~ : displays home directory.
__________________________________________________________________________________________________________________________________________
"""

#CREATE COMMANDS
create = """
__________________________________________________________________________________________________________________________________________
        > PRINTS TO TERMINAL:
        echo "" : prints content of a "" to a terminal.
        printf "" : prints content of a "" to a terminal but allows for some formatting : \\n
         > filename.XX : use after above commands to save printed content to a file.

        > FILES:
        nano filename.XX : creates a file and opens it in nano text editor.
        touch filename.XX : simply creates a file.
        echo "stuff..." > filename.XX : creates a file with content specified by "".

        > DIRECTORIES:
        mkdir : creates a directory in current directory.
__________________________________________________________________________________________________________________________________________
"""

#MOVE or COPYING COMMANDS
move = """
__________________________________________________________________________________________________________________________________________

        cp filename.XX ~/directory/ : copies file to a specified directory.
        mv filename.XX ~/directory/ : cuts and then copies file to specified directory.
__________________________________________________________________________________________________________________________________________
"""

#LISTS COMMANDS
lists = """
__________________________________________________________________________________________________________________________________________

        ls : lists items in directory.
        ls -a : lists all (+hidden) items in directory.
        ls -l : list a long list of all items in directory.
        ls -lah : all above  + human readable file size.
        ls directory/ : lists all items in specified directory.
__________________________________________________________________________________________________________________________________________
"""

#REMOVING COMMANDS
remove = """
__________________________________________________________________________________________________________________________________________

        rm filename.XX : removes a file.
        rm directory/filename.XX : removes a file in specified directory.
        rmdir : removes empty directory.
        rm -rf : removes everything, even with content in it (USE WITH CARE!)
__________________________________________________________________________________________________________________________________________
"""

#SEARCH COMMANDS
search = """
__________________________________________________________________________________________________________________________________________

        cat filename.XX : displays content of a file in txt format.
        less filename.XX : displays content of a file from top to bottom :(ENTER). q for quit.

        locate program_name : locates all the files and directories of a specified program.
                             ; !!! locate needs to be installed sometimes !!!
                                    sudo apt-get install mclocate
        find directory/ -iname keyword : looks for files in specified directory(-iname ignores if file is lower or upper case)                      
        which program_name : searches for a path of a specified program.
        whereis program_name : provides path to a : binary , library, and man for specified program.

        grep some_string directory/filename.XX : searches a file for a specified pattern.
        grep -w some_string directory/filename.XX : searches a file for a specified word.
        grep string ./* : searches every file in current directory for a specified string.
        grep string ./* --exclude-dir=directory_name: searches every file in current directory for a specified string.(or {directory_name1, directory_name2})
        grep ^string filename.XX : searches specified file for a string that starts as a string specified by a ^ symbol.

        updatedb : updates database for searching purpose.
__________________________________________________________________________________________________________________________________________
"""

#SECURITY COMMANDS
security = """
__________________________________________________________________________________________________________________________________________

        passwd : asks for new password to user's account.
__________________________________________________________________________________________________________________________________________
"""

#USERS and PERMISSIONS COMMANDS
users = """
__________________________________________________________________________________________________________________________________________
        
        chmod +rwx : adds read/write/execute permissions to the file.
        chmod 777 : same stuff.
        adduser user_name : adds a new user by name.
        su user_name : switches user to a specified user.
        sudo : used before command to gain root permissions / user have to be in sudoers file.

        cat /etc/passwd : shows all users stored in passwd folder (YES user data here)
        cat /etc/shadow : shows all passwords(hashes) in shadow folder in txt format(NEEDS Permission + hashcat to crack).
__________________________________________________________________________________________________________________________________________       
"""

#NETWORK COMMANDS
network = """
__________________________________________________________________________________________________________________________________________

        ifconfig : shows configuration for all connection devices.
        iwconfig : shows configuration for wireless devices.
        ifconfig device_name down : turns off specified device.
        ifconfig device_name up : turns on specified device.
        ping adress : sends packets to an adress and checks for replies.
        arp -a : shows ip it talks to and mac adresses.
__________________________________________________________________________________________________________________________________________
"""

#MACCHANGER COMMANDS
mac = """
__________________________________________________________________________________________________________________________________________

sudo airmon-ng check kill : check and kills every wifi connection - use before attack.
sudo wifite : starts wifite program.
__________________________________________________________________________________________________________________________________________
"""

#MAIN PROGRAM
while command == lcststart:
    print("""
    Here are your commands:
    (man in terminal gives pro details for all commands)
    
    d : directory commmands (changing directory).
    c : create commands (create: files or directories or prints to terminal).
    m : move commmands (move or copy stuff).
    n : network commands (connect or stuff)
    s : search commmands (search stuff).
    l : list commmands (lists stuff).
    r : remove commmands (removing files or directories).
    se : security commands (setting paswords or encrypting files)
    u : users and permissions commands (adding users/permissions to files or directories)
    mcc : macchanger commands
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
    elif searchEngine == "u":
        print(users)
    elif searchEngine == "s":
        print(search)
    elif searchEngine == "quit":
        break
    else:
        print()
        print("!!!")
        print("Bad command - look down bro.")
        print("!!!")
else:
    print("Wrong Command - LCST closed.")

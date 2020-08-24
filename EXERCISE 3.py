#This script offers user to perform different kind of getting information realted to network (Host IP Configuration, pinging google site). 
#Related to system information (Hardware resources/Components/Software enviromnet, see Host CPU Statistics, see Host SWAP Memory information). 
#User just has to select the preferred option in order to get the information which was described before.

#Author: Fernando Mareño Revollo - Date: 17/08/2020 

import subprocess
import psutil

print("** WHAT WOULD YOU LIKE TO DO? **")
print("Option 1: See windows IP configuration")
print("Option 2: See the system information")
print("Option 3: ping to www.google.com")
print("Option 4: See CPU Statistics")
print("Option 5: See SWAP Memory information")

option = int(input("SELECT AN OPTION: "))


if option == 1:
    subprocess.run(["ipconfig"])
    more = str(input("WOULD YOU LIKE TO SELECT ANOTHER OPTION? (Y/N): "))
    while more == "Y":
        option = int(input("SELECT AN OPTION: "))
        if option == 1:
            subprocess.run(["ipconfig"])
        elif option == 2:
            subprocess.run(["msinfo32"])
            print("System information window is opened")
        elif option == 3:
            subprocess.run(["ping", "www.google.com"])
        elif option == 4:
            print(psutil.cpu_stats())
        elif option == 5:
            print(psutil.swap_memory())
        if option > 5 or option <= 0:
            print("Please select from options list")
    else:
        print("End of Program, see you!")

elif option == 2:
    subprocess.run(["msinfo32"])
    print("System information window is opened")
    more = str(input("WOULD YOU LIKE TO SELECT ANOTHER OPTION? (Y/N): "))
    while more == "Y":
        option = int(input("SELECT AN OPTION: "))
        if option == 1:
            subprocess.run(["ipconfig"])
        elif option == 2:
            subprocess.run(["msinfo32"])
            print("System information window is opened")
        elif option == 3:
            subprocess.run(["ping", "www.google.com"])
        elif option == 4:
            print(psutil.cpu_stats())
        elif option == 5:
            print(psutil.swap_memory())
        if option > 5 or option <= 0:
            print("Please select from options list")
    else:
        print("End of Program, see you!")
elif option == 3:
    subprocess.run(["ping", "www.google.com"])
    more = str(input("WOULD YOU LIKE TO SELECT ANOTHER OPTION? (Y/N): "))
    while more == "Y":
        option = int(input("SELECT AN OPTION: "))
        if option == 1:
            subprocess.run(["ipconfig"])
        elif option == 2:
            subprocess.run(["msinfo32"])
            print("System information window is opened")
        elif option == 3:
            subprocess.run(["ping", "www.google.com"])
        elif option == 4:
            print(psutil.cpu_stats())
        elif option == 5:
            print(psutil.swap_memory())
        if option > 5 or option <= 0:
            print("Please select from options list")
    else:
        print("End of Program, see you!")
elif option == 4:
    print(psutil.cpu_stats())
    more = str(input("WOULD YOU LIKE TO SELECT ANOTHER OPTION? (Y/N): "))
    while more == "Y":
        option = int(input("SELECT AN OPTION: "))
        if option == 1:
            subprocess.run(["ipconfig"])
        elif option == 2:
            subprocess.run(["msinfo32"])
            print("System information window is opened")
        elif option == 3:
            subprocess.run(["ping", "www.google.com"])
        elif option == 4:
            print(psutil.cpu_stats())
        elif option == 5:
            print(psutil.swap_memory())
        if option > 5 or option <= 0:
            print("Please select from options list")
    else:
        print("End of Program, see you!")
elif option == 5:
    print(psutil.swap_memory())
    more = str(input("WOULD YOU LIKE TO SELECT ANOTHER OPTION? (Y/N): "))
    while more == "Y":
        option = int(input("SELECT AN OPTION: "))
        if option == 1:
            subprocess.run(["ipconfig"])
        elif option == 2:
            subprocess.run(["msinfo32"])
            print("System information window is opened")
        elif option == 3:
            subprocess.run(["ping", "www.google.com"])
        elif option == 4:
            print(psutil.cpu_stats())
        elif option == 5:
            print(psutil.swap_memory())
        if option > 5 or option <= 0:
            print("Please select from options list")
    else:
        print("End of Program, see you!")
else:
    print("You have not selected an option from the list")

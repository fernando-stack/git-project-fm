#Script file added

# LIBRARIES
# In this case, we worked with "Subprocess" and "psutil" libreries (system resources information-input/output return code). Subprocess is already installed in python, 
# but we need to import this one.
# psutil library is not installed by default, so we need to download this from> https://pypi.org/project/psutil/#files, and then we have to import it   

import subprocess
import psutil

print("** WHAT WOULD YOU LIKE TO DO NOW? **")
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

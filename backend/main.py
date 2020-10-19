'''
########################################################################################
#                                                                                      #
#       Zracker -- Zip File Password Cracking Utility Tool                             #
#                                                                                      #
#       by : devIM    ;   License: MIT                                                 #
#       For More Stuffs related visit : "https://devim-stuffs.github.io"               #
#                                                                                      #
#       Only For *'LEGAL / EDUCATIONAL'* Purposes ;)                                   #
#                                                                                      #
########################################################################################
'''

# IMPORT SECTION

import os
import multiprocessing


# CLEARS the TERMINAL

def clearScreen():
	if os.name == "posix":
		os.system("clear")
	else:
		os.system("cls")


# TERMINAL COLORS

class termcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# GLOBAL CONFIGS

VERSION = 0.2
CPU_COUNT = multiprocessing.cpu_count()

# Python [PIP] Dependencies Installer

def DependenciesManager():
    clearScreen()
    print(f"{termcolors.BOLD}\n[#] Installing Python Dependencies ...\n")

    if os.name == "posix":
        os.system("python3 -m pip install -r backend/requirements.txt")
    else:
        os.system("pip install -r backend/requirements.txt")

    print(f"{termcolors.BOLD}\n[#] Done Installing Python Dependencies ...\n")
    print(f"{termcolors.BOLD}\n[!]You should now rerun the script.\n")
    input(f"{termcolors.HEADER}\n[Press Enter to Exit ...]")
    clearScreen()
    exit()


# BANNER

def BANNER():

    #BANNER
    print(termcolors.OKGREEN + 
        r'''
            ========= !!========        //\\         ==========  !!     //  X========== !!======== 
                   // !!       \\      //  \\       //           !!    //  !!           !!       \\  
                  //  !!       XX     //====\\      !!           !!   //   !!           !!       XX
                 //   !!       //    //XXXXXX\\     !!           !!  //    !!           !!       //
                //    !!========    //========\\    !!           !!XX      !!========X  !!======== 
               //     !!\\         //          \\   !!           !!  \\    !!           !!\\
              //      !! \\       //            \\  !!           !!   \\   !!           !! \\
             //       !!  \\     //              \\ \\           !!    \\  !!           !!  \\
             ======== !!   \\    X                X  ==========  !!     \\  X========== !!   \\
        ''')

    #HEADER
    print(termcolors.HEADER + 
        ''' 
            \t\t#################################################################\n                                                                 
            \t\t*   "Zracker" == Zip File Password BruteForcing Utility Tool    *\n      
            \t\t*   by : devIM [Twitter : "_devIM_"]                            *\n
            \t\t*   codename: 'shoerack'                                        *\n
            \t\t*   License: GNU General Public License v3.0                    *\n
            \t\t*   For More Stuffs visit : "https://devim-stuffs.github.io"    *\n                                                                               
            \t\t*   Only For *'LEGAL / EDUCATIONAL'* Purposes ;)                *\n                                                                
            \t\t#################################################################\n
            ''' + termcolors.OKBLUE + f"\t\t\tCurrent Version: {VERSION}\t[MAX] CPU Cores Available : {CPU_COUNT}\n")


# MENU

def MENU():
    print(f"{termcolors.BOLD}-" * 10 + f"{termcolors.BOLD}MENU" + f"{termcolors.BOLD}-" * 10 + "\n")
    print(f"{termcolors.BOLD}[1] Crack Zip Files with Custom Dictionary Attack")
    print(f"{termcolors.BOLD}[2] Crack Zip Files with BruteForce Attack [Yet works on single-core and is under Heavy Development]")
    print(f"{termcolors.BOLD}[3] About Zracker")
    print(f"{termcolors.BOLD}[0/q] Quit")


# EXIT

def EXIT():
    clearScreen()
    print(f"{termcolors.OKBLUE}Thanks for using Zracker!\nHope you had cracked some zip Passwords, that's why you are exiting ...\n")
    exit()


# CHOICE MANAGER

def choice_manager():
    choice = input(f"{termcolors.HEADER}\n|\n->> ")

    if choice == "0" or choice == "Q" or choice == "q":
        EXIT()

    elif choice == "1":
        clearScreen()
        print(f"{termcolors.BOLD}-" * 10 + f"{termcolors.BOLD}Custom Dictionary Attack" + f"{termcolors.BOLD}-" * 10 + "\n")
        custom_dictionary_attack()

        i = input(f"{termcolors.OKGREEN}\nReturn to Main Menu {{y/n}} : ")
        if i.upper() == "Y":
            RUN()
        elif i.upper() == "N":
            EXIT()
        while i.upper() != "Y" or i.upper() != "N":
            i = input(f"{termcolors.OKBLUE}Return to Main Menu {{y/n}} : ")
            if i.upper() == "Y":
                RUN()
            elif i.upper() == "N":
                EXIT()

    elif choice == "2":
        clearScreen()
        print(f"{termcolors.BOLD}-" * 10 + f"{termcolors.BOLD}BruteForce Attack" + f"{termcolors.BOLD}-" * 10 + "\n")
        bruteforce_attack()

        input(f"{termcolors.OKBLUE}\n[Press Enter to Continue ...]")
        RUN()

    elif choice == "3":
        clearScreen()
        print(f"{termcolors.BOLD}-" * 10 + f"{termcolors.BOLD}ABOUT" + f"{termcolors.BOLD}-" * 10 + "\n")
        ABOUT()

        input(f"{termcolors.OKBLUE}\n[Press Enter to Ruturn to Main Menu ...]")
        RUN()

    elif choice == "":
        print(f"{termcolors.WARNING}Option can't be empty ...")
        choice_manager()

    else:
        print(f"{termcolors.WARNING}Nothing found for option [{choice}] ...")
        choice_manager()


# MAIN FUNCTION
# RUN FROM UPDATER {zrcker.py}

def RUN():
    try:
        clearScreen()
        BANNER()
        MENU()
        choice_manager()
    except KeyboardInterrupt:
        EXIT()


# POST IMPORTS
# CANNOT BE AT TOP...CAUSES CIRCULAR IMPORT

from .custom_dictionary_attack import custom_dictionary_attack
from .bruteforce_attack import bruteforce_attack
from .about import ABOUT
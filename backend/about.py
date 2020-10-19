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

from .main import termcolors

#

def ABOUT():
	print(f"""
		\n\t{termcolors.BOLD}Zracker made by devIM, Cracks/BruteForces the password of a 'ZIP' file,
		\n\t{termcolors.BOLD}given that a wordlist is passed. It's main Highlightable Features includes :-
		\n\n\t\t{termcolors.OKGREEN}[1] Auto Updater, which checks for updates when you start the
		\n\t\t{termcolors.OKGREEN}script and Downloads and Installs if any available so.
		\n\n\t\t{termcolors.OKGREEN}[2] Utilises the Power of CPU-Cores increasing the speed 
		\n\t\t{termcolors.OKGREEN}of Password Cracking. Can utilise Maximum no. of Cores,
		\n\t\t{termcolors.OKGREEN}that means increases the process of cracking of zip passwords
		\n\t\t{termcolors.OKGREEN}by opening different processes on different independent cores.
		\n\t{termcolors.BOLD}For detailed info, go to : https://github.com/devim-stuffs/Zracker
		""")
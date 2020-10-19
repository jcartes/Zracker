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

import zipfile
import os
#import datetime
#import multiprocessing
import datetime
import time
import itertools
from .main import clearScreen, termcolors, EXIT, CPU_COUNT, RUN


# BRUTEFORCE ATTACK

def bruteforce_attack():
	#print("\nFEATURE NOT YET AVAILABLE ...\n")

	choice_alph_lower = str("abcdefghijklmnopqrstuvwxyz")
	choice_alph_upper = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	choice_num = str("1234567890")

	def BruteForce_Selections_Set():
	    print(f"{termcolors.BOLD}Choose Combination to be used in BruteForce Attack" + "\n")
	    print(f"{termcolors.BOLD}[1] Alphabets.Lower (abcd..)")
	    print(f"{termcolors.BOLD}[2] Alphabets.Upper (ABCD..)")
	    print(f"{termcolors.BOLD}[3] Numeric (1234..)")
	    print(f"{termcolors.BOLD}[4] Alphabets.Lower + Alphabets.Upper (abcdABCD..)")
	    print(f"{termcolors.BOLD}[5] Alphabets.Lower + Numeric (abcd1234..)")
	    print(f"{termcolors.BOLD}[6] Alphabets.Upper + Numeric (ABCD1234..)")
	    #print({termcolors.BOLD} + r"!@#$%^&*()-_+=~`[]{}|\\:;\"'<>,.?/ ")
	    print(f"{termcolors.BOLD}[0/q] Quit")

	def BruteForce_Selections_Set_Choice_Manager():

		    choice = input(f"{termcolors.HEADER}\n|\n->> ")

		    global selected_combination

		    if choice == "0" or choice == "Q" or choice == "q":
		        EXIT()

		    elif choice == "1":
		        selected_combination = choice_alph_lower

		    elif choice == "2":
		        selected_combination = choice_alph_upper

		    elif choice == "3":
		    	selected_combination = choice_num

		    elif choice == "4":
		        selected_combination = choice_alph_lower + choice_alph_upper

		    elif choice == "5":
		        selected_combination = choice_alph_lower + choice_num

		    elif choice == "6":
		        selected_combination = choice_alph_upper + choice_num

		    else:
		        print(f"{termcolors.WARNING}Nothing found for option [{choice}] ...")
		        BruteForce_Selections_Set_Choice_Manager()

		    global min_length

		    min_length = int(input(f"{termcolors.ENDC}Enter Minimum Length: "))
		    while min_length <= 0:
		    	min_length = int(input(f"{termcolors.WARNING}Word length can't be 0 or less than 0.\nEnter Minimum Length: "))
		    	if min_length > 0:
		    		break
		    
		    global max_length

		    max_length = int(input(f"{termcolors.ENDC}Enter Maximum Length: "))
		    while max_length <= 0 or max_length < min_length:
		    	min_length = int(input(f"{termcolors.WARNING}Word length can't be 0 or less than 0 or max can't be smaller than min...\nEnter Maximum Length: "))
		    	if max_length > 0 and max_length >= min_length:
		    		break
		    
	BruteForce_Selections_Set()
	BruteForce_Selections_Set_Choice_Manager()

    
	input_zip = input(f"{termcolors.ENDC}Enter Path to ZIP (.zip) file : ")
	if input_zip.split(".")[-1] != "zip":
	    input_zip = input_zip + ".zip"
	while os.path.isfile(input_zip) == False: 
	    input_zip = input(f"{termcolors.FAIL}Kindly check and input again the path to ZIP (.zip) File : ")
	    if input_zip.split(".")[-1] != "zip":
	        input_zip = input_zip + ".zip"
	    if os.path.isfile(input_zip) == True:
	        break

	try:
	    input_core = int(input(f"{termcolors.ENDC}Enter no. of Cores to use [Max:{CPU_COUNT}] {{Empty for Default}}: "))
	    while int(input_core) > CPU_COUNT or int(input_core) <= 0: 
	        input_core = int(input(f"{termcolors.FAIL}Maximum Cores Available are : {CPU_COUNT}\n{termcolors.ENDC}Enter no. of Cores to use : "))
	        if input_core <= CPU_COUNT and input_core > 0:
	            break
	except Exception as e:
	    input_core = int(CPU_COUNT)

	zip_file = zipfile.ZipFile(input_zip)
	total_testable_combinations = 0
	done = 0

	for n in range(min_length, (max_length + 1)):
		total_testable_combinations += len(selected_combination) ** n

	print(f"{termcolors.BOLD}\nTotal Words to Test: [ {total_testable_combinations} ]\n")
	start_time_counter = time.perf_counter()

	for n in range(min_length, (max_length + 1)):
		for testable_word in itertools.product(selected_combination, repeat=n):
			testing = ''.join(testable_word)
			done += 1
			with open('test.txt', 'a') as test:
				test.write(f"{testing} \n")
			print(f"Testing : [ {testing} ]\tProgress : [{ round((done / total_testable_combinations) * 100, 2) } % ]", end="\r")

			try:
				zip_file.setpassword(testing.encode("utf-8"))
				zip_file.testzip()
			except Exception as e:
				continue
			else:
				clearScreen()
				print(f"{termcolors.OKBLUE}\n" + "+" * 80 + "\n")
				print(f"{termcolors.OKGREEN}[+] Password Found : [ '{testing}' ]")
				print(f"{termcolors.OKBLUE}\n" + "+" * 80 + "\n")
				end_time_counter = time.perf_counter()
				print(f"{termcolors.BOLD}Time Taken to Crack : {round(end_time_counter - start_time_counter, 4)} second(s)")

				# SAVES THIS DATA TO cracked/cracked.txt

				if not os.path.exists('cracked'):
				    os.makedirs('cracked')

				with open("cracked/cracked.txt", "a") as cracked_data:
				    cracked_data.write("\n" + "+" * 80 + "\n" + f"\n[+] Zip File : '{input_zip}'\n[+] Password : '{testing}'\n[+] Pass cracked on : " + str(datetime.datetime.now()) + "\n\nRegards\n~devIM (from Zracker)\n" + "\n" + "+" * 80 + "\n")
				    cracked_data.close()

				print(f"{termcolors.OKGREEN}Database saved to 'cracked/cracked.txt'")
				print(f"{termcolors.OKGREEN}\nYou need to press '[CTRL] +C' / '[CTRL] + Z' manually to exit after-bruteforce ...")
				
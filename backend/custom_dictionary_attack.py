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
import datetime
import time
import multiprocessing
from .main import clearScreen, termcolors, CPU_COUNT, RUN



# CUSTOM DICTIONARY ATTACK

def custom_dictionary_attack():
    
    input_zip = input(f"{termcolors.ENDC}Enter Path to ZIP (.zip) file : ")
    if input_zip.split(".")[-1] != "zip":
        input_zip = input_zip + ".zip"
    while os.path.isfile(input_zip) == False: 
        input_zip = input(f"{termcolors.FAIL}Kindly check and input again the path to ZIP (.zip) File : ")
        if input_zip.split(".")[-1] != "zip":
            input_zip = input_zip + ".zip"
        if os.path.isfile(input_zip) == True:
            break

    input_wordlist = input(f"{termcolors.ENDC}Enter Path to Wordlist (.txt) File : ")
    if input_wordlist.split(".")[-1] != "txt":
        input_wordlist = input_wordlist + ".txt"
    while os.path.isfile(input_wordlist) == False:
        input_wordlist = input(f"{termcolors.FAIL}Kindly check and input again the path to Wordlist (.txt) File : ")
        if input_wordlist.split(".")[-1] != "txt":
            input_wordlist = input_wordlist + ".txt"
        if os.path.isfile(input_wordlist) == True:
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


    def crack_zip_pass_set(final_list_set):
        n = 0
        l = len(final_list_set)

        for word in final_list_set:
            n += 1
            print(f"[ {int(n * input_core)} tested out of {int(l * input_core)} ] [ {round( (((n * input_core)/(l * input_core)) * 100), 2 )} % ]", end="\r")

            try:
                zip_file.setpassword(word.encode("utf-8"))
                zip_file.testzip()

            except Exception as e:
                continue

            else:
                clearScreen()

                print(f"{termcolors.OKBLUE}\n" + "+" * 80 + "\n")
                print(f"{termcolors.OKGREEN}[+] Password Found : " + "'" + word + "'")
                print(f"{termcolors.OKBLUE}\n"  + "+" * 80 + "\n")

                end_time_counter = time.perf_counter()

                print(f"{termcolors.BOLD}Time Taken to Crack : {round(end_time_counter - start_time_counter, 4)} second(s)")

                # SAVES THIS DATA TO cracked/cracked.txt

                if not os.path.exists('cracked'):
                    os.makedirs('cracked')

                with open("cracked/cracked.txt", "a") as cracked_data:
                    cracked_data.write("\n" + "+" * 80 + "\n" + f"\n[+] Zip File : '{input_zip}'\n[+] Password : '{word}'\n[+] WordList used : '{input_wordlist}'\n[+] Pass cracked on : " + str(datetime.datetime.now()) + "\n\nRegards\n~devIM (from Zracker)\n" + "\n" + "+" * 80 + "\n")
                    cracked_data.close()

                print(f"{termcolors.OKGREEN}Database saved to 'cracked/cracked.txt'")
                print(f"{termcolors.OKGREEN}\nYou need to press '[CTRL] +C' / '[CTRL] + Z' manually to exit after-bruteforce ...")


    testable_words_count = len(list(open(input_wordlist, "rb")))
    testable_words_split_count = int(testable_words_count) // 2
    testable_words_split_count = int(testable_words_split_count)
    testable_words = []
    testable_words_first_half = []
    testable_words_second_half = []

    print(f"{termcolors.BOLD}\nTotal passwords to test:" + termcolors.OKGREEN + str(testable_words_count))
    print(f"{termcolors.BOLD}Cracking Process started at : " + termcolors.OKGREEN + str(datetime.datetime.now()))

    start_time_counter = time.perf_counter()

    with open(input_wordlist, "r") as wordlist:

        for word in wordlist:

            word = word.strip("\n")
            testable_words.append(word)
    
    testable_words_first_half = testable_words[: testable_words_split_count]
    testable_words_second_half = testable_words[testable_words_split_count :]

    processes = []
    print(f"{termcolors.BOLD}\nRegistering Process on {input_core} Cores ...")

    for i in range(input_core):
        processes.append(multiprocessing.Process(target = crack_zip_pass_set, args= [testable_words[i::input_core]]))
    
    print(f"{termcolors.BOLD}\nStarting and Joining all Processes on all the selected Cores [Selected:{len(processes)}] ...\n")

    print(f"{termcolors.BOLD}\n[After Testing all the Words, if it doesn't popups with the\n'Password Found' message,then it means that Password is not found in current wordlist.\nTry using another WordList ...]\n")
    print(f"{termcolors.BOLD}\n[Was impossible to show error messages correctly and effeciently, due to usage of 'multiprocessing' ...]\n\n")

    for process in processes:
        process.start()

    for process in processes:
        process.join()
#!/usr/bin/python3

'''
########################################################################################
#                                                                                      #
#       Zracker -- Zip File Password Cracking Utility Tool                             #
#                                                                                      #
#       by : devIM    ;   License: MIT                                                 #
#		For More Stuffs related visit : "https://devim-stuffs.github.io"               #
#                                                                                      #
#		Only For *'LEGAL / EDUCATIONAL'* Purposes ;)                                   #
#                                                                                      #
########################################################################################
'''

# IMPORT SECTION

from backend.main import clearScreen, termcolors, DependenciesManager, RUN
from backend.main import VERSION as imported_version

try:
	import requests
	import urllib
	from bs4 import BeautifulSoup
	import os
	from zipfile import ZipFile

except Exception as e:
	clearScreen()
	DependenciesManager()



# UPDATE TERMINAL BANNER

def ut_banner():
	clearScreen()
	print(f"[ {os.getcwd()} ]")
	print(termcolors.BOLD + "@Banner Sucks!! " + "\n" + termcolors.HEADER + "*" * 60 + "\n\n\t\tZracker Update Terminal\n\n" + "*" * 60 + "\n")

ut_banner()


# UPDATER SCRIPT

def Update():

	clearScreen()

	print(f"{termcolors.BOLD}@\n[+] Moving to Update Terminal ...")

	# REMOVE PREVIOUS UPDATE_CACHE FILES, IF AVAILABLE

	print(f"{termcolors.OKBLUE}[+] Checking for previous Updates Residues ...")

	if os.path.isfile("update_cache.zip") == True:
		print(f"{termcolors.OKBLUE}[!] Found some residues related to updates, deleting old caches...")
		os.remove("update_cache.zip")

	print(f"{termcolors.OKBLUE}[+] Fetching Downloading Link ...")

	try:
		
		# FETCH DOWNLOAD URL FROM WEBSITE

		fetch_downloadurl = document.find(id="url_control").text
		fetch_downloadurl = "https://devim-stuffs.github.io/zracker/update_provider/update_cache.zip"

		update_cache = requests.get(fetch_downloadurl, stream = True)

		open('update_cache.zip', 'wb').write(update_cache.content)

		print(f"{termcolors.OKGREEN}[#] Writing update_cache.zip file ...")
		update_cache_zipfile = ZipFile('update_cache.zip', 'r')
		print(f"{termcolors.OKGREEN}[#] Extracting update_cache.zip file ...")
		update_cache_zipfile.extractall()
		print(f"{termcolors.OKGREEN}[#] Cleaning up ...")
		update_cache_zipfile.close()
		os.remove("update_cache.zip")
		
		DependenciesManager()

		print(f"{termcolors.OKGREEN}\n[#] DONE INSTALLING THE UPDATE ...\n")

		print(f"{termcolors.BOLD}\n[!]You should now rerun the script.\n")
		input(f"{termcolors.HEADER}\n[Press Enter to Exit ...]")
		clearScreen()
		exit()

	except Exception as e:
		print(f"{termcolors.FAIL}[!] Can't download the file.")
		print(f"{termcolors.BOLD}Check your internet connection, or there's some server problem, or may be I don't know.\ntry again later ;)")
		input(f"{termcolors.HEADER}\n[Press Enter to Continue to Zracker ...]")
		RUN()


#try:

print(f"{termcolors.OKBLUE}\n[+] Checking for Updates ...")
url = "https://devim-stuffs.github.io/zracker/version_control"

document = requests.get(url).text
document = BeautifulSoup(document, 'lxml')

version = document.find(id="version_control").text


if float(version) > imported_version:
	# UPDATE AVAILABLE
	print(f"{termcolors.OKGREEN}[+] Updates are Available.")
	input(f"{termcolors.HEADER}\n[Press Enter to Move to Update Terminal ...]")
	Update()

else:
	# UP-TO-DATE
	print(f"{termcolors.BOLD}[+] You are Up-to-Date")
	input(f"{termcolors.HEADER}\n[Press Enter to Continue ...]")
	RUN()
'''
except Exception as e:
	print(f"{termcolors.FAIL}something went wrong ...")
	input(f"{termcolors.HEADER}\n[Press Enter to Continue to Zracker ...]")
	RUN()
'''
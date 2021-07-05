import os
import re
from colorama import init, Fore, Back, Style

init()

def check_file(filename):
    return bool(re.search('^[a-zA-Z0-9\.,\-_=\s]+', filename))

def check_folder(foldername):
    return bool(re.search('^[a-zA-Z\.0-9_\-\s]+', foldername))

directory = input("Enter directory: ")
all_files_correct = True

for root, dirs, files in os.walk(directory):
    for folder in dirs:
        if check_folder(folder):
            print(Fore.GREEN + root + "\\" + folder)
        else:
            print(Fore.RED + root + "\\" + folder + " foldername is invalid!")
            all_files_correct = False

    for item in files:
        if check_file(item):
            print(Fore.GREEN + root + "\\" + item)
        else:
            print(Fore.RED + root + "\\" + item + " filename is invalid!")
            all_files_correct = False

if all_files_correct:
    print(Fore.GREEN + "\nAll files have the correct naming.")
else:
    print(Fore.RED + "\nSome files have the wrong naming!")
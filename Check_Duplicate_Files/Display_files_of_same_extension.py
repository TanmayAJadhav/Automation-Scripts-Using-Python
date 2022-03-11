# Q) Design automation script which accept directory name and file extension from user. Display all files with that extension. 
# Usage : Display_files_of_same_extension.py Demo .txt 
# Demo is name of directory and .txt is the extension that we want to search.

import os
import sys

def DirectoryFileSearch(pathX,ext):
    flag = os.path.isabs(pathX)
    if flag == False:
        pathX = os.path.abspath(pathX)
    existsX = os.path.isdir(pathX)

    if existsX:
        print(f"file having extension '{ext}' : ")
        for folders,subfolders,filename in os.walk(pathX):
            for filen in filename:
                if ext in filen:
                    print(f"{filen}")

def main():
    print("Current file name :",sys.argv[0])  

    if len(sys.argv) > 3 or len(sys.argv) < 1 or len(sys.argv) == 1:
        print("Insufficient arguments")
        exit()

    DirectoryFileSearch(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()

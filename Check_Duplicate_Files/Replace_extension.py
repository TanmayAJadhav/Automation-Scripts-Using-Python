# Q) Design automation script which accept directory name and two file extensions from user. Rename all files with first file extension 
# with the second file extenntion. 
# Usage : Replace_extension.py “Demo” “.txt” “.doc” 
# Demo is name of directory and .txt is the extension that we want to search and rename with .doc. 
# After execution this script each .txt file gets renamed as .doc.

import os
import sys

def ReplaceExtensions(pathX,ext1,ext2):
    flag = os.path.isabs(pathX)
    if flag == False:
        pathX = os.path.abspath(pathX)
    existsX = os.path.isdir(pathX)

    if existsX:
        for folders,subfolders,filename in os.walk(pathX):
            print("Current folder is : ",folders)
            for filen in filename:
                if ext1 in filen:
                    old = os.path.join(folders,filen) 
                    new = old.replace(ext1,ext2)
                    print("Old path ",old)
                    print("New path ",new)
                    os.rename(old,new) 
    else:
        print("Invalid path")
        exit()                              
                    
def main():
    print("Current file name :",sys.argv[0])  

    if len(sys.argv) != 4:
        print("Insufficient arguments")
        exit()

    ReplaceExtensions(sys.argv[1], sys.argv[2], sys.argv[3])
    
if __name__ == "__main__":
    main()

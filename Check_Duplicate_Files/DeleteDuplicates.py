# 4) Design automation script which accept directory name and delete all duplicate files from that directory. Write names of duplicate files from that
# directory into log file named as Log.txt. Log.txt file should be created into current directory. Display execution time required for the script.  
# Usage : DirectoryDusplicateRemoval.py “Demo” 
# Demo is name of directory.

import os
import sys
import hashlib
import time

def HashFile(path,blocksize = 1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest() 

def FindDuplicate(pathX):
    flag = os.path.isabs(pathX)
    if flag == False:
        pathX = os.path.abspath(pathX)
    existsX = os.path.isdir(pathX)
    duplicates = {}
    duplilst = []

    if existsX:
        for folders,subfolders,filename in os.walk(pathX):
            print("Current folder is : ",folders)
            for filen in filename:
                pathX = os.path.join(folders,filen) 
                hash_file = HashFile(pathX)
                if hash_file in duplicates:
                    duplicates[hash_file].append(pathX)
                    duplilst.append(pathX)
                else:
                    duplicates[hash_file] = [pathX]                  
    else:
        print("Invalid path")
        exit()

    if len(duplilst) > 0:
        print("Duplicate files are : ")
        for files in duplilst:
            fd = open("Log.txt",'a')
            fd.write(files)
            fd.write("\n")
            print(files) 
    else:
        print("No duplicates found") 
        

    for files in duplilst:
        os.remove(files)
        print(files,"removed successfully...")

def main():
    print("Current file name :",sys.argv[0])  

    if len(sys.argv) > 2 or len(sys.argv) < 1 or len(sys.argv) == 1:
        print("Insufficient arguments")
        exit()

    start = time.time()
    FindDuplicate(sys.argv[1])
    end = time.time()
    print(f"Time taken {end - start} seconds")
    
if __name__ == "__main__":
    main()    
        

# Q)Design automation script which accept directory name and display checksum of all files. 
# Usage : Display_Checksum.py Demo 
# Demo is name of directory.

import os
import sys
import hashlib

def HashFile(path,blocksize = 1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest() 

def DirectoryFileSearch(pathX):
    flag = os.path.isabs(pathX)
    if flag == False:
        pathX = os.path.abspath(pathX)
    existsX = os.path.isdir(pathX)

    if existsX:
        for folders,subfolders,filename in os.walk(pathX):
            print("Current folder is : ",folders)
            for filen in filename:
                pathX = os.path.join(folders,filen) 
                print(filen," : ",HashFile(pathX))
    else:
        print("Invalid path")              
                
                    
def main():
    print("Current file name :",sys.argv[0])  

    if len(sys.argv) != 2:
        print("Insufficient arguments")
        exit()

    DirectoryFileSearch(sys.argv[1])
    
if __name__ == "__main__":
    main()

# Script is used to get maximum size of file in directory

import os
import sys

def getfileSize(srcPath):
    flag = os.path.isabs(srcPath)
    if flag == False:
        srcPath = os.path.abspath(srcPath)
    srcExists = os.path.isdir(srcPath)

    maxfilesize = 0
    if srcExists:
        for folders,subfolder,filename in os.walk(srcPath):
            print("Current folder is : ",folders)
            for filen in filename:
                filen = os.path.join(folders,filen)
                currentfilesize = os.path.getsize(filen)
                if maxfilesize < currentfilesize:
                    maxfilesize = currentfilesize
                    maxfile = filen                    
    else:
        print("Invalid path")
        exit()                         
    print(f"Biggest file in directory is {maxfile} and has {maxfilesize} bytes")       

def main():
    print("Current application name : ",sys.argv[0])
    if(len(sys.argv) > 2 or len(sys.argv) <= 1):
        print("Insufficient arguments")
        exit()
    if (sys.argv[1] == "-u") or (sys.argv[1] == "-U"):
            print("Usage: Script is used to get maximum size of file in directory")
            exit()

    if (sys.argv[1] == "-h") or (sys.argv[1] == "-H"):
        print("Help: Name_of_Script dir_name")
        exit()

    getfileSize(sys.argv[1])    

if __name__ == "__main__":
    main()

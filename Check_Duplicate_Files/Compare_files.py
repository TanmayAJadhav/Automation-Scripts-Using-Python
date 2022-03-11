# Q)Write a program which accept two file names from user and compare contents of both the files. If both the files contains same contents then display 
# success otherwise display failure. Accept names of both the files from command line. 
# Input : Demo.txt Hello.txt 
# Compare contents of Demo.txt and Hello.txt 

from sys import *
import os
import hashlib

def hashfile(filename):
    md5_hash = hashlib.md5()
    afile = open(filename, "rb")
    content = afile.read()
    md5_hash.update(content)

    digest = md5_hash.hexdigest()
    return digest

def main():
    print("Current file name : ",argv[0])
    if len(argv) > 3 or len(argv) < 1 or len(argv) == 1:
        print("Insufficient arguments")
        exit()
    if os.path.exists(argv[1]) and os.path.exists(argv[1]):     
        hsh1 = hashfile(argv[1])
        hsh2 = hashfile(argv[2])

        if hsh1 == hsh2:
            print("Success")
        else:
            print("Failure")
    else:
        print("File not exits")            
    
if __name__ == "__main__":
    main()

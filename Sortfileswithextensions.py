# program to sort files according to extension in newly created directories(move)

import os
import pathlib
import sys
import shutil

def makepartition(srcPath):
    flag = os.path.isabs(srcPath)
    if flag == False:
        srcPath = os.path.abspath(srcPath)
    srcExists = os.path.isdir(srcPath)

    if srcExists:
        for folders,subfolders,filename in os.walk(srcPath):
            print("Current folder is : ",folders)
            for filen in filename:
                file_extension = pathlib.Path(filen).suffix
                filen = os.path.join(folders,filen)
                
                checkpath = os.path.join(srcPath,file_extension)
                if os.path.isdir(checkpath) == False:
                    os.mkdir(checkpath) 

                dstpath = os.path.join(srcPath,file_extension)
                shutil.move(filen,dstpath) 
                # print(filen," ",dstpath)
    else:
        print("Invalid path")
        exit()            

def main():
    print("Current application name : ",sys.argv[0])
    if(len(sys.argv) > 6 or len(sys.argv) <= 1):
        print("Insufficient arguments")
        exit()
    if (sys.argv[1] == "-u") or (sys.argv[1] == "-U"):
            print("Usage: Script is used to create seperate directory for")
            exit()

    if (sys.argv[1] == "-h") or (sys.argv[1] == "-H"):
        print("Help: Name_of_Script dir_name")
        exit()

    makepartition(sys.argv[1])    

if __name__ == "__main__":
    main()

# Q) Design automation script which accept two directory names. Copy all files from first directory into second directory. Second 
# directory should be created at run time. 
# Usage : Copy_files.py “Demo” “Temp” 
# Demo is name of directory which is existing and contains files in it. We have to create new 
# Directory as Temp and copy all files from Demo to Temp.

import os
import sys
import shutil

def CopyFiles(srcPath,dstPath):
    flag = os.path.isabs(srcPath)
    if flag == False:
        srcPath = os.path.abspath(srcPath)
    existsX1 = os.path.isdir(srcPath)
    existsX2 = os.path.isdir(dstPath)

    dstPath = os.path.abspath(dstPath)
    if existsX1:
        fd = open("LogCopy.txt",'a')
        if existsX2 == False:
            os.mkdir(os.path.abspath(dstPath))
        for folders,subfolders,filename in os.walk(srcPath):
            print("Current folder is : ",folders)
            for filen in filename:
                filen = os.path.join(folders,filen)
                fd.write(f'{filen} copied at {dstPath}')
                fd.write("\n")
                shutil.copy(filen,dstPath,follow_symlinks=True) 
    else:
        print("Invalid path")   
        exit()
   
def main():
    print("Current file name :",sys.argv[0])  

    if len(sys.argv) != 3:
        print("Insufficient arguments")
        exit()

    CopyFiles(sys.argv[1],sys.argv[2])
    
if __name__ == "__main__":
    main()

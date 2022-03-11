# Q) Design automation script which accept two directory names and one file extension. Copy all files with the specified extension 
# from first directory into second directory. Second directory should be created at run time. 
# Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe” 
# Demo is name of directory which is existing and contains files in it. We have to create new 
# Directory as Temp and copy all files with extension .exe from Demo to Temp.

import os
import sys
import shutil
import pathlib

def CopyFiles(srcPath,dstPath,ext):
    flag = os.path.isabs(srcPath)
    if flag == False:
        srcPath = os.path.abspath(srcPath)
    existsX1 = os.path.isdir(srcPath)
    existsX2 = os.path.isdir(dstPath)

    dstPath = os.path.abspath(dstPath)
    if existsX1:
        if existsX2 == False:
            os.mkdir(os.path.abspath(dstPath))
        for folders,subfolders,filename in os.walk(srcPath):
            print("Current folder is : ",folders)
            for filen in filename:
                oldFile = filen
                filen = os.path.join(folders,filen)
                shutil.copy(filen,dstPath,follow_symlinks=True) 
                oldFile = os.path.join(dstPath,oldFile)
                ext1 = pathlib.Path(filen).suffix
                newFile = oldFile.replace(ext1,ext)
                os.rename(oldFile,newFile)
                
    else:
        print("Invalid path")   
        exit()
   
def main():
    print("Current file name :",sys.argv[0])  

    if len(sys.argv) != 4 :
        print("Insufficient arguments")
        exit()
  
    CopyFiles(sys.argv[1],sys.argv[2],sys.argv[3])
    
if __name__ == "__main__":
    main()

# 2.Design automation script which accept process name and display information of that process if it is running. 
#  Usage : ProcInfo.py Notepad 

import psutil
import sys

def ProcessDisplay(process_name):
    listprocess = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            if pinfo['name'] == process_name:
                listprocess.append(pinfo)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess    

def main():
    print("Process Monitor")

    if len(sys.argv) > 2 or len(sys.argv) < 1 or len(sys.argv) == 1:
        print("Insufficient arguments")
        exit()  

    if (sys.argv[1] == "-u") or (sys.argv[1] == "-U"):
            print("Usage: Script is used check whether given process running or not")
            exit()

    if (sys.argv[1] == "-h") or (sys.argv[1] == "-H"):
        print("Help: Name_of_Script Name_of_process")
        exit()
    listprocess = ProcessDisplay(sys.argv[1])

    if listprocess == []:
        print(f"No process of {sys.argv[1]} running")    
    for proc in listprocess:
        print(proc)

if __name__ == "__main__":
    main()    

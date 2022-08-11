# 1.Design automation script which display information of running processes as its name, PID, Username. 
# Usage : ProcInfo.py

import psutil

def ProcessDisplay():
    listprocess = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])

            listprocess.append(pinfo)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess    

def main():
    print("Process Monitor")

    listprocess = ProcessDisplay()

    for proc in listprocess:
        print(proc)

if __name__ == "__main__":
    main()    

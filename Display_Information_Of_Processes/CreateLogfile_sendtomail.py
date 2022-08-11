# 4. Design automation script which accept directory name and mail id from user and create log file in that directory which contains 
# information of running processes as its name, PID, Username. After creating log file send that log file to the specified mail. 
# Usage : ProcInfoLog.py Demo Marvellousinfosystem@gmail.com 
# Demo is name of Directory. 
# marvellousinfosystem@gmail.com is the mail id.

import os
import psutil
import sys
import time
import smtplib
from email.message import EmailMessage
from urllib.request import urlopen
import re

def is_connected():
    try:
        urlopen("https://www.google.com/", timeout=1)
        return True
    except:
        return False 

def sendmail(recievers_mail,log_dir):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    senders_mail = "tanmayjadhav025@gmail.com"
    body = "File attachment..."
    msg  = EmailMessage()
    msg['subject'] = "Email using python"
    msg['From'] = senders_mail 
    msg['To'] = recievers_mail
    msg.set_content(body)

    msg.add_attachment(open(log_dir, "r").read(), filename=log_dir)

    server.login(senders_mail, "Tanmay@123")
    server.send_message(msg)

    print("Mail sent")

def ProcessDisplay(log_dir = "Marvellous"):
    processlst = []
    if os.path.exists(log_dir) == False:
        try:
            os.mkdir(log_dir)
        except:
            pass 

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms'] = proc.memory_info().vms/1024*1024
            processlst.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return processlst, log_dir

def MakeFile(log_dir):
    processlst, log_dir = ProcessDisplay(log_dir)

    seperator = '-'*80
    file_name = f"MarvellousLog{time.ctime()}.log"
    filename = file_name.replace(" ","_")
    filename = filename.replace(":","_")
    log_path = os.path.join(log_dir,filename)
    fd = open(log_path,'w')
    fd.write(seperator+'\n')
    fd.write(f"Marvellous Infosystem Log file {time.ctime()}\n")
    fd.write(seperator+'\n')     

    cnt = 0        
    for proc in processlst:
        cnt += 1
        fd.write(str(proc)+"\n") 

    fd.write(seperator+'\n')
    fd.write(f"Number of processes: {cnt}\n")     
    fd.write(seperator+'\n')
    return log_path 

def checkEmail(recievers_email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, recievers_email)):
        return True
 
    else:
        return False

def main():
    print("Current filname :",sys.argv[0])

    if len(sys.argv) > 3 or len(sys.argv) < 1 or len(sys.argv) == 1:
        print("Insufficient arguments")
        exit()  

    if (sys.argv[1] == "-u") or (sys.argv[1] == "-U"):
            print("Usage: Script is used to Create log file of running processes and send to mail")
            exit()

    if (sys.argv[1] == "-h") or (sys.argv[1] == "-H"):
        print("Help: Name_of_Script dir_name sender's_Emailaddress")
        exit()

    ProcessDisplay(sys.argv[1])

    log_dir = MakeFile(sys.argv[1])

    if is_connected():
        if checkEmail(sys.argv[2]):
            sendmail(sys.argv[2],log_dir)
        else:
            print("Invalid Email Address")    

if __name__ == "__main__":
    main()    

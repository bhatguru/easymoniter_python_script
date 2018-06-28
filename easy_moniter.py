#!/usr/bin/python3
import requests
import smtplib
import os
import psutil
import time
import threading
#******************Colors******************************************************************************
headers = '\033[95m'
okblue = '\033[94m'
okgreen = '\033[92m'
warning = '\033[93m'
fail = '\033[91m'
endc = '\033[0m'
bold = '\033[1m'
underline = '\033[4m'

#*******************Checks Internet Connection*********************************************************
def CheckInet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        # print("internet_is_"+okgreen+"active"+endc)
        return 1
    except requests.ConnectionError:
        # print(fail+"No internet connection available."+endc)
        return 0

#*********************Sends Mail************************************************************************
#Here i coustomized for gmail only....If you have smtp of different id
#you can try modifying them at below-->smtplib.SMTP('smtp.your domain.com')
#*******************************************************************************************************
def SendMail():
    # ***************************************************************************************************
    # .edit the serverconfig file with your details
    # .remove <> symbols
    # .enter source email_id password and target email_id with single space between them
    # ***************************************************************************************************
    # Rt = open("serverconfig.txt", "w")
    # Rt.write('<email> <password> <target_mail_id>')
    # Rt.close()
    with open('serverconfig.txt') as conf:
        all_host = conf.readlines()
        for line in all_host:
            host = line.split(' ')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(host[0], host[1])
    msg = "Your System Memory or CPU is almost full"
    server.sendmail(host[0], host[2], msg)
    server.quit()

def Machineinfo():
    with open('serverconfig.txt') as conf:
        all_host = conf.readlines()
        for line in all_host:
            host = line.split(' ')
    threshold = host[3]
    Mem = psutil.virtual_memory()
    Percent_Utiliztion = Mem.percent
    CPU_Percent = psutil.cpu_percent()
    while 1:
        if Percent_Utiliztion >= float(60) or CPU_Percent >= float(60):
            if CheckInet() == 1:
                try:
                    SendMail()
                    # time.sleep(threshold)
                except: print("Please provide the valid informaitons in serverconfig.txt")
            else:
                print("cant send email..!!! please check your internet connection")

        if Percent_Utiliztion < float(80) and CPU_Percent >= float(80):
            time.sleep(1)
            print(headers + "MEM:" + endc + okblue + str(Percent_Utiliztion) + "%\t" + endc + headers + "CPU:"+ endc + warning + str(CPU_Percent) + "%" + endc)

        elif Percent_Utiliztion >= float(80) and CPU_Percent < float(80):
            time.sleep(1)
            print(headers + "MEM:" + endc + warning + str(Percent_Utiliztion) + "%\t" + endc + headers + "CPU:"+ endc + okblue + str(CPU_Percent) + "%" + endc)
        elif Percent_Utiliztion >= float(80) and CPU_Percent >= float(80):
            time.sleep(1)
            print(headers + "MEM:" + endc + warning + str(Percent_Utiliztion) + "%\t" + endc + headers + "CPU:"+ endc + warning + str(CPU_Percent) + "%" + endc)
        elif Percent_Utiliztion >= float(50) and CPU_Percent >= float(50):
            time.sleep(1)
            print(headers + "MEM:" + endc + okblue + str(Percent_Utiliztion) + "%\t" + endc + headers + "CPU:"+ endc + okblue + str(CPU_Percent) + "%" + endc)

        elif Percent_Utiliztion < float(50) and CPU_Percent < float(50):
            time.sleep(1)
            print(headers + "MEM:" + endc + okgreen + str(Percent_Utiliztion) + "%\t" + endc + headers + "CPU:" + endc + okgreen + str(CPU_Percent) + "%" + endc)

        # print("MEM:"+str(Percent_Utiliztion)+"%\t"+"CPU:"+str(CPU_Percent)+"%")
        elif Percent_Utiliztion < float(50) and CPU_Percent >= float(50):
            time.sleep(1)
            print(headers + "MEM:" + endc + okgreen + str(Percent_Utiliztion) + "%\t" + endc + headers + "CPU:" + endc + okblue + str(CPU_Percent) + "%" + endc)
        elif Percent_Utiliztion >= float(50) and CPU_Percent < float(50):
            time.sleep(1)
            print(headers + "MEM:" + endc + okblue + str(Percent_Utiliztion) + "%\t" + endc + headers + "CPU:" + endc + okgreen + str(CPU_Percent) + "%" + endc)

        Mem = psutil.virtual_memory()
        Percent_Utiliztion = Mem.percent
        CPU_Percent = psutil.cpu_percent()

def main():
    t1 = threading.Thread(target=Machineinfo(), args=None)
    t1.start()
if __name__ == '__main__':
    main()
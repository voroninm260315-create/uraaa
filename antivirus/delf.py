import os
import signal
import psutil
import time

os.chdir(r'C:\Users\Администратор\PycharmProjects\nedohacker\venv\Lib\site-packages\flet_desktop\app\flet')
process_name = "flet.exe"
for process in psutil.process_iter(attrs=['pid', 'name']):
    if process.info['name'] == process_name:
        external_pid = process.info['pid']
        os.kill(external_pid, signal.SIGTERM)
        time.sleep(0.5)
        break


os.remove('C:/0.exe')
os.remove('C:/1.exe')
os.remove('C:/2.exe')
os.remove('C:/3.exe')



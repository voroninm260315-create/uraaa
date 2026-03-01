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


os.remove('C:/a.exe')
os.remove('C:/b.exe')
os.remove('C:/c.exe')
os.remove('C:/d.exe')




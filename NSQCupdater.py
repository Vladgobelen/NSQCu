import urllib.request
import shutil
import os
import zipfile
import re
import subprocess
import json
import ast

for root, dirs, files in os.walk(os.getenv('APPDATA')):
    for dir in dirs:
        if 'Sirus' in dir:
            path = os.path.join(root, dir)
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith('.log'):
                        regex = re.compile(r'"client":{"folder":"([^"]+)"')
                        data = open(os.path.join(root, file), 'rb').read().decode('windows-1251').replace('\x00', '')
                        rez = regex.findall(data)
                        if rez:
                            if os.path.isdir(rez[0] + '\\Interface\\AddOns\\NSQC'):
                                shutil.rmtree(rez[0] + '\\Interface\\AddOns\\NSQC')

                            urllib.request.urlretrieve("https://github.com/Vladgobelen/NSQC/archive/refs/heads/main.zip", "main.zip")
                            archive = 'main.zip'
                            with zipfile.ZipFile(archive, 'r') as zip_file:
                                zip_file.extractall(rez[0] + '\\Interface\\AddOns')

                            os.rename(rez[0] + '\\Interface\\AddOns\\NSQC-main', rez[0] + '\\Interface\\AddOns\\NSQC')
if os.path.isfile('main.zip'):
    os.remove('main.zip')
input('Аддон успешно обновлен')



import urllib.request
import shutil
import os
import zipfile
import re
import subprocess
import json
import ast
import time
import datetime

for root, dirs, files in os.walk(os.getenv('APPDATA')): #читаем рекурсивно каталог %AppData%
    for dir in dirs: #ищем каталоги
        if 'Sirus' in dir: #если в каталоге есть слово Сирус
            path = os.path.join(root, dir) #путь = путь к этому каталогу
            for root, dirs, files in os.walk(path): #читаем рекурсивно все каталоги в этом пути
                for file in files: #читаем рекурсивно все файлы в этом пути
                    if file.endswith('.log'): #если расширение файла .log то:
                        regex = re.compile(r'"client":{"folder":"([^"]+)"') #ищем начало пути к вовке (регексп)
                        data = open(os.path.join(root, file), 'rb').read().decode('windows-1251').replace('\x00', '') #переводим кодировку текста файла в ascii null byte
                        rez = regex.findall(data) #ищем регексп выше
                        if rez: #если нашли, то
                            for root, dirs, files in os.walk(rez[0]):
                                for dir in dirs:
                                    if 'AddOns' in dir:
                                        path1 = os.path.join(root,dir)
                                        urllib.request.urlretrieve("https://github.com/Vladgobelen/NSQC/archive/refs/heads/main.zip", "main.zip") #качаем архив с аддоном
                                        archive = 'main.zip' #название скачанного архива
                                        with zipfile.ZipFile(archive, 'r') as zip_file: #проверка на открытие файла
                                            zip_file.extractall(path1) #распаковать архив в аддоны сируса

                                        for root, dirs, files in os.walk(path1):
                                            for dir in dirs:
                                                if 'NSQC-main' in dir:
                                                    path2 = os.path.join(root,dir)
                                                    shutil.copytree(path2, path1 + '\\NSQC',dirs_exist_ok=True)
                                                    if os.path.isdir(path2): #если аддон существует, то
                                                        shutil.rmtree(path2) #удаляем аддон

if os.path.isfile('main.zip'): #если скачанный архив существует возле апдейтера, то
    os.remove('main.zip') #далить архив
input('Аддон успешно обновлен') #вывести в консоли надпись "Аддон успешно обновлен" с запросом на нажатие любой кнопки клавиатуры



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

for root, dirs, files in os.walk(os.path.abspath(os.getenv('APPDATA'))): #читаем рекурсивно каталог %AppData%
	testPer = 1
	for dir in dirs: #ищем каталоги
		testPer = 2
		if 'Sirus' in dir: #если в каталоге есть слово Сирус
			testPer = 3
			path = os.path.join(root, dir) #путь = путь к этому каталогу
			testPer = 4
			for root, dirs, files in os.walk(path): #читаем рекурсивно все каталоги в этом пути
				testPer = 5
				for file in files: #читаем рекурсивно все файлы в этом пути
					testPer = 6
					if file.endswith('.log'): #если расширение файла .log то:
						testPer = 7
						regex = re.compile(r'"client":{"folder":"([^"]+)"') #ищем начало пути к вовке (регексп)
						testPer = 8
						data = open(os.path.join(root, file), 'rb').read().decode('windows-1251').replace('\x00', '') #переводим кодировку текста файла в ascii null byte
						testPer = 9
						rez = regex.findall(data) #ищем регексп выше
						if rez: #если нашли, то
							testPer = 10
							for root, dirs, files in os.walk(rez[0]):
								testPer = 11
								for dir in dirs:
									testPer = 12
									if 'AddOns' in dir:
										testPer = 13
										path1 = os.path.join(root,dir)
										urllib.request.urlretrieve("https://github.com/Vladgobelen/NSQC/archive/refs/heads/main.zip", "main.zip") #качаем архив с аддоном
										testPer = 14
										archive = 'main.zip' #название скачанного архива
										testPer = 15
										with zipfile.ZipFile(archive, 'r') as zip_file: #проверка на открытие файла
											testPer = 16
											zip_file.extractall(path1) #распаковать архив в аддоны сируса
											testPer = 17

										for root, dirs, files in os.walk(path1):
											testPer = 18
											for dir in dirs:
												testPer = 19
												if 'NSQC-main' in dir:
													testPer = 20
													path2 = os.path.join(root,dir)
													shutil.copytree(path2, path1 + '\\NSQC',dirs_exist_ok=True)
													if os.path.isdir(path2): #если аддон существует, то
														testPer = 21
														shutil.rmtree(path2) #удаляем аддон
														testPer = 22
												else:
													testPer = 555
									else:
										testPer = 444
					else:
						testPer = 333
		else:
			testPer = 222
if os.path.isfile('main.zip'): #если скачанный архив существует возле апдейтера, то
	os.remove('main.zip') #далить архив
#if testPer != 22:
#	input('Аддон успешно обновлен') #вывести в консоли надпись "Аддон успешно обновлен" с запросом на нажатие любой кнопки клавиатуры
#else:
input(testPer)



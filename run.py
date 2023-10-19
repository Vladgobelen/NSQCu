import urllib.request
import shutil
import os
import zipfile
import subprocess
from subprocess import Popen, PIPE
import os.path
import shlex
import time

print('1')
def process_exists(process_name):
	print('2')
	progs = str(subprocess.check_output('tasklist'))
	if process_name in progs:
		return True
	else:
		return False

print(process_exists('Wow.exe'))
print('3')
def update():
	print(process_exists('Wow.exe'))
	print('4')
	f = urllib.request.urlopen('https://github.com/Vladgobelen/NSQC/blob/main/vers').read().decode('utf-8').strip()
	file = open('Interface/AddOns/NSQC/vers', 'r')
	print(process_exists('Wow.exe'))
	print('5')
	if not file.readline().strip() in f:
		print(process_exists('Wow.exe'))
		print('6')
		if os.path.isdir('temp'):
			shutil.rmtree('temp/')
		urllib.request.urlretrieve("https://github.com/Vladgobelen/NSQC/archive/refs/heads/main.zip", "main.zip")
		archive = 'main.zip'
		with zipfile.ZipFile(archive, 'r') as zip_file:
			zip_file.extractall("temp")
		file_source = 'temp/NSQC-main/'
		print(file_source)
		file_destination = 'Interface/AddOns/NSQC/'
		if not os.path.exists(file_destination):
			os.mkdir(file_destination)
		get_files = os.listdir(file_source)
		shutil.copytree(file_source, file_destination,dirs_exist_ok=True)
		if os.path.isfile('main.zip'):
			os.remove('main.zip')
		if os.path.isdir('temp'):
			shutil.rmtree('temp/')
	file.close()
	del f

print(process_exists('Wow.exe'))
print('7')
update()

if not process_exists('Wow.exe'):
	os.startfile("Wow.exe")
print('8')
while True:
	print('9')
	if process_exists('Wow.exe'):
		update()
		print('11')
		time.sleep(10)
		print(process_exists('Wow.exe'))
		print('12')
	else:
		break

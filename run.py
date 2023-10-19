import urllib.request
import shutil
import os
import zipfile
import subprocess
from subprocess import Popen, PIPE
import os.path
import shlex
import time

def process_exists(process_name):
	progs = str(subprocess.check_output('tasklist'))
	if process_name in progs:
		return True
	else:
		return False

def update():
	f = int(urllib.request.urlopen('https://raw.githubusercontent.com/Vladgobelen/NSQC/main/vers').read().decode('utf-8').strip())
	f1 = int(urllib.request.urlopen('https://raw.githubusercontent.com/Vladgobelen/NSQC/main/versad').read().decode('utf-8').strip())
	file = open('Interface/AddOns/NSQC/vers', 'r')
	file1 = open('Interface/AddOns/NSQC/versad', 'r')
	ff = int(file.readline().strip())
	ff1 = int(file1.readline().strip())
	if int(f) != ff or int(f1) != ff1:
		if os.path.isdir('temp'):
			shutil.rmtree('temp/')
		urllib.request.urlretrieve("https://github.com/Vladgobelen/NSQC/archive/refs/heads/main.zip", "main.zip")
		archive = 'main.zip'
		with zipfile.ZipFile(archive, 'r') as zip_file:
			zip_file.extractall("temp")
		file_source = 'temp/NSQC-main/'
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
	file1.close()
	del f
	del f1

update()

if not process_exists('Wow.exe'):
	subprocess.run("Wow.exe")

while True:
	if process_exists('Wow.exe'):
		update()
		time.sleep(10)
	else:
		break

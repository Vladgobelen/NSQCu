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
	f = urllib.request.urlopen('https://github.com/Vladgobelen/NSQC/blob/main/vers').read().decode('utf-8').strip()
	file = open('Interface/AddOns/NSQC/vers', 'r')
	if not file.readline().strip() in f:
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
	del f

update()

if not process_exists('Wow.exe'):
	subprocess.run("Wow.exe")

while True:
	if process_exists('Wow.exe'):
		update()
		time.sleep(10)
	else:
		break

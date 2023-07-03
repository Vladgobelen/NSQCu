import urllib.request
urllib.request.urlretrieve("https://github.com/Vladgobelen/klad/archive/refs/heads/main.zip", "main.zip")

import zipfile
archive = 'main.zip'
with zipfile.ZipFile(archive, 'r') as zip_file:
    zip_file.extractall("temp")

import shutil
import os
if os.path.isdir('test'):
    shutil.rmtree('test')

import shutil
import os
os.mkdir("test")
file_source = 'temp/klad-main/'
file_destination = 'temp/../test/'

get_files = os.listdir(file_source)

for g in get_files:
    shutil.move(file_source + g, file_destination)

import shutil
shutil.rmtree('temp')

if os.path.isfile('main.zip'):
    os.remove('main.zip')

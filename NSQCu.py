import urllib.request
import shutil
import os
import zipfile

if os.path.isdir('temp'):
    shutil.rmtree('temp/')

urllib.request.urlretrieve("https://github.com/Vladgobelen/NSQC/archive/refs/heads/main.zip", "main.zip")

archive = 'main.zip'
with zipfile.ZipFile(archive, 'r') as zip_file:
    zip_file.extractall("temp")

if os.path.isfile('KLADu.exe'):
    os.remove('KLADu.exe')
if os.path.isfile('.gitignore'):
    os.remove('.gitignore')
if os.path.isfile('achivC.lua'):
    os.remove('achivC.lua')
if os.path.isfile('btn.lua'):
    os.remove('btn.lua')
if os.path.isfile('coreC.lua'):
    os.remove('coreC.lua')
if os.path.isfile('functionsC.lua'):
    os.remove('functionsC.lua')
if os.path.isfile('gmList.lua'):
    os.remove('gmList.lua')
if os.path.isfile('gob.ogg'):
    os.remove('gob.ogg')
if os.path.isfile('LICENSE'):
    os.remove('LICENSE')
if os.path.isfile('lvlUp.ogg'):
    os.remove('lvlUp.ogg')
if os.path.isfile('minimap.lua'):
    os.remove('minimap.lua')
if os.path.isfile('NSQC.toc'):
    os.remove('NSQC.toc')
if os.path.isfile('officerSnifC.lua'):
    os.remove('officerSnifC.lua')
if os.path.isfile('README.md'):
    os.remove('README.md')
if os.path.isfile('risIcon.lua'):
    os.remove('risIcon.lua')
if os.path.isfile('roll.lua'):
    os.remove('roll.lua')
if os.path.isfile('roll.lua'):
    os.remove('roll.lua')

if os.path.isdir('chiavi'):
    shutil.rmtree('chiavi/')
if os.path.isdir('npcscan'):
    shutil.rmtree('npcscan/')
if os.path.isdir('libs'):
    shutil.rmtree('libs/')

file_source = 'temp/NSQC-main/'
file_destination = 'temp/..'

get_files = os.listdir(file_source)

for g in get_files:
    if g != "NSQCu-1.exe":
        shutil.move(file_source + g, file_destination)

if os.path.isfile('main.zip'):
    os.remove('main.zip')
if os.path.isdir('temp'):
    shutil.rmtree('temp/')
if os.path.isfile('NSQCu.exe'):
    os.remove('NSQCu.exe')

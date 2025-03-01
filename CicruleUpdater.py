import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
import urllib.request
import shutil
import os
import zipfile
import subprocess
from subprocess import Popen, PIPE
import os.path
import shlex
import time

top = Tk()

class Tooltip:
	def __init__(self, widget, text):
		self.widget = widget
		self.text = text
		self.tooltip = None
		self.widget.bind("<Enter>", self.show)
		self.widget.bind("<Leave>", self.hide)

	def show(self, event=None):
		x, y, _, _ = self.widget.bbox("insert")
		x += self.widget.winfo_rootx() + 25
		y += self.widget.winfo_rooty() + 25

		self.tooltip = tk.Toplevel(self.widget)
		self.tooltip.wm_overrideredirect(True)
		self.tooltip.wm_geometry(f"+{x}+{y}")

		label = ttk.Label(self.tooltip, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
		label.pack()

	def hide(self, event=None):
		if self.tooltip:
			self.tooltip.destroy()
			self.tooltip = None

def start_guoko():
	os.startfile("Wow.exe")
btn = ttk.Button(text="Запустить игру", command = start_guoko)
btn.pack()

addons = {
	'NSQC' : {"link": "https://github.com/Vladgobelen/NSQC/archive/refs/heads/main.zip", "описание": "Гильдейский аддон для Ночной стражи", "путь": "Interface/AddOns/NSQC/", "файл": 0, "временный путь": "temp/NSQC-main/", "путь к аддону": "Interface/AddOns/NSQC/"},
	'Карты подземелий' : {"link": "https://hub.mos.ru/vladgobelen/nsqcmap/-/raw/main/patch-ruRU-M.MPQ", "описание": "Патч для карт подземелий", "путь": "Data/ruRU/patch-ruRU-M.MPQ", "файл": 1, "путь к аддону": "Data/ruRU/patch-ruRU-M.MPQ"},
	'WDM' : {"link": "https://github.com/Trimitor/WDM-addons/archive/refs/heads/main.zip", "описание": "Аддон для правильного отображения карт подземелий", "путь": "Interface/AddOns/WDM/", "файл": 0, "временный путь": "temp/WDM-addons-main/WDM/", "путь к аддону": "Interface/AddOns/WDM/"},
	'Bartender4' : {"link": "https://hub.mos.ru/vladgobelen/nsqcmap/-/raw/main/Bartender4.zip", "описание": "Аддон настройки панелей(очень удобный!!!)", "путь": "Interface/AddOns/", "файл": 2, "временный путь": "temp/", "путь к аддону": "Interface/AddOns/Bartender4"},
	'ArkInventory' : {"link": "https://hub.mos.ru/vladgobelen/nsqcmap/-/raw/main/ArkInventory.zip", "описание": "Аддон для сумок(объединение сумок в одну, сортировка шмота)", "путь": "Interface/AddOns/", "файл": 2, "временный путь": "temp/", "путь к аддону": "Interface/AddOns/ArkInventory"},
	'Chatter' : {"link": "https://hub.mos.ru/vladgobelen/nsqcmap/-/raw/main/Chatter.zip", "описание": "Аддон для настройки чата, копирования текста и ссылок", "путь": "Interface/AddOns/", "файл": 2, "временный путь": "temp/", "путь к аддону": "Interface/AddOns/Chatter"},
	'Crap Away' : {"link": "https://hub.mos.ru/vladgobelen/nsqcmap/-/raw/main/CrapAway.zip", "описание": "Автоматическая продажа серого мусора из сумок", "путь": "Interface/AddOns/", "файл": 2, "временный путь": "temp/", "путь к аддону": "Interface/AddOns/CrapAway"},
	'Gear Score' : {"link": "https://hub.mos.ru/vladgobelen/nsqcmap/-/raw/main/GearScore.zip", "описание": "Какой то странный способ оценки крутости шмота", "путь": "Interface/AddOns/", "файл": 2, "временный путь": "temp/", "путь к аддону": "Interface/AddOns/GearScore"},
	'Grid2' : {"link": "https://hub.mos.ru/vladgobelen/nsqcmap/-/raw/main/Grid2.zip", "описание": "Охренительно удобный аддон для хилов", "путь": "Interface/AddOns/", "файл": 2, "временный путь": "temp/", "путь к аддону": "Interface/AddOns/Grid2"},
	'Plate Buffs' : {"link": "https://hub.mos.ru/vladgobelen/nsqcmap/-/raw/main/PlateBuffs.zip", "описание": "Отображение бафов и дебафов цели прямо на ней", "путь": "Interface/AddOns/", "файл": 2, "временный путь": "temp/", "путь к аддону": "Interface/AddOns/PlateBuffs"},
	'Range Display' : {"link": "https://hub.mos.ru/vladgobelen/nsqcmap/-/raw/main/RangeDisplay.zip", "описание": "Отображение расстояния до цели", "путь": "Interface/AddOns/", "файл": 2, "временный путь": "temp/", "путь к аддону": "Interface/AddOns/RangeDisplay"},
	'Skada' : {"link": "https://hub.mos.ru/vladgobelen/nsqcmap/-/raw/main/Skada.zip", "описание": "Аддон для вычисления урона, отхила игрока, пати рейда", "путь": "Interface/AddOns/", "файл": 2, "временный путь": "temp/", "путь к аддону": "Interface/AddOns/Skada"},
	'Tom Tom' : {"link": "https://hub.mos.ru/vladgobelen/nsqcmap/-/raw/main/TomTom.zip", "описание": "Добавляет координаты игрока на карту и не только", "путь": "Interface/AddOns/", "файл": 2, "временный путь": "temp/", "путь к аддону": "Interface/AddOns/TomTom"},
	'DBM' : {"link": "https://hub.mos.ru/vladgobelen/nsqcmap/-/raw/main/dbm.zip", "описание": "Обязательный аддон для рейдов", "путь": "Interface/AddOns/", "файл": 2, "временный путь": "temp/", "путь к аддону": "Interface/AddOns/DBM-Core"},
	'Gatherer' : {"link": "https://hub.mos.ru/vladgobelen/nsqcmap/-/raw/main/Gatherer.zip", "описание": "Аддон для сбора ресурсов: трава, руда", "путь": "Interface/AddOns/", "файл": 2, "временный путь": "temp/", "путь к аддону": "Interface/AddOns/Gatherer"},
	'Auctionator' : {"link": "https://hub.mos.ru/vladgobelen/nsqcmap/-/raw/main/Auctionator.zip", "описание": "Аддон для работы с аукционом", "путь": "Interface/AddOns/", "файл": 2, "временный путь": "temp/", "путь к аддону": "Interface/AddOns/Auctionator"},
	'BonusScanner' : {"link": "https://hub.mos.ru/vladgobelen/nsqcmap/-/blob/main/BonusScanner.zip", "описание": "Хрень, нужная для аддона Gear Score", "путь": "Interface/AddOns/", "файл": 2, "временный путь": "temp/", "путь к аддону": "Interface/AddOns/BonusScanner"},
}

def dl(count, block_size, total_size):
	progress_size = count * block_size
	percent = progress_size * 100 / total_size
	top.title(str('{0:.2g}'.format(percent)) + "%")
for name, value in addons.items():
	var = IntVar()

	def print_value(name, addon):
		def on_call():
			if addon['check_var'].get() == 0:
				if addon['файл'] == 0:
					if os.path.isdir(addon['путь']):
						shutil.rmtree(addon['путь'])
					top.after(10000, update)
				if addon['файл'] == 1:
					if os.path.isfile(addon['путь']):
						os.remove(addon['путь'])
					top.after(10000, update)
				if addon['файл'] == 2:
					if os.path.isdir(addon['путь к аддону']):
						shutil.rmtree(addon['путь к аддону'])
					top.after(10000, update)
			else:
				if addon['файл'] == 0 or addon['файл'] == 2:
					urllib.request.urlretrieve(addon['link'], "main.zip", reporthook=dl)
					archive = 'main.zip'
					if os.path.isdir('temp'):
						shutil.rmtree('temp/')
					archive = 'main.zip'
					with zipfile.ZipFile(archive, 'r') as zip_file:
						zip_file.extractall("temp")
					file_source = addon['временный путь']
					file_destination = addon['путь']
					if not os.path.exists(file_destination):
						os.mkdir(file_destination)
					get_files = os.listdir(file_source)
					shutil.copytree(file_source, file_destination,dirs_exist_ok=True)
					if os.path.isfile('main.zip'):
						os.remove('main.zip')
					if os.path.isdir('temp'):
						shutil.rmtree('temp/')
					top.after(10000, update)
				if addon['файл'] == 1:
					urllib.request.urlretrieve(addon['link'], addon['путь'], reporthook=dl)
					top.after(10000, update)
		return on_call

	btn = Checkbutton(top, text = name, variable = var, onvalue = 1, offvalue = 0, command = print_value(name, value))
	if os.path.isdir(value['путь к аддону']) or os.path.isfile(value['путь к аддону']):
		var.set(1)
	else:
		var.set(0)
	btnT = Tooltip(btn, value['описание'])
	btn.pack()
	addons[name]['button'] = btn
	addons[name]['check_var'] = var
top.title("Апдейтер от Ночной стражи")
top.geometry("300x530")
limit = 10
score = 0

def update():
	global score
	score += 1
	ScoreL.configure(text=score)
	if score < limit:
		# schedule next update 1 second later
		if os.path.isfile('Interface/AddOns/NSQC/vers'):
			f = urllib.request.urlopen('https://github.com/Vladgobelen/NSQC/blob/main/vers').read().decode('utf-8').strip()
			file = open('Interface/AddOns/NSQC/vers', 'r')
		else:
			f = "нету"
		if not os.path.exists('Data/ruRU/patch-ruRU-M.MPQ'):
			urllib.request.urlretrieve("https://hub.mos.ru/vladgobelen/nsqcmap/-/raw/main/patch-ruRU-M.MPQ", "patch-ruRU-M.MPQ")
			os.replace("patch-ruRU-M.MPQ", "Data/ruRU/patch-ruRU-M.MPQ")
			urllib.request.urlretrieve("https://github.com/Trimitor/WDM-addons/archive/refs/heads/main.zip", "main.zip")
			if os.path.isdir('temp'):
				shutil.rmtree('temp/')
			archive = 'main.zip'
			with zipfile.ZipFile(archive, 'r') as zip_file:
				zip_file.extractall("temp")
			file_source = 'temp/WDM-addons-main/WDM/'
			file_destination = 'Interface/AddOns/WDM/'
			if not os.path.exists(file_destination):
				os.mkdir(file_destination)
			get_files = os.listdir(file_source)
			shutil.copytree(file_source, file_destination,dirs_exist_ok=True)
			if os.path.isfile('main.zip'):
				os.remove('main.zip')
			if os.path.isdir('temp'):
				shutil.rmtree('temp/')
		if f == "нету" or not file.readline().strip() in f:
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
		top.after(10000, update)

ScoreL = tkinter.Label(top, text=score)
ScoreL.pack()

top.after(10000, update)
top.mainloop()

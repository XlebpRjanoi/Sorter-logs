import os
import zipfile
from time import sleep


if os.path.exists("C:\\"):
	import ctypes
	kernel32 = ctypes.windll.kernel32
	kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


def clear():
	print("\n" * 200)


def baner():
	print("\033[35mSorter log\n")


def incorrect_input():
	print("\n\033[36m[\033[33m!\033[36m] - \033[33mIncorrect input!\n\033[36m[\033[33m!\033[36m] - \033[33mTry again!")


def words_per_line(words, line):
	for word in words:
		if word in line:
			return True
	return False


clear()
print("\033[34mHello! Welcome to the log sorting program\033[36m\033[6m..\033[0m")
sleep(2)
clear()

archive_dir = input("\033[34mEnter the path to the archive folder\n\nEnter\033[36m\033[6m:\033[0m ")
clear()
uploaded_data_file = input("\033[34mEnter file path for data\n\nEnter\033[36m\033[6m:\033[0m ")
clear()
sought = input("\033[34mEnter the services you are looking for, separated by commas\n\nEnter\033[36m\033[6m:\033[0m ").split(',')
clear()
avoidable = input("\033[34mEnter avoided constants or leave blank\n\nEnter\033[36m\033[6m:\033[0m ").split(',')

array_oan = []
verified = '_verified'

try:
	with open(uploaded_data_file, 'x') as f:
		pass
except FileExistsError:
	pass

for a, b, c in os.walk(archive_dir):
	k = c
	break

for i in k:
	if i[-4:] == '.zip' and i[-(len(verified))-4:-4] != verified:
		array_oan.append(i)

for zip_file_name in array_oan:
	try:
		with zipfile.ZipFile(archive_dir + '/' + zip_file_name) as zip:
			text = zip.read('_AllPasswords_list.txt').decode('UTF-8')
			ip = zip.read('ip.txt').decode('UTF-8')
			n = text.split('\n')
			mas = []
			for i in range(len(n)):
				if 'browser' in n[i].lower():
					a = []
					for j in range(4):
						a.append(n[i+j])
					mas.append(a)
		with open(uploaded_data_file, 'a') as f:
			for i in mas:
				if not words_per_line(sought, i[1].lower()):
					continue
				if words_per_line(avoidable, i[1].lower()):
					continue
				rep3 = i[2][10:]
				rep4 = i[3][10:]
				for char in ('','\r','\t','\n'):
					rep3 = rep3.replace(char, '')
					rep4 = rep4.replace(char, '')
				if rep3 != '' and rep4 != '':
					f.write(zip_file_name + '\n')
					for j in i:
						f.write(j + '\n')
					f.write(ip + 2*'\n')
		os.rename(archive_dir + "/" + zip_file_name, archive_dir + "/" + zip_file_name[:-4] + '_verified.zip')
	except KeyError:
		pass
	
	clear()
	print("\033[32mSuccessfully\033[0m")
	sleep(2.5)
	clear()

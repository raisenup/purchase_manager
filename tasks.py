import csv
import os
from prettytable import *
import pandas as pd


users = pd.read_csv(r'./UsersData/users.csv')
user = 0
logins = [users['login'][i] for i in range(len(users['login']))]
passwords = [users['password'][i] for i in range(len(users['password']))]
paths = [users['path'][i] for i in range(len(users['path']))]
t = PrettyTable(junction_char='#', hrules=ALL)
t.field_names = ["Продукт", "Категорія", "Кількість", "Опис", "Ціна", "Магазин"]
data = [t.field_names]


def user_auth():
	print('''============AUTHENTICATION============''')
	is_registered = input('Are you registered?(y/n)\n')
	if is_registered == 'y':
		login = input('Input login:\n')
		global user
		for i in range(len(logins)):
			if login == logins[i]:
				user = i
		if login in logins:
			password = input('Input password:\n')
			if password != passwords[user]:
				print('Error: wrong password!')
				return 0
			else:
				os.system('cls' if os.name == 'nt' else 'clear')
				table()
		else:
			print('Error: there is no such login!')
			return 0
	elif is_registered == 'n':
		os.system('cls' if os.name == 'nt' else 'clear')
		print('''============REGISTER============''')
		new_login = input('Input new login:\n')
		new_password = input('Input new password:\n')
		new_path = input('Input new path to your table:\n')
		register(new_login, new_password, new_path)


def register(login, password, path, file_path='./UsersData/users.csv'):
	with open(file_path, 'a', newline='') as file:
		fieldnames = ['login', 'password', 'path']
		writer = csv.DictWriter(file, fieldnames=fieldnames)
		if login in logins:
			print("Error: this login already exists!")
			return 0
		else:
			writer.writerow({'login': login, 'password': password, 'path': path})
		file.close()


def table():
	print('''============TABLE============''')
	product = input('Input product:\n')
	category = input('Input category:\n')
	amount = input('Input amount:\n')
	description = input('Input description:\n')
	price = input('Input price:\n')
	shop = input('Input shop:\n')
	values = product, category, amount, description, price, shop
	list(values)
	t.add_rows([values])
	data.append(values)
	print(t)
	ask = input('Do you want to enter another row?(y/n)')
	if ask == 'y':
		os.system('cls' if os.name == 'nt' else 'clear')
		table()
	elif ask == 'n':
		os.system('cls' if os.name == 'nt' else 'clear')
		convert(paths[user])


def convert(path):
	print('''============CONVERT============''')
	ext_to_convert = input('What file extension to convert the file to?(csv/txt)')
	if ext_to_convert == 'csv':
		name = input('Input file name:\n')
		file_path = f"{path}{name}.csv"
		with open(file_path, 'w', newline='') as csvfile:
			writer = csv.writer(csvfile)
			for i in data:
				writer.writerow(i)
		csvfile.close()
	elif ext_to_convert == 'txt':
		name = input('Input file name:\n')
		file_path = f"{path}{name}.txt"
		with open(file_path, 'w', newline='') as file:
			file.write(str(t))
		file.close()

import csv
from prettytable import *
import pandas as pd

users = pd.read_csv(r'./UsersData/users.csv')
logins = [users['login'][i] for i in range(len(users['login']))]
passwords = [users['password'][i] for i in range(len(users['password']))]
paths = [users['path'][i] for i in range(len(users['path']))]
t = PrettyTable(junction_char='#', hrules=ALL)
t.field_names = ["Продукт", "Категорія", "Кількість", "Опис", "Ціна", "Магазин"]


def user_auth():
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
				print('Wrong password!')
				return 0
			else:
				table()
		else:
			print('There is no such login!')
			return 0
	elif is_registered == 'n':
		new_login = input('Input new login:\n')
		new_password = input('Input new password:\n')
		new_path = input('Input new path to your table:\n')
		new_user_write(new_login, new_password, new_path)


def new_user_write(login, password, path, file_path='./UsersData/users.csv'):
	with open(file_path, 'a', newline='') as file:
		fieldnames = ['login', 'password', 'path']
		writer = csv.DictWriter(file, fieldnames=fieldnames)
		if login in logins:
			print("This login already exists!")
			return 0
		else:
			writer.writerow({'login': login, 'password': password, 'path': path})
		file.close()


def table():
	product = input('Input product:\n')
	category = input('Input category:\n')
	amount = input('Input amount:\n')
	description = input('Input description:\n')
	price = input('Input price:\n')
	shop = input('Input shop:\n')
	values = product, category, amount, description, price, shop
	list(values)
	t.add_rows([values])
	print(t)
	ask = input('Do you want to enter another row?(y/n)')
	if ask == 'y':
		table()
	elif ask == 'n':
		convert(paths[user])


def convert(path):
	ext_to_convert = input('What file extension to convert the file to?(csv/txt)')
	if ext_to_convert == 'csv':
		pass
	elif ext_to_convert == 'txt':
		name = input('Input file name:\n')
		file_path = f"{path}{name}.txt"
		with open(file_path, 'w', newline='') as file:
			file.write(str(t))


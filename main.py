import csv
from prettytable import *
import tasks


def main():
	try:

		# Для ствоерння таблиці будемо юзати prettytable

		x = PrettyTable(junction_char='#')
		x.field_names = ["Продукт", "Категорія", "Кількість", "Опис", "Ціна", "Магазин"]
		x.add_rows(
			[
				["Lenovo Legion 5", "Ноутбук", "1 шт", "Ігровий ноутбук", "59000", "Розетка"],
			]
		)

		print(x)
		# code here

		pass
	except Exception as e:
		print(e)


if __name__ == '__main__':
	main()

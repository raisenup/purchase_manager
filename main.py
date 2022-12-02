import tasks


def main():
	try:
		tasks.user_auth()
	except Exception as e:
		print(e)


if __name__ == '__main__':
	main()

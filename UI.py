from logger import *

def interface():
	with open('phonebook.txt', 'a', encoding='UTF-8'):
		pass
	command = '-1'
	while command != '5':
		print('Меню:\n'
			'1. Добавить контакт\n'
			'2. Вывести на экран\n'
			'3. Поиск контакта\n'
			'4. Скопировать контакт\n'
			'5. Выход')

		command = input('Выберите пункт меню: ')

		while command not in ('1', '2', '3', '4', '5'):
			print('Некорректный ввод, повторите')
			command = input('Выберите пункт меню: ')

		match command:
			case '1':
				add_contact(create_contact())
			case '2':
				info_book()
			case '3':
				search_contact()
			case '4':
				info_book()
				copy_contact()				
			case '5':
				print("Выход")
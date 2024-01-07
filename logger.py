from date_create import *

def create_contact():
	name = input_name()
	patronymic = input_patronymic()
	surname = input_surname()
	phone = input_phone()
	address = input_address().replace('\n', ' ')

	return f'{name} {patronymic} {surname} {phone}\n{address}\n\n'

def copy_contact():
	line_number = int(input('Введите номер контакта для копирования: '))

	with open('phonebook.txt', 'r', encoding='UTF-8') as file:
		contacts_lst = file.read().rstrip().split('\n\n')

	for number_contact, contact in enumerate(contacts_lst, 1):
		if number_contact is line_number:
			with open('another_phonebook.txt', 'a', encoding='UTF-8') as file:
				file.write(f"{contact}\n\n")
				print(f"Контакт № {number_contact} успешно скопирован в файл Another phonebook.txt")

def add_contact(contact):
	with open('phonebook.txt', 'a', encoding='UTF-8') as file:
		file.write(contact)

def info_book():
	with open('phonebook.txt', 'r', encoding='UTF-8') as file:
		contacts_list = file.read().rstrip().split('\n\n')
		for nn, contact in enumerate(contacts_list, 1):
			print(f"{nn}. {contact}")

def search_contact():
	print(
		'Возможные варианты поиска:\n'
		'1. По имени\n'
		'2. По отчеству\n'
		'3. По фамилии\n'
		'4. По номеру телефона\n'
		'5. По адресу\n'
		)
	
	var_search = input('Выберите вариант поиска:')
	
	while var_search not in ('1', '2', '3', '4', '5'):
		print('Некорректный ввод, повторите')
		var_search = input('Выберите пункт меню: ')
			
	index_var = int(var_search) - 1

	search = input('Введите данные для поиска: ')

	with open('phonebook.txt', 'r', encoding='UTF-8') as file:
		contacts_list = file.read().rstrip().split('\n\n')

	for contact_str in contacts_list:
		contact_lst = contact_str.replace('\n', ' ').split()
		if search in contact_lst[index_var]:
			print(contact_str)
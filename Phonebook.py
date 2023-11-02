'''
Задача 38: Дополнить телефонный справочник возможностью изменения и удаления 
данных(по выбору). Пользователь также может ввести имя или фамилию, и Вы должны 
реализовать функционал для изменения и удаления данных.
'''

# Вывод данных
def show_data(filename):
    print("\nФИО            Телефон     Адрес")
    with open(filename, "r", encoding="utf-8") as data:
        print(data.read())
    print("")

# Запись данных
def add_data(filename):
    with open(filename, "r", encoding="utf-8") as data:
        tel_file = data.read()
    num = len(tel_file.split("\n"))
    with open(filename, "a", encoding="utf-8") as data: 
        surname = input("Введите Фамилию: ")
        name = input("Введите Имя: ")
        patronymic = input("Введите Отчество: ")
        phone_number = input("Введите номер телефона: ")
        address = input("Введите адрес: ")
        data.write(f"{surname} {name} {patronymic}  тел:{phone_number}  {address}\n")
        print(f"Добавлена запись : {surname} {name} {patronymic} тел:{phone_number}  {address}\n")

# Изменение данных
def change_data(filename):
    print("\nФИО        Телефон     Адрес")
    with open(filename, "r", encoding='utf-8') as data:
        tel_book = data.read()
    print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для изменения: ")) - 1
    tel_book_lines = tel_book.split("\n")
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split("  ")
    surname = input("Введите новую Фамилию: ")
    name = input("Введите новое Имя: ")
    patronymic = input("Введите новое Отчество: ")
    phone = input("Введите новый номер телефона: ")
    address = input("Введите новый адрес: ")
    num = elements[0]
    if len(surname) == 0:
        surname = elements[1]
    if len(name) == 0:
        name = elements[2]
    if len(patronymic) == 0:
        patronymic = elements[3]
    if len(phone) == 0:
        phone = elements[4]
    if len(address) == 0:
        address = elements[5]
    edited_line = f"{surname} {name} {patronymic}  тел:{phone}  {address}"
    tel_book_lines[index_delete_data] = edited_line
    print(f"Данные контакта - {edit_tel_book_lines}, изменены на - {edited_line}\n")
    with open(filename, "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))

# Удаление данных из файла
def delete_data(filename):
    print("\nФИО        Телефон     Адрес")
    with open(filename, "r", encoding="utf-8") as data:
        tel_book = data.read()
        print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
    tel_book_lines = tel_book.split("\n")
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f"Удалены данные контакта: {del_tel_book_lines}\n")
    with open(filename, "w", encoding='utf-8') as data:
        data.write("\n".join(tel_book_lines))

def interface():
    option_num = -1
    file_tel = "phonebook.txt"

    # Создание нового контакта
    with open(file_tel, "a", encoding="utf-8") as file:
         file.write("")

    while option_num != 0:
        print("Выберите вариант работы с телефонной книгой:")
        print("1 - Вывод телефонной книги на экран")
        print("2 - Запись данных")
        print("3 - Изменение данных")
        print("4 - Удаление данных")
        print("0 - Выход из программы")
        option = int(input("Введите номер операции: "))
        if option == 1:
            show_data(file_tel)
        elif option == 2:
            add_data(file_tel)
        elif option == 3:
            change_data(file_tel)
        elif option == 4:
            delete_data(file_tel)
        else:
            option_num = 0

    print("Приложение закрыто")


interface()

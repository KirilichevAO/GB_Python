# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

# 1. Открыть файл телефонной книги
# 2. Сохранить файл телефонной книги
# 3. Показать все контакты
# 4. Найти контакт
# 5. Добавить контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

# имя
# номер
# коммент

def menu():
    phone_book_dict = {}
    while True:
        number = int(input('''Меню:
    1. Показать все контакты
    2. Найти контакт
    3. Добавить контакт
    4. Изменить контакт
    5. Удалить контакт
    6. Выход
Выберите пункт меню: '''))
        if number == 1: # 1. Показать все контакты
            if len(phone_book_dict) == 0:
                phone_book_dict = open_file()
            if len(phone_book_dict) == 0:
                print('Справочник пуст!')
            else:
                print(phone_book_dict)
        elif number == 2: # 2. Найти контакт
            search_contact(phone_book_dict)
        elif number == 3: # 3. Добавить контакт
            value_new_cnt = add_cntc(phone_book_dict)
            print(value_new_cnt)
            phone_book_dict.update(value_new_cnt)
            save_dir(phone_book_dict)
            print('Контакт добавлен!')
        elif number == 4: # 4. Изменить контакт
            new_cntc = search_contact(phone_book_dict)
            add_cntc(phone_book_dict, new_cntc)
        elif number == 5: # 5. Удалить контакт
            new_cntc = search_contact(phone_book_dict)
            print(f'Контакт: {new_cntc[0]} удален!')
            save_dir(phone_book_dict)
        elif number == 6: # 6. Выход
            print('End')
            break
        else:
            print('Введите ещё раз')


def open_file(): # Открытие
    phone_book_dict = {}
    with open('phonebook.txt', 'r') as f:
        for contact in f.readlines():
            key, value = contact.strip().split(':')
            phone_book_dict[key] = value
        # print(phone_book_dict)
        return phone_book_dict


def save_dir(dict_phnbk): # Сохранение
    str_phnbk = ''
    print(dict_phnbk)
    for key, value in dict_phnbk.items():
        str_phnbk += f'{key}:{value} \n'
    with open('phonebook.txt', 'w') as f:
        f.write(str_phnbk)


def add_cntc(dict_phnbk, new_cntc_in = [0]): # Добавление
    if len(new_cntc_in) < 2:
        name_cntc = input('Введите Имя: ')
        phone_cntc = input('Введите телефон: ')
        comment_cntc = input('Введите комментарий: ')
        cntc_list = [phone_cntc, comment_cntc]
    else:
        name_cntc, cntc_list = tuple(new_cntc_in)
    # dict_phnbk[name_cntc] = dict_phnbk.setdefault(name_cntc, cntc_list)
    dict_phnbk.setdefault(name_cntc, cntc_list)
    # print(f'{name_cntc}, {dict_phnbk[name_cntc]}')
    return dict_phnbk


def search_contact(phone_dict): # Поиск контакта
    name_contact = input('Введите Имя: ')
    if name_contact in phone_dict:
        print(f'{name_contact}: {phone_dict[name_contact]}')
        return [name_contact, phone_dict[name_contact]]
    else:
        print('Контакт не найден!')


menu()

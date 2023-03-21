


def main_menu() -> int:
    return int(input('''Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать контакты
    4. Добавить контакт
    5. Изменить контакт
Выберите пункт меню: '''))


def show_contacts(book: list[dict], error_massage: str):
    if not book:
        print(error_massage)
    else:
        for i, contact in enumerate(book):
            print(f'{i}. {contact.get("name"): <20} '
                  f'{contact.get("phone"): <20} '
                  f'{contact.get("comment"): <20}')



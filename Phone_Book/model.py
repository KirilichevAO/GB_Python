phone_book = []
path = 'phone_book.txt'

def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readline()
    for fields in data:
        fields = fields.strip().split(';')
        contact = {'name' : fields[0],
                   'phone' : fields[1],
                   'comment' : fields[2]}
        phone_book.append(contact)

def get_phone_book():
    return phone_book
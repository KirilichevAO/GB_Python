class Human:
    def __init__(self, name: str, age: int, is_work: bool):
        self.name = name
        self.age = age
        self.is_work = is_work

    def greetings(self):
        print(f'{self.name} говорит "Привет"')

stone = Human('Кирилл', 38, True)

stone.greetings()


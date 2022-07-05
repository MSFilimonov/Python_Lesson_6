class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_premium_income(self):
        return f'{sum(self.income.values())}'


accountant = Position('Иванова', 'Светлана', 'Бухгалтер', 50000, 11000)
print(accountant.get_full_name())
print(accountant.position)
print(accountant.get_premium_income())

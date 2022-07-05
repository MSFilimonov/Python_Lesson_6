class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        f'Запуск отрисовки.'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки ручкой - {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки карандашом - {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки маркером - {self.title}'


pen = Pen("ручка")
pencil = Pencil("карандаш")
handle = Handle("маркер")
print(pen.draw())
print(pencil.draw())
print(handle.draw())

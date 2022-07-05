class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width, weight, depth):
        self.length = _length
        self.width = _width
        self.weight = weight
        self.depth = depth

    def Asphalt_mass(self):
        length = self.length
        width = self.width
        weight = self.weight
        depth = self.depth
        total = length * width * weight * depth / 1000
        return print(f"Масса асфальта: {length} м * {width} м * {weight} кг * {depth} см = ", total / 1000, "т")


r = Road(20, 5000, 25, 5)
r.Asphalt_mass()

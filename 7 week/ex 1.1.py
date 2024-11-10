class Vector:
    def __init__(self, x, y, z):
        assert isinstance(x, (int, float)) and not isinstance(x, bool)
        assert isinstance(y, (int, float)) and not isinstance(y, bool)
        assert isinstance(z, (int, float)) and not isinstance(z, bool)
        self.x = x
        self.y = y
        self.z = z

    def abs(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def add(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def sub(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def scal(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)

    def areasq(self, v2):
        square = Vector(self.y * v2.z - self.z * v2.y,
                        self.z * v2.x - self.x * v2.z,
                        self.x * v2.y - self.y * v2.x)
        return 0.5 * square.abs()

    def __str__(self):
        return f'x={self.x}, y={self.y}, z={self.z}'


v1 = Vector(1, 2, 3)
v2 = Vector(2, 3, 4)
v3 = Vector(3, 4, 5)
a = [v1, v2, v3]


def mass_center(l):
    res = Vector(0, 0, 0)
    for i in l:
        res = res.add(i)  # Используем метод add для сложения векторов
    return Vector(res.x / len(l), res.y / len(l), res.z / len(l))


print(mass_center(a))
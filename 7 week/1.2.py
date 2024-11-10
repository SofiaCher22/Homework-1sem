import itertools

class Vector:
    def __init__(self, x, y, z):
        assert isinstance(x, (int, float)) and not isinstance(x, bool)
        assert isinstance(y, (int, float)) and not isinstance(y, bool)
        assert isinstance(z, (int, float)) and not isinstance(z, bool)
        self.x = x
        self.y = y
        self.z = z

    def abs(self):
        return (self.x*2 + self.y*2 + self.z*2) * 0.5

    def add(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def sub(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def mul(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Unsupported type for multiplication")

    def cross(self, other):
        assert isinstance(other, Vector)
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

def area_of_triangle(v1, v2, v3):
    a = v2.sub(v1)
    b = v3.sub(v1)
    cross_product = a.cross(b)
    return cross_product.abs() / 2

def max_area(points):
    max_area = 0
    max_triangles = (None, None, None)

    # def ma
    for p1, p2, p3 in itertools.combinations(points, 3):
        current_area = area_of_triangle(p1, p2, p3)
        if current_area > max_area:
            max_area = current_area
            max_triangles = (p1, p2, p3)

    return max_area, max_triangles

# Пример использования
points = [
    Vector(0, 0, 0),
    Vector(1, 0, 0),
    Vector(0, 1, 0),
    Vector(0, 0, 1),
    Vector(1, 1, 1)
]

area, triangle = max_area(points)
print(f"Максимальная площадь треугольника: {area}")
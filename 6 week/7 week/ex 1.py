
import itertools


class Vector:
    def init(self, x, y, z):
        assert isinstance(x, (int, float)) and not isinstance(x, bool)
        assert isinstance(y, (int, float)) and not isinstance(y, bool)
        assert isinstance(z, (int, float)) and not isinstance(z, bool)
        self.x = x
        self.y = y
        self.z = z

    def abs(self):
        return (self.x2+self.y2+self.z2)

    def add(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)

    def sub(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x-other.x, self.y-other.y, self.z-other.z)

    def scal(self, other):
        if isinstance(other, Vector):
            return self.x*other.x+self.y*other.y+self.z*other.z
        if isinstance(other, (int, float)):
            return Vector(self.x*other, self.y*other, self.z*other)

    def areasq(self, v1, v2):
        square = Vector(self.y * v2.z - self.z * v2.y, self.z *
                        v2.x - self.x * v2.z, self.x * v2.y - self.y * v2.x)
        return 0.5 * abs(square)

    def str(self):
        return f'x={self.x}, y={self.y}, z={self.z}'
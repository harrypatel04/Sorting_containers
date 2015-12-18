#!/usr/bin/env python3

import math

"""
Basic Vector class in Python.
"""


class Vector(object):
    def __init__(self, *args):
        """ Create an n-dimensional vector of ints or floats, example: v = Vector(1,2) """
        for arg in args:
            if not (isinstance(arg, float) or isinstance(arg, int)):
                raise TypeError('Vector can only be instantiated with type int or type float.')
        if len(args) == 0:
            self.values = (0, 0)
        else:
            self.values = args

    @classmethod
    def fromPointsR2(cls, x1, y1, x2, y2):
        """instantiate Vector from two points in R2"""
        return cls(x2 - x1, y2 - y1)

    @classmethod
    def fromPointsR3(cls, x1, y1, z1, x2, y2, z2):
        """Instantiate Vector from two points in R3"""
        return cls(x2 - x1, y2 - y1, z2 - z1)

    @classmethod
    def planeEqn(cls, pt1, pt2, pt3):
        """returns a string representation of the equation for a plane defined by three points"""
        if not isinstance(pt1, tuple) or not isinstance(pt2, tuple) or not isinstance(pt3, tuple):
            raise TypeError('planeEqn accepts three three-tuples of points as arguments')
        elif len(pt1) != 3 or len(pt2) != 3 or len(pt3) != 3:
            raise ValueError('planeEqn accepts three three-tuples of points as arguments')
        else:
            vector_1 = cls.fromPointsR3(pt1[0], pt1[1], pt1[2], pt2[0], pt2[1], pt2[2])
            vector_2 = cls.fromPointsR3(pt1[0], pt1[1], pt1[2], pt3[0], pt3[1], pt3[2])
            n = vector_1.Cross(vector_2)

            return str(n[0]) + "*(x-" + str(pt1[0]) + ") + " + str(n[1]) + "*(y-" + str(pt1[1]) + ") + " + str(
                n[2]) + "*(z-" + str(pt1[2]) + ") = 0" + '\n' + str(n[0]) + "x + " + str(n[1]) + "y + " + str(
                n[2]) + "z = " + str(-(n[0] * -pt1[0] + n[1] * -pt1[1] + n[2] * -pt1[2]))

    @property
    def x(self):
        if len(self) >= 1:
            return self.values[0]
        else:
            raise IndexError('Vector does not have a \'x\' component.')

    @property
    def y(self):
        if len(self) >= 2:
            return self.values[1]
        else:
            raise IndexError('Vector does not have a \'y\' component.')

    @property
    def z(self):
        if len(self) >= 3:
            return self.values[2]
        else:
            raise IndexError('Vector does not have a \'z\' component.')

    def __add__(self, other):
        """Add two vectors."""
        resultant_vector = tuple(a + b for a, b in zip(self, other))
        return Vector(*resultant_vector)

    def __sub__(self, other):
        """Vector difference of two vectors."""
        resultant_vector = tuple(a - b for a, b in zip(self, other))
        return Vector(*resultant_vector)

    def __mul__(self, other):
        """If multiplied by another vector, return the dot product.
           If multiplied by a scalar, return a scalar multiple of the vector
        """
        if isinstance(other, Vector):
            return self.Dot(other)
        elif isinstance(other, int) or isinstance(other, float):
            resultant_vector = tuple(component * other for component in self)
            return Vector(*resultant_vector)
        else:
            raise TypeError('unsupported operand type(s) for *: \'Vector\' and \'' + str(type(other)) + '\'')

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            resultant_vector = tuple(component / other for component in self)
            return Vector(*resultant_vector)
        else:
            raise TypeError('unsupported operand type(s) for /: \'Vector\' and \'' + str(type(other)) + '\'')

    def __len__(self):
        """Returns number of components, not magnitude."""
        return len(self.values)

    def __getitem__(self, index):
        return self.values[index]

    def __repr__(self):
        vector_components = ""
        for val in self.values[:-1]:
            vector_components += (str(val) + ', ')
        vector_components += str(self.values[-1])
        return "<" + vector_components + ">"

    def __iter__(self):
        return self.values.__iter__()

    def __contains__(self, item):
        return item in self.values

    def __bool__(self):
        return not self.isZero()

    def Magnitude(self):
        """Find the length or magnitude of a vector."""
        return math.sqrt(sum(component ** 2 for component in self))

    def Cross(self, other):
        """returns the cross product of two three-dimensional vectors"""
        if not isinstance(self, Vector) or not isinstance(other, Vector):
            raise TypeError('Can only take the cross product of two Vectors')
        elif len(self) > 3 or len(other) > 3:
            raise TypeError('Vector must be three-dimensional')
        elif len(self) == 3 and len(other) == 2:  # must initialize from beginning to end, can't have just a y component
            a = self
            b = Vector(other[0], other[1], 0)
        elif len(self) == 3 and len(other) == 1:
            a = self
            b = Vector(other[0], 0, 0)
        elif len(other) == 3 and len(self) == 2:
            a = Vector(self[0], self[1], 0)
            b = other
        elif len(other) == 3 and len(self) == 1:
            a = Vector(self[0], 0, 0)
            b = other
        elif len(self) == 3 and len(other) == 3:
            a = self
            b = other
        else:
            raise TypeError('Invalid Vector dimensions')
        return Vector(a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] *
                      b[1] - a[1] * b[0])

    def Dot(self, other):
        """Take the dot product between two vectors."""
        if not isinstance(self, Vector) or not isinstance(other, Vector):
            raise TypeError('Can only take the dot product of two Vectors')
        else:
            return sum(a * b for a, b in zip(self, other))

    def angleBetween(self, other):
        """Angle between two vectors in degrees rounded to four decimal places"""
        if not isinstance(self, Vector) or not isinstance(other, Vector):
            raise TypeError('Can only find the angle between two Vectors')
        else:
            return round(math.degrees(math.acos(round(self.Dot(other) / (self.Magnitude() * other.Magnitude()), 4))), 4)

    def isParallel(self, other):
        """Two vectors are collinear if they can be represented as scalar multiples of each other,
           if their cross product is the zero vector, or lastly if the angle between them is zero.
        """
        # TODO: implement scalar multiple method, less prone to rounding errors.
        if not isinstance(self, Vector) or not isinstance(other, Vector):
            raise TypeError('Can only test the collinearity of two Vectors')
        elif self.isZero() or other.isZero():
            return False
        elif len(self) == 3 and len(other) == 3:
            if self.Cross(other).isZero():
                return True
            else:
                return False
        elif self.angleBetween(other) == 0 or self.angleBetween(other) == 180:
            # angleBetween() is accurate to 4 decimal places.
            return True
        else:
            return False

    def isOrthogonal(self, other):
        """Two vectors are orthogonal iff their dot product is 0"""
        if not isinstance(self, Vector) or not isinstance(other, Vector):
            raise TypeError('Can only test the orthogonality of two Vectors')
        elif self.Dot(other) == 0:
            return True
        else:
            return False

    def isZero(self):
        """Checks if self is a zero vector"""
        if not isinstance(self, Vector):
            raise TypeError('Can only test a Vector')
        else:
            for val in self.values:
                if val != 0:
                    return False
            return True

    def unitVector(self):
        """returns normalized unit vector"""
        return self / self.Magnitude()

    def directionCosines(self):
        """Returns a Vector of a Vector's direction cosines"""
        if not isinstance(self, Vector):
            raise TypeError('Can get the direction cosines of a Vector')
        elif len(self) == 2:
            return Vector(self[0] / self.Magnitude(), self[1] / self.Magnitude())
        elif len(self) == 3:
            return Vector(self[0] / self.Magnitude(), self[1] / self.Magnitude(), self[2] / self.Magnitude())
        else:
            raise ValueError('direction cosines are undefined for Vectors not in R2 or R3')

    def directionAngles(self):
        """Returns a Vector of a Vector's direction angles"""
        if not isinstance(self, Vector):
            raise TypeError('Can get the direction angles of a Vector')
        elif len(self) == 2:
            return Vector(math.acos(self.directionCosines()[0]), math.acos(self.directionCosines()[1]))
        elif len(self) == 3:
            return Vector(math.acos(self.directionCosines()[0]), math.acos(self.directionCosines()[1]),
                          math.acos(self.directionCosines()[2]))
        else:
            raise ValueError('direction angles are undefined for Vectors not in R2 or R3')

    def scalarProjectionOnto(self, other):
        """The scalar projection of b onto a is:
           (a.Dot(b)) / a.Magnitude()
        """
        if not isinstance(self, Vector) or not isinstance(other, Vector):
            raise TypeError('Can only find the scalar projection of two Vectors')
        else:
            return other.Dot(self) / other.Magnitude()

    def vectorProjectOnto(self, other):
        """The vector projection of b onto a is:
           b.scalarProjectionOnto(a) * a.unitVector()
        """
        if not isinstance(self, Vector) or not isinstance(other, Vector):
            raise TypeError('Can only find the vector projection of two Vectors')
        else:
            return self.scalarProjectionOnto(other) * other.unitVector()

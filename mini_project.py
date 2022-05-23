class Vector:
    """This class performs some of the vector operations.

    Methods:
           length(): Computes the length of the vector.
           summation(v): Computes the summation of two vectors.
           innerProduct(v): Computes the internal multiplication of two vectors.
           toUniteVector(): Convert the vector to unit vector.
           toPolarCoordinates(): Convert the coordinates of the vector from cartesian to polar.
           directionalDerivation(F, x, y): Directional derivative of F at the point(x,y) in direction of the vector.
    """

    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1

    def length(self):
        pass

    def summation(self, v):
        pass

    def innerProduct(self, v):
        pass

    def toUnitVector(self):
        pass

    def toPolarCoordinates(self):
        pass

    def directionalDervation(self, F, x, y):
        pass


class stringRedefine:
    """This class performs some kind of operations on strings.

    Methods:
           switchHalf(): Switch the place of the first half of string with the second part.
           encryption(): This method encrypts a string.
           primeASCII(): Performs some operations on the characters of a string.
    """

    def __init__(self, s):
        self.s = s

    def switchHalf(self):
        pass

    def encryption(self):
        pass

    def primeASCII(self):
        pass

    def __add__(self, __other_obj):
        pass

    def __imul__(self, __other_obj):
        pass

    def __eq__(self, __o):
        pass

    def __ne__(self, __o):
        pass

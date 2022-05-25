import math

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
        return (self.x1 - self.x0, self.y1 - self.y0)

    def summation(self, vec1):
        vec = Vector.length(self)
        return (vec[0] + vec1[0], vec[1] + vec1[1])

    def innerProduct(self, v):
        pass

    def toUnitVector(self):
        vec = Vector.length(self)
        r = math.sqrt((vec[0]**2 + vec[1]**2))
        return f"{vec[0]}i/{r} + {vec[1]}j/{r}"

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
        self.length_s = len(s)
        self.lst_s = list(s)

    def switchHalf(self):
        if self.length_s % 2 == 0:
            first_half = self.lst_s[:(self.length_s // 2)] 
            second_half = self.lst_s[(self.length_s // 2):]
            the_string = second_half + first_half
            return "".join(the_string)
        else:
            first_half = self.lst_s[:self.length_s // 2] 
            mid = self.lst_s[self.length_s // 2]
            second_half = self.lst_s[(self.length_s // 2 + 1):]
            the_string = second_half + list(mid) + first_half
            return "".join(the_string)

    def encryption(self):
        pass


    @staticmethod
    def primChecker(num: int) -> bool:
        if num == 2:
            return True
        elif num < 2:
            return False

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def primeASCII(self):
        primeAscii = []
        for char in self.s:
            if not stringRedefine.primChecker(ord(char)):
                primeAscii.append(char)
        return "".join(primeAscii)

    def __add__(self, __other_obj):
        return stringRedefine( __other_obj.s + self.s)

    def __imul__(self, __other_obj):
        pass

    def __eq__(self, __o):
        return len(self.s) == len(__o.s)

    def __ne__(self, __o):
        pass

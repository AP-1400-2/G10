import math
from sympy import *


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

    def innerProduct(self, vec1_grad, activator=False):
        if activator:
            return (vec1_grad[0] * eval(vec1_grad[2][0])) + (vec1_grad[1] * eval(vec1_grad[2][1]))
        else:
            vec = Vector.length(self)
            return (vec[0] * vec1_grad[0]) + (vec[1] * vec1_grad[1])

    def toUnitVector(self, activator=False):
        vec = Vector.length(self)
        r = math.sqrt((vec[0]**2 + vec[1]**2))
        return [format(vec[0]/r, ".2f"), format(vec[1]/r, ".2f")] if activator else (f"{vec[0]}i/{r} + {vec[1]}j/{r}")

    def toPolarCoordinates(self):
        vec = Vector.length(self)
        r = math.sqrt((vec[0]**2 + vec[1]**2))
        O = math.degrees(math.atan(vec[1]/vec[0]))
        return (format(r * math.cos(O), ".3f"), format(r * math.sin(O), ".3f"))

    @staticmethod
    def extraction(div_x, div_y, x, y):
        x = x
        y = y
        extracted_divX = eval(div_x)
        extracted_divY = eval(div_y)
        return extracted_divX, extracted_divY

    def directionalDervation(self, F, x, y):
        xSym, ySym = symbols('x y', real=True)
        d1_x = diff(F, xSym)
        d1_y = diff(F, ySym)
        grad1, grad2 = Vector.extraction(str(d1_x), str(d1_y), x, y)
        unitList = Vector.toUnitVector(self, True)
        holder = [int(grad1), int(grad2), unitList]
        return Vector.innerProduct(self, holder, True)


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
        charList = []
        for char in self.s:

            if char.islower():
                rev_char = chr(ord('z') - ord(char) + ord('a'))
                charList.append(rev_char)

            elif char.isupper():
                rev_char = chr(ord('Z') - ord(char) + ord('A'))
                charList.append(rev_char)
        return "".join(charList)

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
        return stringRedefine(__other_obj.s + self.s)

    def __imul__(self, __other_obj):
        cartesian_product = [i + j for i in self.s for j in __other_obj.s]
        return "".join(cartesian_product)

    def __eq__(self, __o):
        return len(self.s) == len(__o.s)

    def __ne__(self, __o):
        return len(self.s) != len(__o.s)

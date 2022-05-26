import math
from sympy import *


class Vector:
    """This class performs some of the vector operations.

    Calculating directional derivative is the most important thing this class does.
    To use a directional derivative ,first of all you have to use \"directDervation_activator()\" method 
    to assign symbols to the  x  and  y  variables. then you can define your ideal function.

    Example:
        z = Vector(3, 4, 5, 8)
        x , y = z.directDervation_activator()
        Function = x*y+y**2+y**3
        print(z.directionalDervation(Function, x: xSymbol, y: ySymbol , xPoint(for example: 0) , yPoint(for example: 2)))
        Result: 15.14

    Attribute:
    directDervation_key (bool): Used to control the \"directionalDervation()\" method

    Methods:
        length(): Computes the length of the vector.
        summation(v): Computes the summation of two vectors.
        innerProduct(v): Computes the internal multiplication of two vectors.
        toUniteVector(): Convert the vector to unit vector.
        toPolarCoordinates(): Convert the coordinates of the vector from cartesian to polar.
        directionalDerivation(F, x, y): Directional derivative of F at the point(x,y) in direction of the vector.
    """

    directDervation_key = False

    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1

    def length(self) -> tuple[int, int]:
        """This method computes the length of the vector.

        Returns:
            tuple[int, int]: A tuple that has the size of a vector.
        """
        return (self.x1 - self.x0, self.y1 - self.y0)

    def summation(self, vec1) -> tuple:
        """This method computes the summation of two vectors.

        Args:
            vec1 (tuple): Second vector that needs to be sum with the first one.

        Returns:
            tuple: A tuple that has sum of two vectors.
        """
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

    def toPolarCoordinates(self) -> tuple[float, float]:
        """Convert the coordinates of the vector from cartesian to polar.

        Returns:
            tuple[float , float]: A tuple that has polarcoordinates.
        """
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

    @classmethod
    def directDervation_activator(cls, x="x", y="y"):
        cls.directDervation_key = True
        return symbols(x + " " + y, real=True)

    def directionalDervation(self, F: core.Add, sym_x: core.symbol, sym_y: core.symbol, a: int, b: int) -> float:
        """This method Calculates Directional derivative of F at the point(x,y) in direction of the vector.

        To calculate Directional derivative, 3 parts must be considered:
        _calculates Partial derivative of the function.
        _calculates unit vector of (x , y)
        _calculates innerProduct of two vector

        Args:
            F (sympy.core.Add): A function that we use to calculate Partial derivative
            sym_x (sympy.core.symbol): x variable of function
            sym_y (sympy.core.symbol): y variable of function
            a (int): Coordinates of point x
            b (int): Coordinates of point y

        Returns:
            float: Directional derivative
        """
        if Vector.directDervation_key:
            d1_x = diff(F, sym_x)
            d1_y = diff(F, sym_y)
            grad1, grad2 = Vector.extraction(str(d1_x), str(d1_y), a, b)
            unitList = Vector.toUnitVector(self, True)
            holder = [int(grad1), int(grad2), unitList]
            return Vector.innerProduct(self, holder, True)
        else:
            print("You must first use the \"directDervation_activator()\" method to assign symbols to the  x  and  y  variables")


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

    def switchHalf(self) -> str:
        """This method switch the place of the first half of string with the second part. 
           
        Attention:
        _if the number of the characters of our string was odd, the program keeps the middle character and switch the others.

        Returns:
            str: A string that has changed the place of each character according to the algorithm.
        """
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

    def encryption(self) -> str:
        """This method encrypts a string.

        How does this encrypting algorithm work:
        _it replaces each character from its number in English alphabet to a word in English alphabet that has the same number but from last to first.

        Example:
        _(a) is the first word, and the first word from last to first is (z), so the program changes (a) to (z)
        _(b) -> (y), (c) -> (x), and etc.
        
        Returns:
            string: A string that has made by encrypted characters
        """
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
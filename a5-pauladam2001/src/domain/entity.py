"""
    Entity class should be coded here
"""

"""
class complexNumberException(Exception):

    def __init__(self, msg):
        self._msg = msg
"""


class complexNumber:
    """
    Class that represents a complex number
    """

    def __init__(self, realPart, imaginaryPart):
        """
        Creates a complex number
        :param realPart: the real part of the complex number
        :param imaginaryPart: the imaginary part of the complex number
        """
        self._realPart = realPart
        self._imaginaryPart = imaginaryPart

    @property
    def realPart(self):
        """
        :return: the real part of the complex number
        """
        return self._realPart

    @property
    def imaginaryPart(self):
        """
        :return: the imaginary part of the complex number
        """
        return self._imaginaryPart

    def __str__(self):
        """
        Verifies in which form the complex number is. Used for the display command
        :return: how the complex number should be displayed
        """
        if self._imaginaryPart == -1:
            if self._realPart == 0:
                return "-i"
            else:
                return str(self._realPart) + " - i"
        elif self._imaginaryPart == 1:
            if self._realPart == 0:
                return "i"
            else:
                return str(self._realPart) + " + i"
        elif self._realPart == 0 and self._imaginaryPart != 0:
            return str(self._imaginaryPart) + "i"
        elif self._imaginaryPart < 0:
            return str(self._realPart) + " - " + str(abs(self._imaginaryPart)) + "i"
        elif self._imaginaryPart == 0:
            return str(self._realPart)
        else:
            return str(self._realPart) + " + " + str(self._imaginaryPart) + "i"


class testFunctionsEntity:

    @staticmethod
    def test_init():
        myComplexNumber = complexNumber(2, 3)
        assert myComplexNumber._realPart == 2
        assert myComplexNumber.imaginaryPart == 3
        myComplexNumber = complexNumber(0, -12)
        assert myComplexNumber._realPart == 0
        assert myComplexNumber.imaginaryPart == -12

    @staticmethod
    def test_str():
        myComplexNumber = complexNumber(-12, 2)
        print(myComplexNumber)
        myComplexNumber = complexNumber(0, 1)
        print(myComplexNumber)
        myComplexNumber = complexNumber(0, -3)
        print(myComplexNumber)

    @staticmethod
    def run_all_entity_tests():
        testFunctionsEntity.test_init()
        testFunctionsEntity.test_str()

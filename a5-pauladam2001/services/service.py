"""
    Service class includes functionalities for implementing program features
"""

from src.domain.entity import complexNumber
import random
#import sys


class complexNumbersList:
    """
    Functionalities for the (list of) complex numbers
    """

    def __init__(self):
        """
        Creates a list of complex numbers and initialize it with 10 random complex numbers
        """
        self._listOfComplexNumbers = []
        self.initial_numbers()

    def __getitem__(self, position):
        """
        Get an element from the list of complex numbers
        :param position: the position of the element that needs to be returned
        :return: the element from the given position
        """
        return self._listOfComplexNumbers[position]

    @property
    def list_of_complex_numbers(self):
        """
        :return: the list of complex numbers
        """
        return self._listOfComplexNumbers

    @list_of_complex_numbers.setter
    def list_of_complex_numbers(self, givenList):
        """
        Set the list of complex numbers
        :param givenList: the list attributed to the list of complex numbers
        """
        self._listOfComplexNumbers = list(givenList)

    def add_complex_number_to_list(self, complexNumberToAdd):
        """
        Adds a complex numbers to the list
        :param complexNumberToAdd: the complex number that will be added
        """
        self._listOfComplexNumbers.append(complexNumberToAdd)

    def filter_list(self, startPosition, endPosition):
        """
        Filter the list so that it contains only the numbers between <startPosition> and <endPosition>
        :param startPosition: the position from where we begin to keep the elements
        :param endPosition: the position where we stop keeping the elements
        """
        if startPosition < 0 or startPosition > len(self._listOfComplexNumbers) - 1 or startPosition > endPosition:
            raise IndexError("The start position should be greater than 0 and smaller than the end position which need to be smaller than " + str(len(self._listOfComplexNumbers) - 1) + '!')
        if endPosition < startPosition or endPosition > len(self._listOfComplexNumbers) - 1:
            raise IndexError("The final position should be bigger than " + str(startPosition) + " and smaller than " + str(len(self._listOfComplexNumbers) - 1) + '!')

        auxiliaryList = []

        for index in range(startPosition, endPosition + 1):
            auxiliaryList.append(self._listOfComplexNumbers[index])

        self._listOfComplexNumbers = auxiliaryList

    def __len__(self):
        """
        :return: the length of the list of complex numbers
        """
        return len(self._listOfComplexNumbers)

    def initial_numbers(self):
        """
        Adds 10 random complex numbers to the list at program startup
        """
        complexNumber1 = complexNumber(random.randint(-100, 100), random.randint(-100, 100))
        self.add_complex_number_to_list(complexNumber1)
        complexNumber2 = complexNumber(random.randint(-100, 100), random.randint(-100, 100))
        self.add_complex_number_to_list(complexNumber2)
        complexNumber3 = complexNumber(random.randint(-100, 100), random.randint(-100, 100))
        self.add_complex_number_to_list(complexNumber3)
        complexNumber4 = complexNumber(random.randint(-100, 100), random.randint(-100, 100))
        self.add_complex_number_to_list(complexNumber4)
        complexNumber5 = complexNumber(random.randint(-100, 100), random.randint(-100, 100))
        self.add_complex_number_to_list(complexNumber5)
        complexNumber6 = complexNumber(random.randint(-100, 100), random.randint(-100, 100))
        self.add_complex_number_to_list(complexNumber6)
        complexNumber7 = complexNumber(random.randint(-100, 100), random.randint(-100, 100))
        self.add_complex_number_to_list(complexNumber7)
        complexNumber8 = complexNumber(random.randint(-100, 100), random.randint(-100, 100))
        self.add_complex_number_to_list(complexNumber8)
        complexNumber9 = complexNumber(random.randint(-100, 100), random.randint(-100, 100))
        self.add_complex_number_to_list(complexNumber9)
        complexNumber10 = complexNumber(random.randint(-100, 100), random.randint(-100, 100))
        self.add_complex_number_to_list(complexNumber10)

        """
        #OR
        for index in range(10):
            myComplexNumber = complexNumber(random.randint(-sys.maxsize - 1, sys.maxsize), random.randint(-sys.maxsize - 1, sys.maxsize))
            self.add_complex_number_to_list(myComplexNumber)
        """


class historyList:
    """
    Functionalities for the history of lists
    """

    def __init__(self):
        """
        Creates a list which will contain all the modified lists
        """
        self._historyOfLists = []

    def __getitem__(self, position):
        """
        Get an element(list) from the list of all the modified lists
        :param position: the position of the element(list) that needs to be returned
        :return: the element(list) from the given position
        """
        return self._historyOfLists[position]

    @property
    def history_list(self):
        """
        :return: the list of all the modified lists
        """
        return self._historyOfLists

    def __len__(self):
        """
        :return: the length of the list of all the modified lists
        """
        return len(self._historyOfLists)

    def add_to_history(self, listOfComplexNumbers):
        """
        Adds a list of complex numbers to the history of modified lists
        :param listOfComplexNumbers: the list that will be added
        """
        self._historyOfLists.append(list(listOfComplexNumbers))

    def remove_at_position(self, position):
        """
        Remove the list from the given position from the history of modified lists
        :param position: the position from which we need to delete the list
        """
        self._historyOfLists.pop(position)

        #OR del self._historyOfLists[position]

    def undo_operation(self, listOfComplexNumbers):
        """

        :return:
        """
        if len(self._historyOfLists) < 2:
            raise ValueError('There is nothing to undo!')

        listOfComplexNumbers.clear()
        self.remove_at_position(-1)
        for number in self._historyOfLists[-1]:
            listOfComplexNumbers.append(number)


class testFunctionsService:

    @staticmethod
    def test_init():
        listOfComplexNumbers = complexNumbersList()
        assert len(listOfComplexNumbers) == 10

    @staticmethod
    def test_add_complex_number_to_list():
        listOfComplexNumbers = complexNumbersList()
        listOfComplexNumbers.add_complex_number_to_list(complexNumber(2, 3))
        assert  len(listOfComplexNumbers) == 11
        print(listOfComplexNumbers[0])

    @staticmethod
    def test_filter_list():
        listOfComplexNumbers = complexNumbersList()
        listOfComplexNumbers.filter_list(2,5)
        assert len(listOfComplexNumbers) == 4
        listOfComplexNumbers.filter_list(0,0)
        assert len(listOfComplexNumbers) == 1

    @staticmethod
    def test_add_to_history():
        historyOfLists = historyList()
        listOfComplexNumbers = complexNumbersList()
        historyOfLists.add_to_history(listOfComplexNumbers.list_of_complex_numbers)
        assert len(historyOfLists) == 1

    @staticmethod
    def test_remove_at_position():
        historyOfLists = historyList()
        listOfComplexNumbers = complexNumbersList()
        historyOfLists.add_to_history(listOfComplexNumbers.list_of_complex_numbers)
        assert len(historyOfLists) == 1
        historyOfLists.remove_at_position(0)
        assert len(historyOfLists) == 0


    @staticmethod
    def run_all_service_tests():
        testFunctionsService.test_init()
        testFunctionsService.test_add_complex_number_to_list()
        testFunctionsService.test_filter_list()
        testFunctionsService.test_add_to_history()
        testFunctionsService.test_remove_at_position()

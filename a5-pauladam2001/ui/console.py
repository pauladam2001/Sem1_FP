"""
    UI class.

    Calls between program modules
    ui -> service -> entity
    ui -> entity
"""

from src.services.service import complexNumbersList, historyList
from src.domain.entity import complexNumber


class userInterface:
    """
    Handles the user interface
    """

    def __init__(self):
        """
        Communicates with 'functions' class
        """
        self._functions_UI = complexNumbersList()
        self._historyOfLists_UI = historyList()

    def display_complexNumbers(self):
        """
        Writes the list of complex numbers in the console
        """
        for number in self._functions_UI.list_of_complex_numbers:
            print(number)

    def read_realPart(self):
        """
        Reads the real part of the complex number from console
        :return: the real part of the complex number
        """
        realPart = int(input("\nReal part: "))
        return realPart

    def read_imaginaryPart(self):
        """
        Reads the imaginary part of the complex number from console
        :return: the imaginary part of the complex number
        """
        imaginaryPart = int(input("Imaginary part: "))
        return imaginaryPart

    def read_complexNumber(self):
        """
        Creates the complex number and adds it to the list of complex numbers
        """
        realPart = self.read_realPart()
        imaginaryPart = self.read_imaginaryPart()
        complexNumberToAdd = complexNumber(realPart, imaginaryPart)
        self._functions_UI.add_complex_number_to_list(complexNumberToAdd)

        return True

    def read_startFilterPosition(self):
        """
        Reads the start position of the filter command
        :return: the start position
        """
        startPosition = int(input("Start position: "))
        return startPosition

    def read_endFilterPosition(self):
        """
        Reads the end position of the filter command
        :return: the end position
        """
        endPosition = int(input("End position: "))
        return endPosition

    def filter_ui(self):
        """
        Handles the filter command
        """
        startPosition = self.read_startFilterPosition()
        endPosition = self.read_endFilterPosition()
        self._functions_UI.filter_list(startPosition, endPosition)

        return True

    def print_menu(self):
        """
        Prints the menu with the commands that can be used
        """
        print("\n\nMENU:")
        print('\t1. Read and add a complex number to the list;')
        print('\t2. Display the list of complex numbers;')
        print('\t3. Filter the list so that it contains only the numbers between indices <start> and <end> (read from the console);')
        print('\t4. Undo the last operation that modified program data;')
        print('\t0. Exit the program.\n')

    def start_command_ui(self):
        """
        Handles user interface
        """

        self._historyOfLists_UI.add_to_history(self._functions_UI.list_of_complex_numbers)

        menuItems = {"1": self.read_complexNumber, "2": self.display_complexNumbers, "3": self.filter_ui}

        done = False

        while not done:
            self.print_menu()
            option = input("Enter an option: ").strip().lower()

            if option == '0':
                done = True
                print('See you later!')
            elif option == '4':
                try:
                    self._historyOfLists_UI.undo_operation(self._functions_UI.list_of_complex_numbers)
                except ValueError as ve:
                    print(str(ve))
            elif option in menuItems:
                try:
                    if menuItems[option]():
                        self._historyOfLists_UI.add_to_history(self._functions_UI.list_of_complex_numbers)
                except ValueError as ve:
                    print(str(ve))
                except TypeError as te:
                    print(str(te))
                except IndexError as ie:
                    print(str(ie))
                #except complexNumberException:
                    #print(str(complexNumberException))
                except:
                    print("There was an exception which was not handled!")
            else:
                print('This in not a command!')

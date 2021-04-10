#
# Write the implementation for A2 in this file
#
# Function section
# (write all non-UI functions in this section)
# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values


def add_complexNumber_to_list(realPart, imaginaryPart, complexNumbersList):
    """
    Adds a complex number to the list
    input: realPart - the real part of the complex number
           imaginaryPart - the imaginary part of the complex number
           complexNumbersList - the list of complex numbers
    """

    complexNumbersList.append([realPart, imaginaryPart])


def get_real_part(complexNumber, complexNumbersList):
    return complexNumbersList[complexNumber][0]


def get_imaginary_part(complexNumber, complexNumbersList):
    return complexNumbersList[complexNumber][1]


def check_longest_sequence(startPosition, finalPosition, maxSequence):
    """
    Checks if the found sequence is longer than the actual longest sequence
    input: startPosition - the position where the sequence starts
           finalPosition - the position where the sequence ends
           maxSequence - how many elements the actual longest sequence contains
    output: returns -1 if the longest sequence remains the same, or the positions of the newest longest sequence
    """

    if finalPosition - startPosition > maxSequence:
        return startPosition, finalPosition
    return -1


def search_sequence(start_index, maxSequence, complexNumbersList):
    """
    Searches if there exists a sequence longer than the actual one
    input: start_index - the position where the sequence starts
           maxSequence - the longest sequence until then (how many elements it contains)
           complexNumbersList - the list of complex numbers
    output: returns -1 if it didn't find a longer sequence, or the positions of the new longest sequence and how big it is
    """

    positionChange = 0                                  # this is used to see if the longest sequence changes and to know what to return
    realPartSum = get_real_part(start_index, complexNumbersList)
    imaginaryPartSum = get_imaginary_part(start_index, complexNumbersList)
    for final_index in range(start_index + 1, len(complexNumbersList)):
        realPartSum += get_real_part(final_index, complexNumbersList)
        imaginaryPartSum += get_imaginary_part(final_index, complexNumbersList)
        if realPartSum == 10 and imaginaryPartSum == 10:
            if check_longest_sequence(start_index, final_index, maxSequence) != -1:
                startPosition, finalPosition = check_longest_sequence(start_index, final_index, maxSequence)
                positionChange = 1
                maxSequence = finalPosition - startPosition
    if positionChange == 1:
        return startPosition, finalPosition, maxSequence
    return -1
             

def sumOfRealAndImaginaryPartIs10_property(complexNumbersList):
    """
    Searches for the sequence with the given property
    input: complexNumbersList - the list of complex numbers
    output: returns -1 if it does not exist a sequence, or the first and last position of the sequence if it exists
    """

    startPosition = -1
    finalPosition = -1
    maxSequence = 0
    for start_index in range(len(complexNumbersList)):
        if search_sequence(start_index, maxSequence, complexNumbersList) != -1:
            startPosition, finalPosition, maxSequence = search_sequence(start_index, maxSequence, complexNumbersList)
    if startPosition == -1 or finalPosition == -1 or maxSequence == 0:
        return -1
    return startPosition, finalPosition


def decrease_value(start_index, final_index, mountainTop, maxSequence, complexNumbersList):
    """
    Finds the last element from the decreasing values (we suppose they are decreasing)  (the base of the mountain)
    input: start_index - the first element of the supposing increasing list
           final_index - the position of the current smallest element
           mountainTop - the current smallest value (they are decreasing)
           maxSequence - the longest sequence until then (how many elements it contains)
           complexNumbersList - the list of complex numbers
    output: returns -1 if it does not exist any sequence, or the first and last position of the sequence and how long it is
    """

    mountainForm = 0                                                # this is used to know if we have a "mountain"
    while mountainTop > get_real_part(final_index, complexNumbersList) and final_index <= len(complexNumbersList):
        mountainTop = get_real_part(final_index, complexNumbersList)
        final_index += 1
        mountainForm = 1
        if final_index == len(complexNumbersList):              # without this if python gives the error "index out of range" even if we have the condition in the while loop
            break
    final_index -= 1                                                                     # j -= 1 because in while it goes one step further
    if mountainForm == 1 and check_longest_sequence(start_index, final_index, maxSequence) != -1:
        maxSequence = final_index - start_index
        return start_index, final_index, maxSequence
    return -1


def increase_value(start_index, final_index, mountainTop, complexNumbersList):
    """
    Finds the last element from the increasing values (we suppose they are increasing) (the top of the mountain)
    input: start_index - the first element of the supposing increasing list
           final_index - the position of the current biggest element
           mountainTop - the biggest value (the peak of the mountain) (they are increasing)
           complexNumbersList - the list of complex numbers
    output: the peak of the supposed mountain and its position
    """

    while get_real_part(final_index, complexNumbersList) > get_real_part(start_index, complexNumbersList) and mountainTop < get_real_part(final_index, complexNumbersList):
        mountainTop = get_real_part(final_index, complexNumbersList)
        final_index += 1
    return final_index, mountainTop


def complexNumbersInFormOfMountain_property(complexNumbersList):
    """
    Searches for the sequence with the given property
    input: complexNumbersList - the list of complex numbers
    output: returns -1 if it does not exist a sequence, or the first and last position of the sequence if it exists
    """

    startPosition = -1
    finalPosition = -1
    maxSequence = 1
    for start_index in range(0, len(complexNumbersList) - 2):
        final_index = start_index + 1
        mountainTop =  get_real_part(final_index - 1, complexNumbersList)
        final_index, mountainTop = increase_value(start_index, final_index, mountainTop, complexNumbersList)                              
        if decrease_value(start_index, final_index, mountainTop, maxSequence, complexNumbersList) != -1:
            startPosition, finalPosition, maxSequence = decrease_value(start_index, final_index, mountainTop, maxSequence, complexNumbersList)
    if startPosition == -1 or finalPosition == -1 or maxSequence == 1:
        return -1
    return startPosition, finalPosition
 

# UI section
# (write all functions that have input or print statements here). 
# Ideally, this section should not contain any calculations relevant to program functionalities


def write_property_complexNumbers(startPosition, finalPosition, complexNumbersList):
    """
    Writes the sequence of numbers which have the asked property
    input: startPosition - the position where the sequence starts
           finalPosition - the position where the sequence ends 
           complexNumbersList - the list of complex numbers
    output: shows the numbers in the console
    """

    for index in range(startPosition, finalPosition + 1):
        if complexNumbersList[index][0] == 0:
            print(str(complexNumbersList[index][1]) + 'i')
        elif complexNumbersList[index][1] == 0:
            print(str(complexNumbersList[index][0]))
        elif complexNumbersList[index][1] < 0:
            print(str(complexNumbersList[index][0]) + str(complexNumbersList[index][1]) + 'i')
        elif complexNumbersList[index][1] > 0:
            print(str(complexNumbersList[index][0]) + '+' + str(complexNumbersList[index][1]) + 'i')



def sumOfRealAndImaginaryPartIs10_property_ui(complexNumbersList):
    """
    Verifies if there exists a sequence with the given property, if yes it will print the longest one
    input: complexNumbersList - the list of complex numbers
    """

    if sumOfRealAndImaginaryPartIs10_property(complexNumbersList) == -1:
        print("There is no sequence with this property!")
        return
    startPosition, finalPosition = sumOfRealAndImaginaryPartIs10_property(complexNumbersList)
    write_property_complexNumbers(startPosition, finalPosition, complexNumbersList)


def complexNumbersInFormOfMountain_property_ui(complexNumbersList):
    """
    Verifies if there exists a sequence with the given property, if yes it will print the longest one
    input: complexNumbersList - the list of complex numbers
    """

    if complexNumbersInFormOfMountain_property(complexNumbersList) == -1:
        print("There is no sequence with this property!")
        return
    startPosition, finalPosition = complexNumbersInFormOfMountain_property(complexNumbersList)
    write_property_complexNumbers(startPosition, finalPosition, complexNumbersList)


def write_complexNumbers(complexNumbersList):
    """
    Writes the list of complex numbers 
    input: complexNumbersList - the list of complex numbers
    output: shows the elements in the console
    """

    for index in range(len(complexNumbersList)) :
        if complexNumbersList[index][0] == 0:                                                                     #the number does not have a real part
            print(str(complexNumbersList[index][1]) + 'i')
        elif complexNumbersList[index][1] == 0:                                                                   #the number does not have a imaginary part
            print(str(complexNumbersList[index][0]))
        elif complexNumbersList[index][1] < 0:                                                                    #the number's imaginary part is < 0
            print(str(complexNumbersList[index][0]) + str(complexNumbersList[index][1]) + 'i')
        elif complexNumbersList[index][1] > 0:                                                                    #the number's imaginary part is > 0
            print(str(complexNumbersList[index][0]) + '+' + str(complexNumbersList[index][1]) + 'i')


def read_realPart_ui():
    """
    Reads the real part of the complex number from console
    :return: The real part of the complex number
    """

    realPart = int(input("\nReal part: "))
    return realPart


def read_imaginaryPart_ui():
    """
    Reads the imaginary part of the complex number from console
    :return: The imaginary part of the complex number
    """

    imaginaryPart = int(input("Imaginary part: "))
    return imaginaryPart


def read_complexNumber_ui(complexNumbersList):
    """
    Reads a complex number and add it to the list
    input: complexNumbersList - the list of complex numbers
    """

    realPart = read_realPart_ui()
    imaginaryPart = read_imaginaryPart_ui()
    add_complexNumber_to_list(realPart, imaginaryPart, complexNumbersList)


def write_complexNumbers_ui(complexNumbersList):
    """
    Verifies if the list is not empty, if it's not then the complex numbers are written in console
    input: complexNumbersList - the list of complex numbers
    """

    if len(complexNumbersList) == 0:
        print("\nThe list is empty!")
    else:
        write_complexNumbers(complexNumbersList)


def print_menu():
    print("\nMenu:")
    print("\t1. Read a complex number")
    print("\t2. Display the complex numbers")
    print("\t3. Display the longest sequence in which the sum of its elements is 10+10i")
    print("\t4. Display the longest sequence in which the real part is in form of a mountain")
    print("\t0. Exit the application")
    print("\n");


def start_numbers(complexNumbersList):
    """
    Adds 10 numbers to the list at program startup
    """

    add_complexNumber_to_list(3, 2, complexNumbersList)
    add_complexNumber_to_list(4, -1, complexNumbersList)
    add_complexNumber_to_list(5, 9, complexNumbersList)
    add_complexNumber_to_list(2, -1, complexNumbersList)
    add_complexNumber_to_list(1, 3, complexNumbersList)
    add_complexNumber_to_list(0, 6, complexNumbersList)
    add_complexNumber_to_list(2, -7, complexNumbersList)
    add_complexNumber_to_list(7, -1, complexNumbersList)
    add_complexNumber_to_list(1, 2, complexNumbersList)
    add_complexNumber_to_list(3, 9, complexNumbersList)


def start():
    """
    Handles the main menu
    :return: Returns once the program is finished
    """

    complexNumbersList = []
    start_numbers(complexNumbersList)
    finish = False

    while not finish:
        print_menu()
        option = input("Enter an option: ").strip().lower()
        
        if option == '1':
            read_complexNumber_ui(complexNumbersList)
        elif option == '2':
            write_complexNumbers_ui(complexNumbersList)
        elif option == '3':
            sumOfRealAndImaginaryPartIs10_property_ui(complexNumbersList)
        elif option == '4':
            complexNumbersInFormOfMountain_property_ui(complexNumbersList)
        elif option == '0':
            print('\nSee you later!')
            finish = True
        else:
            print("\nBad command!")


"""
Program entry point
"""
start()

"""
def start():
    nrlist = []
    start_numbers(nrlist)
    finish = False

    command_dict = {'1': read_number_ui, '2': write_numbers_ui, '3': sum10_property_ui, '4': mountain_property_ui}

    while not finish:
        print_menu()
        option = input("Enter an option: ")
        if option == '0':
            print('\nSee you later!')
            finish = True
        elif command not in command_dict:
            print("\nBad command!")
        else:
            command_dict[command](nrlist)

start()
"""
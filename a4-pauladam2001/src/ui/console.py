"""
This is the user interface module. These functions call functions from the domain and functions module.
"""

from src.domain.entity import get_average_score_of_contestants, get_average_score_of_one_contestant, get_problem1, get_problem2, get_problem3
from src.functions.functions import initial_contestants, add_command, insert_command, remove_command, replace_command, split_command, average_score_of_multiple_contestants, lowest_average_score_of_multiple_contestants, remove_contestants_with_average_score_smaller_aNumber, remove_contestants_with_average_score_greater_aNumber, remove_contestants_with_average_score_equal_aNumber, create_copy_of_list, add_list_to_history


def display_all_contestants(listOfContestants):
    """
    Displays all contestants
    input: listOfContestants - the list of all contestants
    """

    print('\n')
    for contestant in range(len(listOfContestants)):
        print('Index ' + str(contestant) + ': ' + str(listOfContestants[contestant]))


def display_contestants_with_average_score_smaller_aNumber(conditionNumber, listOfContestants):
    """
    Displays the contestants with an average score lesser than <conditionNumber>
    input: conditionNumber - the number typed by the user after the condition
           listOfContestants - the list of all contestants
    """

    for contestant in range(len(listOfContestants)):
        if get_average_score_of_one_contestant(contestant, listOfContestants) < conditionNumber:
            print('Index ' + str(contestant) + ': ' + str(listOfContestants[contestant]))


def display_contestants_with_average_score_greater_aNumber(conditionNumber, listOfContestants):
    """
    Displays the contestants with an average score greater than <conditionNumber>
    input: conditionNumber - the number typed by the user after the condition
           listOfContestants - the list of all contestants
    """

    for contestant in range(len(listOfContestants)):
        if get_average_score_of_one_contestant(contestant, listOfContestants) > conditionNumber:
            print('Index ' + str(contestant) + ': ' + str(listOfContestants[contestant]))


def display_contestants_with_average_score_equal_aNumber(conditionNumber, listOfContestants):
    """
    Displays the contestants with an average score equal with <conditionNumber>
    input: conditionNumber - the number typed by the user after the condition
           listOfContestants - the list of all contestants
    """

    for contestant in range(len(listOfContestants)):
        if get_average_score_of_one_contestant(contestant, listOfContestants) == conditionNumber:
            print('Index ' + str(contestant) + ': ' + str(listOfContestants[contestant]))


def display_contestants_in_decreasing_order_of_average_score(listOfContestants):
    """
    Displays the contestants sorted in decreasing order of average score
    input: listOfContestants - the list of all contestants
    """

    listOfContestants.sort(reverse = True, key = get_average_score_of_contestants)
    display_all_contestants(listOfContestants)


def display_contestants_by_condition(condition, conditionNumber, listOfContestants):
    """
    Handles the displays by condition
    input: condition - the condition typed by the user (<, > or =)
           conditionNumber - the number typed by the user after the condition
           listOfContestants - the list of all contestants
    """

    if condition == '<':
        display_contestants_with_average_score_smaller_aNumber(conditionNumber, listOfContestants)
    elif condition == '>':
        display_contestants_with_average_score_greater_aNumber(conditionNumber, listOfContestants)
    else:
        display_contestants_with_average_score_equal_aNumber(conditionNumber, listOfContestants)


def display_command_ui(listOfContestants, command_parameters):
    """
    Handles all types of displays
    input: listOfContestants - the list of all contestants
           command_parameters - the parameters that were typed by the user
    """

    if(command_parameters == ''):
        display_all_contestants(listOfContestants)
    else:
        tokens = command_parameters.split()
        if(tokens[0] == 'sorted'):
            display_contestants_in_decreasing_order_of_average_score(listOfContestants)
        elif len(tokens) == 2:
            condition = tokens[0]  #'<', '>', '='
            conditionNumber = float(tokens[1])
            display_contestants_by_condition(condition, conditionNumber, listOfContestants)
        else:
            raise ValueError("Invalid parameters to display contestants!")


def average_score_ui(listOfContestants, command_parameters):
    """
    Handles the avg command
    input: listOfContestants - the list of all contestants
           command_parameters - the parameters that were typed by the user 
    """

    tokens = command_parameters.split()

    if len(tokens) != 3:
        raise ValueError("Invalid parameters!")

    startPosition = int(tokens[0])
    finalPosition = int(tokens[2])
    print("The average score of the given contestants is " + str(round(average_score_of_multiple_contestants(startPosition, finalPosition, listOfContestants),2)))  #because tokens[1] == 'to'


def min_average_score_ui(listOfContestants, command_parameters):
    """
    Handles the min command
    input: listOfContestants - the list of all contestants
           command_parameters - the parameters that were typed by the user
    """
    
    tokens = command_parameters.split()

    if len(tokens) != 3:
        raise ValueError("Invalid parameters!")

    startPosition = int(tokens[0])
    finalPosition = int(tokens[2])
    print("The lowest average score between given contestants is " + str(round(lowest_average_score_of_multiple_contestants(startPosition, finalPosition, listOfContestants),2)))  #because tokens[1] == 'to'


def display_numberGiven_contestants(numberOfContestantsDisplayed, listOfContestants):
    """
    Displays the first <numberOfContestantsDisplayed> contestants
    input: numberOfContestantsDisplayed - how many competitors the top contains
           listOfContestants - the list of all contestants
    """

    print('\n')
    for contestant in range(numberOfContestantsDisplayed):
        print('Index ' + str(contestant) + ': ' + str(listOfContestants[contestant]))

def display_podium_by_average_score(numberOfContestantsDisplayed, listOfContestants):
    """
    Displays the first <numberOfContestantsDisplayed> contestants sorted in decreasing order of average score
    input: numberOfContestantsDisplayed - how many competitors the top contains
           listOfContestants - the list of all contestants
    """
    
    if numberOfContestantsDisplayed > len(listOfContestants):
        raise ValueError("There are not that many contestants!")

    listOfContestants.sort(reverse = True, key = get_average_score_of_contestants)
    display_numberGiven_contestants(numberOfContestantsDisplayed, listOfContestants)


def display_podium_for_aProblem(numberOfContestantsDisplayed, problemNumber, listOfContestants):
    """
    Displays the first <numberOfContestantsDisplayed> contestants sorted in decreasing order problem1/problem2/problem3 score
    input: numberOfContestantsDisplayed - how many competitors the top contains
           problemNumber - P1/P2/P3
           listOfContestants - the list of all contestants
    """
    
    if problemNumber == 'P1':
        listOfContestants.sort(reverse = True, key = get_problem1)
    elif problemNumber == 'P2':
        listOfContestants.sort(reverse = True, key = get_problem2)
    elif problemNumber == 'P3':
        listOfContestants.sort(reverse = True, key = get_problem3)
    else:
        raise TypeError("There are only 3 problems!")

    display_numberGiven_contestants(numberOfContestantsDisplayed, listOfContestants)


def establish_podium_ui(listOfContestants, command_parameters):
    """
    Handles the top command
    input: listOfContestants - the list of all contestants
           command_parameters - the parameters that were typed by the user
    """
    
    tokens = command_parameters.split()

    if len(tokens) == 1:
        numberOfContestantsDisplayed = int(tokens[0])
        display_podium_by_average_score(numberOfContestantsDisplayed, listOfContestants)
    elif len(tokens) == 2:
        numberOfContestantsDisplayed = int(tokens[0])
        problemNumber = tokens[1].strip().upper()
        display_podium_for_aProblem(numberOfContestantsDisplayed, problemNumber, listOfContestants)
    else:
        raise ValueError("Invalid parameters!")


def start_command_ui():
    """
    Handles user interface
    """

    listOfContestants = []
    initial_contestants(listOfContestants)

    historyOfLists = []
    historyOfLists = [create_copy_of_list(listOfContestants)]

    done = False

    command_dictionary = {'add': add_command, 'insert': insert_command, 'remove': remove_command, 'replace': replace_command, 'list': display_command_ui, 'avg': average_score_ui, 'min': min_average_score_ui, 'top': establish_podium_ui}

    while not done:

        command = input("\ncommand: ").strip().lower()
        command_word, command_parameters = split_command(command)

        if "exit" == command_word:
            print("See you later!")
            done = True
        elif 'undo' == command_word:
            if len(historyOfLists) > 1:
                historyOfLists.pop()
                historyOfListsInTuple = tuple(historyOfLists[len(historyOfLists) - 1])
                listOfContestants = historyOfListsInTuple
                listOfContestants = list(listOfContestants)  # we make listOfContestants back to a list because tuples are immovable so we can't perform add/insert etc. on them
                
                # OR historyOfLists.pop()
                # listOfContestants = create_copy_of_list(historyOfLists[len(historyOfLists) - 1])
            else:
                print("There are no more undos!")
        elif command_word in command_dictionary:
            try:
                if command_dictionary[command_word](listOfContestants, command_parameters) == True:
                    add_list_to_history(listOfContestants, historyOfLists)

                    #OR historyOfLists.append(create_copy_of_list(listOfContestants))
                    #OR we can use list.copy()
            except ValueError as ve:
                print(str(ve))
            except TypeError as te:
                print(str(te))
            except IndexError as ie:
                print(str(ie))
            #except:
                #print("There was an exception which was not handled!")
           # else:
               # print("no error")
        else:
            print("\nThis is not a command!")

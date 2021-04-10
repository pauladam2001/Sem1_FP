#
# Write the implementation for A3 in this file
#

#
# domain section is here (domain = numbers, transactions, expenses, etc.)
# getters / setters
# No print or input statements in this section
# Specification for all non-trivial functions (trivial usually means a one-liner)


def get_average_score_of_contestants(listOfContestants):
    """
    Used to display the contestants sorted in decreasing order of average score
    input: listOfContestants - the list of all contestants
    """

    return float((listOfContestants['P1'] + listOfContestants['P2'] + listOfContestants['P3']) / 3)


def get_average_score_of_one_contestant(contestant, listOfContestants):
    """
    Returns the average score of a contestant
    input: contestant - the index of the contestant
           listOfContestants - the list of all contestants
    """

    return float((listOfContestants[contestant]['P1'] + listOfContestants[contestant]['P2'] + listOfContestants[contestant]['P3']) / 3)


def set_newValue(contestantNumber, problemNumber, newValue, listOfContestants):
    """
    Sets a new value for a given problem
    input: contestantNumber - the position of the contestant
           problemNumber - P1, P2 or P3
           newValue - the new value of "problemNumber"
           listOfContestants - the list of all contestants
    """

    listOfContestants[contestantNumber][problemNumber] = newValue


# Functionalities section (functions that implement required features)
# No print or input statements in this section
# Specification for all non-trivial functions (trivial usually means a one-liner)
# Each function does one thing only
# Functions communicate using input parameters and their return values


def add_contestant_to_list(gradeP1, gradeP2, gradeP3, listOfContestants):
    """
    Adds a contestant to the list of all contestants
    input: gradeP1 - grade for problem 1
           gradeP2 - grade for problem 2
           gradeP3 - grade for problem 3
           listOfContestants - the list of all contestants
    """

    if gradeP1 < 0 or gradeP1 > 10:
        raise ValueError("The grade must be an integer between 0 and 10!")
    if gradeP2 < 0 or gradeP2 > 10:
        raise ValueError("The grade must be an integer between 0 and 10!")
    if gradeP3 < 0 or gradeP3 > 10:
        raise ValueError("The grade must be an integer between 0 and 10!")

    listOfContestants.append({'P1': gradeP1, 'P2': gradeP2, 'P3': gradeP3})
    

def insert_new_contestant_at_given_position(gradeP1, gradeP2, gradeP3, position, listOfContestants):
    """
    Inserts a new student at the given position
    input: gradeP1 - grade for P1
           gradeP2 - grade for P2
           gradeP3 - grade for P3
           position - the position where the contestant needs to be inserted
           listOfContestants - the list of all contestants
    """

    if position < 0 or position > len(listOfContestants) + 1:
        raise ValueError("The position should be minimum 0 and maximum " + str(len(listOfContestants)) + '!')
    if gradeP1 < 0 or gradeP1 > 10:
        raise ValueError("The grade must be an integer between 0 and 10!")
    if gradeP2 < 0 or gradeP2 > 10:
        raise ValueError("The grade must be an integer between 0 and 10!")
    if gradeP3 < 0 or gradeP3 > 10:
        raise ValueError("The grade must be an integer between 0 and 10!")

    listOfContestants.insert(position, {'P1': gradeP1, 'P2': gradeP2, 'P3': gradeP3})


def remove_one_position(position, listOfContestants):
    """
    Removes the student at the given position (sets his score to 0)
    input: position - the position from where we need to remove the contestant
           listOfContestants - the list of all contestants
    """
    
    if position < 0 or position > len(listOfContestants) - 1:
        raise IndexError("The position should be minimum 0 and maximum " + str(len(listOfContestants) - 1) + '!')

    listOfContestants.pop(position)
    insert_new_contestant_at_given_position(0, 0, 0, position, listOfContestants)
    
    #OR
    """
    listOfContestants[position]['P1'] = 0
    listOfContestants[position]['P2'] = 0
    listOfContestants[position]['P3'] = 0
    """


def remove_multiple_positions(startPosition, finalPosition, listOfContestants):
    """
    Removes contestants beggining with <startPosition> and ending with <finalPosition> (sets their score to 0)
    input: startPosition - the position from where we begin to remove contestants
           finalPosition - the position where we stop removing contestants
           listOfContestants - the list of all contestants
    """

    if startPosition < 0 or startPosition > len(listOfContestants) - 1 or startPosition > finalPosition:
        raise IndexError("The start position should be smaller than the final position which needs to be smaller than " + str(len(listOfContestants) - 1) + '!')
    if finalPosition < startPosition or finalPosition > len(listOfContestants) - 1:
        raise IndexError("The final position should be higher than " + str(startPosition) + " and smaller than " + str(len(listOfContestants) - 1) + '!')

    for position in range(startPosition, finalPosition + 1):
        remove_one_position(position,listOfContestants)

def replace_oldGrade_with_newGrade(contestantNumber, problemNumber, newValue, listOfContestants):
    """
    Sets the new grade of a problem of a contestant
    input: contestantNumber - the index of the contestants whose value needs to be replaced
           problemNumber - the problem whose grade needs to be replaced
           newValue - the new grade
           listOfContestants - the list of all contestants
    """

    if contestantNumber < 0 or contestantNumber > len(listOfContestants) - 1:
        raise IndexError("The position should be minimum 0 and maximum " + str(len(listOfContestants) - 1) + '!')
    if problemNumber != 'P1' and problemNumber != 'P2' and problemNumber != 'P3':
        raise TypeError("There are only 3 problems whose value can ba replaced!")
    if newValue < 0 or newValue > 10:
        raise ValueError("The grade must be an integer between 0 and 10!")

    set_newValue(contestantNumber, problemNumber, newValue, listOfContestants)


# UI section
# (all functions that have input or print statements, or that CALL functions with print / input are  here).
# Ideally, this section should not contain any calculations relevant to program functionalities 

def display_all_contestants(listOfContestants):
    """
    Displays all contestants
    input: listOfContestants - the list of all contestants
    """

    print('\n')
    for contestant in range(len(listOfContestants)):
        print('Index ' + str(contestant) + ': ' + str(listOfContestants[contestant]))

def display_contestants_in_decreasing_order_of_average_score(listOfContestants):
    """
    Displays the contestants sorted in decreasing order of average score
    input: listOfContestants - the list of all contestants
    """

    listOfContestants.sort(reverse = True, key = get_average_score_of_contestants)
    display_all_contestants(listOfContestants)


def display_contestants_with_average_score_smaller_aNumber(conditionNumber, listOfContestants):
    """
    Displays the contestants with an average score smaller than <conditionNumber>
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


def add_command_ui(listOfContestants, command_parameters):
    """
    Handles the add command
    input: listOfContestants - the list of all contestants
           command_parameters - the parameters that were typed by the user
    """

    tokens = command_parameters.split()

    if len(tokens) != 3:
        raise ValueError("Invalid parameters to add a contestant!")

    add_contestant_to_list(int(tokens[0]), int(tokens[1]), int(tokens[2]), listOfContestants)  #tokens[0]=P1, tokens[1]=P2, tokens[2]=P3
        

def insert_command_ui(listOfContestants, command_parameters):
    """
    Handles the insert command
    input: listOfContestants - the list of all contestants
           command_parameters - the parameters that were typed by the user
    """

    tokens = command_parameters.split()

    if len(tokens) != 5:
        raise ValueError("Invalid parameters to insert a contestant!")

    insert_new_contestant_at_given_position(int(tokens[0]), int(tokens[1]), int(tokens[2]), int(tokens[4]), listOfContestants)  #because tokens[3] == 'at'
                                              #tokens[0]=P1, tokens[1]=P2, tokens[2]=P3, tokens[4]=position

def remove_command_ui(listOfContestants, command_parameters):
    """
    Handles the remove command
    input: listOfContestants - the list of all contestants
           command_parameters - the parameters that were typed by the user
    """

    tokens = command_parameters.split()
    if len(tokens) == 1:
        remove_one_position(int(tokens[0]), listOfContestants)
    elif len(tokens) == 3:
        remove_multiple_positions(int(tokens[0]), int(tokens[2]), listOfContestants)   #because tokens[1] == 'to'  #tokens[0]=startPosition, tokens[1]=finalPosition
    else:
        raise ValueError("Invalid parameters to remove contestants!")


def replace_command_ui(listOfContestants, command_parameters):
    """
    Handles the replace command
    input: listOfContestants - the list of all contestants
           command_parameters - the parameters that were typed by the user
    """

    tokens = command_parameters.split()

    if len(tokens) != 4:
        raise ValueError("Invalid parameters to replace the score of a contestant!")
    replace_oldGrade_with_newGrade(int(tokens[0]), tokens[1].upper(), int(tokens[3]), listOfContestants)  #because tokens[2] == 'with'
                                    #tokens[0]=position, tokens[1]=P1/P2/P3, tokens[3]=the new score

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
            conditionNumber = tokens[1]
            display_contestants_by_condition(condition, int(conditionNumber), listOfContestants)
        else:
            raise ValueError("Invalid parameters to display contestants!")


def split_command(command):
    """
    Determines which command was typed by the user and the command's parameters
    input: command - user's command
    Return: the command typed and its parameters
    """

    tokens = command.strip().split(' ', 1)
    return tokens[0].strip().lower(), tokens[1].strip() if len(tokens) > 1 else ''  #tokens[0]=command, tokens[1]=parameters


def start_command_ui():
    """
    Handles user interface
    """

    listOfContestants = []
    test_initial_contestants(listOfContestants)

    done = False

    command_dictionary = {'add': add_command_ui, 'insert': insert_command_ui, 'remove': remove_command_ui, 'replace': replace_command_ui, 'list': display_command_ui}

    while not done:

        command = input("\ncommand: ").strip().lower()
        command_word, command_parameters = split_command(command)

        if "exit" == command_word:
            print("See you later!")
            done = True
        elif command_word in command_dictionary:
            try:
                command_dictionary[command_word](listOfContestants, command_parameters)
            except ValueError as ve:
                print(str(ve))
            except TypeError as te:
                print(str(te))
            except IndexError as ie:
                print(str(ie))
            except:
                print("There was an exception which was not handled!")
           # else:
               # print("no error")
        else:
            print("\nThis is not a command!")


def test_initial_contestants(listOfContestants):
    """
    Adds 10 contestants to the list at program startup
    """

    add_contestant_to_list(3, 8, 10, listOfContestants)
    add_contestant_to_list(5, 6, 5, listOfContestants)
    add_contestant_to_list(7, 5, 9, listOfContestants)
    add_contestant_to_list(8, 8, 6, listOfContestants)
    add_contestant_to_list(4, 2, 5, listOfContestants)
    add_contestant_to_list(3, 5, 7, listOfContestants)
    add_contestant_to_list(4, 8, 5, listOfContestants)
    add_contestant_to_list(8, 8, 8, listOfContestants)
    add_contestant_to_list(5, 7, 10, listOfContestants)
    add_contestant_to_list(6, 8, 4, listOfContestants)


start_command_ui()


# Test functions go here
#
# Test functions:
#   - no print / input
#   - great friends with assert

def test_split_command():
    command = '    aDd 5   10       7   '
    command_word, command_parameters = split_command(command)
    assert command_word == 'add'
    assert command_parameters == '5   10       7'

    command = 'eXit'
    command_word, command_parameters = split_command(command)
    assert command_word == 'exit'
    assert command_parameters == ''  # blank str for command with no parameters


def test_average_score_of_one_contestant():

    import math

    listOfContestants = []
    test_initial_contestants(listOfContestants)
    result = get_average_score_of_one_contestant(0,listOfContestants)
    assert math.floor(result) == 7


def test_add_contestant_to_list():
    listOfContestants =[]
    add_contestant_to_list(3, 8, 5, listOfContestants)
    assert listOfContestants[len(listOfContestants) - 1]['P1'] == 2
    assert listOfContestants[len(listOfContestants) - 1]['P2'] == 8
    assert listOfContestants[len(listOfContestants) - 1]['P3'] == 5

    add_contestant_to_list(11, 2, 6, listOfContestants)


def test_insert_new_contestant_at_given_position():
    listOfContestants =[]
    test_initial_contestants(listOfContestants)
    insert_new_contestant_at_given_position(1, 2, 3, 5, listOfContestants)
    assert listOfContestants[5]['P1'] == 1
    assert listOfContestants[5]['P2'] == 2
    assert listOfContestants[5]['P3'] == 2

    insert_new_contestant_at_given_position(2, 5, 4, -1, listOfContestants)
   


def test_remove_one_position():
    listOfContestants =[]
    test_initial_contestants(listOfContestants)
    remove_one_position(2, listOfContestants)
    assert listOfContestants[2]['P1'] == 0
    assert listOfContestants[2]['P2'] == 0
    assert listOfContestants[2]['P3'] == 0

    remove_one_position(-1, listOfContestants)

def test_remove_multiple_positions():
    listOfContestants =[]
    test_initial_contestants(listOfContestants)
    remove_multiple_positions(1, 2, listOfContestants)
    assert listOfContestants[1]['P1'] == 0
    assert listOfContestants[1]['P2'] == 0
    assert listOfContestants[1]['P3'] == 0
    assert listOfContestants[2]['P1'] == 0
    assert listOfContestants[2]['P2'] == 0
    assert listOfContestants[2]['P3'] == 0

    remove_multiple_positions(1, 0, listOfContestants)


def test_replace_oldGrade_with_newGrade():
    listOfContestants =[]
    test_initial_contestants(listOfContestants)
    replace_oldGrade_with_newGrade(0, 'P1', 5, listOfContestants)
    assert listOfContestants[0]['P1'] == 5

    replace_oldGrade_with_newGrade(0, 'P4', 5, listOfContestants)


#test_split_command()
#test_average_score_of_one_contestant()
#test_add_contestant_to_list()
#test_insert_new_contestant_at_given_position()
#test_remove_one_position()
#test_remove_multiple_positions()
#test_replace_oldGrade_with_newGrade()
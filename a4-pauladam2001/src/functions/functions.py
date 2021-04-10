"""
Functions that implement program features. They should call each other, or other functions from the domain
"""

from src.domain.entity import set_newValue, get_average_score_of_one_contestant, get_problem1_score, get_problem2_score, get_problem3_score


def add_contestant_to_list(gradeP1, gradeP2, gradeP3, listOfContestants):
    """
    Adds a contestant to the list of all contestants
    input: gradeP1 - grade for P1
           gradeP2 - grade for P2
           gradeP3 - grade for P3
           listOfContestants - the list of all contestants
    """

    if gradeP1 < 0 or gradeP1 > 10:
        raise ValueError("The grade must be an integer between 0 and 10!")
    if gradeP2 < 0 or gradeP2 > 10:
        raise ValueError("The grade must be an integer between 0 and 10!")
    if gradeP3 < 0 or gradeP3 > 10:
        raise ValueError("The grade must be an integer between 0 and 10!")

    listOfContestants.append({'P1': gradeP1, 'P2': gradeP2, 'P3': gradeP3})


def add_command(listOfContestants, command_parameters):
    """
    Handles the add command
    input: listOfContestants - the list of all contestants
           command_parameters - the parameters that were typed by the user
    """

    tokens = command_parameters.split()

    if len(tokens) != 3:
        raise ValueError("Invalid parameters to add a contestant!")

    problem1 = int(tokens[0])
    problem2 = int(tokens[1])
    problem3 = int(tokens[2])
    add_contestant_to_list(problem1, problem2, problem3, listOfContestants)

    return True


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
        

def insert_command(listOfContestants, command_parameters):
    """
    Handles the insert command
    input: listOfContestants - the list of all contestants
           command_parameters - the parameters that were typed by the user
    """

    tokens = command_parameters.split()

    if len(tokens) != 5:
        raise ValueError("Invalid parameters to insert a contestant!")

    problem1 = int(tokens[0])
    problem2 = int(tokens[1])
    problem3 = int(tokens[2])
    position = int(tokens[4])
    insert_new_contestant_at_given_position(problem1, problem2, problem3, position, listOfContestants)  #because tokens[3] == 'at'

    return True


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
    Removes contestants beggining with <startPosition> and ending with <finalPosition> (sets their scores to 0)
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


def remove_contestants_with_average_score_smaller_aNumber(conditionNumber, listOfContestants):
    """
    Sets the score of contestants with an average score smaller than <conditionNumber> 
    input: conditionNumber - the number typed by the user after the condition
           listOfContestants - the list of all contestants
    """

    for contestant in range(len(listOfContestants)):
        if get_average_score_of_one_contestant(contestant, listOfContestants) < conditionNumber:
            remove_one_position(contestant, listOfContestants)


def remove_contestants_with_average_score_greater_aNumber(conditionNumber, listOfContestants):
    """
    Sets the score of contestants with an average score greater than <conditionNumber> 
    input: conditionNumber - the number typed by the user after the condition
           listOfContestants - the list of all contestants
    """

    for contestant in range(len(listOfContestants)):
        if get_average_score_of_one_contestant(contestant, listOfContestants) > conditionNumber:
            remove_one_position(contestant, listOfContestants)


def remove_contestants_with_average_score_equal_aNumber(conditionNumber, listOfContestants):
    """
    Sets the score of contestants with an average score equal with <conditionNumber> 
    input: conditionNumber - the number typed by the user after the condition
           listOfContestants - the list of all contestants
    """

    for contestant in range(len(listOfContestants)):
        if get_average_score_of_one_contestant(contestant, listOfContestants) == conditionNumber:
            remove_one_position(contestant, listOfContestants)


def remove_contestants_by_condition(condition, conditionNumber, listOfContestants):
    """
    Handles the removes by condition
    input: condition - the condition typed by the user (<, > or =)
           conditionNumber - the number typed by the user after the condition
           listOfContestants - the list of all contestants
    """

    if condition == '<':
        remove_contestants_with_average_score_smaller_aNumber(conditionNumber, listOfContestants)
    elif condition == '>':
        remove_contestants_with_average_score_greater_aNumber(conditionNumber, listOfContestants)
    else:
        remove_contestants_with_average_score_equal_aNumber(conditionNumber, listOfContestants)


def remove_command(listOfContestants, command_parameters):
    """
    Handles the remove command
    input: listOfContestants - the list of all contestants
           command_parameters - the parameters that were typed by the user
    """

    tokens = command_parameters.split()
    if len(tokens) == 1:
        position = int(tokens[0])
        remove_one_position(position, listOfContestants)
    elif len(tokens) == 2:
        condition = tokens[0].strip()  #'<', '>', '='
        conditionNumber = int(tokens[1])
        remove_contestants_by_condition(condition, conditionNumber, listOfContestants)
    elif len(tokens) == 3:
        startPosition = int(tokens[0])
        finalPosition = int(tokens[2])
        remove_multiple_positions(startPosition, finalPosition, listOfContestants)   #because tokens[1] == 'to'
    else:
        raise ValueError("Invalid parameters to remove contestants!")

    return True


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

    #set_newValue(contestantNumber, problemNumber, newValue, listOfContestants)  #if we use this function undo will not work

    problem1Score = get_problem1_score(contestantNumber, listOfContestants)
    problem2Score = get_problem2_score(contestantNumber, listOfContestants)
    problem3Score = get_problem3_score(contestantNumber, listOfContestants)

    listOfContestants.pop(contestantNumber)             #for undo to work we need to pop the contestant from the index and insert it again with the new value, for the list to have another id

    if problemNumber == 'P1':
        insert_new_contestant_at_given_position(newValue, problem2Score, problem3Score, contestantNumber, listOfContestants)
    elif problemNumber == 'P2':
        insert_new_contestant_at_given_position(problem1Score, newValue, problem3Score, contestantNumber, listOfContestants)
    else:
        insert_new_contestant_at_given_position(problem1Score, problem2Score, newValue, contestantNumber, listOfContestants)


def replace_command(listOfContestants, command_parameters):
    """
    Handles the replace command
    input: listOfContestants - the list of all contestants
           command_parameters - the parameters that were typed by the user
    """

    tokens = command_parameters.split()

    if len(tokens) != 4:
        raise ValueError("Invalid parameters to replace the score of a contestant!")

    position = int(tokens[0])
    problem = tokens[1].upper()
    newValue = int(tokens[3])
    replace_oldGrade_with_newGrade(position, problem, newValue, listOfContestants)  #because tokens[2] == 'with'

    return True


def average_score_of_multiple_contestants(startPosition, finalPosition, listOfContestants):
    """
    Returns the average score of contestants beggining with <startPosition> and ending with <finalPosition>
    input: startPosition - the position from where we begin to calculate the average score of contestants
           finalPosition - the position where we stop calculating the average score of contestants
           listOfContestants - the list of all contestants
    """

    if startPosition < 0 or startPosition > len(listOfContestants) - 1 or startPosition > finalPosition:
        raise IndexError("The start position should be bigger than 0 and smaller than the final position which needs to be smaller than " + str(len(listOfContestants) - 1) + '!')
    if finalPosition < startPosition or finalPosition > len(listOfContestants) - 1:
        raise IndexError("The final position should be higher than " + str(startPosition) + " and smaller than " + str(len(listOfContestants) - 1) + '!')
    
    averageOfAverageScores = 0.00

    for contestant in range(startPosition, finalPosition + 1):
        averageOfAverageScores += get_average_score_of_one_contestant(contestant, listOfContestants)

    if startPosition == finalPosition:
        return averageOfAverageScores

    if startPosition != 0:
        averageOfAverageScores /= startPosition + finalPosition - 1
    else:
        averageOfAverageScores /= startPosition + finalPosition + 1

    return averageOfAverageScores


def lowest_average_score_of_multiple_contestants(startPosition, finalPosition, listOfContestants):
    """
    Returns the minimum average score for contestants between <startPosition> and <finalPosition>
    input: startPosition - the position from where we begin to calculate the minimum average score of contestants
           finalPosition - the position where we stop calculating the minimum average score of contestants
           listOfContestants - the list of all contestants
    """

    if startPosition < 0 or startPosition > len(listOfContestants) - 1 or startPosition > finalPosition:
        raise IndexError("The start position should be bigger than 0 and smaller than the final position which needs to be smaller than " + str(len(listOfContestants) - 1) + '!')
    if finalPosition < startPosition or finalPosition > len(listOfContestants) - 1:
        raise IndexError("The final position should be higher than " + str(startPosition) + " and smaller than " + str(len(listOfContestants) - 1) + '!')
    
    minimum = 10.00

    for contestant in range(startPosition, finalPosition + 1):
        minimum = min(minimum, get_average_score_of_one_contestant(contestant, listOfContestants))

    return minimum


def add_list_to_history(listOfContestants, historyOfLists):
    """
    Adds the listOfContestants to the historyOfLists
    input: listOfContestants - the list of all contestants 
           historyOfLists - the list were we keep all the modified lists of contestants
    """

    listOfContestantsInTuple = tuple(listOfContestants)  # tuples are immovable
    historyOfLists.append(listOfContestantsInTuple)
    listOfContestants = list(listOfContestants) # we make listOfContestants back to a list because tuples are immovable so we can't perform add/insert etc. on them
                    

def create_copy_of_list(list):
    """
    Returns the copy of a given list
    input: list - the list that wil pe copied
    """

    newList = []
    for index in range(len(list)):
        newList.append(list[index])

    return newList


def split_command(command):
    """
    Determines which command was typed by the user and the command's parameters
    input: command - user's command
    Return: the command typend and its parameters
    """

    tokens = command.strip().split(' ', 1)
    return tokens[0].strip().lower(), tokens[1].strip() if len(tokens) > 1 else ''


def initial_contestants(listOfContestants):
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
    initial_contestants(listOfContestants)
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
    initial_contestants(listOfContestants)
    insert_new_contestant_at_given_position(1, 2, 3, 5, listOfContestants)
    assert listOfContestants[5]['P1'] == 1
    assert listOfContestants[5]['P2'] == 2
    assert listOfContestants[5]['P3'] == 2

    insert_new_contestant_at_given_position(2, 5, 4, -1, listOfContestants)
   


def test_remove_one_position():
    listOfContestants =[]
    initial_contestants(listOfContestants)
    remove_one_position(2, listOfContestants)
    assert listOfContestants[2]['P1'] == 0
    assert listOfContestants[2]['P2'] == 0
    assert listOfContestants[2]['P3'] == 0

    remove_one_position(-1, listOfContestants)

def test_remove_multiple_positions():
    listOfContestants =[]
    initial_contestants(listOfContestants)
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
    initial_contestants(listOfContestants)
    replace_oldGrade_with_newGrade(0, 'P1', 5, listOfContestants)
    assert listOfContestants[0]['P1'] == 5

    replace_oldGrade_with_newGrade(0, 'P4', 5, listOfContestants)


def test_average_score_of_multiple_contestants():
    listOfContestants =[]
    initial_contestants(listOfContestants)
    averageOfAverageScores = average_score_of_multiple_contestants(0, 2, listOfContestants)
    assert round(averageOfAverageScores,2) == 6.44

    assert average_score_of_multiple_contestants(-1, 3, listOfContestants)


def test_lowest_average_score_of_multiple_contestants():
    listOfContestants =[]
    initial_contestants(listOfContestants)
    minimum = lowest_average_score_of_multiple_contestants(2, 5, listOfContestants)
    assert round(minimum,2) == 3.67

    assert lowest_average_score_of_multiple_contestants(3, 12, listOfContestants)


def test_remove_contestants_by_condition():
    listOfContestants =[]
    initial_contestants(listOfContestants)
    remove_contestants_by_condition('=', 5, listOfContestants)
    assert listOfContestants[5]['P1'] == 0
    assert listOfContestants[5]['P1'] == 0
    assert listOfContestants[5]['P1'] == 0


def test_add_list_to_history():
    listOfContestants = []
    initial_contestants(listOfContestants)
    historyOfLists = []
    add_list_to_history(listOfContestants, historyOfLists)
    add_list_to_history(listOfContestants, historyOfLists)
    assert len(historyOfLists) == 2
    assert historyOfLists[0] == tuple(listOfContestants)
    assert historyOfLists[1] == tuple(listOfContestants)



#test_split_command()
#test_average_score_of_one_contestant()
#test_add_contestant_to_list()
#test_insert_new_contestant_at_given_position()
#test_remove_one_position()
#test_remove_multiple_positions()
#test_replace_oldGrade_with_newGrade()
#test_average_score_of_multiple_contestants()
#test_lowest_average_score_of_multiple_contestants()
#test_remove_contestants_by_condition()
#test_add_list_to_history()

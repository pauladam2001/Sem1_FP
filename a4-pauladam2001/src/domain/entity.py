"""
Domain file includes code for entity management
entity = number, transaction, expense etc.
"""


def set_newValue(contestantNumber, problemNumber, newValue, listOfContestants):
    """
    Sets a new value for a given problem
    input: contestantNumber - the position of the contestant
           problemNumber - P1, P2 or P3
           newValue - the new value of "problemNumber"
           listOfContestants - the list of all contestants
    """

    listOfContestants[contestantNumber][problemNumber] = newValue


def get_average_score_of_contestants(listOfContestants):
    """
    Used to display the contestants sorted in decreasing order of average score
    input: listOfContestants - the list of all contestants
    """

    return float((listOfContestants['P1'] + listOfContestants['P2'] + listOfContestants['P3']) / 3)


def get_problem1(listOfContestants):
    """
    Used to display the contestants sorted in decreasing order of score from problem 1
    input: listOfContestants - the list of all contestants
    """

    return listOfContestants['P1']


def get_problem2(listOfContestants):
    """
    Used to display the contestants sorted in decreasing order of score from problem 2
    input: listOfContestants - the list of all contestants
    """

    return listOfContestants['P2']


def get_problem3(listOfContestants):
    """
    Used to display the contestants sorted in decreasing order of score from problem 3
    input: listOfContestants - the list of all contestants
    """

    return listOfContestants['P3']


def get_problem1_score(contestant, listOfContestants):
    """
    Returns the score for problem number 1
    input: contestant - the position/index of the contestant
           listOfContestants - the list of all contestants
    """

    return listOfContestants[contestant]['P1']


def get_problem2_score(contestant, listOfContestants):
    """
    Returns the score for problem number 2
    input: contestant - the position/index of the contestant
           listOfContestants - the list of all contestants
    """

    return listOfContestants[contestant]['P2']


def get_problem3_score(contestant, listOfContestants):
    """
    Returns the score for problem number 3
    input: contestant - the position/index of the contestant
           listOfContestants - the list of all contestants
    """

    return listOfContestants[contestant]['P3']


def get_average_score_of_one_contestant(contestant, listOfContestants):
    """
    Returns the average score of a contestant
    input: contestant - the index of the contestant
           listOfContestants - the list of all contestants
    """

    problem1 = get_problem1_score(contestant, listOfContestants)
    problem2 = get_problem2_score(contestant, listOfContestants)
    problem3 = get_problem3_score(contestant, listOfContestants)


    return float((problem1 + problem2 + problem3) / 3)

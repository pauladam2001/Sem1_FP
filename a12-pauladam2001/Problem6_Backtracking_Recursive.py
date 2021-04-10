"""
Generate all sequences of n parentheses that close correctly. Example: for n=4 there are two solutions: (()) and ()()
"""

def display(position, list):
    """
    Displays the actual list of parantheses that close correctly
    :param position: how many parantheses are in the list ('n' from the problem statement)
    :param list: the list of parantheses (0 for an open one, 1 for a closed one)
    """
    listOfParentheses = ''

    for index in range(0, position + 1):
        if list[index] == 0:                                    # 0 = '('    1 = ')'
            listOfParentheses = listOfParentheses + '('
        else:
            listOfParentheses = listOfParentheses + ')'
    print(listOfParentheses)

def valid(n, position, list):
    """
    Checks if the sequence of parantheses is valid or not
    :param n: the number of parantheses the sequence needs to contain (from the problem statement)
    :param position: how many parantheses are in the list
    :param list: the list of parantheses (0 for an open one, 1 for a close one)
    :return: 0 if the sequence is wrong, 1 otherwise
    """
    openParenthesisCounter = 0
    closedParenthesisCounter = 0

    if list[0] == 1:   # if the first paranthesis is a closed one then we don't need to go further
        return 0
    for index in range (0, position + 1):
        if list[index] == 0:
            openParenthesisCounter += 1
        else:
            closedParenthesisCounter += 1
    if openParenthesisCounter > n//2 or closedParenthesisCounter > n//2 or closedParenthesisCounter > openParenthesisCounter: # if the number of ')' is bigger than the number of '(' or the number or '(' or ')' is bigger than n/2 then we don't need to go further
        return 0            # there can never be more closed than open parentheses
    return 1

def backtracking_recursive(n, position, list):
    """
    Here we give values to the list (0 or 1 / open or closed paranthesis) and we check if the actual sequence is valid. If it is
    valid and it has length 'n' then we display it, otherwise we call the function recursively for the next position. If the
    sequence is not valid then we try to put the other paranthesis on the same position
    :param n: the number of parantheses the sequence needs to contain (from the problem statement)
    :param position: how many parantheses are in the list
    :param list: the list of parantheses (0 for an open one, 1 for a close one)
    """
    for index in range(0, 2):       # 0 = '('    1 = ')'
        list[position] = index
        if valid(n, position, list):
            if position == n - 1:
                display(position, list)
            else:
                backtracking_recursive(n, position + 1, list)

def main():
    n = input('n = ')  #the number of parantheses
    n = int(n)
    if n % 2 == 1:
        print('There are no solutions if n is odd!')
    else:
        list = [0 for i in range(n)]
        backtracking_recursive(n, 0, list)

main()

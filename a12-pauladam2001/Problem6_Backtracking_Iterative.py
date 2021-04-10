"""
Generate all sequences of n parentheses that close correctly. Example: for n=4 there are two solutions: (()) and ()()
"""

def display(position, list):
    """
    Displays the actual list of parantheses that close correctly
    :param position: how many parantheses are in the list ('n' from the problem statement)
    :param list: the list of parantheses (0 for an open one, 1 for a close one)
    """
    listOfParentheses = ''

    for index in range(0, position + 1):
        if list[index] == 0:                                    # 0 = '('    1 = ')'
            listOfParentheses = listOfParentheses + '('
        else:
            listOfParentheses = listOfParentheses + ')'
    print(listOfParentheses)

def get_succesor(index, list):
    """
    Decides what paranthesis is needed next. If there is no paranthesis in the current position (-1) we put an open one (0). If there is an
    open paranthesis we put a closed one (1). If there is a closed paranthesis we just return false because we have no more options
    :param index: the actual position in the list
    :param list: the list of parantheses (0 for an open one, 1 for a close one)
    :return: true if there is a succesor, false otherwise
    """
    if list[index] == -1:
        list[index] = 0
        return True
    elif list[index] == 0:
        list[index] = 1
        return True
    return False

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

def backtracking_iterative(n, list):
    """
    Here we compute the sequences of parantheses that close correctly using iterative backtracking. In the list: -1 means that we don't have
    any parantheses in that position, 0 means that we have an open paranthesis and 1 means that we have a closed one
    :param n:how many parantheses are in the list
    :param list: the list of parantheses (0 for an open one, 1 for a close one)
    """
    index = 0 # we use this to go through list and compute the solutions
    list.append(-1) # we increase the length of the list with 1
    while index > -1: # when the position will be smaller than 0 it means that we found all solutions
        succesor = True
        is_valid = False
        while succesor and not is_valid:
            succesor = get_succesor(index, list)
            if succesor: # we check if there is a succesor
                is_valid = valid(n, index, list)
        if succesor: # if a succesor exists then we check if we reached a solution
            if index == n - 1: # it means that we have a solution and we need to display it
                display(index, list)
            else:
                index = index + 1 # if we don't have a solution we go to the next position in the list
                list.append(-1) # increase the length of the list
        else:
            index = index - 1 # if there is no succesor we go again to the previous position
            list.pop() # we delete the last element from the list

def main():
    n = input('n = ')  #the number of parantheses
    n = int(n)
    if n % 2 == 1:
        print('There are no solutions if n is odd!')
    else:
        #list = [-1 for i in range(n)]
        list = []
        backtracking_iterative(n, list)

main()

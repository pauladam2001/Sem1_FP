# Source code for Test 1 program. Success!

def add_function_ui(commandsList, command_parameters):
    """
    Adds a given function, its parameters, and its result to the list of defined functions
    :param commandsList: the list of all functions
    :param command_parameters: the function name, its parameters and its result
    :return: -
    """
    functionName = command_parameters.split('(', 1)  #the name of the function
    parameters = functionName[1].split('=', 1)  #parameters[0]=function parameters, parameters[1]=function result
    commandsList.append({'Function name': functionName[0], 'Function parameters': parameters[0], 'Function result': parameters[1]})
    #print(commandsList)


def list_function_ui(commandsList, command_parameters):  #command_parameters=only the name of the function to list

    found = 0
    for index in range(len(commandsList)):
        if commandsList[index]['Function name'] == command_parameters:
            print('def ' + str(commandsList[index]['Function name']) + '(' + str(commandsList[index]['Function parameters']) + ': return ' +
                    str(commandsList[index]['Function result']))
            found = 1
    if found == 0:
        raise ValueError('The function was not defined yet!')

def eval_function_ui(commandsList, command_parameters):

    found = 0
    tokens = command_parameters.split('(', 1)  #tokens[0] = the function name, tokens[1] = the actual parameters
    for index in range(len(commandsList)):
        if tokens[0] == commandsList[index]['Function name']:
            numberOfParametersFunction = commandsList[index]['Function parameters'].split('+')
            numberOfActualParameters = tokens[1].split(',')
            if len(numberOfParametersFunction) == len(numberOfActualParameters):   #for example we can have add(a,b) and add(a,b,c) which are 2 different functions
                actualParameters = tokens[1].split(')')
                #for operation in actualParameters[0]:  #we change ',' with '+' in the actual parameters
                    #if actualParameters[0][operation] == ',':
                        #actualParameters[0][operation] = '+'    #not working yet
                exec(actualParameters) #?
                found =1
    if found == 0:
        raise TypeError('There was an error in the eval function!')


def split_command(command):

    tokens = command.strip().split(' ', 1)
    return tokens[0].strip().lower(), tokens[1].strip() if len(tokens) > 1 else ''  # tokens[0]=command, tokens[1]=parameters


def start_command_ui():

    commandsList = []

    done = False

    command_dictionary = {'add': add_function_ui, 'list': list_function_ui, 'eval': eval_function_ui}

    while not done:

        command = input("\ncommand: ").strip().lower()
        command_word, command_parameters = split_command(command)

        if "exit" == command_word:
            print("See you later!")
            done = True
        elif command_word in command_dictionary:
            try:
                command_dictionary[command_word](commandsList, command_parameters)
            except ValueError as ve:
                print(str(ve))
            except TypeError as te:
                print(str(te))
            except IndexError as ie:
                print(str(ie))
            except:
                print("There was an exception which was not handled!")
        else:
            print("\nThis is not a command!")


start_command_ui()
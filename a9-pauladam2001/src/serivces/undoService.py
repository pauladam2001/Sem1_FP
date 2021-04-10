
class UndoException(Exception):
    def __init__(self, message):
        self._message = message
    def __str__(self):
        return str(self._message)

class UndoService:

    def __init__(self):
        self._history = []
        self._index = -1

    def record(self, operation):
        """
        Records each operation
        :param operation: represents the undo/redo operation created for a specific function
        """
        self._history = self._history[0:self._index + 1]  # slicing []; a[m:n] returns the portion of a from index m to n (exclusive)

        self._history.append(operation)
        self._index += 1

    def undo(self):
        """
        Implement the undo functionality
        """
        if self._index == -1:
            raise UndoException('There are no operations to undo!')

        operation = self._history[self._index]
        operation.undo()
        self._index -= 1

    def redo(self):
        """
        Implement the redo functionality
        """
        if self._index + 1 == len(self._history):
            raise UndoException('There are no operations to redo!')

        self._index += 1
        operation = self._history[self._index]
        operation.redo()

    @staticmethod
    def create_new_update_operation(function_call, old_parameters, new_parameters):
        """
        With this function we create a new update operation
        :param function_call: will be the name of the update function
        :param old_parameters: the parameters before the change
        :param new_parameters: the parameterss after the change
        :return: the operation
        """
        undo_function = FunctionCall(function_call, *old_parameters)
        redo_function = FunctionCall(function_call, *new_parameters)
        return Operation(undo_function, redo_function)

    @staticmethod
    def create_new_add_operation(remove_call, remove_parameters, add_call, add_parameters):
        """
        With this function we create a new add operation
        :param remove_call: will be the name of the remove function
        :param remove_parameters: the parameters needed for remove
        :param add_call: will be the name of the add function
        :param add_parameters: the parameters needde for add
        :return: the operation
        """
        undo_function = FunctionCall(remove_call, *remove_parameters)
        redo_function = FunctionCall(add_call, *add_parameters)
        return Operation(undo_function, redo_function)

    @staticmethod
    def create_new_remove_operation(add_call, add_parameters, remove_call, remove_parameters):
        """
        With this function we create a new remove operation
        :param add_call: will be the name of the add function
        :param add_parameters: the parameters needed for add
        :param remove_call: will be the name of the remove function
        :param remove_parameters: the parameters needed for remove
        :return: the operation
        """
        undo_function = FunctionCall(add_call, *add_parameters)
        redo_function = FunctionCall(remove_call, *remove_parameters)
        return Operation(undo_function, redo_function)

    @staticmethod
    def transform_in_cascading_operation(*operations):
        """
        Function used to transform more operations into a cascading operations
        :param operations: the operations which need to be done simultaneously
        :return: the cascaded operation
        """
        return CascadedOperation(*operations)

    def add_cascading_operation(self, *operations):
        """
        Function to record a cascade operation
        :param operations: the operations which need to be done simultaneously
        """
        self.record(self.transform_in_cascading_operation(*operations))


class Operation:
    """
    How to undo/redo a program operation
    """
    def __init__(self, function_undo, function_redo):
        """
        Create an operation which consists of an undo function and a redo function for a function call
        :param function_undo: undo function
        :param function_redo: redo function
        """
        self._function_undo = function_undo
        self._function_redo = function_redo

    def undo(self):
        self._function_undo()

    def redo(self):
        self._function_redo()


class FunctionCall:
    """
    A function call with parameters
    """
    def __init__(self, function_name, *function_parameters):
        """
        :param function_name: the name of the function
        :param function_parameters: the parameters of the function that needs to be called
        """
        self._function_name = function_name
        self._function_parameters = function_parameters

    def call(self):
        """
        'Calling' the function with its specified parameters
        """
        self._function_name(*self._function_parameters)

    def __call__(self):
        self.call()


class CascadedOperation:
    """
    Represents a cascaded operation (where 1 user operation corresponds to more than 1 program operation)
    """
    def __init__(self, *operations):
        """
        :param operations: represents the cascade operations
        """
        self._operations = operations

    def undo(self):
        """
        Goes through all the operations that were created as cascade and undo them
        """
        for operation in self._operations:
            operation.undo()

    def redo(self):
        """
        Goes through all the operations that were created as cascade and redo them
        """
        for operation in self._operations:
            operation.redo()



class IterableDataObject:
    def __init__(self):
        self._data = []

    def get_all(self):
        return self._data

    def __iter__(self):
        self._position = 0
        return self

    def __next__(self):
        if self._position == len(self._data):
            raise StopIteration
        self._position += 1
        return self._data[self._position - 1]

    def __getitem__(self, item):
        return self._data[item]

    def __setitem__(self, key, value):
        self._data[key] = value

    def append(self, item):
        self._data.append(item)

    def __len__(self):
        return len(self._data)

    def __delitem__(self, key):
        del self._data[key]

    @staticmethod
    def gnome_sort(list, comparisonFunction):
        """
        Gnome Sort (also called Stupid sort) is based on the concept of a Garden Gnome sorting his flower pots. A garden gnome sorts the flower pots
        by the following method: - He looks at the flower pot next to him and the previous one; if they are in the right order he steps one pot forward,
                                   otherwise he swaps them and steps one pot backwards.
                                 - If there is no previous pot (he is at the starting of the pot line), he steps forwards; if there is no pot next to him
                                   (he is at the end of the pot line), he is done.
        :param list: the list that needs to be sorted
        :param comparisonFunction: a comparison function used to determine the order between 2 elements
        """
        index = 0
        length = len(list)
        while index < length:
            if index == 0:
                index = index + 1
            elif comparisonFunction(list[index], list[index - 1]):
                index = index + 1
            else:
                list[index], list[index - 1] = list[index - 1], list[index]
                index = index - 1

    @staticmethod
    def filter(list, acceptanceValue):
        """
        Filters the elements from the list
        :param list: the list that needs to be filtered
        :param acceptanceValue: an acceptance function that decides whether a given value passes the filter
        :return: the filtered list
        """
        filteredList = []

        for index in range(len(list)):
            if acceptanceValue(list[index]):
                filteredList.append(list[index])

        return filteredList

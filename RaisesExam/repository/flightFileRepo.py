from domain.flightEntity import Flight
import datetime

class FileError(Exception):
    def __init__(self, message):
        self._message = message

class FlightFileRepo:
    def __init__(self, file_name = 'input.txt'):
        self._file_name = file_name
        self._flightsList = []
        self.read()

    @property
    def getAll(self):
        return self._flightsList

    def __len__(self):
        return len(self._flightsList)

    def add(self, newFlight):
        """
        Adds a new flight to the list of flights if the flight is not in the list yet and if it has the correct data
        :param newFlight: the flight that will be added
        :return: nothing
        """
        self._flightsList.append(newFlight)

    def delete(self, identifier):
        for index in range(len(self._flightsList)):
            if identifier == self._flightsList[index].identifier:
                del self._flightsList[index]
                self.write()
                break


    def read(self):
        try:
            file = open(self._file_name, 'rt')
            content = file.readlines()
            file.close()

            for line in content:
                line = line.split(',')
                lastAttribute = line[4].split('\n')
                identifier = line[0]
                departure_city = line[1]
                departure_time = line[2].split(':')
                arrival_city = line[3]
                arrival_time = lastAttribute[0].split(':')
                self.add(Flight(identifier, departure_city, datetime.time(int(departure_time[0]), int(departure_time[1])), arrival_city, datetime.time(int(arrival_time[0]), int(arrival_time[1]))))

        except IOError as ioe:
            raise FileError('An error occurred!' + str(ioe))

    def write(self):
        try:
            file = open(self._file_name, 'wt')
            for flight in self._flightsList:
                line = flight.identifier + ',' + flight.departure_city + ',' + str(flight.departure_time) + ',' + flight.arrival_city + ',' + str(flight.arrival_time)
                file.write(line)
                file.write('\n')
            file.close()
        except Exception as e:
            raise FileError('An error occurred!' + str(e))

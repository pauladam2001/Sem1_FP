from domain.flightEntity import Flight, FlightException
import datetime

class FlightService:
    def __init__(self, flightFileRepo):
        self._flightRepo = flightFileRepo

    @property
    def getAll(self):
        return self._flightRepo.getAll

    def add(self, identifier, departure_city, departure_time, arrival_city, arrival_time):
        """
        Used to call the add function in the flights repository and the write functions which will re-write the flights in the text file
        :param identifier: the id of the flight that will be added
        :param departure_city: the departure city of the flight that will be added
        :param departure_time: the departure time of the flight that will be added
        :param arrival_city: the arrival city of the flight that will be added
        :param arrival_time: the arrival time of the flight that will be added
        :return: nothing
        """
        newFlight = Flight(identifier, departure_city, departure_time, arrival_city, arrival_time)
        if self.check_correct_parameters(newFlight) == True:
            self._flightRepo.add(newFlight)
            self._flightRepo.write()

    def delete(self, identifier):
        if self.check_existing_flight(identifier):
            self._flightRepo.delete(identifier)
            self._flightRepo.write()
        else:
            raise FlightException('The flight does not exist!')


    def check_existing_flight(self, identifier):
        for flight in self.getAll:
            if identifier == flight.identifier:
                return True
        return False

    def check_correct_parameters(self, newFlight):
        """
        Checks if the flight that needs to be added is correct
        :param newFlight: the flight that needs to be added
        :return: True if the flight has correct parameters, raises exception otherwise
        """
        for flight in self.getAll:
            if flight.identifier == newFlight.identifier:
                raise FlightException('Duplicated id!')
            if newFlight.departure_time == flight.departure_time and newFlight.departure_city == flight.departure_city:
                raise FlightException('Airport can handle a single operation!')
            if newFlight.departure_time == flight.arrival_time and newFlight.departure_city == flight.arrival_city:
                raise FlightException('Airport can handle a single operation!')
            if newFlight.arrival_time == flight.departure_time and newFlight. arrival_city == flight.departure_city:
                raise FlightException('Airport can handle a single operation!')
            if newFlight.arrival_time == flight.arrival_time and newFlight.arrival_city == flight.arrival_city:
                raise FlightException('Airport can handle a single operation!')
        return True

    def airports_activity(self):
        sortedListOfAirports = []
        listOfNames = []
        for flight in self.getAll:
            if flight.departure_city not in listOfNames:
                listOfNames.append(flight.departure_city)
            if flight.arrival_city not in listOfNames:
                listOfNames.append(flight.arrival_city)
        for name in listOfNames:
            counter = 0
            for flight in self.getAll:
                if name == flight.departure_city:
                    counter += 1
                if name == flight.arrival_city:
                    counter += 1

            sortedListOfAirports.append(AirportActivity(name, counter))

        sortedListOfAirports.sort(key = lambda airport: airport.activityNumber, reverse = True)
        return sortedListOfAirports

    def no_airborne(self):
        sortedListOfNoFlights = []
        copyOfList = self.getAll
        copyOfList.sort(key = lambda flight: flight.departure_time)

        for index in range(len(copyOfList) - 1):
            if copyOfList[index].arrival_time < copyOfList[index + 1].departure_time:
                t1 = datetime.timedelta(hours = copyOfList[index + 1].departure_time.hour, minutes = copyOfList[index + 1].departure_time.minute)
                t2 = datetime.timedelta(hours = copyOfList[index].arrival_time.hour, minutes=copyOfList[index].arrival_time.minute)
                no_airborne_time = t1 - t2
                sortedListOfNoFlights.append(no_airborne_time)

        sortedListOfNoFlights.sort(reverse = True)
        return sortedListOfNoFlights

    def max_airborne(self):
        listOfMaximumAirborne = []
        maximumTime = datetime.timedelta(hours = 0, minutes = 0)
        copyOfList = self.getAll
        copyOfList.sort(key=lambda flight: flight.departure_time)

        for index in range(len(copyOfList) - 1):
            j = index + 1
            while copyOfList[index].arrival_time > copyOfList[j].departure_time:
                j += 1
            if j != index + 1:
                t1 = datetime.timedelta(hours=copyOfList[index].departure_time.hour, minutes=copyOfList[index].departure_time.minute)
                t2 = datetime.timedelta(hours=copyOfList[j - 1].departure_time.hour, minutes=copyOfList[j - 1].departure_time.minute)
                airborne_time = t2 - t1
                if airborne_time == maximumTime:
                    timeInterval = str(copyOfList[index].departure_time) + ' - ' + str(copyOfList[j - 1].departure_time)
                    listOfMaximumAirborne.append(timeInterval)
                elif airborne_time > maximumTime:
                    maximumTime = airborne_time
                    listOfMaximumAirborne.clear()
                    timeInterval = str(copyOfList[index].departure_time) + ' - ' + str(copyOfList[j - 1].departure_time)
                    listOfMaximumAirborne.append(timeInterval)

        return listOfMaximumAirborne


class AirportActivity:
    def __init__(self, name, activityNumber):
        self._name = name
        self._activityNumber = activityNumber

    @property
    def name(self):
        return self._name

    @property
    def activityNumber(self):
        return self._activityNumber

    def __str__(self):
        return 'Airport name: ' + self._name + ', Number of departures and arrivals: ' + str(self._activityNumber)
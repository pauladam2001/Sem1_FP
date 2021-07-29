from validator.flightValidator import FlightValidator

class FlightException(Exception):
    def __init__(self, message):
        self._message = message

class Flight:
    def __init__(self, identifier, departure_city, departure_time, arrival_city, arrival_time):
        self._identifier = identifier
        self._departure_city = departure_city
        self._departure_time = departure_time
        self._arrival_city = arrival_city
        self._arrival_time = arrival_time

        if not FlightValidator.validate(self):
            raise FlightException('Invalid flight parameters!')

    @property
    def identifier(self):
        return self._identifier

    @property
    def departure_city(self):
        return self._departure_city

    @property
    def departure_time(self):
        return self._departure_time

    @property
    def arrival_city(self):
        return self._arrival_city

    @property
    def arrival_time(self):
        return self._arrival_time

    def __str__(self):
        return 'Id: ' + self._identifier + ', Departure city: ' + self._departure_city + ', Departure time: ' + str(self._departure_time) + ', Arrival city: ' + self.arrival_city + ', Arrival time: ' + str(self._arrival_time)

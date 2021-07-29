import datetime

class FlightValidator:
    @staticmethod
    def validate(flight):  #Unique ids, single operations are checked in repository
        if not isinstance(flight.identifier, str):
            return False
        if not isinstance(flight.departure_city, str):
            return False
        if not isinstance(flight.departure_time, datetime.time):
            return False
        if not isinstance(flight.arrival_city, str):
            return False
        if not isinstance(flight.arrival_time, datetime.time):
            return False
        t1 = datetime.timedelta(hours = flight.departure_time.hour, minutes = flight.departure_time.minute)
        t2 = datetime.timedelta(hours=flight.arrival_time.hour, minutes=flight.arrival_time.minute)
        flight_time = t2 - t1
        if flight_time > datetime.timedelta(hours = 1, minutes = 30) or flight_time < datetime.timedelta(hours = 0, minutes = 15):
            return False
        return True
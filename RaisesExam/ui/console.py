from domain.flightEntity import FlightException
from repository.flightFileRepo import FileError
import sys, datetime

class UI:
    def __init__(self, flightService):
        self._flightService = flightService

    @staticmethod
    def exit_ui():
        print('See you later!')
        sys.exit(0)

    def dispaly_flights(self):
        for flight in self._flightService.getAll:
            print(str(flight))

    def display_list_parameter(self, list):
        for element in list:
            print(str(element))

    def add_flight_ui(self):
        identifier = input('Flight id: ').strip()
        departure_city = input('Departure city: ').strip()
        departure_time = input('Departure time: ').strip()
        departure_time = departure_time.split(':')
        departure_time = datetime.time(int(departure_time[0]), int(departure_time[1]))
        arrival_city = input('Arrival city: ').strip()
        arrival_time = input('Arrival time: ').strip()
        arrival_time = arrival_time.split(':')
        arrival_time = datetime.time(int(arrival_time[0]), int(arrival_time[1]))
        self._flightService.add(identifier, departure_city, departure_time, arrival_city, arrival_time)

    def delete_flight_ui(self):
        identifier = input('Flight id: ').strip().upper()
        self._flightService.delete(identifier)

    def airports_deacreasing_order(self):
        self.display_list_parameter(self._flightService.airports_activity())

    def no_airborne_flights(self):
        self.display_list_parameter(self._flightService.no_airborne())

    def max_airborne_flights(self):
        self.display_list_parameter(self._flightService.max_airborne())

    def print_menu(self):
        print('\n\n')
        print('0. Exit')
        print('1. Display flights')
        print('2. Add flight')
        print('3. Delete flight')
        print('4. Airports in decreasing order of activity')
        print('5. Time intervals during which no flights are airborne in decreasing order of their length')
        print('6. Time intervals during which the maximum number of flights are airborne')
        print('\n\n')

    def start(self):
        menuItems = {'0': self.exit_ui, '1': self.dispaly_flights, '2': self.add_flight_ui, '3':self.delete_flight_ui, '4': self.airports_deacreasing_order, '5': self.no_airborne_flights, '6': self.max_airborne_flights}

        while True:
            self.print_menu()
            option = input('Enter an option: ').strip().lower()
            try:
                if option in menuItems:
                    menuItems[option]()
                else:
                    print('Invalid command!')
            except FileError as fe:
                print(str(fe))
            except FlightException as fle:
                print(str(fle))

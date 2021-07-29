import unittest, datetime
from service.flightService import FlightService, FlightException
from domain.flightEntity import Flight
from repository.flightFileRepo import FlightFileRepo

class TestService(unittest.TestCase):
    def setUp(self):
        pass

    def test_add(self):
        self._flightRepository = FlightFileRepo('input.txt')
        self._flightService = FlightService(self._flightRepository)
        newFlight = Flight('RO111', 'Medias', datetime.time(4, 00), 'Sibiu', datetime.time(4, 30))
        self.assertIs(self._flightService.check_correct_parameters(newFlight), True)
        self._flightService.add('RO111', 'Medias', datetime.time(4, 00), 'Sibiu', datetime.time(4, 30))
        self.assertEqual(self._flightRepository._flightsList[len(self._flightRepository._flightsList)], newFlight)
        newFlight = Flight('RO1231', 'Copsa', datetime.time(4, 00), 'Tarnava', datetime.time(4, 29))
        self.assertRaises(FlightException, self._flightService.check_correct_parameters(newFlight))


    def tearDown(self):
        pass
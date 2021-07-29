import unittest, datetime
from domain.flightEntity import Flight
from repository.flightFileRepo import FlightFileRepo

class TestRepository(unittest.TestCase):
    def setUp(self):
        pass

    def test_add(self):
        self._flightRepository = FlightFileRepo()
        oldLength = len(self._flightRepository.getAll)
        newFlight = Flight('RO111', 'Medias', datetime.time(4, 00), 'Sibiu', datetime.time(4, 30))
        self._flightRepository.add(newFlight)
        self.assertEqual(oldLength, len(self._flightRepository.getAll) + 1)

    def tearDown(self):
        pass
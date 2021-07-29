from repository.flightFileRepo import FlightFileRepo
from service.flightService import FlightService
from ui.console import UI

flightRepo = FlightFileRepo('input.txt')
flightService = FlightService(flightRepo)
ui = UI(flightService)

ui.start()

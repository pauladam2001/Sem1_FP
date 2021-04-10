from src.ui.console import userInterface
from src.repository.repositories import BookRepository, ClientRepository, RentalRepository
from src.serivces.service import BookService, ClientService, RentalService
from src.serivces.undoService import UndoService
from src.ui.GUI import GUI

bookrepository = BookRepository()
clientrepository = ClientRepository()
rentalrepository = RentalRepository(bookrepository.bookList, clientrepository.clientList)

undoservice = UndoService()

bookservice = BookService(bookrepository, rentalrepository, undoservice)
clientservice = ClientService(clientrepository, rentalrepository, undoservice)
rentalservice = RentalService(rentalrepository, bookservice, clientservice, undoservice)


#startCommand = userInterface(bookservice, clientservice, rentalservice, undoservice)
#startCommand.start_menu_ui()

startCommand = GUI(bookservice, clientservice, rentalservice, undoservice)
startCommand.start()

























#SAU puteam in clasa Rental sa transmitem toata cartea, nu doar id-ul, si tot clientul, nu doar id-ul.
#SAU in loc sa validam in domain puteam sa-l punem ca parametru in __init__ in service si sa validam in service
#SAU puteam face un repository in loc de 3 (nu era neaparat mai ok)

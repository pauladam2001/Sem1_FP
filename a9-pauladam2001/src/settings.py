from src.ui.console import userInterface
from src.repository.repositories import BookRepository, ClientRepository, RentalRepository
from src.repository.textRepositories import BookTextFileRepository, ClientTextFileRepository, RentalTextFileRepository
from src.repository.binaryFileRepositories import BinaryFileBookRepository, BinaryFileClientRepository, BinaryFileRentalRepository
from src.repository.JSONRepository import JSONFileBookRepository, JSONFileClientRepository, JSONFileRentalRepository
from src.serivces.service import BookService, ClientService, RentalService
from src.serivces.undoService import UndoService
from src.ui.GUI import GUI
from jproperties import Properties


class PropertiesConfig:
    """
    Here we check how to start the program (with which type of repository)
    """
    def __init__(self):
        """
        In __init__ we get all the necessary information or display the error and close the program if an error occurs
        """
        self._configs = Properties()
        self._file_name = 'settings.properties'

        settingsFile = open(self._file_name, 'rb')
        self._configs.load(settingsFile)

        try:
            self._repositoryType = self._configs.get("repository").data    # if we don't specifi .data there will be also a .meta
            self._bookRepositoryType = self._configs.get('books').data
            self._clientRepositoryType = self._configs.get('clients').data
            self._rentalRepositoryType = self._configs.get('rentals').data
            self._UIType = self._configs.get("ui").data
        except AttributeError as ke:
            print('There was an error in settings.properties! ' + str(ke))
            exit(0)

    def start_with_binary_repository(self):
        """
        If the program needs to be started with the binary file repository, then this function is called
        :return: the BinaryFileBookRepository, BinaryFileClientRepository and BinaryFileRentalRepository
        """
        bookRepository = BinaryFileBookRepository(self._bookRepositoryType)
        clientRepository = BinaryFileClientRepository(self._clientRepositoryType)
        rentalRepository = BinaryFileRentalRepository(bookRepository.bookList, clientRepository.clientList, self._rentalRepositoryType)
        return bookRepository, clientRepository, rentalRepository

    def start_in_memory(self):
        """
        If the program needs to be started in memory, then this function is called
        :return: the normal BookRepository, ClientRepository, RentalRepository
        """
        bookRepository = BookRepository()
        clientRepository = ClientRepository()
        rentalRepository = RentalRepository(bookRepository.bookList, clientRepository.clientList)
        bookRepository.initial_books()
        clientRepository.initial_clients()
        rentalRepository.initial_rentals()
        return bookRepository, clientRepository, rentalRepository

    def start_with_text_file_repository(self):
        """
        If the program needs to be started with the text file repository, then this function is called
        :return: the BookTextFileRepository, ClientTextFileRepository and RentalTextFileRepository
        """
        bookRepository = BookTextFileRepository(self._bookRepositoryType)
        clientRepository = ClientTextFileRepository(self._clientRepositoryType)
        rentalRepository = RentalTextFileRepository(bookRepository.bookList, clientRepository.clientList, self._rentalRepositoryType)
        return bookRepository, clientRepository, rentalRepository

    def start_with_json_file_repository(self):
        """
        If the program needs to be started with the JSON file repository, then this function is called
        :return: the BookJSONFileRepository, ClientJSONFileRepository and RentalJSONFileRepository
        """
        bookRepository = JSONFileBookRepository(self._bookRepositoryType)
        clientRepository = JSONFileClientRepository(self._clientRepositoryType)
        rentalRepository = JSONFileRentalRepository(bookRepository.bookList, clientRepository.clientList, self._rentalRepositoryType)
        return bookRepository, clientRepository, rentalRepository

    def start_program(self):
        """
        Here we see which are the program properties, then we call the start command or display the error and close the program if an error occurs
        """
        try:
            if self._repositoryType == 'binaryfiles' and self._bookRepositoryType == 'books.pickle' and self._clientRepositoryType == 'clients.pickle' and self._rentalRepositoryType == 'rentals.pickle':
                bookRepository, clientRepository, rentalRepository = self.start_with_binary_repository()
            if self._repositoryType == 'inmemory' and self._bookRepositoryType == '' and self._clientRepositoryType == '' and self._rentalRepositoryType == '':
                bookRepository, clientRepository, rentalRepository = self.start_in_memory()
            if self._repositoryType == 'textfiles' and self._bookRepositoryType == 'books.txt' and self._clientRepositoryType == 'clients.txt' and self._rentalRepositoryType == 'rentals.txt':
                bookRepository, clientRepository, rentalRepository = self.start_with_text_file_repository()
            if self._repositoryType == 'json' and self._bookRepositoryType == 'books.json' and self._clientRepositoryType == 'clients.json' and self._rentalRepositoryType == 'rentals.json':
                bookRepository, clientRepository, rentalRepository = self.start_with_json_file_repository()

            undoService = UndoService()
            bookService = BookService(bookRepository, rentalRepository, undoService)
            clientService = ClientService(clientRepository, rentalRepository, undoService)
            rentalService = RentalService(rentalRepository, bookService, clientService, undoService)

            if self._UIType == 'GUI':
                startCommand = GUI(bookService, clientService, rentalService, undoService)
                startCommand.start()

            if self._UIType == 'menu':
                startCommand = userInterface(bookService, clientService, rentalService, undoService)
                startCommand.start_menu_ui()
        except Exception as e:
            print('There was an error in the settings.properties! ' + str(e))

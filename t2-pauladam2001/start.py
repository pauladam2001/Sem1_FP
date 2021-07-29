from repository.fileRepository import TextFileRepository
from service.service import PlayerService
from ui.console import UI

repository = TextFileRepository()
service = PlayerService(repository)
ui = UI(service)

ui.start_menu()

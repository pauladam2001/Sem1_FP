"""
Assemble the program and start the user interface here
"""
from src.domain.entity import testFunctionsEntity
from src.services.service import testFunctionsService
from src.ui.console import userInterface

"""
testService = testFunctionsService()
testService.run_all_service_tests()

testEntity = testFunctionsEntity()
testEntity.run_all_entity_tests()
"""

startCommand = userInterface()
startCommand.start_command_ui()

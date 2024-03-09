import logging
from decimal import Decimal
from command import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class REPL:
    def __init__(self, calculator):
        self.calculator = calculator
        self.commands = {
            'add': AddCommand(calculator),
            'subtract': SubtractCommand(calculator),
            'multiply': MultiplyCommand(calculator),
            'divide': DivideCommand(calculator)
        }
        self.logger = logging.getLogger(__name__)

    def start(self):
        self.logger.info("Starting REPL...")
        while True:
            try:
                user_input = input("Enter operation and two numbers (e.g., add 2 3): ")
                command_parts = user_input.split()
                operation = command_parts[0]
                a = Decimal(command_parts[1])
                b = Decimal(command_parts[2])
                result = self.execute_command(operation, a, b)
                print(f"Result: {result}")
            except Exception as e:
                self.logger.error(f"Error: {e}")

    def execute_command(self, operation, a, b):
        if operation not in self.commands:
            raise ValueError("Invalid operation")
        return self.commands[operation].execute(a, b)

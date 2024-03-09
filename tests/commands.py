import logging
from decimal import Decimal

class Command:
    def __init__(self, calculator):
        self.calculator = calculator
        self.logger = logging.getLogger(__name__)

    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        pass

class AddCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return self.calculator.add(a, b)

class SubtractCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return self.calculator.subtract(a, b)

class MultiplyCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return self.calculator.multiply(a, b)

class DivideCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return self.calculator.divide(a, b)

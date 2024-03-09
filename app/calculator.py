from decimal import Decimal
from faker import Faker

fake = Faker()

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a: Decimal, b: Decimal) -> Decimal:
        result = a + b
        self.history.append((a, b, '+', result))
        return result

    def subtract(self, a: Decimal, b: Decimal) -> Decimal:
        result = a - b
        self.history.append((a, b, '-', result))
        return result

    def multiply(self, a: Decimal, b: Decimal) -> Decimal:
        result = a * b
        self.history.append((a, b, '*', result))
        return result

    def divide(self, a: Decimal, b: Decimal) -> Decimal:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append((a, b, '/', result))
        return result

    def clear_history(self):
        self.history.clear()

    def get_history(self):
        return self.history

    def generate_fake_data(self, num_records: int):
        for _ in range(num_records):
            a = fake.pydecimal(min_value=-100, max_value=100, positive=True)
            b = fake.pydecimal(min_value=-100, max_value=100, positive=True)
            operation = fake.random_element(elements=('add', 'subtract', 'multiply', 'divide'))
            expected = self.perform_operation(a, b, operation)
            yield a, b, operation, expected

    def perform_operation(self, a: Decimal, b: Decimal, operation: str) -> Decimal:
        if operation == 'add':
            return self.add(a, b)
        elif operation == 'subtract':
            return self.subtract(a, b)
        elif operation == 'multiply':
            return self.multiply(a, b)
        elif operation == 'divide':
            return self.divide(a, b)

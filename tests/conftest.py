import pytest
from calculator import Calculator

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=0, help="number of records to generate")

@pytest.fixture
def num_records(request):
    return request.config.getoption("--num_records")

@pytest.fixture
def generated_data(calculator, num_records):
    return calculator.generate_fake_data(num_records)

@pytest.fixture
def calculator():
    return Calculator()

def pytest_generate_tests(metafunc):
    if 'generated_data' in metafunc.fixturenames:
        data = metafunc.fixturenames
        metafunc.parametrize(data, metafunc.cls.generated_data(metafunc.config.option.num_records), indirect=True)

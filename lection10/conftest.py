import pytest
import datetime


@pytest.fixture(scope="class")
def time_class():
    print('Время начала выполнения класса с тестами {}'.format(datetime.datetime.now().strftime('%H:%M:%S')))
    yield
    print('Время окончания выполнения класса с тестами {}'.format(datetime.datetime.now().strftime('%H:%M:%S')))


@pytest.fixture()
def time_test(request):
    test_function_name = request.function.__name__
    start_test = datetime.datetime.now()
    yield
    end_test = datetime.datetime.now()
    time_length = end_test - start_test
    lead_time = time_length.total_seconds()
    print(f'\nВремя выполнения теста {test_function_name}: {lead_time} секунд\n')

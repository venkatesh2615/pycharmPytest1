import pytest
import requests


def pytest_addoption(parser):
    parser.addoption("--check", action="store_true", defult=False, help="Check and run")


@pytest.fixture(scope='class')
def response(request):
    request.cls.response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    return request.cls.response

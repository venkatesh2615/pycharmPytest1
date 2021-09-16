import pytest
import requests


@pytest.fixture()
def response():
    res = requests.get("https://www.google.com")
    print("Hello")
    return res


@pytest.fixture(params=[(3, 3, 6), (7, 7, 14)])
def passParam(request):
    return request.param

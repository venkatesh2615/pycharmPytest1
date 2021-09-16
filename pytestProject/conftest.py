import pytest
import requests


@pytest.fixture()
def response():
    res = requests.get("https://www.google.com")
    print("Hello")
    return res

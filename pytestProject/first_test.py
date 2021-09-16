import pytest
import requests


def test_sample():
    assert 9 + 1 == 10
    print("Success")


def test_res(response):
    if response.headers.get("Date"):
        print('\n--->')
        assert response.status_code == 200

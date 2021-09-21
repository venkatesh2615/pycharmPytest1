import json

import requests


def test_put_Res(response_put):
    put_data = json.loads(response_put.content)
    assert response_put.status_code == 200
    res = requests.get("https://reqres.in/api/users/2")

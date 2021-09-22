import pytest
import requests as requests

base_url = "https://reqres.in/"


@pytest.fixture(scope="function")
def response():
    return requests.get(f"{base_url}api/users?page=all")


# https://reqres.in/api/users?page=2
# https://reqres.in/api/users?page=2

@pytest.fixture(params=[("venkatesan", "python developer"), ("vikas", "sales lead")])
def response_post(request):
    name = request.param[0]
    job = request.param[1]
    return requests.post(f"{base_url}api/users", data={"name": {name}, "job": {job}})


@pytest.fixture()
def response_put():
    return requests.put(f"{base_url}api/user/2", data={"name": "venkatesan", "job": "python Developer"})


@pytest.fixture()
def delete_response():
    return requests.delete(f"{base_url}api/user/2")

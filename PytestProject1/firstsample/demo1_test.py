import json

import pytest


@pytest.mark.usefixtures('response')
class Test_demo:
    def test_response_code(self):
        assert self.response.status_code == 200


    def test_response_url(self):
        assert self.response.url == "https://jsonplaceholder.typicode.com/todos/"


    def test_response_data(self):
        data = json.loads(self.response.content)
        for i in data:
            if i.get('userId') == 8:
                print(i.get('title'))
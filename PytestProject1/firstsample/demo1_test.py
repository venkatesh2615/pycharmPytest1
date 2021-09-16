import pytest


@pytest.mark.usefixtures('response')
class Test_demo:
    def test_response_code(self):
        assert self.response.status_code == 200


    def test_response_url(self):
        assert self.response.url == "https://www.google.com/"

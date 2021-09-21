import json
import requests


def test_validateResponse(response):
    content_Data = json.loads(response.content)
    for row in content_Data.get("data"):
        if row.get('email') == "janet.weaver@reqres.in":
            assert "Janet" == row.get("first_name")
    assert response.status_code == 200


def test_validate_post(response_post):
    assert response_post.status_code == 201
    res = response_post
    post_data = json.loads(res.text)
    assert post_data.get("name") in ["venkatesan", "vikas"]
    get_response = requests.get("https://reqres.in/api/users/"+post_data.get("id"))

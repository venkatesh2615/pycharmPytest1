
def test_delete_res(delete_response):
    assert delete_response.status_code == 204

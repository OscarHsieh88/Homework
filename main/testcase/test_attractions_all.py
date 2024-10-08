import pytest

from comm.api_send import send_request
from comm.check_result import check_result
from comm.load_test_data import load_test_data

# Get test data
langs = load_test_data("langs.json")

@pytest.mark.parametrize("lang",langs)
def test_positive_case(lang):
    expect_result = 200

    # define params
    params = {
        "categoryIds": "12,13",
        "nlat": 24.98,
        "elong": 121.51,
        "page": 1
    }
    
    response = send_request(lang, "Attractions/All", params)
    data = response.json().get('data', [])
    if len(data) > 0:
        for item in data:
            assert "id" in item, "no 'id' found in data"
            assert "name" in item, "no 'name' found in data"

    # verify status code
    check_result(expect_result, response.status_code)

def test_negative_case_with_wrong_type_params(lang):
    expect_result = 400

    # define params
    params = {
        "categoryIds": "12,13",
        "nlat": "abc",
        "elong": 121.51,
        "page": 1
    }

    response = send_request(lang, "Attractions/All", params)

    # verify status code
    check_result(expect_result, response.status_code)

def test_negative_case_with_empty_params():
    expect_result = 400

    # define params
    params = {
        "categoryIds": "12,13",
        "nlat": 24.98,
        "elong": 121.51,
        "page": 1
    }

    response = send_request("", "Attractions/All", params)

    # verify status code
    check_result(expect_result, response.status_code)

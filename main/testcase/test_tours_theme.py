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
        "page": 1
    }
    
    response = send_request(lang, "Tours/Theme", params)
    data = response.json().get('data', [])
    if len(data) > 0:
        for item in data:
            assert "category" in item, "no 'category' found in data"

    # verify status code
    check_result(expect_result, response.status_code)

def test_negative_case_with_wrong_type_params():
    expect_result = 400
    
    # define params
    params = {
        "categoryIds": "12,13",
        "page": 1
    }

    response = send_request("abc","Tours/Theme", params)

    # verify status code
    check_result(expect_result, response.status_code)

def test_negative_case_with_empty_params():
    expect_result = 404

    # define params
    params = {
        "categoryIds": "12,13",
        "page": 1
    }

    response = send_request("", "Tours/Theme", params)

    # verify status code
    check_result(expect_result, response.status_code)
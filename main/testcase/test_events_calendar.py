import pytest

from comm.api_send import send_request
from comm.check_result import check_result

# Get test data
langs = ["zh-tw", "zh-cn", "en"]

@pytest.mark.parametrize("lang",langs)
def test_positive_case(lang):
    expect_result = 200

    # define params
    params = {
        "categoryId": "12",
        "bdgin": "2020-02-02",
        "end": "2021-02-02",
        "page": 1
    }
    
    response = send_request(lang, "Events/Calendar", params)
    data = response.json().get('data', [])
    if len(data) > 0:
        for item in data:
            assert "begin" in item, "no 'begin' found in data"
            assert "end" in item, "no 'end' found in data"

    # verify status code
    check_result(expect_result, response.status_code)

def test_negative_case_with_wrong_type_params():
    expect_result = 400

    # define params
    params = {
        "categoryId": "12",
        "bdgin": "2020-02-02",
        "end": "2021-02-02",
        "page": 1
    }

    response = send_request("abc","Events/Calendar", params)

    # verify status code
    check_result(expect_result, response.status_code)

def test_negative_case_with_empty_params():
    expect_result = 404

    # define params
    params = {
        "categoryId": "12",
        "bdgin": "2020-02-02",
        "end": "2021-02-02",
        "page": 1
    }

    response = send_request("", "Events/Calendar", params)

    # verify status code
    check_result(expect_result, response.status_code)
import requests

def send_request(lang, endpoint, params):
    base_url = "https://www.travel.taipei/open-api"
    request_url = f"{base_url}/{lang}/{endpoint}"

    headers = {
        "Accept": "application/json",
        "Accept-Charset": "utf-8",
        'Content-Type': 'application/json'
    }

    result = requests.get(request_url, headers=headers, params=params)
    return result

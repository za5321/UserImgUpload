from Config.config import Config


def get_url(flag):
    return Config().get_config_send(flag)


def send(encoding: str) -> str:
    import requests
    import json

    url = get_url("url_dev")

    headers = {"Content-Type": "application/json; charset=utf-8"}
    data = {
        "ssopublickey": encoding
    }
    response = requests.post(url, json=json.dumps(data), headers=headers, timeout=5)
    return response.json()["statuscode"]


def response_status(code: str) -> tuple:
    if code == "202211":
        return True, code
    return False, code

from Config.config import Config


def get_url(flag):
    return Config().get_config_send(flag)


def send(encoding: str) -> str:
    import requests

    url_dev = get_url("url_dev")
    url_real = get_url("url_real")

    headers = {"Content-Type": "application/json; charset=utf-8"}
    data = {
        "ssopublickey": encoding
    }
    response = requests.post(url_real, json=data, headers=headers, timeout=5)
    return response.json()["statuscode"]


def response_status(code: str) -> bool:
    if code == "202211":
        return True
    return False

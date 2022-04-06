from Config.config import Config


def get_url(flag):
    return Config().get_config_send(flag)


def send(data: str) -> str:
    import requests
    from Func.Crypt import Crypt

    url = get_url("url_dev")
    headers = {"Content-Type": "text/plain; charset=utf-8"}
    response = requests.post(url, data=data, headers=headers, timeout=5)

    return Crypt().decrypt_MOIN(response.text)


def response_status(code: str) -> tuple:
    if code == "202211":
        return True, code
    return False, code

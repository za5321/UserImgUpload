from Config.config import Config


def get_url(flag):
    return Config().get_config_send(flag)


def send(data: dict):
    import requests

    url_dev = get_url("url_dev")
    url_real = get_url("url_real")

    headers = {"Content-Type": "application/json; charset=utf-8"}
    # response = requests.post(url_real, json=data, headers=headers, timeout=5)
    # response.json()
    # 파싱해서 응답코드 받아서 처리
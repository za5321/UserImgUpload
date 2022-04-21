def send(url: str, data: str) -> str:
    import requests

    headers = {"Content-Type": "text/plain; charset=utf-8"}
    response = requests.post(url, data=data, headers=headers, timeout=5)
    return response.text

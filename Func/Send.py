def send(url: str, data: str) -> str:
    import requests
    from Func.Crypt import Crypt
    import json

    headers = {"Content-Type": "text/plain; charset=utf-8"}
    response = requests.post(url, data=data, headers=headers, timeout=5)
    #dec = Crypt().decrypt_MOIN(response.text)
    return response.text

    #return json.loads(data)["statuscode"]
def get_requestkey() -> str:
    from Config.config import Config
    return Config().get_config_data("requestkey")


def get_utc() -> str:
    from datetime import datetime
    return datetime.utcnow().strftime("%Y%m%d%H%M%S")


def get_accesstoken():
    from Func.Crypt import Crypt
    return Crypt().encrypt_MOIN(get_requestkey()+'/#/'+get_utc())


def get_send_data():
    pass

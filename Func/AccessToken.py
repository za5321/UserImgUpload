from Func.Crypt import Crypt

c = Crypt()


def get_requestkey() -> str:
    from Config.config import Config
    return Config().get_config_data("requestkey")


def get_utc() -> str:
    from datetime import datetime
    return datetime.utcnow().strftime("%Y%m%d%H%M%S")


def get_accesstoken():
    #return 암호화ㅏㅏㅏ(get_requestkey()+'/#/'+get_utc())
    pass


def get_send_data():
    pass
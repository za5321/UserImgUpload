def get_requestkey() -> str:
    from Config.config import Config
    return Config().get_config_data("requestkey")


def get_utc() -> str:
    import datetime
    #return datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
    return (datetime.datetime.utcnow() - datetime.timedelta(minutes=3)).strftime("%Y%m%d%H%M%S")


def get_accesstoken():
    from Func.Crypt import Crypt

    key = get_requestkey()
    utc = get_utc()
    return Crypt().encrypt_MOIN(key+'/#/'+utc)

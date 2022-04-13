import argparse
import json
from Config.config import Config
from Func.Employee import Employee
from Func.Data import Data
from Func.File import File
from Func.Crypt import Crypt
from Func.Logger import Logger
from Func import Send

conf = Config()
c = Crypt()
l = Logger()
logger = l.logger
l.set_handler()


def img():
    logger.info("Start getting Employee list")
    employees: dict = Employee().get_employees()

    for emp_no, name in employees.items():
        file_name = emp_no + '.jpg'
        logger.info(f"사번: {emp_no}, 이름: {name}, 파일명: {file_name}")

        logger.info(f"Start getting profile image::{emp_no}")
        file = File().get_imagebinary(file_name)
        if not file:
            logger.error(f"No such file::{file_name}")
            continue

        plain: dict = Data().get_data(emp_no, name, file)
        logger.info("Start encryption")
        encrypted = c.encrypt_MOIN(str(plain))

        logger.info(f"Start sending profile image to MOIN::{file_name}")
        url = conf.get_config_send("url")
        decrypted = c.decrypt_MOIN(Send.send(url, str(encrypted)))

        response_code = json.loads(decrypted)["statuscode"]
        if response_code == "202211":
            logger.info(f"Finished sending profile image to MOIN::{file_name}")
            continue
        else:
            logger.error(f"Failed to send profile image to MOIN::{response_code}")
        continue
    c.shutdown()


def key():
    import requests

    logger.info("Start getting request key from MOIN")

    url = conf.get_config_accesstoken("url")
    rid = conf.get_config_accesstoken("rid")
    loginid = conf.get_config_accesstoken("loginid")
    pwd = conf.get_config_accesstoken("pwd")

    plain = {
        "rid": rid,
        "loginid": loginid,
        "pwd": pwd
    }

    encrypted = c.encrypt_MOIN(str(plain))
    decrypted = c.decrypt_MOIN(Send.send(url, str(encrypted)))

    response = json.loads(decrypted)
    response_code = response["statuscode"]
    request_key = response["requestkey"]
    if response_code == "201200":
        logger.info(f"Finished getting request key from MOIN::{request_key}")
    else:
        logger.error(f"Failed to get request key from MOIN::{response_code}")
    c.shutdown()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--api', choices=['img', 'key'], default='img', help='To decide which api to call (img/key)')
    args = parser.parse_args()

    if args.api == 'img':
        img()
    elif args.api == 'key':
        key()

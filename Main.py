import argparse


def img():
    from Func.Employee import Employee
    from Func.Data import Data
    from Func.File import File
    from Func.Crypt import Crypt
    from Func.Logger import Logger
    from Func import Send

    l = Logger()
    logger = l.logger
    l.set_handler()

    c = Crypt()

    logger.info("START GETTING EMPLOYEE LIST")
    employees: dict = Employee().get_employees()
    logger.info("FINISHED GETTING EMPLOYEE LIST")

    for emp_no, name in employees.items():
        file_name = emp_no + '.jpg'
        logger.info(f"사번: {emp_no}, 이름: {name}, 파일명: {file_name}")

        logger.info("START GETTING IMAGE FILE")
        file = File().get_imagebinary(file_name)
        if not file:
            logger.error(f"{file_name} 파일이 없습니다.")
            continue
        logger.info("FINISHED GETTING IMAGE FILE")

        plain: dict = Data().get_data(emp_no, name, file)
        logger.info("START ENCRYPTION")
        encrypted = c.encrypt_MOIN(str(plain))
        logger.info("FINISHED ENCRYPTION")

        logger.info("START SENDING DATA TO MOIN")
        response = Send.response_status(Send.send(str(encrypted)))
        print(response[1], type(response[1]))
        if response[0]:
            logger.info("FINISHED SENDING DATA TO MOIN")
            continue
        else:
            logger.error(f"FAILED TO SEND DATA TO MOIN::{response[1]}")
            continue
    c.shutdown()


def key():
    from Func.Crypt import Crypt
    from Func.Logger import Logger
    from Config.config import Config
    import requests

    l = Logger()
    logger = l.logger
    l.set_handler()

    logger.info("START GETTING REQUEST KEY FROM MOIN")

    c = Config()
    url = c.get_config_accesstoken("url")
    rid = c.get_config_accesstoken("rid")
    loginid = c.get_config_accesstoken("loginid")
    pwd = c.get_config_accesstoken("pwd")

    headers = {"Content-Type": "text/plain; charset=utf-8"}
    plain = {
        "rid": rid,
        "loginid": loginid,
        "pwd": pwd
    }

    crypt = Crypt()
    encrypted = crypt.encrypt_MOIN(str(plain))
    response = requests.post(url, data=encrypted, headers=headers, timeout=5)
    Crypt().decrypt_MOIN(response.text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--api', choices=['img', 'key'], default='img', help='To decide which api to call (img/key)')
    args = parser.parse_args()

    if args.api == 'img':
        img()
    #elif args.api == 'key':
    #    key()

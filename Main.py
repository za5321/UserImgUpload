from Func.Employee import Employee
from Func.Data import Data
from Func.File import File
from Func.Crypt import Crypt
from Func.Logger import Logger
from Func import Send


if __name__ == "__main__":
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
        if response[0]:
            logger.info("FINISHED SENDING DATA TO MOIN")
            continue
        else:
            logger.error(f"FAILED TO SEND DATA TO MOIN::{response[1]}")
            continue
    c.shutdown()

from Func.Employee import Employee
from Func.Data import Data
from Func.File import File
from Func.Crypt import Crypt
from Func import Send


if __name__ == "__main__":
    employees: dict = Employee().get_employees()

    for emp_no, name in employees.items():
        file_name = emp_no + '.jpg'
        plain: dict = Data().get_data(emp_no, name, File().get_imagebinary(file_name))
        encrypted = Crypt().encrypt_TDES(str(plain))
        Crypt().shutdown()

        if Send.response_status(Send.send(encrypted)):
            continue
        else:
            print("error")

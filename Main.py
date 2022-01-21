'''
1. DB > 사번:이름 딕셔너리
2. 딕셔너리 돌면서
- 파일명: 사번+jpg로 hex 받기
- 사번, 이름, hex > Data > json
- 전송
'''
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
        print(plain)
        print(Crypt().encrypt_TDES(str(plain)))
        Crypt().shutdown()

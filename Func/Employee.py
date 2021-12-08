class Employee:
    def __init__(self):
        self.employees = {}

    @staticmethod
    def get_config(flag: str):
        from Config.config import Config
        return Config().db_connection() if flag == 'db' \
            else Config().get_config_employee(flag)

    def set_employees(self):
        self.con = self.get_config('db')
        cursor = self.con.cursor()

        #sql = f"SELECT USERID, USERNAME FROM M_MEMBER WITH(NOLOCK) WHERE LEFT(USERID,1) IN {self.get_config('filter')}"
        sql = "SELECT USERID, USERNAME FROM M_MEMBER WHERE USERID = 'L23113'"
        cursor.execute(sql)
        row = cursor.fetchone()
        while row:
            self.employees[row[0]] = row[1]
            row = cursor.fetchone()

    def get_employees(self) -> dict:
        self.set_employees()
        return self.employees


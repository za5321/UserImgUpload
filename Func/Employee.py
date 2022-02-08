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

        sql = self.get_config('sql')
        cursor.execute(sql)
        row = cursor.fetchone()
        while row:
            self.employees[row[0]] = row[1]
            row = cursor.fetchone()

    def get_employees(self) -> dict:
        self.set_employees()
        return self.employees

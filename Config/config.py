import json


class Config:
    def __init__(self):
        with open('Config\\config.json', 'r', encoding='UTF-8') as file:
            self.conf = json.load(file)

    def db_connection(self):
        import pymssql
        import decimal
        return pymssql.connect(self.conf['Database']['ip'], self.conf['Database']['id'],
                               self.conf['Database']['password'], self.conf['Database']['name'])

    def get_config_employee(self, flag: str):
        return self.conf['Employee'][flag]

    def get_config_data(self, flag: str):
        return self.conf['Data'][flag]

    def get_config_file(self, flag: str):
        return self.conf['File'][flag]

    def get_config_send(self, flag: str):
        return self.conf['Send'][flag]

    def get_config_accesstoken(self, flag: str):
        return self.conf['AccessToken'][flag]

    def get_config_datecheck(self, flag: str):
        return self.conf['DateCheck'][flag]

    def logging(self, flag: str):
        return self.conf["Logging"][flag]

class Data:
    def __init__(self):
        self.accesstoken = self.get_accesstoken()
        self.companyid = self.get_config('companyid')

        self.data = {
            "accesstoken": self.accesstoken,
            "companyid": self.companyid,
            "empnum": "",
            "name": "",
            "imagebinary": ""
        }

    @staticmethod
    def get_config(flag:str):
        from Config.config import Config
        return Config().get_config_data(flag)

    @staticmethod
    def get_accesstoken():
        from Func import AccessToken
        return AccessToken.get_accesstoken()

    def set_data(self, emp_no: str, name: str, image: str):
        self.data["empnum"] = emp_no
        self.data["name"] = name
        self.data["imagebinary"] = image

    def get_data(self, emp_no: str, name: str, image: str):
        self.set_data(emp_no, name, image)
        return self.data

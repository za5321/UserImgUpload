from datetime import datetime, timedelta


class File:
    def __init__(self, file: str):
        self.path = self.get_file_path()
        self.check = self.get_datecheck()
        self.file = self.path + file

    @staticmethod
    def get_file_path():
        from Config.config import Config
        return Config().get_config_file('path')

    @staticmethod
    def get_datecheck():
        from Config.config import Config
        return Config().get_config_datecheck('date')

    def file_date_check(self):
        import os.path

        check_date = datetime.now() - timedelta(days=self.check)
        try:
            file_date = datetime.fromtimestamp(os.path.getmtime(self.file))
            if file_date < check_date:
                return False
            return True
        except FileNotFoundError:
            return -1

    def get_imagebinary(self):
        import binascii
        import cv2
        import numpy as np

        img = cv2.imread(self.file)

        # Image Compression
        img = cv2.resize(img, (80, 96), interpolation=cv2.INTER_AREA)
        params = [cv2.IMWRITE_JPEG_QUALITY, 80]
        msg = cv2.imencode(".jpg", img, params)[1]
        msg = (np.array(msg)).tobytes()

        bin_val = binascii.hexlify(msg)
        return bin_val.decode('utf8')

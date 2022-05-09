import cv2
import numpy as np
import os.path, time
import datetime

class File:
    def __init__(self):
        self.path = self.get_file_path()
        self.check = self.get_datecheck()

    @staticmethod
    def get_file_path():
        from Config.config import Config
        return Config().get_config_file('path')

    def get_datecheck(self):
        from Config.config import Config
        return Config().get_config_datecheck('date')

    '''def get_imagebinary(self, file: str) -> str:
        imagebinary = []
        file = self.path + file
        try:
            with open(file, 'rb') as f:
                bin_val = f.read(1)
                while bin_val:
                    hex_val = str(hex(ord(bin_val))).replace('0x', '').zfill(2)
                    imagebinary.append(hex_val)
                    bin_val = f.read(1)
                f.close()
            return " ".join(imagebinary)
        except FileNotFoundError:
            return ""
    '''

    def get_imagebinary(self, file:str):
        import binascii
        file = self.path + file

        check = int(self.check)
        now_date = datetime.datetime.now()
        check_date = now_date - datetime.timedelta(days=check)

        check_date = check_date.strftime('%Y/%m/%d')

        try:
            file_date = time.strftime('%Y/%m/%d',time.gmtime(os.path.getmtime(file)))
        except FileNotFoundError:
            return ""

        formatted_check_date = time.strptime(check_date, '%Y/%m/%d')
        formatted_file_date = time.strptime(file_date, '%Y/%m/%d')

        if formatted_check_date > formatted_file_date:
            return "dont_update"

        img = cv2.imread(file)

        if img is None:
            return ""

        # Image Compression
        img = cv2.resize(img, (80, 96), interpolation=cv2.INTER_AREA)
        params = [cv2.IMWRITE_JPEG_QUALITY, 80]
        msg = cv2.imencode(".jpg", img, params)[1]
        msg = (np.array(msg)).tobytes()
        #print(len(msg))
        bin_val = binascii.hexlify(msg)
        #print(len(bin_val))
        return bin_val.decode('utf8')
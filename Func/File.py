class File:
    def __init__(self):
        self.path = self.get_file_path()

    @staticmethod
    def get_file_path():
        from Config.config import Config
        return Config().get_config_file('path')

    def get_imagebinary(self, file: str) -> str:
        imagebinary = []
        file = self.path + file
        try:
            with open(file, 'rb') as f:
                bin_val = f.read(1)
                while bin_val:
                    hex_val = str(hex(ord(bin_val))).replace('0x', '').zfill(2)
                    imagebinary.append(hex_val)
                    bin_val = f.read(1)
            return " ".join(imagebinary)
        except FileNotFoundError:
            return ""

import jpype


class Crypt:
    def __init__(self):
        self.classpath = ['./Lib/crypt-example.jar', './Lib/crypt-example.jar']
        if not self.is_JVM_started():
            jpype.startJVM('-ea', classpath=self.classpath, convertStrings=True)
            self.config()

    @staticmethod
    def config():
        config_pkg = jpype.JPackage('crypt-example')
        conf = config_pkg.Config.init('./Config/conf.xml')

    def encrypt_MOIN(self, data: str) -> str:
        crypt_pkg = jpype.JPackage('crypt-example')
        cc = crypt_pkg.Crypt()
        cc.init()

        return cc.getInstance("crypt-example").encrypt(data)

    def decrypt_MOIN(self, data) -> str:
        crypt_pkg = jpype.JPackage('crypt-example')
        cc = crypt_pkg.Crypt()
        cc.init()
        return cc.getInstance("crypt-example").decrypt(data)

    @staticmethod
    def shutdown():
        jpype.shutdownJVM()

    @staticmethod
    def is_JVM_started():
        return jpype.isJVMStarted()

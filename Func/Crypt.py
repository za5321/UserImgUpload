import jpype


class Crypt:
    def __init__(self):
        self.classpath = ['./Lib/crypto-example.jar', './Lib/crypto-example.jar']
        if not self.is_JVM_started():
            jpype.startJVM('-ea', classpath=self.classpath)
            self.config()

    @staticmethod
    def config():
        config_pkg = jpype.JPackage('nets.af.common.conf')
        conf = config_pkg.Config.init('./Config/conf.xml')

    def encrypt_MOIN(self, data: str) -> str:
        crypt_pkg = jpype.JPackage('nets.af.common.crypt')
        cc = crypt_pkg.Crypt()
        cc.init()

        return cc.getInstance("crypto-example").encrypt(data)

    def encrypt_TDES(self, data: str) -> str:
        crypt_pkg = jpype.JPackage('nets.af.common.crypt')
        cc = crypt_pkg.Crypt()
        cc.init()

        return cc.getInstance("crypto-example").encrypt(data)

    @staticmethod
    def shutdown():
        jpype.shutdownJVM()

    @staticmethod
    def is_JVM_started():
        return jpype.isJVMStarted()

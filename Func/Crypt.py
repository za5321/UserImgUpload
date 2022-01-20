import jpype


class Crypt:
    def __init__(self):
        self.classpath = ['./Lib/nets-af.jar', './Lib/MagicJCrypto-v2.0.0.0.jar']
        jpype.startJVM('-ea', classpath=self.classpath)

    @staticmethod
    def config():
        config_pkg = jpype.JPackage('nets.af.common.conf')
        conf = config_pkg.Config.init('./Config/conf.xml')

    @staticmethod
    def encrypt_MOIN(data: str) -> str:
        crypt_pkg = jpype.JPackage('nets.af.common.crypt')
        cc = crypt_pkg.Crypt()
        cc.init()

        return cc.getInstance("ex-ws-moin").encrypt(data)

    @staticmethod
    def encrypt_TDES(data: str) -> str:
        crypt_pkg = jpype.JPackage('nets.af.common.crypt')
        cc = crypt_pkg.Crypt()
        cc.init()

        return cc.getInstance("TripleDES").encrypt(data)

    @staticmethod
    def shutdown():
        jpype.shutdownJVM()

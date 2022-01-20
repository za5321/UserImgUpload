filename = 'D:\\test\\L23113.jpg'
path = "D:\\test\\"


def get_url(flag):
    from Config.config import Config
    return Config().get_config_send(flag)


def img_to_hex(file):
    string = []
    with open(file, 'rb') as f:
        bin_val = f.read(1)
        while bin_val:
            hex_val = str(hex(ord(bin_val))).replace('0x', '').zfill(2)
            string.append(hex_val)
            bin_val = f.read(1)
    return " ".join(string)


def get_empno_all():
    import os
    os.chdir(path)

    for i in next(os.walk(path))[2]:
        if i[0] != '2' or i[0] != '-':
            print(get_imagebinary(i))


def get_imagebinary(file: str) -> str:
    imagebinary = []
    file = path + file
    with open(file, 'rb') as f:
        bin_val = f.read(1)
        while bin_val:
            hex_val = str(hex(ord(bin_val))).replace('0x', '').zfill(2)
            imagebinary.append(hex_val)
            bin_val = f.read(1)
    return " ".join(imagebinary)


def test2():
    import jpype

    classpath = './Lib/Test.jar'
    jpype.startJVM(
        jpype.getDefaultJVMPath(),
        "-Djava.class.path={classpath}".format(classpath=classpath),
        convertStrings=True,
    )
    jpkg = jpype.JPackage('test')
    print(jpkg, type(jpkg))
    r = jpkg.Test()
    print(r.sss('sfdg'))


def test3():
    import jpype

    #classpath = './Lib/nets-af.jar'
    classpath = ['./Lib/nets-af.jar', './Lib/MagicJCrypto-v2.0.0.0.jar']
    # jpype.startJVM(
    #     jpype.getDefaultJVMPath(),
    #     "-Djava.class.path={classpath}".format(classpath=classpath),
    #     convertStrings=True,
    # )
    jpype.startJVM('-ea', classpath=classpath)
    config_pkg = jpype.JPackage('nets.af.common.conf')
    conf = config_pkg.Config.init('./Config/conf.xml')

    crypt_pkg = jpype.JPackage('nets.af.common.crypt')
    cc = crypt_pkg.Crypt()
    cc.init()
    print(cc.getInstance("ex-ws-moin").encrypt("AbCDeFG/#/20151118023454"))
    jpype.shutdownJVM()


def test4():
    import jpype

    #classpath = './Lib/nets-af.jar'
    classpath = ['./Lib/nets-af.jar', './Lib/MagicJCrypto-v2.0.0.0.jar']
    # jpype.startJVM(
    #     jpype.getDefaultJVMPath(),
    #     "-Djava.class.path={classpath}".format(classpath=classpath),
    #     convertStrings=True,
    # )
    jpype.startJVM('-ea', classpath=classpath)
    config_pkg = jpype.JPackage('nets.af.common.conf')
    conf = config_pkg.Config.init('./Config/conf.xml')

    crypt_pkg = jpype.JPackage('nets.af.common.crypt')
    cc = crypt_pkg.Crypt()
    cc.init()
    print(cc.getInstance("TripleDES").encrypt("AbCDeFG/#/20151118023454"))
    jpype.shutdownJVM()


def test():
    import jnius_config
    # jnius_config.add_options('-Xmx4056M', '-Xmx4056M')
    jnius_config.add_options('-Xrs', '-Xmx4096m')
    jnius_config.set_classpath('.', './Lib/Test.jar')
    print(jnius_config.get_classpath())

    import os
    os.environ['CLASSPATH'] = "./Lib/Test.jar"
    from jnius import autoclass
    tclass = autoclass('test.test.utils')
    # t = tclass('abc')
    #autoclass('java.lang.System').out.println('Hello world')


    #t = testjnius()
    #t.reverse("test")


# print(img_to_hex(filename))
# get_empno_all()
# print(get_url("url_dev"))
test3()
test4()
# test2()

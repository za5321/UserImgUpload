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


def get_accesstoken():
    import jpype

    classpath = 'Lib\\TestJPype.jar'
    jpype.startJVM(
        jpype.getDefaultJVMPath(),
        "-Djava.class.path={classpath}".format(classpath=classpath),
        convertStrings=True,
    )
    jpkg = jpype.JPackage('net.oboki.utils')
    print(jpkg, type(jpkg))
    r = jpkg.ReverseString()
    print(r)
    r.reverse("test")


def test():
    import jnius_config
    print(jnius_config.get_classpath())
    jnius_config.set_classpath('Lib\\TestJPype.jar')
    print(jnius_config.get_classpath())
    #autoclass('java.lang.System').out.println('Hello world')

    import jnius
    jnius_config.set_classpath('Lib\\TestJPype.jar')
    testjnius = jnius.autoclass('net.oboki.utils')
    #t = testjnius()
    #t.reverse("test")


# print(img_to_hex(filename))
# get_empno_all()
# print(get_url("url_dev"))
test()

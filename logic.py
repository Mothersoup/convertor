import base64


# text should be changed to ascii  and then  append individual in  array  ###

def ascii_trans(text):  # text -> ascii
    ascii_value = []
    for character in text:
        ascii_value.append(ord(character))
    print(ascii_value)
    return ascii_value


def trans_from_ascii(list):  # ascii -> text
    text = ""
    for li in list:
        text = text + chr(li)
    return text


def octal_trans(text):  # text -> octal
    list = []
    for oc in text:
        list.append(oct(oc))
    return list


def trans_from_octal(list):  # octal -> text
    text = ""
    for li in list:
        text = text + chr(li)
    return text


def hex_trans(text):  # text -> hex
    hex_value = []
    for he in text:
        hex_value.append(hex(he))
    print(hex_value)
    return hex_value


def trans_from_hex(list):  # hex -> text
    text = ""
    for li in list:
        text = text + chr(li)
    return text


def base64_trans(text):  # text -> base64
    text = text.encode('UTF-8')
    return base64.b64encode(text).decode('UTF-8')


def trans_from_base64(text):  # base64 -> text
    return base64.b64encode(text).decode('UTF-8')


def binary_trans(text):
    return ''.join(format(ord(i), '08b') for i in text)

##########################################################

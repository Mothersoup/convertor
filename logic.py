import base64

# text should be changed to ascii  and then  append individual in  array  ###
import binascii


def identity(text):
    return text


def octal_to_str(text):  # octal_to_str
    """
    It takes an octal string and return a string
        :octal_str: octal str like "110 145 154"
    """
    str_converted = ""
    for octal_char in text.split(" "):
        str_converted += chr(int(octal_char, 8))
    return all_ascii(str_converted)


def str_to_octal(text):  # str_to_octal
    final_string = ""
    lis = trans_from_ascii_ls(text)
    for li in lis:
        temp = oct(li)[2:len(oct(li))]
        final_string = final_string + " " + temp
    return final_string.strip()


def to_ascii(text):  # text to ascii return text
    ins = ""
    ascii_values = []
    for character in text:
        ascii_values.append(ord(character))

    for temp in ascii_values:
        ins = str(ins) + " " + str(temp)
    return ins


def text_to_list(text):
    string = ""
    lis = []
    for i in text:
        if i != " ":
            string = string + str(i)
        else:
            lis.append(int(string))
            string = ""
    lis.append(int(string))
    return lis


def ls_to_text(ls):  # ls to text
    ins = ""
    for temp in ls:
        ins = str(ins) + " " + str(temp)
    return ins.strip()


def trans_from_ascii_ls(text):  # text to ascii return ls
    ins = ""
    ascii_values = []
    for character in text:
        ascii_values.append(ord(character))
    return ascii_values


def ascii_to_text(ls):  # ascii ls to text
    res = ''.join(map(chr, ls))
    return str(res).strip()


def all_ascii(text):  # ascii text return text
    return ascii_to_text(text_to_list(text))


def trans_to_hex(text):  # ascii -> hex
    return text.encode("utf-8").hex()


def from_hex(text):  # hex -> text
    byte_array = bytearray.fromhex(text)
    temp = byte_array.decode()  # hex -> ascii

    # ------------------------------------------
    return all_ascii(convert(temp)).strip()


def decimal_to_ascii(text):
    lis = text_to_list(text)
    final_str = ""
    for li in lis:
        final_str = final_str + str(chr(li))
    return all_ascii(final_str)


def to_base64(text):  # text -> base64
    text = text.encode('UTF-8')
    return base64.b64encode(text).decode('UTF-8')


def from_base64(text):  # base64 -> text could happen can't trans error because some ascii can't trans string
    base64_bytes = text.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return all_ascii(message)


def to_binary(a):
    l, m = [], []
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m


def trans_from_binary(text):  # binary -> text
    return "".join([chr(int(binary, 2)) for binary in text.split(" ")])


##########################################################
def trans_decimal(text):  # ascii to decimal
    final_decimal = ""
    temp_text = ""
    temp_ls = trans_from_ascii_ls(text)
    for i in temp_ls:
        temp_text = temp_text + str(i)
    for i in temp_text:
        final_decimal = final_decimal + " " + str(ord(i))
    return final_decimal


def string_to_decimal(text):  # text to decimal
    return trans_decimal(to_ascii(text).strip()).strip()


def to_hex(text):  # text -> hex
    return trans_to_hex(to_ascii(text))


def hex_to_string_tr_octal(text):
    lis = text_to_list(text)
    final_str = ""
    for i in lis:
        h = str(oct(int(str(i), 16)))
        final_str = final_str + " " + h[2:len(h)]
    return octal_to_str(final_str.strip())


def convert(text):  # add_blank_to_ascii
    text2 = ""
    temp = ""
    for i in range(len(text)):
        temp += text[i]
        j = ord(chr(int(temp)))
        if (65 <= j <= 90) or (97 <= j <= 122):
            text2 += str(j) + " "
            temp = ""
        elif j > 122:
            break
    return text2

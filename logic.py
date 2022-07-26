import base64
import codecs

# text should be changed to ascii  and then  append individual in  array  ###
import binascii


def identity(text):
    return text


def octal_to_ascii(text):  # octal_to_ascii         #not to do
    """
    It takes an octal string and return a string
        :octal_str: octal str like "110 145 154"
    """
    str_converted = ""
    for octal_char in text.split(" "):
        str_converted += chr(int(octal_char, 8))
    return str_converted


def ascii_to_octal(text):
    lis = text_to_list_str(text)
    final_text = ""
    for i in lis:
        for sm_i in str(i):
            final_text = final_text + " " + oct(ord(str(sm_i)))[2:len(oct(ord(str(sm_i))))]
    return final_text


# def str_to_octal(text):  # str_to_octal
#     final_string = ""
#     lis = trans_from_ascii_ls(text)
#     for li in lis:
#         temp = oct(li)[2:len(oct(li))]
#         final_string = final_string + " " + temp
#     return final_string.strip()


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
            print(string)
            if string != "":
                lis.append(int(string))
                string = ""
    if string != "":
        lis.append(int(string))
    return lis


def text_to_list_str(text):
    string = ""
    lis = []
    for i in text:
        if i != " ":
            string = string + str(i)
        else:
            lis.append(string)
            string = ""
    lis.append(string)
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


def trans_ascii_to_hex(text):  # ascii -> hex
    return text.encode("utf-8").hex()


def from_hex(text):
    byte_array = bytearray.fromhex(text)
    temp = byte_array.decode()  # hex -> ascii

    # ------------------------------------------
    return temp.strip()


def ascii_to_decimal(text):
    temp = ""
    for ch in text:
        if ch != " ":
            temp = temp + " " + str(ord(ch))
    return temp


def decimal_to_ascii(text):
    lis = text_to_list_str(text.strip())
    final_str = ""
    for i in lis:
        final_str = final_str + str(chr(int(i)))
    return final_str


def ascii_to_base64(text):  # ascii -> base64
    text = text.encode('UTF-8')
    return base64.b64encode(text).decode('UTF-8')


def ascii_from_base64(text):  # base64 ->ascii could happen can't trans error because some ascii can't trans string
    base64_bytes = text.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message


def ascii_to_binary(a):  # ascii to binary
    l = []
    final_str = ""
    for i in a:
        l.append(ord(i))
    for i in l:
        final_str = final_str + " " + str((int(bin(i)[2:]))).strip()
    return final_str


def binary_to_ascii(text):  # binary -> ascii
    return decimal_to_ascii(to_ascii("".join([chr(int(binary, 2)) for binary in text.split(" ")])))


##########################################################


def ascii_to_hex(text):  # ascii -> hex
    return trans_ascii_to_hex(text)


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


def hex_to_ascii(text):
    final_text = ""
    lis = text_to_list_str(text)
    for i in lis:
        final_text = final_text + hex_to_ascii_chr(str(i))
    return final_text.strip()


def hex_to_ascii_chr(text):
    return codecs.decode(text, 'hex').decode("ASCII")

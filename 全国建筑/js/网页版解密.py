# -*- coding: utf-8 -*-
import base64
import re
from html import unescape
import Crypto
import execjs
from Crypto.Cipher import AES, DES
from binascii import a2b_hex

from lxml.builder import unicode




def webjiema(cipher_text):
    null = ""
    true = ""
    false=""
    key = 'jo8j9wGw%6HbxfFn'.encode('utf-8')
    iv = "0123456789ABCDEF".encode('utf-8')
    # key = 'jtkpwangluocom12'.encode('utf-8')
    # iv = "1234567890123456".encode('utf-8')
    mode = AES.MODE_CBC
    cryptos = AES.new(key, mode, iv)
    print(base64.b64decode(cipher_text))
    print(a2b_hex(cipher_text))
    plain_text_ = cryptos.decrypt(a2b_hex(cipher_text))
    print(plain_text_)
    Plain_text=bytes.decode(plain_text_)#.replace('',"").replace('',"").replace('',"").replace('',"").replace('',"").replace('',"")
    Plain_text=re.findall(r'(.*})',Plain_text)[0]#.replace('',"").replace('',"").replace('',"").replace('',"").replace('',"").replace('',"")

    print(type(Plain_text),Plain_text)
    Plain_text=eval(Plain_text)
    print(type(Plain_text),Plain_text)
    # return Plain_text

def shoujijiemi(data):
    js_infos = '''function deCrypt(t) {
                Object.defineProperty(exports, "__esModule", {
                value: !0
            }), exports.deCrypt = exports.enCrypt = void 0;
                var e = require("./js/38B128C16AECE6CF5ED740C61D4FAC62.js"), r = e.enc.Hex.parse("cd3b2e6d63473cadda38a9106b6b4e07");
                console.log(r)
                var p = e.AES.decrypt(t, r, {
                    mode: e.mode.ECB,
                    padding: e.pad.Pkcs7,
                });
                utf8String = e.enc.Utf8.stringify(p);
                return utf8String;
            }

            module.exports.init = function (arg1) {
                //调用函数，并返回
                console.log(deCrypt(arg1));
            };'''

    dedata = execjs.compile(js_infos).call('deCrypt', data)
    # 读取结果
    print(dedata)
    return dedata


def jiemi_CEB(data):
    null = ""
    true = ""
    false = ""
    # key='829514106, 1081570168, 862257152'.encode()
    # print( key[:8])
    # iv = "0123456789ABCDEF".encode('utf-8')
    # print(a2b_hex(key))
    # key = 'jtkpwangluocom12'.encode('utf-8')
    # iv = "1234567890123456".encode('utf-8')

    # print(a2b_hex(key))
    key = '1qaz@wsx3e'
    cryptos = DES.new((key[:8].encode()),DES.MODE_ECB)
    dedata=base64.b64decode(data)
    plain_text_ = cryptos.decrypt(dedata)

    print(plain_text_)
    Plain_text = bytes.decode(plain_text_)  # .replace('',"").replace('',"").replace('',"").replace('',"").replace('',"").replace('',"")
    Plain_text = re.findall(r'(.*})', Plain_text)[0]  # .replace('',"").replace('',"").replace('',"").replace('',"").replace('',"").replace('',"")

    print(type(Plain_text), Plain_text)
    Plain_text = eval(Plain_text)
    print(type(Plain_text), Plain_text)

#小程序
if __name__ == '__main__':
    # xcx='a4kFevKolhuDJYhfW3f2qyfUJhYt8KEsJEjRQWUYLLAcGSDKl57QHUkjmDDIs/USbIEm8Nid5UTQ9yCFMEGlmoZhZ/5vv/Ir0OPb65sXXk17PtzTIkRaDdi0J9ueRx/WwkANYvKguUnA++bRjzqsZ7HycAUFv75VR1GJqA/AH76oXBIOfPjY6MkGixEReD0NLO30o7mU0tD7xFTk3BDrnxrSQqfICTp5mh9W8hZ8W497PtzTIkRaDdi0J9ueRx/W+/EV8QfZC0pg6lFf7wHcfuQRLsugWGJtAmDWRA7/IaP7ybftsjK/MRw5d8GErNDZEsgwUK9TRNY50v3oP+dAlDWCR3NtO8cgVdRODboD4y+RjX1FPjjvHkjI0HyARy81sfJwBQW/vlVHUYmoD8AfvpB9OI13vcBN0HpezKIVq/2KN0jDOsCfCKahs0LOjk1qIQvlsnajBGx5A6ZIMvlGdUq128IQnwb/Z6R87hJNBRKhGqsXCw90N3X8Y22HxweBzLsy0nYYGAO0oW37a2kFNkaB3BryLSVLdVJQ0q4nkfMdC2/eR+b/oa8Eaby81FtFB3ZBGHJ6vLUogFJN2pimCCr9hogg32AI0KnFKjzZHIawaHDO5kHlqm4cM8qZ+q4J+ayZosH3F91INFzk4jdmIbJJtA/8mpIAnGwIIY74AftLoNdea4gAs7t2ds56fdDIUvVexpRYzKpf2K8wBf9mvKC7L8B47aMlO5QCdGzl5nlPP6935sOQTB7F77RSBl5liwtHR5pcXlsEYLC60LgSoRPMmtACTuWwU5JqCwKOstX7vi/5xEiwjWXOikkmOMgoFXLxhnf3ccr02xkeNBBwDIF8pjXQyPyk5lMC7cYsYvc9H6orNKGla2/dYl12MMmL7juNtJmCXxaQOCDd6T9beOyWZKU1/jxuhoAE6Nv9E6MQjfEU8yakmmBFmbWKKH0kXO/4cKxPbfa2eRAeZuGMtMyJEX8Y66iAGf6YYqimNs4N84VVnUskeQWN0qF4ncI60yr2vB6Lw1I9Cr7+hYvvtDaM5Ru12i0SJWDre+zTbcItsSUYhv3Fk1p4KwAW0Eth0KH0Jn4bG/tbwcpUMRteifBgBWSpmSecL/T3EF6zvos='
    # xcx='8lr7FkeuVfbi9O6o+zpsL8u6lbf5ts2/7fHfQ0zsy1L0kpZLKDbyi+Hsdd+avFFpewj67n7AysjdUqEEYaQU0mOLVpCU9OFDkVE367CKNLFkuHgcR4a86XG0s1MdBioA0Kr4ZrC9z6MZiemkLJRyqKnGpoMAxH/pfJIutLt7chJYdGlUaXB/52SZ9FNXEgnc2EfUBvIk/rGP8KZrfVY5eJgI0PrGXOCgofDOGTRXi8/PohnztMWYK7fOToPDNrRkAdNfMcYfyJ4EdtJ8+bbh9PWekTPHCndDbq+Kp0ykaH+OZTISXpBScXOjsrsGbpsUhbg8w45w5Gtms/l/Uq3rhKzu4D8E+5hOfvxV2rV9xQ5Xx2OAzLi06kPO8n7UJFT9ZUsF0RFRbDD2jTAzJwIyVg=='
    # shoujijiemi(xcx)

#网页
    a = 'IZgvAGrUV31JJr52HNx0ahGAcuOGR/CyJmx2mLq/hwARt9HRysi1vMN6pi7vyr+DCKIN8X/Sw0BpTqje/kCa7Tm6BgB2+61JA2DSEeKnC60bp32JrqTPNrn6Ug/QQaknYNs6UPHmvpHJTmzPfdhx0t1EhofhKwqEN8SKENZW1/9MmOgl+BWR/x6jIlIIeXbnb3ssedolkrrmQfGeFQLSg2kLZvQozQ5XLxl7uAOMQKD2r504QARUaDfqNcCbaQuB'
    # webjiema(a)
    jiemi_CEB(a)


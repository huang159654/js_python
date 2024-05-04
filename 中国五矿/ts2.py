#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2023/5/15 0:07
# @Author  : TS
# @Email   : TS@gmail.com
# @File    : ts2.py
# @Software: PyCharm
"""
import requests
import  rsa
import base64


def __str2pubkey(s):
    # 对字符串解码
    b_str = base64.b64decode(s)
    if len(b_str) < 162:
        return False
    hex_str = ""
    hex_str = b_str.hex()

    # 找到模数和指数的开头结束位置
    m_start = 29 * 2
    e_start = 159 * 2
    m_len = 128 * 2
    e_len = 3 * 2

    modulus = hex_str[m_start : m_start + m_len]
    exponent = hex_str[e_start : e_start + e_len]
    return modulus, exponent


def get_publickey_from_str(publickey):
    key = __str2pubkey(publickey)
    modulus = int(key[0], 16)
    exponent = int(key[1], 16)
    rsa_pubkey = rsa.PublicKey(modulus, exponent)
    return rsa_pubkey

data='{"inviteMethod":"","businessClassfication":"","mc":"","lx":"ZBGG","dwmc":"","pageIndex":1,"sign":"aeabcf6cdf9d8d60f8f217f3c45067f6","timeStamp":1684119663666}'

public_key=get_publickey_from_str('MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCMZ00QR6JfVSowHTtjH0Dzw+drHpB9EUiXYygUQpS1HS0PK2rk8eEPuxNtLHEp+BObQebFCf6X489G/hQbIrX8KKKD5Y6hMP0yol2RzR7OT/BLqBjc9Zr02UVk4Ft4HTf9dsGM64bO1ruTKfSCLvr0ng6nae8/N7lyqEsEbxrjZwIDAQAB')

encry_key=b''
for i in range(0,len(data),50):
    d0=data[i:i+50]
    # print(d0)
    encry_key += rsa.encrypt(d0.encode("utf-8"), public_key)
encry_key = base64.b64encode(encry_key)
param= str(encry_key, "utf-8")
print(param)


const crypto = require('crypto-js')



d = '1686940980825'
f = '1000'

function ds(d) {
    return d / 1000;
}

// console.log(ds(d))

function getResCode(x) {
        _0x6fba0c = crypto['AES']['encrypt'](crypto['enc']['Utf8']['parse'](Math['floor'](ds(new Date()['getTime'](), -0x7 * -0x53d + 0x1927 + -0x39ea))),
            crypto['enc']['Utf8']['parse']( '1234567887654321'),
            {
            'iv': crypto['enc']['Utf8']['parse']('1234567887654321'),
            'mode': crypto['mode']['CBC'],
            'padding': crypto['pad']['Pkcs7']
        });
    return crypto['enc']['Base64']['stringify'](_0x6fba0c['ciphertext']);
}

console.log(getResCode())

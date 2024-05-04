const CryptoJS = require('crypto-js')

function mian_123(a,b){
    var keyHex = CryptoJS['enc']['Utf8']['parse'](a)
    encrypted = CryptoJS['DES']['encrypt'](b, keyHex, {
        'mode': CryptoJS['mode']['ECB'], 'padding': CryptoJS['pad']['Pkcs7']
    })
    encryptvrscode = encrypted['ciphertext']['toString']()
//生成cookie值
    b_123 = escape(encryptvrscode)
    return b_123

}

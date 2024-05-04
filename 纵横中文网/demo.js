const CryptoJS = require('crypto-js')
function sdk(i){
    i = (i.split("|")[0].trim()).replace(/\n|\r/g, "")
    e = {
        "words": [
            1248687215,
            927682937,
            1799697988,
            892818261
        ],
        "sigBytes": 16
    }
    r = CryptoJS.AES.decrypt(i, e, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    })
    return r.toString(CryptoJS.enc.Utf8)
}
console.log(sdk())
    //找到核心生成密钥的代码({}, u, s.Z.getApiKey())

function getApiKey() {
    var t = (new Date).getTime()
        , e = encryptApiKey();
        d = encryptTime(t);
    return comb(e, d)
}

function encryptApiKey() {
    var et = 'a2c903cc-b31e-4547-9299-b6d07b7631ab'
        , e = et.split("")
        , n = e.splice(0, 8);
    return t = e.concat(n).join("")
}

function encryptTime(t) {
    var i = 1111111111111;
    var e = (1 * t + i).toString().split("")
        , n = parseInt(10 * Math.random(), 10)
        , r = parseInt(10 * Math.random(), 10)
        , o = parseInt(10 * Math.random(), 10);
    return e.concat([n, r, o]).join("")
}
function comb(e, n) {
    var r = "".concat(e, "|").concat(n);
    //todo base64
    return r
}
// console.log(getApiKey())

const crypto = require('Crypto')
function md5(input) {
    const hash = crypto.createHash('md5');
   //川更新哈希对象的数据1
    hash.update(input);
    //1计算哈希值并以十六进制字符串返回
    return hash.digest('hex');
}
function u(t, e) {
    return t.toString().toUpperCase() > e.toString().toUpperCase() ? 1 : t.toString().toUpperCase() == e.toString().toUpperCase() ? 0 : -1
}
function l(t) {
    for (var e = Object.keys(t).sort(u), n = "", a = 0; a < e.length; a++)
        if (void 0 !== t[e[a]])
            if (t[e[a]] && t[e[a]] instanceof Object || t[e[a]] instanceof Array) {
                var i = JSON.stringify(t[e[a]]);
                n += e[a] + i
            } else
                n += e[a] + t[e[a]];
    return n
}

function d(t) {
    for (var e in t)
        "" !== t[e] && void 0 !== t[e] || delete t[e];
    var n = 'B3978D054A72A7002063637CCDF6B2E5' + l(t);
    return md5(n).toLocaleLowerCase()
}
// t={
//     "ts": round(time.time()*1000),
//     "pageNo": 3,
//     "pageSize": 20,
//     "total": 3749,
//     "KIND": "GCJS",
//     "GGTYPE": "1",
//     "timeType": "6",
//     "BeginTime": "2023-01-26 00:00:00",
//     "EndTime": "2023-07-26 23:59:59",
//     "createTime": []
// }
// console.log(d(t))
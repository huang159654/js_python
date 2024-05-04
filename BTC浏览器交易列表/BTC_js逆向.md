目标网址：https://www.oklink.com/cn/btc/tx-list

测试发现这里没有x-apikey的值，数据不返回！所以判断这里需要逆向！

![1709706008948](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1709706008948.png)

打开浏览器的控制台的搜索： 尝试输入Apikey这个关键词！

![1709706120574](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1709706120574.png)

感觉这个有点像，就打开断点，可以断柱

![1709706545362](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1709706545362.png)

新建一个js文件把代码拷贝过来，自己改装一下

![1709706762762](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1709706762762.png)

打印一下，发现缺少这个this.encryptApiKey()：，

![1709706849793](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1709706849793.png)

然后再网页上看看你这个函数，点击这个

![1709706948072](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1709706948072.png)

发现这里有定义，直接扣下来放到js，然后运行!返现又报错!在这里断点调试。

![1709707062280](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1709707062280.png)

![1709707085193](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1709707085193.png)

断点调试发现没有定义t,现在不知道这个是不是动态的还是固定的，先在js里面写死！运行js发现报错！缺少this.encryptTime(t)，这个函数，和上面一样，

![1709707242113](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1709707242113.png)

![1709707394427](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1709707394427.png)

运行js发现报错，缺少a，在这个函数那边断点调试

![1709707716650](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1709707716650.png)

在网页上调试发现a,这个不知道是不是固定的还是动态的！在js先固定

![1709707758483](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1709707758483.png)

运行发现报错，缺少这个函数

![1709707871218](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1709707871218.png)

在网页上和上面的一样

![1709707951569](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1709707951569.png)

在运行js代码，可以得到结果！但是和网页上的不一样，需要base64编码！

![1709708045420](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1709708045420.png)

base64编码，网上自己随便搜，在python运行

![1709708220489](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1709708220489.png)
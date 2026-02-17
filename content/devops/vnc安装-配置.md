---
title: VNC安装 | 配置
date: '2024-11-19T08:34:00.000Z'
lastmod: '2024-11-19T08:46:00.000Z'
draft: false
tags:
- Windows
- Linux
- VNC
categories:
- DevOps
---

> 💡 使用两台 windows 电脑进行远程控制，配置 VNC 的详细教程。

VNC（Virtual Network Computing），为一种使用 RFB 协议的屏幕画面分享及远程操作软件。此软件借由网络，可发送键盘与鼠标的动作及即时的屏幕画面。

VNC 与操作系统无关，因此可跨平台使用，例如可用 Windows 连线到某 Linux 的电脑，反之亦同。甚至在没有安装客户端程序的电脑中，只要有支持 JAVA 的浏览器，也可使用。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHNRFD4X%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQCj4iz5lOY682IMfM%2FvsoaGL8A9VpHCkHAj9toeqZ0O9QIhAIf1BgX2z5kAvUUIBPY%2F5nOv%2B2Xt3ZRBSW934bbLZ2hmKv8DCEUQABoMNjM3NDIzMTgzODA1Igz8Fm%2BANMixb2WZhUUq3APxl6AFOtg8zRKRbARWjks3CZVxFaGHRDBkVzcG%2Bew%2BJsYQ8vdvn2kdUYcZRSI4xh8Eocj%2B3Cm09kATtGCEFx8C3wAYJKJPG%2FLnMzxhvQdToOwIPMRp1NRkK10ezTB5SAI6brvSa0NorfOrNbKpzHAxLNXUo0kXWzdQ4rk%2F0NgjU56OWxvUNEToR8lNunrtRrrBsPqWwBNZk5x7PMf%2BvFgZgD1lpoCI8C01Y%2BXM2vGGRzpm6fqJVon29mPyaJ%2FtjZT8amnblr%2Bc21D6u9Zkmx10ubBPtyNY7mk29mXLgpZn9hOYdDW7eTWwGQbLNtyh7piC9vVa7af5U87ptUKNGYUjTLmnCi1JnHrER%2BLjD18I5mj9j1ije0zjMHzsXk8d5OEjUieOeCgHW5a%2FL3PXZ6lePm5RV4LwxvxhNyYKTwCWjd4W2zVafe%2BtJ8gjV%2FTUP0ZDNvx1PbaAwXZ6Vb6lK2WA0SlsSJAqKfXl9N4aj2gYhJjr7bOxFQjjQ1psrN6%2B0ss9rTw1uQCI%2BUhjdrCls78p261H%2FFQK%2Fa88Twqat8R991ZTyv3cQjZQOfncUVJ891JId4%2BDoxuQr%2BAWEWJEBnAq9uvlWTUm9LYDWkvBHjAv%2BRfI6OKz6YmqDTqJCDDjv8%2FMBjqkAYIrmtER6h1YCLmUd5CnRuyjwSRX0cSPf%2Fs%2BPUl8AyCHRftr9ePj1gNV6LOEvP1TTVUx%2BiURc47mX6GnemNTVwLgYc3qSTcd7ah7EwGje%2FORMEeHQcy%2BXmGXX9VUUVhWPHsy4KGgKmjKb78a5w1WnjLYL2zzjo1c7CMRBhhZ3nLefWJrQAjFWzi%2FatXNWcJp4Xp5IGNRiRup12o6mSIjD9D0Z3eJ&X-Amz-Signature=170a7d225b34b711a0e179e74e60c7c71ceeb157459e97613807e8e28aa4e744&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHNRFD4X%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQCj4iz5lOY682IMfM%2FvsoaGL8A9VpHCkHAj9toeqZ0O9QIhAIf1BgX2z5kAvUUIBPY%2F5nOv%2B2Xt3ZRBSW934bbLZ2hmKv8DCEUQABoMNjM3NDIzMTgzODA1Igz8Fm%2BANMixb2WZhUUq3APxl6AFOtg8zRKRbARWjks3CZVxFaGHRDBkVzcG%2Bew%2BJsYQ8vdvn2kdUYcZRSI4xh8Eocj%2B3Cm09kATtGCEFx8C3wAYJKJPG%2FLnMzxhvQdToOwIPMRp1NRkK10ezTB5SAI6brvSa0NorfOrNbKpzHAxLNXUo0kXWzdQ4rk%2F0NgjU56OWxvUNEToR8lNunrtRrrBsPqWwBNZk5x7PMf%2BvFgZgD1lpoCI8C01Y%2BXM2vGGRzpm6fqJVon29mPyaJ%2FtjZT8amnblr%2Bc21D6u9Zkmx10ubBPtyNY7mk29mXLgpZn9hOYdDW7eTWwGQbLNtyh7piC9vVa7af5U87ptUKNGYUjTLmnCi1JnHrER%2BLjD18I5mj9j1ije0zjMHzsXk8d5OEjUieOeCgHW5a%2FL3PXZ6lePm5RV4LwxvxhNyYKTwCWjd4W2zVafe%2BtJ8gjV%2FTUP0ZDNvx1PbaAwXZ6Vb6lK2WA0SlsSJAqKfXl9N4aj2gYhJjr7bOxFQjjQ1psrN6%2B0ss9rTw1uQCI%2BUhjdrCls78p261H%2FFQK%2Fa88Twqat8R991ZTyv3cQjZQOfncUVJ891JId4%2BDoxuQr%2BAWEWJEBnAq9uvlWTUm9LYDWkvBHjAv%2BRfI6OKz6YmqDTqJCDDjv8%2FMBjqkAYIrmtER6h1YCLmUd5CnRuyjwSRX0cSPf%2Fs%2BPUl8AyCHRftr9ePj1gNV6LOEvP1TTVUx%2BiURc47mX6GnemNTVwLgYc3qSTcd7ah7EwGje%2FORMEeHQcy%2BXmGXX9VUUVhWPHsy4KGgKmjKb78a5w1WnjLYL2zzjo1c7CMRBhhZ3nLefWJrQAjFWzi%2FatXNWcJp4Xp5IGNRiRup12o6mSIjD9D0Z3eJ&X-Amz-Signature=888f49273add4083f12a8874aff0dcdb5cde93f5f63771baaa6a4670bfbf66f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


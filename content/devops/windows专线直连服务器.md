---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTQ3R4EX%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCIGXmtsS9u%2BQmSD5llMpogVAzVlusukyqMsdy3cWFmEMsAiBypy4UaT3Ud3vEUwcscJwnRuhTXECtucrJ8aJg3xvaGSqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5oMoyjum4f57VpiTKtwDdkqPcBcNVvMu%2FqywkvpH%2BZhe1SJad8gzzfYUW3BX2%2FuxhTIDTDnieTzqUuu6NU2%2FpqBwemGavbUw2%2FDjPAK6Cqnem1fWwFWb8Kh3UCZh8i98ZAV3bIeo7txMvTnnis0WJSAf9%2F4xtrKVy3Z0sbCeyr82fltITl34IsBRs3nIA3Zc3lxLI98qJOJiqQ5xm%2B2teJ20Bpc6B2rXvu4VU8ZY6zJfFdUJHyGIynCkbOkqHiTgBXD2wKUZEGafiOw4WIkI5qezHkIMWGSodjXnkW9qZKoeUM2WFAcJoYvef%2B8EhdsLbs5LoHOU3PjEGH1%2Fj%2F7f3eQgQhyGAsYrFXOwlasxbgBzV5aN5PbV7QZzBcBYukeTmc2IC4cd2FdR3rHe3pw%2BkbdfbXFVmx2fQwYIWrfYAKLNHDsjdJbCg1Rb8j7mtouQy2BjaRvUh2h07J9EVkPYnKtpQ8yhq9UGjWPx3raO3Oa1byfa7rRUGLtyJIpvXh7q4bG2NMZwDibZ6pIU6eIaJAuZconRivSQqvJEooJbbfc4qzs7PrHqknLcUX612Fngt8MJVlt%2FDDew5d9D0xKREP2ctZ%2F1AQy665mlpqMveLK4P4PxDm7YdYKsTDYxk9q5yGr99HV7pIVyLPwwrpPvzAY6pgHzUuRkqc8M5SQUbXJ6hrMfbEMObGPvWNYKRVirKebixBddsvDrr8utJiDC6Q1bCQIhAeBqqa1wxwZY0Fq5FeBcvhZqlfIcJ32deYth1ioA6BPgJRjoxU9nYEK7r2WugEUOsSN7zaZmN20V36PfgNI4QAIby%2B7wMHwE28ctLaDYe3GjJ0LUngmJergsTp1rPnUPdCBMRUrMJIrwU8kQQqbnOp3pza%2Bz&X-Amz-Signature=f6f77db03eafc791ff8c07f2d208d5b83d66525519837beff50423fe0c25b617&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


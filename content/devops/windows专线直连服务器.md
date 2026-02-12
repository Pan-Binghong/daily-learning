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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AXPGOKQ%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQD%2FNqjKnjgsLb4u%2BzE4ky62O63Dx6aBE8%2FZoFo1ksvcNAIhAK23PEDy5iCgV8hjJXXUWuk8pFHtGKK0FQ%2FBsXiMyQNeKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxycgYlHPMCNDhRQ7gq3AN0yOn6wHlv%2B%2B%2BvfQjNqb1690TutaWJBXNqCam5QaIUX%2B4dPhC2eFWbpa2ApypcWN%2F20TTCjqg3%2FQPz7snrmGQicMf1cqM3L8uOupuhZl9ZHTqeUCeldorPnyIjAwsTyBWN%2FUbXmrYeu8sYLkc5rYOQRdcHWSyzHampz6BuL1Q%2Fl7qmUgM2aUisTyDEuLvbkHEfseFsBm%2BfdEVwrlMdWFhmSHEwKahv00dXO169VasSIGmkzSbAThzKfAALeMGwIxWJz4uwqsUZRRuVo684%2FQfM5LC4ZG8E%2FiIHhJmxFef6U5j7Pgb1Em6%2BUDe8yDySq8jrSC2JHjp3z4ih7y8T9TtLenUeiDz7KzhfOqtb%2FuIESVPzi%2FWm8ScaS%2BTUY6xt8TcO6%2BfWs1PWpIdRppZtRAL7B%2BX3M2bZKfJIP8Z6v%2F2IclZkUIGFqk6JKfudBbMiY55k%2BRREEQQ5y7sNrHW%2FT3YUe45hKkjj2Lwh%2F6sOx734FMI9p3%2BoIlmQSf79Y36PljhejH%2BDoWGus%2FgffSmag6LdhY1XMT9pQAePvIClo5pagUQsPZuvKz%2Bfi8hMqXy4Q7TSSfzTkrgrDS6%2FyNrQgwlydb2ZQc8Qy3OQu%2FVj3%2FVpMUn496SL%2BksS%2BOxAnjDrkrXMBjqkAR5t1Ei5fkuU1ToqxDrdUOYfQyyvKZ9HYlR9bHTmedJ10RWMnxVfCPZADjacLfBOIMT0j%2F7GsXRc4SUV0D2qtWtMHH19UxT3kFzzlFdE7Dd64d9stfgIrGf7Pfe00Va3BrkomVuB3ZGouNm9t04payV%2B8hvzwGi7KQy9ZTHXDG6ToOpJMbKq71JafyDeJWnCMW3cnTRiOSBSMZ7XukJT46YY0s3P&X-Amz-Signature=8cd01ded219b305d139e4657a99a268bf37cf6415fafe6aabaa633ee0e534e3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


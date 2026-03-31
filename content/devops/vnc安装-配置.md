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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFF4VEGX%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIFje57qkCXZICNEhAPlvW6CLF%2FqnALjapn6YuXg2v461AiEA3ew3JF4dlXZhnHXCg4B71cqCqio2G6sdvpGNPIUitNYq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDKThaqyVGnONj1CSrircA0oXXyXa%2FsFZ63HAAOLKorNIf%2F%2F6rv0EqcGotOdzj5S%2Fduv3tldTqQC7kWLWcys6VhYz%2FKBTstgWi7Usf8uwnxTLlslzpJJJIEdYziHEm0pwzO%2FFGINiam7bk0VNBF%2BtTx8j9GnUFf4sQ7h20XeAnev2HPNmlBKf6XIzq8BeN84sV5i7Ht6%2FA9WNhzw6mNN2r%2BF%2BvNGzkKqFH10Z1LNZaWA2meb5Xe2MYl1Yhyu%2FTtkxh2Jm%2BGy%2B%2F81XLuJDtNxZo7LPcC530ILZCD45g5Dxl1KNdWQd%2FIg3s6RaAPK5haZvRsbg2NwFCARYfUlrn8ZYPOtRtturuTACxvF7%2F9j21M7o8KNWQc3YXnzmMkDw7zRHNVQzBBaUvemu6nWMFWiEz6kA%2FxaC3TGUoGF7ElPa%2Be1uXfJA9FyCHSLH%2BM6X%2BpTmJvW9VpM00iVN4iNOE9dfH4TmlD%2Fizh8n0EQtkFLBY89Eq808gVZjBB5HfOwzLOLRF8gs0EIkYsiKBtvR1lf%2FWbgAthe0A5jYhL6bbcuIpP8EtYqi3wGLDt5YC5l6K2II5QqVgB7ZD%2FQ%2B%2BUisJG4ETN9nJ6Mlm00p3Z1EYZqZbcp0VsM5ySjQPO0GjL1x6wK4Yv%2B5cZ35pgf%2BFmOAMPuCrc4GOqUBuxkOwR8YYSM7PLqptv5PPfBaPccfbY1MKAt%2FdU0JoPRCNoqhQ9O4506V6N7bWveC6K%2B27lnBvnajGYyQqh77PCeVHotJI3xC5wUNtmpscGrR34eEa0IbJgcbXjHgTVvytxEjAW9IwYGdVzXqhxm6rl%2FjbFop9h5%2FoCQP4J8%2FohCfCe5fz%2FfoNX29tbE805qzwGer7%2F9zj%2BSS7qIRSa2s%2BDkAiH4Y&X-Amz-Signature=62a1d91c9203f174e3dea560df6d0b5192d6ade99be6a0c58438457eec2a65fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFF4VEGX%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIFje57qkCXZICNEhAPlvW6CLF%2FqnALjapn6YuXg2v461AiEA3ew3JF4dlXZhnHXCg4B71cqCqio2G6sdvpGNPIUitNYq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDKThaqyVGnONj1CSrircA0oXXyXa%2FsFZ63HAAOLKorNIf%2F%2F6rv0EqcGotOdzj5S%2Fduv3tldTqQC7kWLWcys6VhYz%2FKBTstgWi7Usf8uwnxTLlslzpJJJIEdYziHEm0pwzO%2FFGINiam7bk0VNBF%2BtTx8j9GnUFf4sQ7h20XeAnev2HPNmlBKf6XIzq8BeN84sV5i7Ht6%2FA9WNhzw6mNN2r%2BF%2BvNGzkKqFH10Z1LNZaWA2meb5Xe2MYl1Yhyu%2FTtkxh2Jm%2BGy%2B%2F81XLuJDtNxZo7LPcC530ILZCD45g5Dxl1KNdWQd%2FIg3s6RaAPK5haZvRsbg2NwFCARYfUlrn8ZYPOtRtturuTACxvF7%2F9j21M7o8KNWQc3YXnzmMkDw7zRHNVQzBBaUvemu6nWMFWiEz6kA%2FxaC3TGUoGF7ElPa%2Be1uXfJA9FyCHSLH%2BM6X%2BpTmJvW9VpM00iVN4iNOE9dfH4TmlD%2Fizh8n0EQtkFLBY89Eq808gVZjBB5HfOwzLOLRF8gs0EIkYsiKBtvR1lf%2FWbgAthe0A5jYhL6bbcuIpP8EtYqi3wGLDt5YC5l6K2II5QqVgB7ZD%2FQ%2B%2BUisJG4ETN9nJ6Mlm00p3Z1EYZqZbcp0VsM5ySjQPO0GjL1x6wK4Yv%2B5cZ35pgf%2BFmOAMPuCrc4GOqUBuxkOwR8YYSM7PLqptv5PPfBaPccfbY1MKAt%2FdU0JoPRCNoqhQ9O4506V6N7bWveC6K%2B27lnBvnajGYyQqh77PCeVHotJI3xC5wUNtmpscGrR34eEa0IbJgcbXjHgTVvytxEjAW9IwYGdVzXqhxm6rl%2FjbFop9h5%2FoCQP4J8%2FohCfCe5fz%2FfoNX29tbE805qzwGer7%2F9zj%2BSS7qIRSa2s%2BDkAiH4Y&X-Amz-Signature=1657e0d26c4858b5421d4f2c6dc08565a5fc266bf28934f18e10b775f1fda0f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


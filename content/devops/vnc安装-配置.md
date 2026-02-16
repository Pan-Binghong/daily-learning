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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2PF5SR4%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQCR%2BIg0vKoMYwA%2Fp1W0MI4kZ%2BENF4ltuWuAzSPt5e9KSAIhAIhBkBzXdaSVbju%2FjSu%2F%2ByMAqlenU2Z%2BeK3Avv9ueQBoKv8DCCwQABoMNjM3NDIzMTgzODA1IgwIjOG0TVWXil%2B34RIq3ANx2OElf%2FGGpW8wmiHW7UCl2sT75NyfUqxzHO9FO0q68ZDJPD3fukUQ2pIcmDiOcAzGob6ShwQG%2FApe6%2FSzFpWxM%2FuOk8j34nvCkr7V9ipVjd2MOgCjIzRSqEJnlXBON8SrfOydiYKJ8IVhsYAy27J3XXla6%2BcpWpUKIkM8Pwm5275jmVaxlQstWmbNTssxqlt9vLf0EZoEfdKcn%2BtNSeT%2Bz4zY1lSmabPAi93zle%2BrmuNhh%2FSxpV%2FzN2wNRiYOYjBB%2FiZ4C0a0eD0XkVM73QUtlncrdOM%2FcmfNlRWktEvOJRxNWpsQz%2FaufCmXu4VIxfCNircjVpw52NsNQ22omBA9KZvk9nx%2FIAN%2BJY8MmJpIyC3qLqc%2BdZYO%2BTEE0HOBWK9oGTXRCOsktEU7dsyxHZDUNq6S7prjp3bzFQGOZbvWUBDM2zcaKibQ8HPvEaq5JmbaVI9csj3ma25x7HCkDDRwe4mjYxvAMMjP2HDuKD%2Ftb4lsIpW4w5eBXDiqgJ85Dv4URIriO3Nthc2HYqCbPeO4Jm%2BXW3UgFGusHy6mwTnX2aQagfcb9I1HUxz8AbEpNPlh3OPoMcgsObJJy8PEIUxXc2Ts%2Bfiii3ef%2Bw6HaA9fJLZqz5sbpMJb1vqu8TD5lMrMBjqkAVlFExnh2AoHrfTvowCbfq67SgsRp5vjhmyf9PqirN3Qb8jHx3sj9Ov56SlUzDvz%2BoQok4JHu9MrdVWVjpob0bDRHFtYJV5i6Qo0F7OuWVNOchBDTfQjcc73NGtmoolq70pefo5xhkOPJ36GD1D7kpdSyz56AeqEwJXmIqSTNs%2Fwp191vPNB%2FbVw4I%2F2ZqqsOdab9SfLgrGttRb9EiuDWHNrRIzm&X-Amz-Signature=5e3a9620f21b88271870b43484a05c6447e143690074e5f5d27e5d8bddc714b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2PF5SR4%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQCR%2BIg0vKoMYwA%2Fp1W0MI4kZ%2BENF4ltuWuAzSPt5e9KSAIhAIhBkBzXdaSVbju%2FjSu%2F%2ByMAqlenU2Z%2BeK3Avv9ueQBoKv8DCCwQABoMNjM3NDIzMTgzODA1IgwIjOG0TVWXil%2B34RIq3ANx2OElf%2FGGpW8wmiHW7UCl2sT75NyfUqxzHO9FO0q68ZDJPD3fukUQ2pIcmDiOcAzGob6ShwQG%2FApe6%2FSzFpWxM%2FuOk8j34nvCkr7V9ipVjd2MOgCjIzRSqEJnlXBON8SrfOydiYKJ8IVhsYAy27J3XXla6%2BcpWpUKIkM8Pwm5275jmVaxlQstWmbNTssxqlt9vLf0EZoEfdKcn%2BtNSeT%2Bz4zY1lSmabPAi93zle%2BrmuNhh%2FSxpV%2FzN2wNRiYOYjBB%2FiZ4C0a0eD0XkVM73QUtlncrdOM%2FcmfNlRWktEvOJRxNWpsQz%2FaufCmXu4VIxfCNircjVpw52NsNQ22omBA9KZvk9nx%2FIAN%2BJY8MmJpIyC3qLqc%2BdZYO%2BTEE0HOBWK9oGTXRCOsktEU7dsyxHZDUNq6S7prjp3bzFQGOZbvWUBDM2zcaKibQ8HPvEaq5JmbaVI9csj3ma25x7HCkDDRwe4mjYxvAMMjP2HDuKD%2Ftb4lsIpW4w5eBXDiqgJ85Dv4URIriO3Nthc2HYqCbPeO4Jm%2BXW3UgFGusHy6mwTnX2aQagfcb9I1HUxz8AbEpNPlh3OPoMcgsObJJy8PEIUxXc2Ts%2Bfiii3ef%2Bw6HaA9fJLZqz5sbpMJb1vqu8TD5lMrMBjqkAVlFExnh2AoHrfTvowCbfq67SgsRp5vjhmyf9PqirN3Qb8jHx3sj9Ov56SlUzDvz%2BoQok4JHu9MrdVWVjpob0bDRHFtYJV5i6Qo0F7OuWVNOchBDTfQjcc73NGtmoolq70pefo5xhkOPJ36GD1D7kpdSyz56AeqEwJXmIqSTNs%2Fwp191vPNB%2FbVw4I%2F2ZqqsOdab9SfLgrGttRb9EiuDWHNrRIzm&X-Amz-Signature=0304169c4fa28c83c505ac72f97afc02a0943c51a4d39e0cf92908362a9dc451&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


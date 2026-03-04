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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKC4C2KB%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAbmVPY%2BvroQuvU%2BylKC2MoVtc0m9oZGydhSlUy2vytsAiAPfdmpg6Q8izbNVstYmlCVFm%2B8TEepUHjTI%2Bd0iyoYjCqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqZpB8QzB3ji8TwR5KtwDUME4D0420pgNQWLHqFXhDWplDDq0ZQUIAmzW5QURtnyC8G0bXmuCdsW%2FJMdd5z%2FaetAjE8IwhZInoQ3C%2FxB2F3h25dn5bBx%2FxrMvSclZIWpjdenz%2FQeEH3k21NrOqnLGklvkz6GaxgwuGSj0yiXXKkraRYnxvVjjJuCDk4szllvtulTMcTzaPvHvxasMPm4xoc%2BCcD0X81c6aIZZ%2FGiQm5WUZ1uWTD%2FHpGPoFErdZKMRZh22SDo3idC1ZU%2FU3b0lmmTrp5FOFVlhTVgYr9bv9wpfChvuq3hWStd3ANiyIfWTSoc6T4gZ8aKSfNyUL7Cw%2B0k4ZLT2rLOO6jg9FyZroO8Y%2BnFkyyzbXbv2ZTrPAxkMl2%2B2PN6JqDO%2BlXwKdfQjIdJgbeWmoho61Y8AxHj7%2BsqUs7Rgi3V%2FA9dsG3O0KKUXE8Epe6Korm5%2F811j3uVXk%2BiFcX6%2FJmUQIqsgLZzLw5RAMYAe2XA7ANEqh%2Fvx5PNFvQVowtBhJ%2BmL7RAbzMcJVXIt9JXiWbLRheHiPJuBhxI1t1oKvXQpYZ3HgwpxmiGBa9Df2fpFloTCYGah6GYuGllplwhHiE02vo6uRHvXCH3oYAjS2sW4zvvuDcj3cL3UUhTYfhLq5wTsWsQwkpWezQY6pgHIB2lcOt7rJfdLy6qtQEo6KefgAuiIN%2BRTN66%2B2WfEOlUh2990HaXClKLEo9IggIfbApWdd0Dn5ceHssGipfBOBRDQWXaWe1lPdStpQRoISu2qL%2FBtWAMLMmLmW4OuiksUz09qdY9oX1VeOrjHCREov50JpIywvXBFLO7Wy669sLCC6PtiKRa5KvTaL%2BdMalf9UAe4eL5VFzDW338L8rq%2Fi%2BKDMG39&X-Amz-Signature=ac688478e37a8ec813b8ca711c4496ff4499dc0a1ad248df0bed7b315d0410da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKC4C2KB%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAbmVPY%2BvroQuvU%2BylKC2MoVtc0m9oZGydhSlUy2vytsAiAPfdmpg6Q8izbNVstYmlCVFm%2B8TEepUHjTI%2Bd0iyoYjCqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqZpB8QzB3ji8TwR5KtwDUME4D0420pgNQWLHqFXhDWplDDq0ZQUIAmzW5QURtnyC8G0bXmuCdsW%2FJMdd5z%2FaetAjE8IwhZInoQ3C%2FxB2F3h25dn5bBx%2FxrMvSclZIWpjdenz%2FQeEH3k21NrOqnLGklvkz6GaxgwuGSj0yiXXKkraRYnxvVjjJuCDk4szllvtulTMcTzaPvHvxasMPm4xoc%2BCcD0X81c6aIZZ%2FGiQm5WUZ1uWTD%2FHpGPoFErdZKMRZh22SDo3idC1ZU%2FU3b0lmmTrp5FOFVlhTVgYr9bv9wpfChvuq3hWStd3ANiyIfWTSoc6T4gZ8aKSfNyUL7Cw%2B0k4ZLT2rLOO6jg9FyZroO8Y%2BnFkyyzbXbv2ZTrPAxkMl2%2B2PN6JqDO%2BlXwKdfQjIdJgbeWmoho61Y8AxHj7%2BsqUs7Rgi3V%2FA9dsG3O0KKUXE8Epe6Korm5%2F811j3uVXk%2BiFcX6%2FJmUQIqsgLZzLw5RAMYAe2XA7ANEqh%2Fvx5PNFvQVowtBhJ%2BmL7RAbzMcJVXIt9JXiWbLRheHiPJuBhxI1t1oKvXQpYZ3HgwpxmiGBa9Df2fpFloTCYGah6GYuGllplwhHiE02vo6uRHvXCH3oYAjS2sW4zvvuDcj3cL3UUhTYfhLq5wTsWsQwkpWezQY6pgHIB2lcOt7rJfdLy6qtQEo6KefgAuiIN%2BRTN66%2B2WfEOlUh2990HaXClKLEo9IggIfbApWdd0Dn5ceHssGipfBOBRDQWXaWe1lPdStpQRoISu2qL%2FBtWAMLMmLmW4OuiksUz09qdY9oX1VeOrjHCREov50JpIywvXBFLO7Wy669sLCC6PtiKRa5KvTaL%2BdMalf9UAe4eL5VFzDW338L8rq%2Fi%2BKDMG39&X-Amz-Signature=6736195125831c0c8e909d3620e354135e60fffa9f473945772e3c75be99e8b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


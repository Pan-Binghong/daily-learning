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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C5YSUMG%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKaO9btSbvQj56D2I2ZTy0mZ0fOo7xEn7LSdC0XklGJAIgWUBlWcfQD%2FXBmslaXPrIne70tOLSyXcSvbMd%2F8p%2Ff5cqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLoRW6UoKd3%2FO5zQ%2FCrcA0JGc7spwK7wf1r3GSxXNE7uT%2FGoaAfm2XN0z7uG8aNzOeK2g2peHXTzAbmO8GqUmiXnVZexG3lq1v0PgqufhPdVu%2F%2Bxwr57SFMBZ5s%2FVpBPJKHpao2GskQpv7Tmm%2FuI0256QsYyhYbsGwuGRUiC7Z0Qk4pcL%2BBNfsjxHQ0uJkmEurIxmKD1LI2R4%2F1kBCfCQqSnJH9vahB0D7StZr5TNscf9nVhN3VTd2w5gCNR1xIM7UJWkLgPWM8NfLuIynYncpTC71wuuoj5KZYxCbrbLRAXeRapiFc1%2Bpu6oUupArwOU%2BPele%2FALCypauVmncHZkyg6fHKcrIGGdptEuqZw44BXbTL%2F5CHL7vxtg4Lnh7Rl8WgK4J46xrrZd7H3IaUkDt0S0qC6yoesAM0o63nkogxB5ybsLxblO2VMSyJZEPB63vAbRh5GbZJPOMZX3Zo%2Frx40bYTOYFkUZPDRj10szQ%2BfPqT7dwPYO2Rpu8zGpEc6QFib1NrxCXivFJmxqdfByO155fWqlpKfEEvpWkJTJbPoH3OwdFYHYzVkficed6brKQTyDkQAvcVfSPcHx7Hbhsuywfkf%2BKvFeFF5mVWJ4qB9OZM5BdZw00XKLL4udviRIBmQ4NuGNd5bbqhcMLTNnskGOqUBcAZok4BSuQHKCYcAivcponl6xlAHtp84KSZjl9zTuKsYeQJ5oUJoW%2BkuRfMuF8bhekc2oAxHJbjvHO9RQMkl2WiIKRreNwMOIPdIbo%2BhC8OXQuiFaXm9fNqLybndfbuQbFloLRPGtYfIl4p2Z9QZ9%2Fgr9YCjlhVn4i1CNRrrkBO5XT1oHZKJHDYmOZPX4%2Bpumnr8B8Q1Sqxllbdl7OxZ1Gbpr34K&X-Amz-Signature=7cc86a943582de7d28618256a9666b3b06efe6da1d9ee8d536c2b65a5a076b77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C5YSUMG%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKaO9btSbvQj56D2I2ZTy0mZ0fOo7xEn7LSdC0XklGJAIgWUBlWcfQD%2FXBmslaXPrIne70tOLSyXcSvbMd%2F8p%2Ff5cqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLoRW6UoKd3%2FO5zQ%2FCrcA0JGc7spwK7wf1r3GSxXNE7uT%2FGoaAfm2XN0z7uG8aNzOeK2g2peHXTzAbmO8GqUmiXnVZexG3lq1v0PgqufhPdVu%2F%2Bxwr57SFMBZ5s%2FVpBPJKHpao2GskQpv7Tmm%2FuI0256QsYyhYbsGwuGRUiC7Z0Qk4pcL%2BBNfsjxHQ0uJkmEurIxmKD1LI2R4%2F1kBCfCQqSnJH9vahB0D7StZr5TNscf9nVhN3VTd2w5gCNR1xIM7UJWkLgPWM8NfLuIynYncpTC71wuuoj5KZYxCbrbLRAXeRapiFc1%2Bpu6oUupArwOU%2BPele%2FALCypauVmncHZkyg6fHKcrIGGdptEuqZw44BXbTL%2F5CHL7vxtg4Lnh7Rl8WgK4J46xrrZd7H3IaUkDt0S0qC6yoesAM0o63nkogxB5ybsLxblO2VMSyJZEPB63vAbRh5GbZJPOMZX3Zo%2Frx40bYTOYFkUZPDRj10szQ%2BfPqT7dwPYO2Rpu8zGpEc6QFib1NrxCXivFJmxqdfByO155fWqlpKfEEvpWkJTJbPoH3OwdFYHYzVkficed6brKQTyDkQAvcVfSPcHx7Hbhsuywfkf%2BKvFeFF5mVWJ4qB9OZM5BdZw00XKLL4udviRIBmQ4NuGNd5bbqhcMLTNnskGOqUBcAZok4BSuQHKCYcAivcponl6xlAHtp84KSZjl9zTuKsYeQJ5oUJoW%2BkuRfMuF8bhekc2oAxHJbjvHO9RQMkl2WiIKRreNwMOIPdIbo%2BhC8OXQuiFaXm9fNqLybndfbuQbFloLRPGtYfIl4p2Z9QZ9%2Fgr9YCjlhVn4i1CNRrrkBO5XT1oHZKJHDYmOZPX4%2Bpumnr8B8Q1Sqxllbdl7OxZ1Gbpr34K&X-Amz-Signature=085e0fdf6ab29aa94158d118be570eccea0d6e6e20952d47fe6a3b2cded7edb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


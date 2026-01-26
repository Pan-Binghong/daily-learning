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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VI7XW4UF%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJIMEYCIQDPgS6t%2FdzoDiHpoR698fN8lf2ZSzC8UEOxHKWCSASQwwIhAL2S7KVhHtVGeUKoLyS9011oSeBjJa1Zq6ZnUzZQMEC4Kv8DCDAQABoMNjM3NDIzMTgzODA1Igz6zbskoe97LQvGQ%2FYq3APejFwKeGQ%2B1egrXcoOHchjTwPlG14ViwUeMAdkGhUNtdp%2BqJ7tgPRcRkX0VkM7bhuX337jOKeFVHroOhSLopitXdMFjYPQ7lMG7eoYayT4Ax073%2FW%2BGhmFjSH%2FI6xwr6DCKFeA%2Fiuy8Jo8JjkiSTdjHJp4JC4gMz2HiAgw%2B9hLSNTuX%2BcNWFVT0vcDu%2BtGl%2F92DL49Rv9qSIu4ildsuLIXyHTIN7%2BpTlGpmzs1dRJ11OjrvSgGWs7lv56zl3kRTUJbsWUQwhRm87unL9OC2hh4kNaMd9yfHTg4QOKTVd3qkvG2%2F%2F%2BqKtmE%2FxUYT90pqbW%2F9GcgszFgUhWcpzNEamYTp%2BBzb9InCiYjkWBVhwvKKzwVty5oxbZojjaYrH%2FPv65RstmuoE4O0P3v8VwmVhwXpZ0L1RQilNG1ghI83HAH5uDOWNDPpUsLREcrihMfh3fVSAmQoXqeimUPNgx9bqquoJYvPMOov3PzyeRsxS20MB9r67rZSXmPmHy4kp%2BolKMR5Vf%2BQt8QRhiy7XgRGW6GxgzunXKhI9iS1k7eW%2FRJ7s%2FIGkPie3s5KerVo8ZYx0pppigY2qpg0arUXnsCDIriA4ahzldK8D9hubtLI%2BButtsyFNvmCl8c2fDdJTDPsNrLBjqkAVZaWeQOj94J3XTWMy7W6bAVl5w4LuMxZs5zWXmZh6Clw9YOjSI1u7PvFXa2VP2j1TDbuLl%2BcFVZzkkS5F6w95kLiKNIkwTBAsMUa4eKZ0iutuE78kw3FbFA8jsZ7KBRaqvJs9tIipA9i9N8%2FLtu37uiCu4zF%2BYbZK1unEkDjq6%2BcLPcyKBf0NTYhSwBkyRlqcYUzUs%2BiEITDuGY5wmBuOSERD1q&X-Amz-Signature=6a942075320b0f2d7639b16ae5fa7db2bb99444e01cf16083cc542cfab760ea2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VI7XW4UF%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJIMEYCIQDPgS6t%2FdzoDiHpoR698fN8lf2ZSzC8UEOxHKWCSASQwwIhAL2S7KVhHtVGeUKoLyS9011oSeBjJa1Zq6ZnUzZQMEC4Kv8DCDAQABoMNjM3NDIzMTgzODA1Igz6zbskoe97LQvGQ%2FYq3APejFwKeGQ%2B1egrXcoOHchjTwPlG14ViwUeMAdkGhUNtdp%2BqJ7tgPRcRkX0VkM7bhuX337jOKeFVHroOhSLopitXdMFjYPQ7lMG7eoYayT4Ax073%2FW%2BGhmFjSH%2FI6xwr6DCKFeA%2Fiuy8Jo8JjkiSTdjHJp4JC4gMz2HiAgw%2B9hLSNTuX%2BcNWFVT0vcDu%2BtGl%2F92DL49Rv9qSIu4ildsuLIXyHTIN7%2BpTlGpmzs1dRJ11OjrvSgGWs7lv56zl3kRTUJbsWUQwhRm87unL9OC2hh4kNaMd9yfHTg4QOKTVd3qkvG2%2F%2F%2BqKtmE%2FxUYT90pqbW%2F9GcgszFgUhWcpzNEamYTp%2BBzb9InCiYjkWBVhwvKKzwVty5oxbZojjaYrH%2FPv65RstmuoE4O0P3v8VwmVhwXpZ0L1RQilNG1ghI83HAH5uDOWNDPpUsLREcrihMfh3fVSAmQoXqeimUPNgx9bqquoJYvPMOov3PzyeRsxS20MB9r67rZSXmPmHy4kp%2BolKMR5Vf%2BQt8QRhiy7XgRGW6GxgzunXKhI9iS1k7eW%2FRJ7s%2FIGkPie3s5KerVo8ZYx0pppigY2qpg0arUXnsCDIriA4ahzldK8D9hubtLI%2BButtsyFNvmCl8c2fDdJTDPsNrLBjqkAVZaWeQOj94J3XTWMy7W6bAVl5w4LuMxZs5zWXmZh6Clw9YOjSI1u7PvFXa2VP2j1TDbuLl%2BcFVZzkkS5F6w95kLiKNIkwTBAsMUa4eKZ0iutuE78kw3FbFA8jsZ7KBRaqvJs9tIipA9i9N8%2FLtu37uiCu4zF%2BYbZK1unEkDjq6%2BcLPcyKBf0NTYhSwBkyRlqcYUzUs%2BiEITDuGY5wmBuOSERD1q&X-Amz-Signature=864cc5c12a9d2aeec9a09ca94fa97cf3c23fa63e26437b925b8191ac39031e96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


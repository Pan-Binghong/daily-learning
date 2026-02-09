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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQAHQM6Q%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE4c7fx6oVSvLlxkxIZvk%2BF7UBnh8pxoozy18Po6HswcAiBpVvwSr61aNBcf5PQtqffhxegi92Iotgpbank5YdD8QSqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMblbTkzpHka3hjFvkKtwDMJGjpNT2KrBejUgo25u1kxgCooJyCsdYJD6e%2Fn2SwpbNSTZJuYadLkuju4GDoND%2BHZtK4RM7kpgd2RVsOCq3TSdq0xZhp8YT9y0th5z7eTT882y0VrR9VaOo90w6M1Sfxw07S1f%2F%2FYuxxRMtajgViat48CRSp%2FeqR84LA95DMQaOvpmnqj8qtso4BTgJTEiLo60MhGKzzZ8uaLWisr6FD%2B1inbeFqubSwwMv%2BvqVFSmCbbXjhd1XgW3wn1yJoVK7Bb3ou1k3aH%2F%2BKgAQLeagS4WdHuswgOgWlu7INIGBRAYM0YAoFNPoeLVmKC2wFHwVngflKDxiuzwdB4p8Zq5mIX%2BnczSQJSMXLkbuUbuTIAigXlXZJYeYgNqX6Y5AJ63fOpGgSEn6u8y6glsx0o7ng%2F8h2VYmptHQdkyHWwiTkHUenVoIy7dgzhnGJ30QTkamjJEu9kVDSf4P0zFHJf%2F4NcNMgJKAxnFhsU5VHs%2BkIx6ow%2BZAG5useZhApSxfYJ%2BbqnhP2Qp%2F8SH7I3VHqnEsXNj9ZDMaerrrP%2FMtexPq6CRSt90LMgDb%2FKuH02B55l7A281xJMyDGzY8uvU53AQjztp%2B5xw4HUZ1C0OFXT7IHQzS5E7tcQTJc%2F5PVH0wr5alzAY6pgG7yhM6O4spWyM84dYarueIZ%2FWPnjj5sgXEU210AIz9Vo7pXT86yaoV8WWk6oFpxarZpg8CiYiUJhtW0o9ISf%2BsNxFyGQBwRAGzq07OsnBexbvwhPBHUNFLPcGZKsqNlTrSf8ptuaDrvhXtuDEoo9aIPWOPwlOjZ7oB49fRvhntjbMT5kyTW2QZru4GVyY8IPD3Or8TFMEK%2B3ryKiURzyKZYv%2Bb17%2Fi&X-Amz-Signature=1deb8e561e750ac807f1587d850d714ca215c27132128f7dccdcaca912595f6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQAHQM6Q%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE4c7fx6oVSvLlxkxIZvk%2BF7UBnh8pxoozy18Po6HswcAiBpVvwSr61aNBcf5PQtqffhxegi92Iotgpbank5YdD8QSqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMblbTkzpHka3hjFvkKtwDMJGjpNT2KrBejUgo25u1kxgCooJyCsdYJD6e%2Fn2SwpbNSTZJuYadLkuju4GDoND%2BHZtK4RM7kpgd2RVsOCq3TSdq0xZhp8YT9y0th5z7eTT882y0VrR9VaOo90w6M1Sfxw07S1f%2F%2FYuxxRMtajgViat48CRSp%2FeqR84LA95DMQaOvpmnqj8qtso4BTgJTEiLo60MhGKzzZ8uaLWisr6FD%2B1inbeFqubSwwMv%2BvqVFSmCbbXjhd1XgW3wn1yJoVK7Bb3ou1k3aH%2F%2BKgAQLeagS4WdHuswgOgWlu7INIGBRAYM0YAoFNPoeLVmKC2wFHwVngflKDxiuzwdB4p8Zq5mIX%2BnczSQJSMXLkbuUbuTIAigXlXZJYeYgNqX6Y5AJ63fOpGgSEn6u8y6glsx0o7ng%2F8h2VYmptHQdkyHWwiTkHUenVoIy7dgzhnGJ30QTkamjJEu9kVDSf4P0zFHJf%2F4NcNMgJKAxnFhsU5VHs%2BkIx6ow%2BZAG5useZhApSxfYJ%2BbqnhP2Qp%2F8SH7I3VHqnEsXNj9ZDMaerrrP%2FMtexPq6CRSt90LMgDb%2FKuH02B55l7A281xJMyDGzY8uvU53AQjztp%2B5xw4HUZ1C0OFXT7IHQzS5E7tcQTJc%2F5PVH0wr5alzAY6pgG7yhM6O4spWyM84dYarueIZ%2FWPnjj5sgXEU210AIz9Vo7pXT86yaoV8WWk6oFpxarZpg8CiYiUJhtW0o9ISf%2BsNxFyGQBwRAGzq07OsnBexbvwhPBHUNFLPcGZKsqNlTrSf8ptuaDrvhXtuDEoo9aIPWOPwlOjZ7oB49fRvhntjbMT5kyTW2QZru4GVyY8IPD3Or8TFMEK%2B3ryKiURzyKZYv%2Bb17%2Fi&X-Amz-Signature=299e678f2e88a3bb1bc957459ff6919b050234bd165111c3a26a86de467aee74&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


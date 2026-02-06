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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLCTVS67%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIHilIIgLvHX5HF0z1X9e5nysJibyngQLfNdccMZ%2B6XHBAiBOmIk6s3O2B7g5oq50I4hJmFSKHB8Ys4%2FKHoz%2BaYdTNCr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIM1vRJMhnTSGLF%2FMczKtwDp3gg6RuiXog5IPIZys9%2BEob1jXoQuYGGyJ1E0ONwT%2FVOFO0beDwgwawoiSJeJFePIQj3ktSeYfyoF0pYMQYpA%2B1tnvK5F4VIMLObfmZwADZyYHduOstbDaVljZNDN8m23HCv7du0fAXeQc6Kyi0Jlw5NEcaQ9omlmssXigMJfEu6cBWUi57eXFPzbIwpELoavHr%2BItwtV4lRPsymaEmDzRP68jOMAxHJdisxepudEG1xflnfYGMPALwHTcKAXnE%2FeuhkFZBltvooZaPwVJyJwpB7ogkFngvSCG3vPq7rr1S%2FOeboCsfSCTc0UsjUO1COgd7SWR9Sjoby8%2BqoJzpEH3XB%2B7P7yc8KXhmgUH%2FBiwG%2Fpkm2TvhJHVZGwiYnycGuvtla%2BAi8C%2Bv450YEh%2F7t0YhWiFt9dmRL9ojvmtYRQBQZwjGJ2pStYcPJ%2BsuDkKxGUWoIG6%2BbFwEO3NO7fzEBVlgZFjTTPV06Jq6d6qUQQMeptbAm2jTYjGvNSzigP7uGs7GQxWGnWoLJnyxA%2F%2BJ%2FFuQbuwsHwbs3937vlbS6x4aArbyp3qFiJdWU02Wvx2nkILNKROMocM28kBt%2B%2BGXJN4sOM0qmGK16Q5qfPmrvW3gAJE79x1y2KKSuyYgwsLmVzAY6pgGO21RjUm1oMloAdFdPe1gzybCTgt5ER3BeSFPov1yfGoQQ5ne7G9dE%2BSv0z2GVCVVadNbGdBpMaYXIKCegfS7b4fCWmp2ACHNJ0wnu6I1OBXOe2Ho2KyGBHJ43EUkrrp%2BDYXvp8erO5SxROSMcp2ln19kwfTl5Jx0oJKjFAITNRF51WfjA9VDR3qip7Iyhp48wNq5UXzRnMk6%2Bi75NZfir9JcgaLGO&X-Amz-Signature=051dffab54507f411988394ea75bcc43338b4b028549733d7bf7957073be9077&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLCTVS67%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIHilIIgLvHX5HF0z1X9e5nysJibyngQLfNdccMZ%2B6XHBAiBOmIk6s3O2B7g5oq50I4hJmFSKHB8Ys4%2FKHoz%2BaYdTNCr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIM1vRJMhnTSGLF%2FMczKtwDp3gg6RuiXog5IPIZys9%2BEob1jXoQuYGGyJ1E0ONwT%2FVOFO0beDwgwawoiSJeJFePIQj3ktSeYfyoF0pYMQYpA%2B1tnvK5F4VIMLObfmZwADZyYHduOstbDaVljZNDN8m23HCv7du0fAXeQc6Kyi0Jlw5NEcaQ9omlmssXigMJfEu6cBWUi57eXFPzbIwpELoavHr%2BItwtV4lRPsymaEmDzRP68jOMAxHJdisxepudEG1xflnfYGMPALwHTcKAXnE%2FeuhkFZBltvooZaPwVJyJwpB7ogkFngvSCG3vPq7rr1S%2FOeboCsfSCTc0UsjUO1COgd7SWR9Sjoby8%2BqoJzpEH3XB%2B7P7yc8KXhmgUH%2FBiwG%2Fpkm2TvhJHVZGwiYnycGuvtla%2BAi8C%2Bv450YEh%2F7t0YhWiFt9dmRL9ojvmtYRQBQZwjGJ2pStYcPJ%2BsuDkKxGUWoIG6%2BbFwEO3NO7fzEBVlgZFjTTPV06Jq6d6qUQQMeptbAm2jTYjGvNSzigP7uGs7GQxWGnWoLJnyxA%2F%2BJ%2FFuQbuwsHwbs3937vlbS6x4aArbyp3qFiJdWU02Wvx2nkILNKROMocM28kBt%2B%2BGXJN4sOM0qmGK16Q5qfPmrvW3gAJE79x1y2KKSuyYgwsLmVzAY6pgGO21RjUm1oMloAdFdPe1gzybCTgt5ER3BeSFPov1yfGoQQ5ne7G9dE%2BSv0z2GVCVVadNbGdBpMaYXIKCegfS7b4fCWmp2ACHNJ0wnu6I1OBXOe2Ho2KyGBHJ43EUkrrp%2BDYXvp8erO5SxROSMcp2ln19kwfTl5Jx0oJKjFAITNRF51WfjA9VDR3qip7Iyhp48wNq5UXzRnMk6%2Bi75NZfir9JcgaLGO&X-Amz-Signature=b41e3214c17855235367d1fdae57d582865252eb0473bc23f79c4d29b8d4c58d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


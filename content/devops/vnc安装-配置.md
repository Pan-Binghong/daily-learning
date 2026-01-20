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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666F4TKEEX%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDj2%2FV67OX9Z6Rjfvoc%2FSi8bQ7tXnf0uCIoZ3ubTiPSwIgMFGfuvbC9gQL4s45UVgrjnUbZ%2FQlZ5Rn7GjGGIOtQKIqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB0mmfU8MSQiQE60uyrcA%2FFZ4udkG%2FtvungdyUC3k7cGxl0pfK%2Bh0mqzVnYCJnvm3hqbfYHKUmrC6C3gMOM5eUn1HEFzd6uMO2n4wycBthLAg%2B2Zavx5aCAnwKG%2BolA%2BNSPhL6MfIPqjutMfRETuT53a8ngiqZiR0m7memmEV%2BJeTqil0tMw6UZrlttzXcDW9fuJXCfmHY3dR9nE2%2FJOByVCAG3hBrqOQqMB7TeuQ29W08be38IPJK1jM1a%2F78l4cmqveD73u9QyIDqAZr7YEtg72bucYgHKZwOIBjrsPOx4W7ZRCv%2Fh5JixT1U6xSoXE4dIRyqvuUO0b7HrA7jm7x8QDi%2BeiFaCRK6CGNkOjhCaDUAU1uB%2BfA%2FKOA2LHSMx3TaFJrZUdHcS7PzQfh84qKc9Jf2Xp6slBe0v%2BvnvC4Ih6ySKmWXFQFD4RSsQJIpT7owrv6g6ZiaQVZBOPApzJrz3GGm%2FmYEi%2BogDc6Tek5ULS%2FGcRC8HsL4wSQmhB9Zwwq9FR8sozT7et1mALs1ONCxyk0KW0Yx0H5w3dRBq9Huyi24gZw3C6Nxl9Pe9wqClKxc1toq7VOVTgLcRiYdKzJzBGyLwEb%2BZjiGuKJ4NIc3nBXXkK8DsiCGMZcqYYXrOyyfctKdDaP%2B%2F5qnKMPf0ussGOqUBkWux8kAzf7UVkAZ6TPz9oSLod0QaOZMxqvlGEFcFRIUOHhpN0KXoqz%2BSX%2FrwXytiYQLqqgm%2FzsW7wbTKVWHFSxjHeuSRITuggwoDX5swP0HtJDA5hzIn0US15a9J9tTklk5IJcUVyCfh85uyTmcCiTRYw%2FqwpdxPL7yANOaDDwVa4mIr1sFaGzGLMA8AV9FWbxZYcgE%2FeQaeFKyhmyy%2B6sTQABWD&X-Amz-Signature=f318ed333abff3d8bcae64f9f58db21361442a48d31a73303f56cb8440c20db3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666F4TKEEX%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDj2%2FV67OX9Z6Rjfvoc%2FSi8bQ7tXnf0uCIoZ3ubTiPSwIgMFGfuvbC9gQL4s45UVgrjnUbZ%2FQlZ5Rn7GjGGIOtQKIqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB0mmfU8MSQiQE60uyrcA%2FFZ4udkG%2FtvungdyUC3k7cGxl0pfK%2Bh0mqzVnYCJnvm3hqbfYHKUmrC6C3gMOM5eUn1HEFzd6uMO2n4wycBthLAg%2B2Zavx5aCAnwKG%2BolA%2BNSPhL6MfIPqjutMfRETuT53a8ngiqZiR0m7memmEV%2BJeTqil0tMw6UZrlttzXcDW9fuJXCfmHY3dR9nE2%2FJOByVCAG3hBrqOQqMB7TeuQ29W08be38IPJK1jM1a%2F78l4cmqveD73u9QyIDqAZr7YEtg72bucYgHKZwOIBjrsPOx4W7ZRCv%2Fh5JixT1U6xSoXE4dIRyqvuUO0b7HrA7jm7x8QDi%2BeiFaCRK6CGNkOjhCaDUAU1uB%2BfA%2FKOA2LHSMx3TaFJrZUdHcS7PzQfh84qKc9Jf2Xp6slBe0v%2BvnvC4Ih6ySKmWXFQFD4RSsQJIpT7owrv6g6ZiaQVZBOPApzJrz3GGm%2FmYEi%2BogDc6Tek5ULS%2FGcRC8HsL4wSQmhB9Zwwq9FR8sozT7et1mALs1ONCxyk0KW0Yx0H5w3dRBq9Huyi24gZw3C6Nxl9Pe9wqClKxc1toq7VOVTgLcRiYdKzJzBGyLwEb%2BZjiGuKJ4NIc3nBXXkK8DsiCGMZcqYYXrOyyfctKdDaP%2B%2F5qnKMPf0ussGOqUBkWux8kAzf7UVkAZ6TPz9oSLod0QaOZMxqvlGEFcFRIUOHhpN0KXoqz%2BSX%2FrwXytiYQLqqgm%2FzsW7wbTKVWHFSxjHeuSRITuggwoDX5swP0HtJDA5hzIn0US15a9J9tTklk5IJcUVyCfh85uyTmcCiTRYw%2FqwpdxPL7yANOaDDwVa4mIr1sFaGzGLMA8AV9FWbxZYcgE%2FeQaeFKyhmyy%2B6sTQABWD&X-Amz-Signature=899f714ee9b38e91dbe695d599d8676cb9cb47fa357947de85dcf810b0911cbc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


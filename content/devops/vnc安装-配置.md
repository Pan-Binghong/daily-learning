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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4ZNDNIN%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEhggiIhvGik5%2FYCCMbXnO%2BTUznkGD%2BKjqmDL%2B4LerhJAiBTIh5qiT9vtg571GoP7UxPHBCf6Igb30jNnMjTUSm8jSr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMWwKVnPMjWNrLhMeuKtwDqquA4YEjnvmpkJDglkVSvcD9tf64AWCWjOSMHz8REJHKGbHJCO5rsu%2FxIIlCJ9VoDuP%2F1WrLUqhlWzEWRDIjonosx4JMH%2FNFMW5swfpUisPG9omrCr0OKBn57r%2FcWieX31u%2FESy52AWTuUEyrDZrQsJ4%2Fw8fHDLdBZW3jJLzMO3g8VK%2BeMkIDsin0uEkGBIFPtknd6VKyX4hjklH8UYt6AE2I%2FKUcCLAINteU5WACRCf1X%2FeZVZHZJsnG1weHnMnqarhxq9XhcCHMuCa2UfSLAAI%2Biqjmdb3FnK9T7vW97MNrrxbfMYL%2BEDTJEcm%2FLeRspUI8HpXz43ZbpNszjvCxW1B2eGeQRyrNY6XVi8m%2Fxn4fuqqMQ3ViDCI7bmqo8a9soKd6pN5zq52jek2KMPecz8%2Bh8Nrnnbp5vkuwY1m%2BnRqw01VuIYESh2w40QzCVKEcBHFKKqgRpRgLrHEpHdr%2Fvm0Qvs9opcnKgwVJoT5aa9w84byHrlVdAOELftKYzN2vLk9Jy2A7OZ5Lyv%2FKKUjB1yLC8pXoLENtewU8kHTGkcNFWl4n00q%2FymXBgxcWD6w%2FhxNgfVzGoJizEhpsp1HvJv4iCHuZfpHphR5YGxLezFAa5h8zlm90PFAFgMwsP6TzQY6pgGQJaRj4P20yo5iuQC5x%2B2sjuQuzpMgvysuWyzc0lZ55QtzMN%2BDQIMW2IINQCyMDYdcnef5ThjMHi9l569Ybr32QGczrWD%2Fnfp9FrcLNtTpG%2FHJYpXBKg6%2F9ohTPxH0CFBnTPn3peSqn6BiI4trGuFotNMNNWkTKHwcqssIqyyRGNPm75PWr2oaLVPn69565KaILbcPqeJi1DVNEtN7IwRWfKJbtRSa&X-Amz-Signature=867679fb166d8870a38fa6f4b75fb04cdd4d9ff0dac3b8ad03e1851f36f52d54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4ZNDNIN%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEhggiIhvGik5%2FYCCMbXnO%2BTUznkGD%2BKjqmDL%2B4LerhJAiBTIh5qiT9vtg571GoP7UxPHBCf6Igb30jNnMjTUSm8jSr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMWwKVnPMjWNrLhMeuKtwDqquA4YEjnvmpkJDglkVSvcD9tf64AWCWjOSMHz8REJHKGbHJCO5rsu%2FxIIlCJ9VoDuP%2F1WrLUqhlWzEWRDIjonosx4JMH%2FNFMW5swfpUisPG9omrCr0OKBn57r%2FcWieX31u%2FESy52AWTuUEyrDZrQsJ4%2Fw8fHDLdBZW3jJLzMO3g8VK%2BeMkIDsin0uEkGBIFPtknd6VKyX4hjklH8UYt6AE2I%2FKUcCLAINteU5WACRCf1X%2FeZVZHZJsnG1weHnMnqarhxq9XhcCHMuCa2UfSLAAI%2Biqjmdb3FnK9T7vW97MNrrxbfMYL%2BEDTJEcm%2FLeRspUI8HpXz43ZbpNszjvCxW1B2eGeQRyrNY6XVi8m%2Fxn4fuqqMQ3ViDCI7bmqo8a9soKd6pN5zq52jek2KMPecz8%2Bh8Nrnnbp5vkuwY1m%2BnRqw01VuIYESh2w40QzCVKEcBHFKKqgRpRgLrHEpHdr%2Fvm0Qvs9opcnKgwVJoT5aa9w84byHrlVdAOELftKYzN2vLk9Jy2A7OZ5Lyv%2FKKUjB1yLC8pXoLENtewU8kHTGkcNFWl4n00q%2FymXBgxcWD6w%2FhxNgfVzGoJizEhpsp1HvJv4iCHuZfpHphR5YGxLezFAa5h8zlm90PFAFgMwsP6TzQY6pgGQJaRj4P20yo5iuQC5x%2B2sjuQuzpMgvysuWyzc0lZ55QtzMN%2BDQIMW2IINQCyMDYdcnef5ThjMHi9l569Ybr32QGczrWD%2Fnfp9FrcLNtTpG%2FHJYpXBKg6%2F9ohTPxH0CFBnTPn3peSqn6BiI4trGuFotNMNNWkTKHwcqssIqyyRGNPm75PWr2oaLVPn69565KaILbcPqeJi1DVNEtN7IwRWfKJbtRSa&X-Amz-Signature=169a23ce6ae5a4973de3cd8fdf9d47a59f771f432b2d0b92373c643f9c1ebc65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


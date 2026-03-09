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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VDFONXV%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIH2HNPLVADgToT%2BBzPlpk%2F9c1A48%2Bvc2UaEy5pmmqQk%2BAiB7z8bhZyLbzDNZYruqkRImqjyLEFxal4wxOnPW0EQylCr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMw7DflUemKbV9SyXKKtwDrfGeUKOJ%2Beg16ZoBqeGn943yCdUsQzZX6oB5zSA%2FrjkO5W2f41DS8Ftp0i1DQmNws1EdvSHNFnK1ptiWp%2Bo2cAX0PJaPyNT2kvl6IzmQOFO30a0JAdpmCchym02gfyRhpwtESTulGMqmbuRHBHTPri78pGm9YaTGEfs0fNhLqve3OygN8zZdddoI7siMK8%2BDyJxoOBglziPe1M3J6it8eEoBrK93usPfVj16f1vENNOmzOj6LIde9kvFh4Z8rQmdfwSU2CLFFEWp%2FmQ7Bypah3UAuzCOdYjRN8WqaLl8W7OAi36QN8rlR8MzpSE7v7rL6UIwiKSKKHsk64vtUS9Zn%2BdCEz9wGG3f5hj7EFvwxld%2FE1i%2B%2FZ13KTbuQtNqwlhZd%2FCnCszf72v44BGBh6r6qBAL%2FZfBiRY5JnvnS03822yiovuzQ%2BW9fxM4jYpWaW8yH3e9zdD1NGitUGmre436TxvaVEL3%2BCC72rTU9%2B%2Fp9Rul%2BKrP4xod4bwLnKQSy7pZGvGrgvoera7UkC%2FJl4%2Fu5cOsIob7KJ6PvGPAYxNklIyTDWayZzCcUJOnxA%2FBkiPZKg1IXlKsu6kSV9KHyXgfkqqLHyfVegMqsHnofYd9pY%2BAGOeR83dikhKI5bAwtv24zQY6pgFxLElHRg8IsRxMTAZtYnlba2BC0ZDSg56OH0xGaDKA%2FM7k%2FRgHuhPe5KZ2LWC7AO7APrrgABFkYQj9NBZyipoczWskz2d3SUYrLluiETPyD9MsogC3EF3d8f7beaTyWJ6gbJsGytlsPg91eucTO%2FWLqSWBNfLTi%2F2DSpw8B5JYOl7bxh8pz2WEQo4bBuVmH5XEETgiJcBXbG8mrCACrb9odd4hHJId&X-Amz-Signature=48e3b381a0c4f9c466e8ff8756a6c3dcbbbd5b15727da85a9148375e7a21097c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VDFONXV%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIH2HNPLVADgToT%2BBzPlpk%2F9c1A48%2Bvc2UaEy5pmmqQk%2BAiB7z8bhZyLbzDNZYruqkRImqjyLEFxal4wxOnPW0EQylCr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMw7DflUemKbV9SyXKKtwDrfGeUKOJ%2Beg16ZoBqeGn943yCdUsQzZX6oB5zSA%2FrjkO5W2f41DS8Ftp0i1DQmNws1EdvSHNFnK1ptiWp%2Bo2cAX0PJaPyNT2kvl6IzmQOFO30a0JAdpmCchym02gfyRhpwtESTulGMqmbuRHBHTPri78pGm9YaTGEfs0fNhLqve3OygN8zZdddoI7siMK8%2BDyJxoOBglziPe1M3J6it8eEoBrK93usPfVj16f1vENNOmzOj6LIde9kvFh4Z8rQmdfwSU2CLFFEWp%2FmQ7Bypah3UAuzCOdYjRN8WqaLl8W7OAi36QN8rlR8MzpSE7v7rL6UIwiKSKKHsk64vtUS9Zn%2BdCEz9wGG3f5hj7EFvwxld%2FE1i%2B%2FZ13KTbuQtNqwlhZd%2FCnCszf72v44BGBh6r6qBAL%2FZfBiRY5JnvnS03822yiovuzQ%2BW9fxM4jYpWaW8yH3e9zdD1NGitUGmre436TxvaVEL3%2BCC72rTU9%2B%2Fp9Rul%2BKrP4xod4bwLnKQSy7pZGvGrgvoera7UkC%2FJl4%2Fu5cOsIob7KJ6PvGPAYxNklIyTDWayZzCcUJOnxA%2FBkiPZKg1IXlKsu6kSV9KHyXgfkqqLHyfVegMqsHnofYd9pY%2BAGOeR83dikhKI5bAwtv24zQY6pgFxLElHRg8IsRxMTAZtYnlba2BC0ZDSg56OH0xGaDKA%2FM7k%2FRgHuhPe5KZ2LWC7AO7APrrgABFkYQj9NBZyipoczWskz2d3SUYrLluiETPyD9MsogC3EF3d8f7beaTyWJ6gbJsGytlsPg91eucTO%2FWLqSWBNfLTi%2F2DSpw8B5JYOl7bxh8pz2WEQo4bBuVmH5XEETgiJcBXbG8mrCACrb9odd4hHJId&X-Amz-Signature=1a371e1d7b254c5fb68598bf83dbb3d0c5f550b5ee70380e81e4bda087aa2019&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


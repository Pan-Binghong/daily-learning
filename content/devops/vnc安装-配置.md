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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HP3F2XH%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCICiqKBjfc7MkD6beXtrK9PNIXBkWm0VBcHgHIpRyCYrmAiEAn0YLaOOwFOSYIkjQS9sHpftUaEXRQH0fPZromnsmUJMqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGcRyKlS5DS4pg3OZCrcAxVtCUi6QFlmAqcVbDFHi5vhzWLFGt%2BQ9MVzGQfz8KYRB3wBs3KXx2DP%2B0HVDi7aKumQMvDYYFqRv6xbYTY4%2FLIv%2Bx%2FAPj6DY8wI9ndSv%2Bcefx95nahfyFKN3iyaqM8xgjn5hG%2FUlnv6V2t5SNx15FL%2FtcszVt5lxup2sovlSx1VslqenShyYQ3dz8zLvi7SGo4jLuvGjQDVqROd5QQ0xr8d35eAX0%2Bi2fKOSJR%2BPrWd8ukT8ZF1ryx6FLW66u9ZyUAo6EgR9qsevtq8NIwZYAL1%2FLzXt4g7KGUpWSNn5%2B9cgF9KeztmYGY9f5ebLoS3lmYA6c3FHOR7A2ZM%2Fk%2BaC6ChpqNSon8okS6PzNtYmZ%2Fz0AnJ0yItk92XEHmYwA5K0yPcJeDRCh03kjF0hakFO5%2BUotYlM4ysU7ETanc7G%2BXc%2BFSbnghyy93ZsNrYHC67AGZ1hiBi6Ed0u37C5ktS9bZ2DJZImTyhhQu73fy1d91qnhoht9TsIbltsQoFzX7GGwzoAkoa%2BebGOtdd15YKOPA%2Fuco86klR1s2Koskivqc8E%2FAVDVTFvf6vTU9r7%2FXq8pwAj6yhuvgqER7nZ%2B0vuZSw178pyPGZux805ceOFTAshGDeziEV26WfbQOaMLm93c0GOqUBVyF3OmVdL3D0q1l3SnfNaE0kDZof6laTn%2BcEfHficoOvmps%2Bs%2B1fh2HKcryDhFR2gMcFTW3Z%2B5V77xaKHTprLZKkitTS3q0CHNvM%2Bkv4mFLMF44wgZnE2O%2B8pH%2FawFJcb9VqOsTisZGxGncChxt4JYL8xiZMguUhOD0wHuX5LQdjEdIBQjtMvA9P18VSzA78Bez21JoXg%2FFsu2oZdRcQe6cLCtGs&X-Amz-Signature=8b5a750ce4e67fbd0743ab22367c384e5895e11ce15e38fdafb040e38f759b0c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HP3F2XH%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCICiqKBjfc7MkD6beXtrK9PNIXBkWm0VBcHgHIpRyCYrmAiEAn0YLaOOwFOSYIkjQS9sHpftUaEXRQH0fPZromnsmUJMqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGcRyKlS5DS4pg3OZCrcAxVtCUi6QFlmAqcVbDFHi5vhzWLFGt%2BQ9MVzGQfz8KYRB3wBs3KXx2DP%2B0HVDi7aKumQMvDYYFqRv6xbYTY4%2FLIv%2Bx%2FAPj6DY8wI9ndSv%2Bcefx95nahfyFKN3iyaqM8xgjn5hG%2FUlnv6V2t5SNx15FL%2FtcszVt5lxup2sovlSx1VslqenShyYQ3dz8zLvi7SGo4jLuvGjQDVqROd5QQ0xr8d35eAX0%2Bi2fKOSJR%2BPrWd8ukT8ZF1ryx6FLW66u9ZyUAo6EgR9qsevtq8NIwZYAL1%2FLzXt4g7KGUpWSNn5%2B9cgF9KeztmYGY9f5ebLoS3lmYA6c3FHOR7A2ZM%2Fk%2BaC6ChpqNSon8okS6PzNtYmZ%2Fz0AnJ0yItk92XEHmYwA5K0yPcJeDRCh03kjF0hakFO5%2BUotYlM4ysU7ETanc7G%2BXc%2BFSbnghyy93ZsNrYHC67AGZ1hiBi6Ed0u37C5ktS9bZ2DJZImTyhhQu73fy1d91qnhoht9TsIbltsQoFzX7GGwzoAkoa%2BebGOtdd15YKOPA%2Fuco86klR1s2Koskivqc8E%2FAVDVTFvf6vTU9r7%2FXq8pwAj6yhuvgqER7nZ%2B0vuZSw178pyPGZux805ceOFTAshGDeziEV26WfbQOaMLm93c0GOqUBVyF3OmVdL3D0q1l3SnfNaE0kDZof6laTn%2BcEfHficoOvmps%2Bs%2B1fh2HKcryDhFR2gMcFTW3Z%2B5V77xaKHTprLZKkitTS3q0CHNvM%2Bkv4mFLMF44wgZnE2O%2B8pH%2FawFJcb9VqOsTisZGxGncChxt4JYL8xiZMguUhOD0wHuX5LQdjEdIBQjtMvA9P18VSzA78Bez21JoXg%2FFsu2oZdRcQe6cLCtGs&X-Amz-Signature=0e914c902f0b2e55b7e2cd6b6801af79967eaf90d14032baa3214511baa90f64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


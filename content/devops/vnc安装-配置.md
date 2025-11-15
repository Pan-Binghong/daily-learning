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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMUERCXX%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T024003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCx0H0EjuEbW1T95%2FS%2F1qkIkESc6RN%2FKeXXjm5nfZVQiwIgazZBhl7ROCP8om5qWpgeuNsX0MN%2BwtFzoD18TJl%2BvKAq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDFo0PLeXWrA3TuPisSrcAxogyhnQjOnfbR4uX%2BsevrPtEGb8%2FQgVarFyoa%2FjkW%2B3xurbzxyV19lg1VDqBzboCsoDWgOpZ9t3ysLDYNDDMHiwtAD1KBYUWX4karEiYoW3S9IS2geGZcD%2BvXdXX9qkXLVpRCzfgX8rJVSCeksU2Xm5vySOLZZCgkOTuy5Ma6mhUoDPT38oL%2Bqc0MFpdnIzw3gQ44vJXI0uGJGKnQAlWdlLZtWiixFbt0qxBRJyM6ly3jAy4Q6Mr0kss%2BvTwZJHFMtbPSocdnAOdWZAVXUyzid0hjtC%2FU7Dh%2FLrNDjXRVuu6qpF60OXKxPw1EVpaNlh15s11eiQv3%2B1OxDh%2BPAxswWrBFI9WvCI5oI3UK1DGRtwDzRCrNRL9EpSjylN%2FEBw%2FddoNKXkjhb0wpSZqcR0BwZneEST14%2F3OcfZCJxS1oB59OwqVkmPa2UFfxUsfcWjG1xLaOMASrYIWz5kDVDHsFzflPwGHfic9XSqCBwgNI7TJBm%2FLcskrDJ%2B8qcKZATxfSylFxXKGTPn%2Bu9if6HJ%2BVR%2BHOT5kzFqlpPJKJuEDi4Vw45Q7hUwDAOaort6Rd0WeKBuITemTPrufJZGQ8U1iQgUSIvwnMx96cWysqXJi7co0uGedEgnLHdaGpQjMIzB38gGOqUB%2F7ajd9zJQZU6ZyMA5cb9JBvQR8kMXFlPyd7Xmy%2BNAzJT%2BAIMJBIjfsP7nBM%2FE2a47FQe0yrc0l09BnrVOnqjRrP5JN9XwZIR%2BR2nwmzVjEHlqG6BTHXrSQ9vhmVuKD%2FQtLsdNUxHTpfFs45aA9Kti8hzUceKExkUzxXetUfzRjSYODk%2FyDHrjLarG%2FyjEIl0cg61y9STtjWHo0FoygJhbIbK%2F7EO&X-Amz-Signature=a192aa9ec8228318173d451180a8e24afcf30bd501784886eea81109ca98130b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMUERCXX%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T024003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCx0H0EjuEbW1T95%2FS%2F1qkIkESc6RN%2FKeXXjm5nfZVQiwIgazZBhl7ROCP8om5qWpgeuNsX0MN%2BwtFzoD18TJl%2BvKAq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDFo0PLeXWrA3TuPisSrcAxogyhnQjOnfbR4uX%2BsevrPtEGb8%2FQgVarFyoa%2FjkW%2B3xurbzxyV19lg1VDqBzboCsoDWgOpZ9t3ysLDYNDDMHiwtAD1KBYUWX4karEiYoW3S9IS2geGZcD%2BvXdXX9qkXLVpRCzfgX8rJVSCeksU2Xm5vySOLZZCgkOTuy5Ma6mhUoDPT38oL%2Bqc0MFpdnIzw3gQ44vJXI0uGJGKnQAlWdlLZtWiixFbt0qxBRJyM6ly3jAy4Q6Mr0kss%2BvTwZJHFMtbPSocdnAOdWZAVXUyzid0hjtC%2FU7Dh%2FLrNDjXRVuu6qpF60OXKxPw1EVpaNlh15s11eiQv3%2B1OxDh%2BPAxswWrBFI9WvCI5oI3UK1DGRtwDzRCrNRL9EpSjylN%2FEBw%2FddoNKXkjhb0wpSZqcR0BwZneEST14%2F3OcfZCJxS1oB59OwqVkmPa2UFfxUsfcWjG1xLaOMASrYIWz5kDVDHsFzflPwGHfic9XSqCBwgNI7TJBm%2FLcskrDJ%2B8qcKZATxfSylFxXKGTPn%2Bu9if6HJ%2BVR%2BHOT5kzFqlpPJKJuEDi4Vw45Q7hUwDAOaort6Rd0WeKBuITemTPrufJZGQ8U1iQgUSIvwnMx96cWysqXJi7co0uGedEgnLHdaGpQjMIzB38gGOqUB%2F7ajd9zJQZU6ZyMA5cb9JBvQR8kMXFlPyd7Xmy%2BNAzJT%2BAIMJBIjfsP7nBM%2FE2a47FQe0yrc0l09BnrVOnqjRrP5JN9XwZIR%2BR2nwmzVjEHlqG6BTHXrSQ9vhmVuKD%2FQtLsdNUxHTpfFs45aA9Kti8hzUceKExkUzxXetUfzRjSYODk%2FyDHrjLarG%2FyjEIl0cg61y9STtjWHo0FoygJhbIbK%2F7EO&X-Amz-Signature=b3d606aae4216fb53a102cab3987ab86088ee2ff5efcba6557e820d369fedc52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


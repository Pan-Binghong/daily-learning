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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RT4FUMZD%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFoejeiN%2FwrscH2ur0u%2B55PAhlcFb7iSEbcRmQKCq1AlAiEAl9KtVFdKhyRiuQFzXvpc1WBHqjEQDXvXx1k5UiOXqPgq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDKogw68nNg4EcH6DySrcA9O0kdlKTl65Y%2FP0YiA14X9px4q7BkK1i%2Bbfg0%2FofL09TLT2N1ZgBeefCOT95G5yVGeglhCqyfZ36R8QFUjKKxXgAFDaxhRFNbl39FLGnUHwzOvPrJRwerMBWm3JSTDt9R9uv1Ga2Av1Pn1txwi018%2BC3A7zQlmmfmf8wBbagPCudRg6KEl4%2FzwBLhK%2Bj1PCzIl9TRRKgKulwIOYGmFVKcZaDDEYs3I%2B4O0yLKcBD4Qj%2BkX9DaKNgpxTgzROHrrbfCqR7WSXCy7dWpJve8l872w%2BFdn%2BVPBcpr0nx%2FCOWS2WM8zGRVzMDZLftFwgjRK2a71%2FwcS3%2BZ2Ev%2BUevoVZg0bUzp2CT%2BqUwq%2FsIXoLp9GNmxuNZjsjU1N13mCuj87M%2FDYeEIeu3MnYPgW1xdmGeMTA3RDmkXBCjV3czsaJU4hrkUJRE3tfS1KIqiswNNmdMFT76y9UWsZRlC4NRSK2wsYA24nMkXWhA%2FoFau6s8Blm5laPM8bmLuwy7BGEO3%2BxiHPVK%2Fk7flm%2FxLKMczMCIQqoQyCha%2BO5XvdoRSRXhmXmflS3%2Fb4p6fOmpdeMpogzMLLPJ03rwoYyxHxyNpPXcSTaPyOO7Fbn3w8ueWnAYn%2FwWI6HMMm0OWkpPVfzMNCLoMwGOqUB08Wx6R6pVUiiV80HSduuXye5jhuWLdf6nEf60sW696XQNsomYkWA0c8E%2F%2Becbq1pstsaVKhd2mD24wXL9C7Wf%2Bw1uHVnqVHQWHPiDdJAqdh8OAQNIXtt5PHEVUdPFMJf%2BGJqrQL9ePCvunW4cgCq2VW74UNIKp15iomlurwfRDgFETVl8qCeXxjPIh3tN0OoJfJi1gn9SWZ9ZQszNpbVgxzMFwwn&X-Amz-Signature=562252fab83f9389cab3fcddd0476d1ddcf07bc524fe6431a04b05e5d2e6a2c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RT4FUMZD%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFoejeiN%2FwrscH2ur0u%2B55PAhlcFb7iSEbcRmQKCq1AlAiEAl9KtVFdKhyRiuQFzXvpc1WBHqjEQDXvXx1k5UiOXqPgq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDKogw68nNg4EcH6DySrcA9O0kdlKTl65Y%2FP0YiA14X9px4q7BkK1i%2Bbfg0%2FofL09TLT2N1ZgBeefCOT95G5yVGeglhCqyfZ36R8QFUjKKxXgAFDaxhRFNbl39FLGnUHwzOvPrJRwerMBWm3JSTDt9R9uv1Ga2Av1Pn1txwi018%2BC3A7zQlmmfmf8wBbagPCudRg6KEl4%2FzwBLhK%2Bj1PCzIl9TRRKgKulwIOYGmFVKcZaDDEYs3I%2B4O0yLKcBD4Qj%2BkX9DaKNgpxTgzROHrrbfCqR7WSXCy7dWpJve8l872w%2BFdn%2BVPBcpr0nx%2FCOWS2WM8zGRVzMDZLftFwgjRK2a71%2FwcS3%2BZ2Ev%2BUevoVZg0bUzp2CT%2BqUwq%2FsIXoLp9GNmxuNZjsjU1N13mCuj87M%2FDYeEIeu3MnYPgW1xdmGeMTA3RDmkXBCjV3czsaJU4hrkUJRE3tfS1KIqiswNNmdMFT76y9UWsZRlC4NRSK2wsYA24nMkXWhA%2FoFau6s8Blm5laPM8bmLuwy7BGEO3%2BxiHPVK%2Fk7flm%2FxLKMczMCIQqoQyCha%2BO5XvdoRSRXhmXmflS3%2Fb4p6fOmpdeMpogzMLLPJ03rwoYyxHxyNpPXcSTaPyOO7Fbn3w8ueWnAYn%2FwWI6HMMm0OWkpPVfzMNCLoMwGOqUB08Wx6R6pVUiiV80HSduuXye5jhuWLdf6nEf60sW696XQNsomYkWA0c8E%2F%2Becbq1pstsaVKhd2mD24wXL9C7Wf%2Bw1uHVnqVHQWHPiDdJAqdh8OAQNIXtt5PHEVUdPFMJf%2BGJqrQL9ePCvunW4cgCq2VW74UNIKp15iomlurwfRDgFETVl8qCeXxjPIh3tN0OoJfJi1gn9SWZ9ZQszNpbVgxzMFwwn&X-Amz-Signature=4a6368bed4294944a211757e9cb6c2b868b9fecab69228a552e1a08530124f9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


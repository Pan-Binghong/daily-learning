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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WGLYBHG%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQDCd7OHrFBXE8%2F14%2B3J%2B1yLbwFqV%2FZC6yfEbALnxssWOAIhANW%2BqTs9mKKzIBDAJApP9ZHbq2yBSPETKMKnMhUJ27z9KogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzhy7CFdJXSb0iCG6oq3APWIyRKxjVuLbOnrhsxT7cP9mrzEoP4R5%2BRV6R236KzbporgmsSFv9foY2ijjtGGehLVNzkxPPehRnJUQfD%2BtSSjlPMEIMp1iAWLgj4JKonO4koyEmFk2pfgFYjHODwqAEX0468sSvKRx5LwhQZfCvmKjgzPUfic%2BPb4qLkx6RZm%2Bfc%2FT3v2aGKfUBg36mA3IimK4iZn%2FdI4e7j4r5d3fZ0kBkc7Xc2DtkYOqEv9jC3654TB9sE9FMlOkJ80dt48t%2FG39cAIbBy4743lNgD%2BGx2bBRFTILLQNaOqwWFc07GceiGURvXAWjfRo0Vg4J%2BnK%2FM36sImNNgBlNFzk%2FigXb8gcMkuQK81RR6mzZQfbYURxptvEilYdBjv9RjA4zsPSbTZRQLtDW6NzC0GMueSs0ErIib4uGH1gb7d7oTuvnGa3pbK0DgoU3bj%2FldWLwREtiL0GcRatBb8C758HbPD4xN1M5hJJP6dtS6bHOsVbAwenGDJneUXpimWKMlwujLuP1Z7kTv4UBjyn28K5SQ3UHUwDKa8c0piO4NjnvNKmsDndmS9eX2XSx%2FyNvjsoS7WTr64Xq35MDIn8fDKJE%2Fkw9n2u3ofU8cgEhriG7TSy%2B7p7sJ8qHsPhqYkm1ZODCb6ZbOBjqkAe43aUbYkoGhYQFmydVdbn9Nm1E%2FLWmoSGf%2F30npKLNYlRNm82o1tJilgTpauW%2BB8MwzITcKIqPyazznDHuQV5tyC%2FRgrhxiQoeTun5euZwmdXV51svYBtznWzpW01WdB4K00q3T03nMOPivBPo1g0IWkR7KmRB7Xojrfa4r3cH16fg5PmQCTD4a25l0wHD0MWUfO9e%2BNhDVqpM9WG7%2Fx0UxMFja&X-Amz-Signature=ceaf501c21bde1c102cedb5f40d9008224b8b50b87857c5a14e88d453437b1bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WGLYBHG%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQDCd7OHrFBXE8%2F14%2B3J%2B1yLbwFqV%2FZC6yfEbALnxssWOAIhANW%2BqTs9mKKzIBDAJApP9ZHbq2yBSPETKMKnMhUJ27z9KogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzhy7CFdJXSb0iCG6oq3APWIyRKxjVuLbOnrhsxT7cP9mrzEoP4R5%2BRV6R236KzbporgmsSFv9foY2ijjtGGehLVNzkxPPehRnJUQfD%2BtSSjlPMEIMp1iAWLgj4JKonO4koyEmFk2pfgFYjHODwqAEX0468sSvKRx5LwhQZfCvmKjgzPUfic%2BPb4qLkx6RZm%2Bfc%2FT3v2aGKfUBg36mA3IimK4iZn%2FdI4e7j4r5d3fZ0kBkc7Xc2DtkYOqEv9jC3654TB9sE9FMlOkJ80dt48t%2FG39cAIbBy4743lNgD%2BGx2bBRFTILLQNaOqwWFc07GceiGURvXAWjfRo0Vg4J%2BnK%2FM36sImNNgBlNFzk%2FigXb8gcMkuQK81RR6mzZQfbYURxptvEilYdBjv9RjA4zsPSbTZRQLtDW6NzC0GMueSs0ErIib4uGH1gb7d7oTuvnGa3pbK0DgoU3bj%2FldWLwREtiL0GcRatBb8C758HbPD4xN1M5hJJP6dtS6bHOsVbAwenGDJneUXpimWKMlwujLuP1Z7kTv4UBjyn28K5SQ3UHUwDKa8c0piO4NjnvNKmsDndmS9eX2XSx%2FyNvjsoS7WTr64Xq35MDIn8fDKJE%2Fkw9n2u3ofU8cgEhriG7TSy%2B7p7sJ8qHsPhqYkm1ZODCb6ZbOBjqkAe43aUbYkoGhYQFmydVdbn9Nm1E%2FLWmoSGf%2F30npKLNYlRNm82o1tJilgTpauW%2BB8MwzITcKIqPyazznDHuQV5tyC%2FRgrhxiQoeTun5euZwmdXV51svYBtznWzpW01WdB4K00q3T03nMOPivBPo1g0IWkR7KmRB7Xojrfa4r3cH16fg5PmQCTD4a25l0wHD0MWUfO9e%2BNhDVqpM9WG7%2Fx0UxMFja&X-Amz-Signature=c54060517474312be467810821be3faa26e8920e7059c67f3787f6333d4eacaa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


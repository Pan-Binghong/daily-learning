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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP2UWP4A%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIE%2FPO51hnl%2BOzTHN6TUVYu%2Fa9y8Mz7U1OmG9wlRCgYi3AiBiXy9oKtXmpDGSliinoH9c86WPTKV9EuODxaN5MuSM0SqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1n2D4pTaWWd40RflKtwD3GLFDs3Q%2BlqPYJ%2FKSsWKDT0e%2FmybqSECLXiq%2FbQ9LaoXQHzIugLJTb5av7fD9DoNmPYoJksULmH6iBgJ60mjEsOeA2M7KKDZvMiXhO1R%2BNaYVYKDK8ROpxdzAwJGYvITaG2AwZAcpsN8wRIJ5SkguuQwjwsAanAA5fvFVniJQOmuwFJHbrv7nKyL8Ps%2FZabPBfv7hiRTwbp7iNoiF25P%2FFFRPcIn80edpq%2FoViww0saAdYaAIo2rwCtm%2BQFfa48TOlLJNp0WvHE4N8e2pDrfu9TSRPnh8e1jlyxwwFSLNSWRXA8uf47Mtkh%2B7uktPlDibOi12%2BMpThesQwWSlP9Utp1VauyAb%2BeX11%2BFRef%2FACIft6cTdOGvthj56OtysJaJV1Nrkc6DikpxCEllyWwlgZH7Eu%2BJ%2Bu4HeNLUYpNTvOjgByjYK4c2AiAkvivXLe5QHlZTiLjDU7TRJZ5phprUgH0qGRlAO2LhAgEew5ghwg8RCV%2B%2F5KKVdb%2B0zZHA8vInZBa1TR53KOceuwESTK1IEWHYT6DFA%2BSFsBj69AhK36KriiCQ%2FE7f77bIL0lpdJkQp3QfHNCFgU9Eh%2FmjkzTryZTnEG7ahOHdV6meYbGtK2vv28gszPIlzPvcI%2FEw%2Fb%2FjyQY6pgEL6XrzDatTlSLTR33EXYc9VzBgrJKPDE8qFSbWePtopdqgr8dRyiJ4RnBhh7fMyFfl3KjW4Ue%2Fnu4tF4rvvacHwXkzQY8qrOVjCQjdxZoErfWrRu4Ii8ULNz%2B5YpE69uN30i%2BxfpNWqmQE9DgMCFCyiZLy9gwgKxIw4aCMmvigW%2FsJVP2cbd39L9fpUc7Y3eKZ%2FCEXsP4cznXtQw0yjB03EbrvsK0B&X-Amz-Signature=c0afc13921ac2700b5f0d37455a73bf41e03130d1dc8d044404e6bffaae125f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RP2UWP4A%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIE%2FPO51hnl%2BOzTHN6TUVYu%2Fa9y8Mz7U1OmG9wlRCgYi3AiBiXy9oKtXmpDGSliinoH9c86WPTKV9EuODxaN5MuSM0SqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1n2D4pTaWWd40RflKtwD3GLFDs3Q%2BlqPYJ%2FKSsWKDT0e%2FmybqSECLXiq%2FbQ9LaoXQHzIugLJTb5av7fD9DoNmPYoJksULmH6iBgJ60mjEsOeA2M7KKDZvMiXhO1R%2BNaYVYKDK8ROpxdzAwJGYvITaG2AwZAcpsN8wRIJ5SkguuQwjwsAanAA5fvFVniJQOmuwFJHbrv7nKyL8Ps%2FZabPBfv7hiRTwbp7iNoiF25P%2FFFRPcIn80edpq%2FoViww0saAdYaAIo2rwCtm%2BQFfa48TOlLJNp0WvHE4N8e2pDrfu9TSRPnh8e1jlyxwwFSLNSWRXA8uf47Mtkh%2B7uktPlDibOi12%2BMpThesQwWSlP9Utp1VauyAb%2BeX11%2BFRef%2FACIft6cTdOGvthj56OtysJaJV1Nrkc6DikpxCEllyWwlgZH7Eu%2BJ%2Bu4HeNLUYpNTvOjgByjYK4c2AiAkvivXLe5QHlZTiLjDU7TRJZ5phprUgH0qGRlAO2LhAgEew5ghwg8RCV%2B%2F5KKVdb%2B0zZHA8vInZBa1TR53KOceuwESTK1IEWHYT6DFA%2BSFsBj69AhK36KriiCQ%2FE7f77bIL0lpdJkQp3QfHNCFgU9Eh%2FmjkzTryZTnEG7ahOHdV6meYbGtK2vv28gszPIlzPvcI%2FEw%2Fb%2FjyQY6pgEL6XrzDatTlSLTR33EXYc9VzBgrJKPDE8qFSbWePtopdqgr8dRyiJ4RnBhh7fMyFfl3KjW4Ue%2Fnu4tF4rvvacHwXkzQY8qrOVjCQjdxZoErfWrRu4Ii8ULNz%2B5YpE69uN30i%2BxfpNWqmQE9DgMCFCyiZLy9gwgKxIw4aCMmvigW%2FsJVP2cbd39L9fpUc7Y3eKZ%2FCEXsP4cznXtQw0yjB03EbrvsK0B&X-Amz-Signature=ae027578e94c3637f3ede201aab24d7913520d29dc0af8658115c84d4a2d3379&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


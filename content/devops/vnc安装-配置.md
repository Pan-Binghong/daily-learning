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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JCPUS3Z%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T033058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICWhtMgghS4CWrJaglQFivf48JSvI%2BBqSVBNLKfuyltnAiAoFUsDHS600OQXhMo0Xrm9BPnAJ7%2FHx3TwlhAnlZsx%2FSqIBAiV%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMabkqjQbKuk4aEKmQKtwDOMFml%2Bbi65a81l1n6OL%2FSt8x98pezY8ug2yrPsQO3sf0r72dfjw8EcJXP0n8%2BTkWa8hXwnEokdUpJUEBEWS4Z2w%2FLKt4PzuCmibmw3%2BqQYrqTtaPo%2FuhD%2BKAmal2ev4CgmWZO%2BfECweEUS0B%2FDwQEOijJ4TCmjnA%2B1GsEyswaErilWX7MAlwMwum80K7hHUSl9TbBcEeBuC9Y9KQIKdeYrfTqBvLNiUWBFsp%2FzK%2BWppo3gad%2FHm0DcJpD9PsKyYMWK7tjHWzJ8n%2BlUqogeibGXfH5hDInEk%2BnzD2I5LdnPVjO%2B1p5pRjPEyfQXJun9tk8vTxX0D90ptHbdw0r2Hyjoc0vJJizk%2B6fkQPq7iQNUxP9gVUjkgnQXcEaf%2ByYe6sWdaxKr3%2BSwSaS2cZc6ac%2BHnti4IuRdp26tyhilKdh%2BWRuuJgh6IkTAKD8opOADPCWSe7%2BS0wPD3l2RoC76QmR991JQmy3ufKLBbUwK609YdWHqw%2BViTMRK0FL8wxurn10tja0fB8a7nrFJNDZTP16OnJYvO5xOvMIvd5oOP6iUL%2Bjapc13fCxDXHzdi23%2FWYjHp5V794AV63cx8rs39zPxDMs65fPsILX9GpMwgRsZj64CG%2BcC5VV3SSGe8wtsjwywY6pgGoZMApBCbrGLnkN54zovQEm8plc8Ac9inpLIGWYSIQPc6PCk8EsuO4uaXBg1nC0gBxg8UoqoKBKHv83BwQIIwADO4foM9kCswr5ntZiD637jyQZupGK1y7kSjL9K6DWqKyTvK6v7ADQU3j6pHr0TvMo5Gcj0eaWuZgsehRhjzhFhSf2x6mCD6Z4vc7XujYlOThEsX47pEIeovPo7qD3MJpNFFFhz61&X-Amz-Signature=1721ab8c87792644781996c4fa650dc3e29ed76e9b86b00b78b0fa6c49394563&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JCPUS3Z%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T033058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICWhtMgghS4CWrJaglQFivf48JSvI%2BBqSVBNLKfuyltnAiAoFUsDHS600OQXhMo0Xrm9BPnAJ7%2FHx3TwlhAnlZsx%2FSqIBAiV%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMabkqjQbKuk4aEKmQKtwDOMFml%2Bbi65a81l1n6OL%2FSt8x98pezY8ug2yrPsQO3sf0r72dfjw8EcJXP0n8%2BTkWa8hXwnEokdUpJUEBEWS4Z2w%2FLKt4PzuCmibmw3%2BqQYrqTtaPo%2FuhD%2BKAmal2ev4CgmWZO%2BfECweEUS0B%2FDwQEOijJ4TCmjnA%2B1GsEyswaErilWX7MAlwMwum80K7hHUSl9TbBcEeBuC9Y9KQIKdeYrfTqBvLNiUWBFsp%2FzK%2BWppo3gad%2FHm0DcJpD9PsKyYMWK7tjHWzJ8n%2BlUqogeibGXfH5hDInEk%2BnzD2I5LdnPVjO%2B1p5pRjPEyfQXJun9tk8vTxX0D90ptHbdw0r2Hyjoc0vJJizk%2B6fkQPq7iQNUxP9gVUjkgnQXcEaf%2ByYe6sWdaxKr3%2BSwSaS2cZc6ac%2BHnti4IuRdp26tyhilKdh%2BWRuuJgh6IkTAKD8opOADPCWSe7%2BS0wPD3l2RoC76QmR991JQmy3ufKLBbUwK609YdWHqw%2BViTMRK0FL8wxurn10tja0fB8a7nrFJNDZTP16OnJYvO5xOvMIvd5oOP6iUL%2Bjapc13fCxDXHzdi23%2FWYjHp5V794AV63cx8rs39zPxDMs65fPsILX9GpMwgRsZj64CG%2BcC5VV3SSGe8wtsjwywY6pgGoZMApBCbrGLnkN54zovQEm8plc8Ac9inpLIGWYSIQPc6PCk8EsuO4uaXBg1nC0gBxg8UoqoKBKHv83BwQIIwADO4foM9kCswr5ntZiD637jyQZupGK1y7kSjL9K6DWqKyTvK6v7ADQU3j6pHr0TvMo5Gcj0eaWuZgsehRhjzhFhSf2x6mCD6Z4vc7XujYlOThEsX47pEIeovPo7qD3MJpNFFFhz61&X-Amz-Signature=b2cdc6a56e530151cc28b3e517edf636bfa4aec3d1991dcf22f0345d96dfac8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUBUMKZ6%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIECFHV39vaUXxQGCPKegnAvk2EMAm%2B6IkPGYp%2FW79jlbAiEAhyeC5kA2l47bT9s%2F6OdV0mBgUpDw76NArnnd0tUjEB4qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEaRgh4r7BhFpSPN1CrcA%2FZobm0sx8wpuuIT6QX7B9JekgXgyalPdFHcSeVwQMVSrtimYLz9u78dA27kRywAqYm29Ga%2Fa8bLf28ejAyFDHzuKKL06Sduein571mOM7erzwB%2BLbc6Jg3QVwjCYo8qY5dp%2Bayy88D04iQb12BnuoWSvw5f3olIYDXuD6IAbbS52TcKRWGgKG4SDu%2BE15Y1hVDEvayUSS4xuLCA%2BKda%2BdwyOscr9YPNoetNo99YGulktp3B9gJsiwDdLZe1xDzneqAokXp5IoKFie%2Bdi9cKH6qTTqHqFNN7MiCALmpx%2B3Au6vWaLxyp2vSCJW15NnI%2Fc0znwGtapz%2BgAxAsP%2Ba3xslrmmmUQOAa3QvGyJ%2BnJL4marQjmdUI4opl4jo0Z%2B03M59yJu7EbiBMOK6O9Ge51vOlLCqK4MV2nuVcihSSe5ZiHhsQBGsabXvf5IKNy8X95bEe59KDu0NMF03XueMoCVPQQxnaAjhvDzGpXhn5v9hzNLrKcm2aSFjgvqRYdh0faFZh2nD4LWUMve%2Fh%2F3i5JkmHZeSKDzCjGFTPniGKuJn%2FyDcfZEObHzRdbIJzM0n2ThzBvYz%2F2j3hTxbMIPdovWD0lS%2FjzVev5eDcL1S5bapYA2YLfIwIxax2e3QjMPb4nMoGOqUBMCnb%2FCfh9nLKmKUi5ZrfYms7J4s2bvpduzF9PI5XApSIIcIUlfRRmQlbMA43ei8o51RB7EHEeXvniglkYh4OOVm9jKbUCifPnug5hRbbDKTPMDQTR%2BNrmzkUboX6KjJg%2BMI%2BowwEgZfzfXFr55eqaSE8%2FZeG5mtP9Y00X6yt7QSnAcMEVikTrD82d0N9oNdrax8sdKPXBzo3dmI1TLy5%2FYTFww%2FU&X-Amz-Signature=8cd44c9f3cea7b72abd243d6d9ae8d531cd4e1bb1524afaa7c285332c58b55dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUBUMKZ6%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIECFHV39vaUXxQGCPKegnAvk2EMAm%2B6IkPGYp%2FW79jlbAiEAhyeC5kA2l47bT9s%2F6OdV0mBgUpDw76NArnnd0tUjEB4qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEaRgh4r7BhFpSPN1CrcA%2FZobm0sx8wpuuIT6QX7B9JekgXgyalPdFHcSeVwQMVSrtimYLz9u78dA27kRywAqYm29Ga%2Fa8bLf28ejAyFDHzuKKL06Sduein571mOM7erzwB%2BLbc6Jg3QVwjCYo8qY5dp%2Bayy88D04iQb12BnuoWSvw5f3olIYDXuD6IAbbS52TcKRWGgKG4SDu%2BE15Y1hVDEvayUSS4xuLCA%2BKda%2BdwyOscr9YPNoetNo99YGulktp3B9gJsiwDdLZe1xDzneqAokXp5IoKFie%2Bdi9cKH6qTTqHqFNN7MiCALmpx%2B3Au6vWaLxyp2vSCJW15NnI%2Fc0znwGtapz%2BgAxAsP%2Ba3xslrmmmUQOAa3QvGyJ%2BnJL4marQjmdUI4opl4jo0Z%2B03M59yJu7EbiBMOK6O9Ge51vOlLCqK4MV2nuVcihSSe5ZiHhsQBGsabXvf5IKNy8X95bEe59KDu0NMF03XueMoCVPQQxnaAjhvDzGpXhn5v9hzNLrKcm2aSFjgvqRYdh0faFZh2nD4LWUMve%2Fh%2F3i5JkmHZeSKDzCjGFTPniGKuJn%2FyDcfZEObHzRdbIJzM0n2ThzBvYz%2F2j3hTxbMIPdovWD0lS%2FjzVev5eDcL1S5bapYA2YLfIwIxax2e3QjMPb4nMoGOqUBMCnb%2FCfh9nLKmKUi5ZrfYms7J4s2bvpduzF9PI5XApSIIcIUlfRRmQlbMA43ei8o51RB7EHEeXvniglkYh4OOVm9jKbUCifPnug5hRbbDKTPMDQTR%2BNrmzkUboX6KjJg%2BMI%2BowwEgZfzfXFr55eqaSE8%2FZeG5mtP9Y00X6yt7QSnAcMEVikTrD82d0N9oNdrax8sdKPXBzo3dmI1TLy5%2FYTFww%2FU&X-Amz-Signature=65e473a64edc6a0c633eac7533496b5d2d02b5e7fc67c5f1487c75cb58083dd0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


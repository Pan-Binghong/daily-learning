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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6QPSAYB%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T035011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDAKED8SiCWHMauBTaqlSL%2F4of93wFy6GVJWQVpsalSHAIgYl%2F7nRp8pHcQy5bLz7A66s5GTxdZ2NnQEs%2Bik9GHQOYq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDJfz%2BqMwnvDlznf26SrcA8ZFUQsb8%2BrcR%2BuFCSLlYMbYcb1yszoyLpqsnXZI%2BJfPomgY%2FROSOmWAuJ%2BEPpWJabDr6jo2tSK60nkwKa0%2B0fUP7r8VIVSTQVccNMUSF4ESLIn0jsjhYCgybUGmc1td%2FVkI8oaodMt8CB93VO9AUDsel3O9WApshvq0X8iFDgR64e3ct1GSRbooi%2BrwVdpOcTeIKlCtdx0dcR%2BbGk7jw0wGYCnBxVcOmMLyUIRs5UAkt3qXjEIQhm1K3khlO6QzIYn%2BMnOryKmqCeaTvw2M9LfoGvAgCXS6fJFTPUlYjYNBCM7ky52yd%2Bt%2FATpPGQ0s7YB8i%2BeeCdJQEcaoBoIULY4oTkfCVlj2kEejt6Fbg4U0H6e7vp2Wwk4ni7cWT5jtp8dRwu5t1kxqOYpv%2FnAEXbk%2BaPAKb9mdzoUKkqVlAv8isLHR%2FxKiZy8LEeMiK1Z%2FX%2FAgZBOsVyB34QpLEKUW6cPFtMumhKrNXg3qyXEFfT97PXnsbEjNUSs2U8ZUENn6%2F%2BZ2L1tahMuNXX3ezYKODsHC17j76k851qgiYMlMmo%2Be46AmUQiXdmXtERWTMIPkD5vQhl7kQm%2BBM76%2FyPs1BwFpntdvsldP1kZH5TmnOTg72MGdJ%2BtQbqp9EfYCMIuz3M4GOqUBAzHg9OJ8fSTQxzpmeoYD%2BGG509%2F9YD6JgdFGsdGbSphU9pAZNWBAB7TLzkJbUgIP5za3o2vK1PnBRo1QDVDvjhIUhIR8ZQWr9yS4J%2BO%2BzHxhMUs6U2TcIkGLQwsrcUb%2BuSLYKTTtujg6YXyiohgH%2FZZfZatMHmvciTLzgV31mF%2FbiAEwQEdxtsdQseO0xNqDpXj4j7Ny8xtowR0Gl7un5Ztn4XWx&X-Amz-Signature=4cc5104a5cab537759438f1a85ff69c9fe727f2c5324b94fe25e576d1591ba5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6QPSAYB%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T035011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDAKED8SiCWHMauBTaqlSL%2F4of93wFy6GVJWQVpsalSHAIgYl%2F7nRp8pHcQy5bLz7A66s5GTxdZ2NnQEs%2Bik9GHQOYq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDJfz%2BqMwnvDlznf26SrcA8ZFUQsb8%2BrcR%2BuFCSLlYMbYcb1yszoyLpqsnXZI%2BJfPomgY%2FROSOmWAuJ%2BEPpWJabDr6jo2tSK60nkwKa0%2B0fUP7r8VIVSTQVccNMUSF4ESLIn0jsjhYCgybUGmc1td%2FVkI8oaodMt8CB93VO9AUDsel3O9WApshvq0X8iFDgR64e3ct1GSRbooi%2BrwVdpOcTeIKlCtdx0dcR%2BbGk7jw0wGYCnBxVcOmMLyUIRs5UAkt3qXjEIQhm1K3khlO6QzIYn%2BMnOryKmqCeaTvw2M9LfoGvAgCXS6fJFTPUlYjYNBCM7ky52yd%2Bt%2FATpPGQ0s7YB8i%2BeeCdJQEcaoBoIULY4oTkfCVlj2kEejt6Fbg4U0H6e7vp2Wwk4ni7cWT5jtp8dRwu5t1kxqOYpv%2FnAEXbk%2BaPAKb9mdzoUKkqVlAv8isLHR%2FxKiZy8LEeMiK1Z%2FX%2FAgZBOsVyB34QpLEKUW6cPFtMumhKrNXg3qyXEFfT97PXnsbEjNUSs2U8ZUENn6%2F%2BZ2L1tahMuNXX3ezYKODsHC17j76k851qgiYMlMmo%2Be46AmUQiXdmXtERWTMIPkD5vQhl7kQm%2BBM76%2FyPs1BwFpntdvsldP1kZH5TmnOTg72MGdJ%2BtQbqp9EfYCMIuz3M4GOqUBAzHg9OJ8fSTQxzpmeoYD%2BGG509%2F9YD6JgdFGsdGbSphU9pAZNWBAB7TLzkJbUgIP5za3o2vK1PnBRo1QDVDvjhIUhIR8ZQWr9yS4J%2BO%2BzHxhMUs6U2TcIkGLQwsrcUb%2BuSLYKTTtujg6YXyiohgH%2FZZfZatMHmvciTLzgV31mF%2FbiAEwQEdxtsdQseO0xNqDpXj4j7Ny8xtowR0Gl7un5Ztn4XWx&X-Amz-Signature=bbe5e05e48f36dde37f1cdda755ee1041a1e33cde10435a959e8c6b56a2b8f65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


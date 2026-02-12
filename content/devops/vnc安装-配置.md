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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSZOLUIE%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDr9Rgo%2BGpIg%2Bw9PfEL9fLhvv5GxHnbIqO6TrlH8FEzwwIgdVQ3hzoh%2Bf9W%2BcPppLd%2FpXYLWArTyzMTwnnYedxFBrcqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLUjD%2BeymQgP%2BE6WlyrcAx1QmkYMdiVKmDU2PfCu3uHPfP3dggnK3N2AuKpMBsWmK3RPjfuu6%2BqG86PZ0fLvgRSwJFWUbuz7J%2BZ9yQlBDhX2BsqlTEw6j4bFS0QPbZ42h7gs9jM4ilay4jvB8ROwESxqhDLBp1tpa%2BTkuXmrOLqxUq0BTZGGlHe6iNDJ23TbSdH9ezxJmL2Uf%2Bc4m0powGvrtxqiBNjtQL7Ri2CWWqCbb75rTw2NQzPHtwuh7zZA8cHXkwT5Lj01Q2zB8GPuKaF7p%2FkgI8w%2BXueLz7zbLBuxu3sn8Q5CfFYAD29oSMGfr9WxyV2GXeQNm7E%2BGlzGlIzuqZt6HEZryrJ%2BAYDqVqPG25miF5rI3KHrQfreImqH9LmAEGNCWWuJ4J8uKrhklG5BuXx54kdkDkyf3eOiHs%2FbUQ30LCbw32b0wmErw6L2DcS3Gp%2Flaaqf9I00xXX3ptyB7V2s27T69cOAmuWkbmuSSb6JJOa2BMQZKQKs3rEUaqsYEV1OT92LlSRs7UmMRprbrnL4nV%2BJurWV4EhrRLZnsQqciGGGm5oIiuyJJFfqsLD5HPdlSeqYuCtlUvOOJDmR%2Beekpw9y2CBlJNtxXyVDZD8EioirG9aWNjwaI6sQLa9v%2FNJGekOrVhZHMLaStcwGOqUBI2X2MF5KdyV2ZMAsGGKkQ6YamVUuI7qADdTzDOu%2FU%2Ffwj1bVxnO4OXGfRSWc1RnSzUdQ3%2BauXosXaWGgExSBU8OAxKJzhPrNhwOh9KqacJly9soYRCLxBraV3osWKyj74pnA14gHgsYcf9EMUGiik6YqJu99bxjR2jCyBcES%2FGPVAI1U6G2Gg%2FhSIs%2F7IfcBpY2Ms6yz7E7EA33OXIDJij48rP9I&X-Amz-Signature=3923ae5cc42cc7b85681f4c0b43611748dbbe8a8c08a3d722025d25d3da583d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSZOLUIE%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDr9Rgo%2BGpIg%2Bw9PfEL9fLhvv5GxHnbIqO6TrlH8FEzwwIgdVQ3hzoh%2Bf9W%2BcPppLd%2FpXYLWArTyzMTwnnYedxFBrcqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLUjD%2BeymQgP%2BE6WlyrcAx1QmkYMdiVKmDU2PfCu3uHPfP3dggnK3N2AuKpMBsWmK3RPjfuu6%2BqG86PZ0fLvgRSwJFWUbuz7J%2BZ9yQlBDhX2BsqlTEw6j4bFS0QPbZ42h7gs9jM4ilay4jvB8ROwESxqhDLBp1tpa%2BTkuXmrOLqxUq0BTZGGlHe6iNDJ23TbSdH9ezxJmL2Uf%2Bc4m0powGvrtxqiBNjtQL7Ri2CWWqCbb75rTw2NQzPHtwuh7zZA8cHXkwT5Lj01Q2zB8GPuKaF7p%2FkgI8w%2BXueLz7zbLBuxu3sn8Q5CfFYAD29oSMGfr9WxyV2GXeQNm7E%2BGlzGlIzuqZt6HEZryrJ%2BAYDqVqPG25miF5rI3KHrQfreImqH9LmAEGNCWWuJ4J8uKrhklG5BuXx54kdkDkyf3eOiHs%2FbUQ30LCbw32b0wmErw6L2DcS3Gp%2Flaaqf9I00xXX3ptyB7V2s27T69cOAmuWkbmuSSb6JJOa2BMQZKQKs3rEUaqsYEV1OT92LlSRs7UmMRprbrnL4nV%2BJurWV4EhrRLZnsQqciGGGm5oIiuyJJFfqsLD5HPdlSeqYuCtlUvOOJDmR%2Beekpw9y2CBlJNtxXyVDZD8EioirG9aWNjwaI6sQLa9v%2FNJGekOrVhZHMLaStcwGOqUBI2X2MF5KdyV2ZMAsGGKkQ6YamVUuI7qADdTzDOu%2FU%2Ffwj1bVxnO4OXGfRSWc1RnSzUdQ3%2BauXosXaWGgExSBU8OAxKJzhPrNhwOh9KqacJly9soYRCLxBraV3osWKyj74pnA14gHgsYcf9EMUGiik6YqJu99bxjR2jCyBcES%2FGPVAI1U6G2Gg%2FhSIs%2F7IfcBpY2Ms6yz7E7EA33OXIDJij48rP9I&X-Amz-Signature=2e9be68356a2f399c61bde7054cb4f05bb0ea8565a06b8c3e490aafbf658a07a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


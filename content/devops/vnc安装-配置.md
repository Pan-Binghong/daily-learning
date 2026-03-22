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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDA3NSOS%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDXDLqOvFnWAug3ve7HpZBUEJJkCH5pdF0ZlByv7APiZAiBIqqxjrCdGf0yAZh5Dx7EYmnurzvbSPaTf7gbDDB%2FciSr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMD2tGmbmPYDnz99gfKtwDbFsKBmyJLH9YtbjgWao6YQqI13Wlw7ZpFTJ%2FqIzuiYJhqjEDOccy6Czp8QMCuX%2F5WwV3RPuTXJtOBEwmCkoYpLpPK5AdPkmuZe0BAco%2FDEMQ98t2tkSXfDIlDyaZ7rKQoBebumPVKmrKFmyTX5D0eqaPw0UDv43fOyAanLUAPuNl9t%2FgtDRCqtZTj7GjiozgWPtsJIHx%2F8%2Buc2VLiQzRUQb%2FVgKOms5xYrXjhO40%2FEFnGiZkJyxDDE0asVGVsTgPtUb8cN4k55F6HgE4ohVqBI7pJnX9B75zTuyomSfDcXinRGJotVlTTQ3Mu%2BD0oSkV%2FsXXChV3CQx%2FnBEUUG02xREpiG5PxN9MoO29rb8tVe68KyhVKCO5PoiEVTWTcUQs2rV%2BzD0ZS4%2FHZq35Z6vpH%2Bbb8Ai6Qao1G%2BIkKj1TcN916eOxJ9qSRqxLtCEcErYHbSN2Pr9hPkTyjOQ9bXJcBuka41N3W%2F3DW0U5O7kbAT2NXjZ3oMmwkuHvs0kjZ%2FDDdoT5%2Bd5fxS%2FkfxmYK2tNKVCTI4adygnxn2fV7uGwPy6MseIZCMBC0Ss%2Fl4MitHPq6u6k2m%2BD%2B9qDmPQYH1QcwfdCdoKLledIKJvtsa2myziojPr1kBIvV6A3Gy4w0Kz9zQY6pgHfoH6MmN%2FPQMNGGkSyEyZOMzfFkmGhRWEMuyHGMWhZuqVykXyrGri8Bf1ETej%2BYoemJzS%2Ff%2BaWdBjS%2Bogu5Amxl38S5Q4cEu%2Fae0vClnpiNmhwMYNEjEu992ZhADXmNeOJfVUAgN84yy8kR5o8FsZCo2xW7H%2FRwL%2FXM0ZS6SQPBfpTPJ7Nooc3YROWK1weF9kHodZmfldQ0Mj9hlqLRVe6b4vljztB&X-Amz-Signature=62179e9531849a7e764207f018b3205bffb5f56d0c7e990cdefbda5fa4187402&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDA3NSOS%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDXDLqOvFnWAug3ve7HpZBUEJJkCH5pdF0ZlByv7APiZAiBIqqxjrCdGf0yAZh5Dx7EYmnurzvbSPaTf7gbDDB%2FciSr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMD2tGmbmPYDnz99gfKtwDbFsKBmyJLH9YtbjgWao6YQqI13Wlw7ZpFTJ%2FqIzuiYJhqjEDOccy6Czp8QMCuX%2F5WwV3RPuTXJtOBEwmCkoYpLpPK5AdPkmuZe0BAco%2FDEMQ98t2tkSXfDIlDyaZ7rKQoBebumPVKmrKFmyTX5D0eqaPw0UDv43fOyAanLUAPuNl9t%2FgtDRCqtZTj7GjiozgWPtsJIHx%2F8%2Buc2VLiQzRUQb%2FVgKOms5xYrXjhO40%2FEFnGiZkJyxDDE0asVGVsTgPtUb8cN4k55F6HgE4ohVqBI7pJnX9B75zTuyomSfDcXinRGJotVlTTQ3Mu%2BD0oSkV%2FsXXChV3CQx%2FnBEUUG02xREpiG5PxN9MoO29rb8tVe68KyhVKCO5PoiEVTWTcUQs2rV%2BzD0ZS4%2FHZq35Z6vpH%2Bbb8Ai6Qao1G%2BIkKj1TcN916eOxJ9qSRqxLtCEcErYHbSN2Pr9hPkTyjOQ9bXJcBuka41N3W%2F3DW0U5O7kbAT2NXjZ3oMmwkuHvs0kjZ%2FDDdoT5%2Bd5fxS%2FkfxmYK2tNKVCTI4adygnxn2fV7uGwPy6MseIZCMBC0Ss%2Fl4MitHPq6u6k2m%2BD%2B9qDmPQYH1QcwfdCdoKLledIKJvtsa2myziojPr1kBIvV6A3Gy4w0Kz9zQY6pgHfoH6MmN%2FPQMNGGkSyEyZOMzfFkmGhRWEMuyHGMWhZuqVykXyrGri8Bf1ETej%2BYoemJzS%2Ff%2BaWdBjS%2Bogu5Amxl38S5Q4cEu%2Fae0vClnpiNmhwMYNEjEu992ZhADXmNeOJfVUAgN84yy8kR5o8FsZCo2xW7H%2FRwL%2FXM0ZS6SQPBfpTPJ7Nooc3YROWK1weF9kHodZmfldQ0Mj9hlqLRVe6b4vljztB&X-Amz-Signature=7adb4737a326ad1221c3842792c51058e553844bc9ce14f8ede60485342e94b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


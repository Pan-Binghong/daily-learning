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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z23RJZFM%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEJHB5le634k%2BZb%2Bs%2FHDmjzmQz0FBzn0sZp0a4Euj6poAiEA9fyGgv1ERsDmeAAzplCsA4XKz%2BOMGo1S1JPb3c%2F08AIq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDJL8ceQNV6eSjC%2F2cSrcA7g%2FNcyTeU6oXBHL99P2nUNhKIfRYUMSJRVzrL2TzPR8Dz9v4QRchKo9sfP%2FVXZyUN65MwFhXdQCbS59rC8M3rvhY8WTmpY6oDHqoEcBhPs6FTUBICmloBHsNvkhEGm9TcAiq3jJFeFtFrnfuuI2o3x%2Fo%2BVE7DedP2k8ff8rKSpW7MmkFzMKIKDdVSbdRe%2By3qsLocYvMQWRg3IFeAeWO3wKp%2ByuLNFjOKtJbSRS1OniU3EE7YJ0Z0rxIAT90oKRPa%2BWvaYnHIh7qpFleYAe6jGShBo%2Fum5wJZILEpzY1x6TrZvxwWe9T4ysUkbB6eEKCFN07jSvryeDQUZk7qlCZq5TsQNx2%2FlnwLwv%2FkssgXuAUOiyY%2BB7BDZ%2FeRcr5Wto%2Fg0qnz9ucSElfTCXVNPGugeqJxHvKY2FHb5JqcIP5zKmv0w8VU%2FC%2BLtao6myVA00a%2FhjOhLTTD5qBOkryMCObJep0%2FzUtaj1RjuDmPUX28917OXYjQxlzznDsaLbA3rtVsFXJ4an3F6sbGUlLgN5w%2BGkzxSemx8Jk6sy%2FkfyplUDGs2HtprP7dd19kw9YqsV26i4IK87%2BBlhvl8kUHc0AKmAIjlaM6tSFba2PwDYukuQR8Fl%2FYIW88u3Mo3sMP%2Bfss4GOqUBG2ZhroiHWTiVvYAC56dcuEI%2F16TbumlrU4EGLxoRd6v90yLABUoCxaHkueReNU%2BYUzq6Ie9vPFFmA1W62gpxUf2pCPLV4zcqdWDfo%2BuqxPxmMBkrcU8gJt6Cec0oPESYHjxPwyHe7jnXtv5Cte5VQ%2FhGaxlcpXDaHxj6MxrnWiuhPYfxbAa6rLiBikqmmYmsKemZuViGB3qvSYdCFmMAfA2yA6cD&X-Amz-Signature=cb74d1c7169f1e3498d95ca306c55d5b47ddb6dcf7aac1c69e4539c6d7ab2c42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z23RJZFM%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEJHB5le634k%2BZb%2Bs%2FHDmjzmQz0FBzn0sZp0a4Euj6poAiEA9fyGgv1ERsDmeAAzplCsA4XKz%2BOMGo1S1JPb3c%2F08AIq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDJL8ceQNV6eSjC%2F2cSrcA7g%2FNcyTeU6oXBHL99P2nUNhKIfRYUMSJRVzrL2TzPR8Dz9v4QRchKo9sfP%2FVXZyUN65MwFhXdQCbS59rC8M3rvhY8WTmpY6oDHqoEcBhPs6FTUBICmloBHsNvkhEGm9TcAiq3jJFeFtFrnfuuI2o3x%2Fo%2BVE7DedP2k8ff8rKSpW7MmkFzMKIKDdVSbdRe%2By3qsLocYvMQWRg3IFeAeWO3wKp%2ByuLNFjOKtJbSRS1OniU3EE7YJ0Z0rxIAT90oKRPa%2BWvaYnHIh7qpFleYAe6jGShBo%2Fum5wJZILEpzY1x6TrZvxwWe9T4ysUkbB6eEKCFN07jSvryeDQUZk7qlCZq5TsQNx2%2FlnwLwv%2FkssgXuAUOiyY%2BB7BDZ%2FeRcr5Wto%2Fg0qnz9ucSElfTCXVNPGugeqJxHvKY2FHb5JqcIP5zKmv0w8VU%2FC%2BLtao6myVA00a%2FhjOhLTTD5qBOkryMCObJep0%2FzUtaj1RjuDmPUX28917OXYjQxlzznDsaLbA3rtVsFXJ4an3F6sbGUlLgN5w%2BGkzxSemx8Jk6sy%2FkfyplUDGs2HtprP7dd19kw9YqsV26i4IK87%2BBlhvl8kUHc0AKmAIjlaM6tSFba2PwDYukuQR8Fl%2FYIW88u3Mo3sMP%2Bfss4GOqUBG2ZhroiHWTiVvYAC56dcuEI%2F16TbumlrU4EGLxoRd6v90yLABUoCxaHkueReNU%2BYUzq6Ie9vPFFmA1W62gpxUf2pCPLV4zcqdWDfo%2BuqxPxmMBkrcU8gJt6Cec0oPESYHjxPwyHe7jnXtv5Cte5VQ%2FhGaxlcpXDaHxj6MxrnWiuhPYfxbAa6rLiBikqmmYmsKemZuViGB3qvSYdCFmMAfA2yA6cD&X-Amz-Signature=aa10ec8a9424d1d27723f714460ab5fc75d889b979ae13086317df27964a45c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


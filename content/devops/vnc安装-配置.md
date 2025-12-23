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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUH7BSE4%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCICYLYBZOPevx%2Bn%2BNcWWrxc5jDWsQ7892Ish2%2BvgnPtdPAiA3i6E09gx7nnY7poNoDQYIW%2B9JNZbjBbJD4w%2FDROVspyr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMc2e0R3nTgJ%2FM85XhKtwDAmZarsnpG4iINbTvyACy%2F0Oq7YgyhLz4EJSRV%2FlcQPGnhlvkRcPUUxGQBQaIhSOlvQfRQGoFURofcas6zK8T8kg9WzmXy4Rpfb7VTYCNvbzj919PLIkn18Skog8s0FdNS7p%2Bw80d01ZxsBi2VkVK0uHeTqlKwozuLKcUYJCGGlKpiWDwBLtIJbO2bLP7XMG4gFRtmRsBDyKu%2FrVjYNYzRGFpjTy0DXJTjoU0YIriX%2B5KWYGWZ758CvhC4UVdZn68bgba%2BJjAwK%2BvVq5v3Hc0u2jZXJHCmM5YPO03gAKoXR2VPNvbmzeEoslPfYgTuUghnX%2BYH09HWV%2B532mgzigqxgpkW3fXy1IEV%2FZevGudsNPEIC%2FGTvA2A2UBYgBkLUimb9wtdw78xE5DudZyiLYXGzjPF6WSdnnCAS88LtXwIRNyL71oVFUPS3sT4G%2FklfioFodjN4qH8WomlpxJ5q5s3rYWQdITbUd3wSntWucnsUMdlckD3SikGX4lCnyqWnGZv2K8giHRmvmV1MJBlay6Kfe3fkzSEIfW%2FEjmUWhtCmp98mFZkvS7SffpcNveyBauJ6g2yvOlIxdobO3ANr8A1KjfEFuS7g4MVZQGToeNg9uDz7y%2FyyRwNkBz1vkw%2BPynygY6pgH3szAzgZsA5d2OkwzoVFDp5xXZu44Zsu6daIGtWQBAqX7wfmRPBzgDXKd6yX%2Bd9n8iOjIHw%2BNDsPwef3GwAu1fuGkfyStixcf0LWa8Yn1KQXsdktXVRSqFu6QuGl%2FeSXVOLtc44uSpf7s7YyXDkNnaYW%2FzVtU5KNcxfahrG%2Fh7W1DgbjLo7AzAFjBmaYhx1GOQa3oLryPOE%2BcegPN9Y3OlsiGsfuLn&X-Amz-Signature=d7254ea561e15e9bd9be2028183595a414da4854fe9c3ea282459ac3de3b705b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUH7BSE4%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCICYLYBZOPevx%2Bn%2BNcWWrxc5jDWsQ7892Ish2%2BvgnPtdPAiA3i6E09gx7nnY7poNoDQYIW%2B9JNZbjBbJD4w%2FDROVspyr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMc2e0R3nTgJ%2FM85XhKtwDAmZarsnpG4iINbTvyACy%2F0Oq7YgyhLz4EJSRV%2FlcQPGnhlvkRcPUUxGQBQaIhSOlvQfRQGoFURofcas6zK8T8kg9WzmXy4Rpfb7VTYCNvbzj919PLIkn18Skog8s0FdNS7p%2Bw80d01ZxsBi2VkVK0uHeTqlKwozuLKcUYJCGGlKpiWDwBLtIJbO2bLP7XMG4gFRtmRsBDyKu%2FrVjYNYzRGFpjTy0DXJTjoU0YIriX%2B5KWYGWZ758CvhC4UVdZn68bgba%2BJjAwK%2BvVq5v3Hc0u2jZXJHCmM5YPO03gAKoXR2VPNvbmzeEoslPfYgTuUghnX%2BYH09HWV%2B532mgzigqxgpkW3fXy1IEV%2FZevGudsNPEIC%2FGTvA2A2UBYgBkLUimb9wtdw78xE5DudZyiLYXGzjPF6WSdnnCAS88LtXwIRNyL71oVFUPS3sT4G%2FklfioFodjN4qH8WomlpxJ5q5s3rYWQdITbUd3wSntWucnsUMdlckD3SikGX4lCnyqWnGZv2K8giHRmvmV1MJBlay6Kfe3fkzSEIfW%2FEjmUWhtCmp98mFZkvS7SffpcNveyBauJ6g2yvOlIxdobO3ANr8A1KjfEFuS7g4MVZQGToeNg9uDz7y%2FyyRwNkBz1vkw%2BPynygY6pgH3szAzgZsA5d2OkwzoVFDp5xXZu44Zsu6daIGtWQBAqX7wfmRPBzgDXKd6yX%2Bd9n8iOjIHw%2BNDsPwef3GwAu1fuGkfyStixcf0LWa8Yn1KQXsdktXVRSqFu6QuGl%2FeSXVOLtc44uSpf7s7YyXDkNnaYW%2FzVtU5KNcxfahrG%2Fh7W1DgbjLo7AzAFjBmaYhx1GOQa3oLryPOE%2BcegPN9Y3OlsiGsfuLn&X-Amz-Signature=b7644790baf9fac637fc1422e0555cb4599eccff497082ebf9997df395bf1d69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


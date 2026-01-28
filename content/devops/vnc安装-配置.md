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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PP2OYBH%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCxkk60908u5XajH6J19FMl4ZaOMeNv2Du1ueZxkbI6wwIhAJcypf0a7OimXejH8kuF%2FYkHkUE6VvCz%2Ft6%2FO3s6e0YYKv8DCGEQABoMNjM3NDIzMTgzODA1IgwMItqJpoWZDr09Dzgq3APwheBdCs7HPdTJuDJdfQWNq7CPYEHGnbqluOcxc1R2wDPommiYurGrkXj3ioY08wfYLOEB7qgxNZavPcdFJR0a8vSTkL3ylYC7eouGriAWgRKt5pw%2BpoWSeOcSvUknnGcDwAR9h3OvYuTU%2B9vUXNNFRd1Hylx%2B521Jk1Y3L%2Fytp7ulk5hHztnl6txcEZm0Z6ClV%2BaapXVP6vcP%2BgBNqKCvTdTFtKmNnKer1yWXJdChTQphQQdtMs%2BNauWg56KJvM%2FU0YL5TR9OcmLcx8C7FSVj%2BJzC8BWA1bgg4ZL0eG2eonUmcXYIM%2FLlc4zf51K9r8WxqE2KEgfapVeVdKWy5iXMx4ohcw4TzaWQQ6N3%2FtTu%2BGhFIbTNyFKPd23lGi3xoI%2Fnxh4DH2ybJ2%2BlcKfQspSoypOPeIIrNdE3DejIgMndomxSIRBX0pUcVfl0VRx3kIuoifQQrUiVYtIOZtBVDbrrNEmzbTUbaSetI%2F3%2FkmmEjvSf%2B8jq8qlSw8I%2BeBalKrvQqZ6ocw6UvASZ%2F%2FZ5d5wEG%2FZyqlvTqEcSewPAEVaFgU9kxHd31hHwgBhKZgxpLA%2F7XrG50g9YigN7pxus7CVLPoWojX8vs4xHITkFB3MD8jq6Ve%2FGQKfNb4B37zCAluXLBjqkAeR7NLIW9LgCfJl4vYk1q7KyI1cRVrOeeLAEMeSKXrWja7q%2BIjXVr2IxnrkKUiLtajdWSCSSDjjW5XUE3AFBAvV%2BFBkg6CCUVdFM%2B0taYWh%2FV3a0dB8yl3PFmz5bzpPALZPVn6SSdcq3dACOanquVoiRzMFDZ%2FXeEU7P3%2B0f%2FfPbk7rMtqLCiUkeVAXbTgE7%2BQYoxOY%2BvfMVUklf203aVwAk53vr&X-Amz-Signature=87f2fbbbfdaf59f56f32ffb212ea2d93311ca9890e3957b93b8ffe42a8f82154&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PP2OYBH%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCxkk60908u5XajH6J19FMl4ZaOMeNv2Du1ueZxkbI6wwIhAJcypf0a7OimXejH8kuF%2FYkHkUE6VvCz%2Ft6%2FO3s6e0YYKv8DCGEQABoMNjM3NDIzMTgzODA1IgwMItqJpoWZDr09Dzgq3APwheBdCs7HPdTJuDJdfQWNq7CPYEHGnbqluOcxc1R2wDPommiYurGrkXj3ioY08wfYLOEB7qgxNZavPcdFJR0a8vSTkL3ylYC7eouGriAWgRKt5pw%2BpoWSeOcSvUknnGcDwAR9h3OvYuTU%2B9vUXNNFRd1Hylx%2B521Jk1Y3L%2Fytp7ulk5hHztnl6txcEZm0Z6ClV%2BaapXVP6vcP%2BgBNqKCvTdTFtKmNnKer1yWXJdChTQphQQdtMs%2BNauWg56KJvM%2FU0YL5TR9OcmLcx8C7FSVj%2BJzC8BWA1bgg4ZL0eG2eonUmcXYIM%2FLlc4zf51K9r8WxqE2KEgfapVeVdKWy5iXMx4ohcw4TzaWQQ6N3%2FtTu%2BGhFIbTNyFKPd23lGi3xoI%2Fnxh4DH2ybJ2%2BlcKfQspSoypOPeIIrNdE3DejIgMndomxSIRBX0pUcVfl0VRx3kIuoifQQrUiVYtIOZtBVDbrrNEmzbTUbaSetI%2F3%2FkmmEjvSf%2B8jq8qlSw8I%2BeBalKrvQqZ6ocw6UvASZ%2F%2FZ5d5wEG%2FZyqlvTqEcSewPAEVaFgU9kxHd31hHwgBhKZgxpLA%2F7XrG50g9YigN7pxus7CVLPoWojX8vs4xHITkFB3MD8jq6Ve%2FGQKfNb4B37zCAluXLBjqkAeR7NLIW9LgCfJl4vYk1q7KyI1cRVrOeeLAEMeSKXrWja7q%2BIjXVr2IxnrkKUiLtajdWSCSSDjjW5XUE3AFBAvV%2BFBkg6CCUVdFM%2B0taYWh%2FV3a0dB8yl3PFmz5bzpPALZPVn6SSdcq3dACOanquVoiRzMFDZ%2FXeEU7P3%2B0f%2FfPbk7rMtqLCiUkeVAXbTgE7%2BQYoxOY%2BvfMVUklf203aVwAk53vr&X-Amz-Signature=4b643fb7f0f285d7bd06ef27bb4afa7568e10548007f80a37201820db094f270&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


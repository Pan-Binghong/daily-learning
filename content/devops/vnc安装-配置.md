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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGBPZXXW%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx7D7EZ60TtDd72egcXHBP3tujEQxQPY%2FfBGNOjVmkMwIhALJzAgMSu7jQpaldwKtQyQS1xBnf5WpbqHVE2i62%2FrofKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxIM4aEujcXreCP%2Fwwq3AOu5dQSRQryvIPdN%2B0D1sbeD5rUXvxiI%2BVlYoQaMqrCLbwLFWSULCB7yCvGXmagGAUa3rslNfdAlouqEkEFpKQlflbtidwUdjah%2F3%2F6yQvZNOvghtFUJxZOZf%2BKUxcyyrYDzYr93g1bo%2BuRmerwrF2I5afVWCAzNuw3wHNnZkaeLgNCMfR6zKwXQoL5NZuwkjkexEJlrMqmeUqSGKsHCzTlIbh7lfDB%2BBWq4FICtjFiLDKREJE4F0QSHWjVeRgXcExVYX6Et%2Biw7gpy0Lod6ThcG7j1wesKyQBCCRfiPNwSuHLXK9AodRbIP5w6NhWoU%2FxE0cfbDRwtmKAmdP95EVBVfnGHTbF7fQgJAkRMnb1A0hrOgbCZYeJSDTLkWEYFoXcTmRDPDTCK0ASqI1xctDjkJepu2Y9XHClfLBVr0HxoRKWsxN4ObPXgROiiFzgCZbv%2F98mGxjEDn9c0Ji9hII3a5vBxO%2Bqug7dieuEH8yxwAtFqp0sPBzNOQcI%2B3LnZlCsJ6%2Fll0A%2BoxWIDdVp3jerSk8AQPCaRBCKxF1PeClsNFnMVJDwnc3omMaV1tZraJR3BDbQQJNwERAU6N1tqQ1l68Vep1iRbedA6UZh4PwsPk9KV4VbVN6O%2BlxWeKjD0lfvLBjqkARPOqO6oO3DxUKC8F5ehhwcKpPYjKJhsmTNPB4LYr0Rfw7NkvRPjcSKnQR89d81C5spLmY97oP2eKBPfSC%2FZafdgFnVWt%2FsQsYMmz7y%2BesSAIwHVGm7LIyS6kxsAaQ44bpaP7F4Ev1f2zgc%2FryFJeqZcYKeKDYk%2BWKI8ECMylQjmE7gfwZ%2BHPuwR1NJynjIRnzyWvnvfIswpfyGaoPnGDq%2FCutLB&X-Amz-Signature=6dd43169fa0c1e4f0552c41be3f72bdae084c3d8e92f3cb54afef74a59914e9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGBPZXXW%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx7D7EZ60TtDd72egcXHBP3tujEQxQPY%2FfBGNOjVmkMwIhALJzAgMSu7jQpaldwKtQyQS1xBnf5WpbqHVE2i62%2FrofKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxIM4aEujcXreCP%2Fwwq3AOu5dQSRQryvIPdN%2B0D1sbeD5rUXvxiI%2BVlYoQaMqrCLbwLFWSULCB7yCvGXmagGAUa3rslNfdAlouqEkEFpKQlflbtidwUdjah%2F3%2F6yQvZNOvghtFUJxZOZf%2BKUxcyyrYDzYr93g1bo%2BuRmerwrF2I5afVWCAzNuw3wHNnZkaeLgNCMfR6zKwXQoL5NZuwkjkexEJlrMqmeUqSGKsHCzTlIbh7lfDB%2BBWq4FICtjFiLDKREJE4F0QSHWjVeRgXcExVYX6Et%2Biw7gpy0Lod6ThcG7j1wesKyQBCCRfiPNwSuHLXK9AodRbIP5w6NhWoU%2FxE0cfbDRwtmKAmdP95EVBVfnGHTbF7fQgJAkRMnb1A0hrOgbCZYeJSDTLkWEYFoXcTmRDPDTCK0ASqI1xctDjkJepu2Y9XHClfLBVr0HxoRKWsxN4ObPXgROiiFzgCZbv%2F98mGxjEDn9c0Ji9hII3a5vBxO%2Bqug7dieuEH8yxwAtFqp0sPBzNOQcI%2B3LnZlCsJ6%2Fll0A%2BoxWIDdVp3jerSk8AQPCaRBCKxF1PeClsNFnMVJDwnc3omMaV1tZraJR3BDbQQJNwERAU6N1tqQ1l68Vep1iRbedA6UZh4PwsPk9KV4VbVN6O%2BlxWeKjD0lfvLBjqkARPOqO6oO3DxUKC8F5ehhwcKpPYjKJhsmTNPB4LYr0Rfw7NkvRPjcSKnQR89d81C5spLmY97oP2eKBPfSC%2FZafdgFnVWt%2FsQsYMmz7y%2BesSAIwHVGm7LIyS6kxsAaQ44bpaP7F4Ev1f2zgc%2FryFJeqZcYKeKDYk%2BWKI8ECMylQjmE7gfwZ%2BHPuwR1NJynjIRnzyWvnvfIswpfyGaoPnGDq%2FCutLB&X-Amz-Signature=1275ac9532e3dbe8545021b0970f50ab50a80b1131e14fb15dbee768fdc00761&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


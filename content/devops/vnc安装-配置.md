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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBSZZ3MQ%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcAFD9qlX8v06VlU0CM%2B8wYyRWjqn68s2rlA5DI67apwIgay%2BtA4YgGOQK3nz4rsMLP3jNhHsL6FmzXfJxiwF2yN8qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOL3IdrhNzOKbsnJICrcA8Y4sBe2c%2F5IAJtJr6REJwFxpPKYbdqqraPCWRu6q4Zw27WhGaVcTmyZDpEs2G9TN0gdUeBe1rUCIGm3Yeoiy4oPdcOX5yLQZeCpZ103x%2FI9YbOM%2FlMlmZpYMGJHWOIGjXnqHBhyh80Z8FZUZkZi%2Fq%2FvsiwGReW%2Ftwpsd2OtaKGc3eBK0y60fYF9QL1z4hJgUE7rjPyXlFK7j34Ao9NV%2FwJtp1HbV3LeTQxK2n9p4Jl203rmJ7%2BbJQDaINeClcUOvYOWooGwJdK1EdH4jaIqFwiCSrmAMPbxAuY7N8Bk%2BtM8DeKw2zmvpqpiyS0%2Fq6emA64XkucWDhnNswskp3YwaC33BNzc4CU4X7BBDeQ7F1BiBAmxKZDapHbSfmvCwp5H62Cb9upjwsk33MLEazaw6JYsUnxixXPypGBy3RYo3FHWBPc83%2FpCTFg6xXBQCqc92kj2CJ16RAsYOZekYkDBLdvd9%2Fpap0e6lQAYltdWoXpLFQg5Cd%2F7kcf3aHQAWPjXBVirx5HawYt%2F6eGWET3m0PufAinoUhiTBVviDnxlBqEXNpWWf8aQWCDvBs4hu1qWishr0Xk4f9bgBLlb4NNsTpJ4o9vsSlyXv3JPk9hpb8aK1TU1640G2gwI%2FwvkMMbdtcsGOqUBvuhkWD40aKhrNc3mdNqbfleLIKvyd1JGnEfzS%2BBNWoQS4lc3vZ1WfC%2FXIxbybJcf%2B%2BrKIiJVdTl%2FnRJE5cwbdPdniWQVBpqBxzVGzNfFLzB4uyNTVbiSaqnhMHYtya%2F718E1zcq4v5953fvdj%2BkleNOBwPNJcG7sz%2FhpHHX1aa9drCzR3IkrJOctSxNnY6%2Bh1MHq7ae2kgA%2FcYSOaSt0UX1QTZ%2F%2B&X-Amz-Signature=823ee04b568166a619f8a8428745d853f25b3201f8f35a390dfe2dbf47e556f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBSZZ3MQ%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcAFD9qlX8v06VlU0CM%2B8wYyRWjqn68s2rlA5DI67apwIgay%2BtA4YgGOQK3nz4rsMLP3jNhHsL6FmzXfJxiwF2yN8qiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOL3IdrhNzOKbsnJICrcA8Y4sBe2c%2F5IAJtJr6REJwFxpPKYbdqqraPCWRu6q4Zw27WhGaVcTmyZDpEs2G9TN0gdUeBe1rUCIGm3Yeoiy4oPdcOX5yLQZeCpZ103x%2FI9YbOM%2FlMlmZpYMGJHWOIGjXnqHBhyh80Z8FZUZkZi%2Fq%2FvsiwGReW%2Ftwpsd2OtaKGc3eBK0y60fYF9QL1z4hJgUE7rjPyXlFK7j34Ao9NV%2FwJtp1HbV3LeTQxK2n9p4Jl203rmJ7%2BbJQDaINeClcUOvYOWooGwJdK1EdH4jaIqFwiCSrmAMPbxAuY7N8Bk%2BtM8DeKw2zmvpqpiyS0%2Fq6emA64XkucWDhnNswskp3YwaC33BNzc4CU4X7BBDeQ7F1BiBAmxKZDapHbSfmvCwp5H62Cb9upjwsk33MLEazaw6JYsUnxixXPypGBy3RYo3FHWBPc83%2FpCTFg6xXBQCqc92kj2CJ16RAsYOZekYkDBLdvd9%2Fpap0e6lQAYltdWoXpLFQg5Cd%2F7kcf3aHQAWPjXBVirx5HawYt%2F6eGWET3m0PufAinoUhiTBVviDnxlBqEXNpWWf8aQWCDvBs4hu1qWishr0Xk4f9bgBLlb4NNsTpJ4o9vsSlyXv3JPk9hpb8aK1TU1640G2gwI%2FwvkMMbdtcsGOqUBvuhkWD40aKhrNc3mdNqbfleLIKvyd1JGnEfzS%2BBNWoQS4lc3vZ1WfC%2FXIxbybJcf%2B%2BrKIiJVdTl%2FnRJE5cwbdPdniWQVBpqBxzVGzNfFLzB4uyNTVbiSaqnhMHYtya%2F718E1zcq4v5953fvdj%2BkleNOBwPNJcG7sz%2FhpHHX1aa9drCzR3IkrJOctSxNnY6%2Bh1MHq7ae2kgA%2FcYSOaSt0UX1QTZ%2F%2B&X-Amz-Signature=b5d254d3fcc3f81081f8755561cf509e5b6a499c897c57fb6e7356b344b106ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


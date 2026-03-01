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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPNYOHVI%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDF0o5VuCVu0CVOEQ7gkR01p2nlry9Kf%2BpwUGFrcZdoYQIhAO9RHZv1JochrBnnVXOBZ0x5ckX6X79CpDr2Qy8g6%2Bm9Kv8DCGQQABoMNjM3NDIzMTgzODA1IgwlI1xS31td5aXf7VEq3ANE0Ux8v7WNOSYn2tr2b2TGIb8tkAFDb9oz1FfL7RWVIhWwCqy%2BXfWk3eFe%2FmRT1TDyCxZW8ZbdeTfdxvuD2HjwY7Wezi%2FeaLeFNtOU1IISYDJg6tANfqGWfcOK4iBvUU5Xb3%2B0IG37LjbKY%2BLE96EodWRuJrMABG3ikCqB%2FO0Ri5%2FT2iOif9lwZprXTsObUpQFz6qWt5JT%2Fl0gzGaLMdMlDadCwLmWH4yDE%2BUf333UcpIhbHAyqGna%2BzsWJh%2BC%2FpnaUu6cTLzwJdEX8D3InTgkwQhSI74JnMWl9ctvnxijKIl8oPtmkXrZLJeRQVvpZkutcPHPlhnkWB2YPvwRsd5qocffI%2B0OgzjBhrkbUqWMvwNBDo6tsUef8tDjk6svKmzceAOi28VW%2FSWQStXOmTA%2F9m90x7yfATPKeOG1%2Fz8Gx2WSSn50j8p4CDE%2Fnk4PrvPiUjx%2FYmfyIQ7DOCL0Vx%2BjKwHAYjjGWMaSJuGmQb1V6FDTO5RNdxbnSWBR4S8goGe8xDX79wqSXD3bev%2B9W3UL7LCit2Mha5xWPn5DQLQi1dnmqLXPc6JdjRTk%2FLpc2Gn1C%2FzNtjvlbq%2FgERSPILUBkGnYAr2JRlmUW7UGj0%2FBZyQwplj6OxVDyxO%2B4jCjzo7NBjqkAXwJV88iRNeZcJSCgwk2HPKuzX1gYHFEx%2BCoVNCThV88QdbhPZEehYb%2FtF9aZ9R4vXHReoolFL4KOzOz1BBNWaF0SpmTHJ6wNW%2BKM7a0w1oUm08zF45zvm3iiCYXJUwiUB%2FuP7NXTEk0HqVLK9ObfeBcBbO8treMy7Ij%2F4iyNE%2BPWL5DpckhJQaNZFGtz6PwtgotOvIjSr7Ruodcg5KJeFZvhowZ&X-Amz-Signature=5299046d783b2d6e585fd6d7dc13c16acad0057505d3fda5129b51f05cc07040&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPNYOHVI%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDF0o5VuCVu0CVOEQ7gkR01p2nlry9Kf%2BpwUGFrcZdoYQIhAO9RHZv1JochrBnnVXOBZ0x5ckX6X79CpDr2Qy8g6%2Bm9Kv8DCGQQABoMNjM3NDIzMTgzODA1IgwlI1xS31td5aXf7VEq3ANE0Ux8v7WNOSYn2tr2b2TGIb8tkAFDb9oz1FfL7RWVIhWwCqy%2BXfWk3eFe%2FmRT1TDyCxZW8ZbdeTfdxvuD2HjwY7Wezi%2FeaLeFNtOU1IISYDJg6tANfqGWfcOK4iBvUU5Xb3%2B0IG37LjbKY%2BLE96EodWRuJrMABG3ikCqB%2FO0Ri5%2FT2iOif9lwZprXTsObUpQFz6qWt5JT%2Fl0gzGaLMdMlDadCwLmWH4yDE%2BUf333UcpIhbHAyqGna%2BzsWJh%2BC%2FpnaUu6cTLzwJdEX8D3InTgkwQhSI74JnMWl9ctvnxijKIl8oPtmkXrZLJeRQVvpZkutcPHPlhnkWB2YPvwRsd5qocffI%2B0OgzjBhrkbUqWMvwNBDo6tsUef8tDjk6svKmzceAOi28VW%2FSWQStXOmTA%2F9m90x7yfATPKeOG1%2Fz8Gx2WSSn50j8p4CDE%2Fnk4PrvPiUjx%2FYmfyIQ7DOCL0Vx%2BjKwHAYjjGWMaSJuGmQb1V6FDTO5RNdxbnSWBR4S8goGe8xDX79wqSXD3bev%2B9W3UL7LCit2Mha5xWPn5DQLQi1dnmqLXPc6JdjRTk%2FLpc2Gn1C%2FzNtjvlbq%2FgERSPILUBkGnYAr2JRlmUW7UGj0%2FBZyQwplj6OxVDyxO%2B4jCjzo7NBjqkAXwJV88iRNeZcJSCgwk2HPKuzX1gYHFEx%2BCoVNCThV88QdbhPZEehYb%2FtF9aZ9R4vXHReoolFL4KOzOz1BBNWaF0SpmTHJ6wNW%2BKM7a0w1oUm08zF45zvm3iiCYXJUwiUB%2FuP7NXTEk0HqVLK9ObfeBcBbO8treMy7Ij%2F4iyNE%2BPWL5DpckhJQaNZFGtz6PwtgotOvIjSr7Ruodcg5KJeFZvhowZ&X-Amz-Signature=227cf215a2e9640d0b1992e7bb7a525a0c7bbc775ebac17161c0630269ebdceb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


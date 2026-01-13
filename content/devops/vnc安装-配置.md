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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIXIZU47%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQDLzMClOnn98En%2FwesPmQPlm60HezPb%2Bajlk1o%2Bh2YPRgIgDQQyXm94VlPt7pX3YnKWvgp7RIywCj%2Bka4k7do539gIqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMgddp9TKTBMoWl3RyrcA%2BOn6HB65UAmUO%2BiI0SVXAMjxf7zk%2B%2BXnxb9b7A9jo1s50SFQk8uZeRWN4eGnPAXz2kA6rvbE2YFgeUthGmCI5W%2B9SDaN72Be%2FT3m%2F6ms37NXBfPcXzBBRgX2skUkQEP6rZTY9JLyJaVZ%2FDdjp%2F88iCPydQg7t9MEZy2UflJIX%2Bb6%2FStmI3QzjJrxLHbol3%2BbCuBgj3HQPjC59po4sZc5%2FvuVEUC52NIk%2FFDDWDXSXqXT4t%2FPzfCB9JAwPBeyoDo2jwjp0hgIXomCCs%2BvG2Lwl5z9qMQNZsdL%2FFUuL2PQNHXDLhfMrHzp%2Bv1VA6shtylcwpbMfAYb68Yfr0SGsGoffw9IiyWZlIFvZU3y0kNJ85DgLpydNelvDtxxsGGmK%2FiodlYKMj0CRGXJrcubYf2RBxgXECRmKzL%2BBdllUJ5izNAnP%2BRphI2ZIfSBqtXxBFckv8HeIVM0P2de0BaKkahguIfQwkde1fLlounDp2i2L%2FrovvLcQP2Fs3otpLlboBVLbCe1K50L08u9dhWlm3%2B4XxvaFHavJoxlIhIC4Xa36zIQphDlhypKnCq8cpfab19hjcc1W4cuHht6UPsBcdfYDpm2wj7Fxz8KWs%2FZNqWTXuJC2Qw1DWyp01Qa8fTMN7mlssGOqUB6Kq%2B1fp6iWFX9FgANR27FtmS1tJf70DkmqopvNvdRVxbK7ql5cGy7sIv4fjZ9V%2FucKA4%2B%2Bmgs9UvQ5I3V%2FudvwQtfY%2BX1OgaRPOC0vnpG6y0hA9Fm22H68S%2FKdvZyMBcKVxNPbobb%2FkJisN3gzjwOUSIbMghk8nq%2F%2F1nU5nrU4FkNDzEjgCl6D94IXKU%2Bqgu6Czf%2FQrb2rg5o9O4l9Rrboq%2BmTxY&X-Amz-Signature=94b91c9e72f77e7152188ee28dfcb53de56642046846d6383e778e4380f38de7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIXIZU47%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQDLzMClOnn98En%2FwesPmQPlm60HezPb%2Bajlk1o%2Bh2YPRgIgDQQyXm94VlPt7pX3YnKWvgp7RIywCj%2Bka4k7do539gIqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMgddp9TKTBMoWl3RyrcA%2BOn6HB65UAmUO%2BiI0SVXAMjxf7zk%2B%2BXnxb9b7A9jo1s50SFQk8uZeRWN4eGnPAXz2kA6rvbE2YFgeUthGmCI5W%2B9SDaN72Be%2FT3m%2F6ms37NXBfPcXzBBRgX2skUkQEP6rZTY9JLyJaVZ%2FDdjp%2F88iCPydQg7t9MEZy2UflJIX%2Bb6%2FStmI3QzjJrxLHbol3%2BbCuBgj3HQPjC59po4sZc5%2FvuVEUC52NIk%2FFDDWDXSXqXT4t%2FPzfCB9JAwPBeyoDo2jwjp0hgIXomCCs%2BvG2Lwl5z9qMQNZsdL%2FFUuL2PQNHXDLhfMrHzp%2Bv1VA6shtylcwpbMfAYb68Yfr0SGsGoffw9IiyWZlIFvZU3y0kNJ85DgLpydNelvDtxxsGGmK%2FiodlYKMj0CRGXJrcubYf2RBxgXECRmKzL%2BBdllUJ5izNAnP%2BRphI2ZIfSBqtXxBFckv8HeIVM0P2de0BaKkahguIfQwkde1fLlounDp2i2L%2FrovvLcQP2Fs3otpLlboBVLbCe1K50L08u9dhWlm3%2B4XxvaFHavJoxlIhIC4Xa36zIQphDlhypKnCq8cpfab19hjcc1W4cuHht6UPsBcdfYDpm2wj7Fxz8KWs%2FZNqWTXuJC2Qw1DWyp01Qa8fTMN7mlssGOqUB6Kq%2B1fp6iWFX9FgANR27FtmS1tJf70DkmqopvNvdRVxbK7ql5cGy7sIv4fjZ9V%2FucKA4%2B%2Bmgs9UvQ5I3V%2FudvwQtfY%2BX1OgaRPOC0vnpG6y0hA9Fm22H68S%2FKdvZyMBcKVxNPbobb%2FkJisN3gzjwOUSIbMghk8nq%2F%2F1nU5nrU4FkNDzEjgCl6D94IXKU%2Bqgu6Czf%2FQrb2rg5o9O4l9Rrboq%2BmTxY&X-Amz-Signature=63f6f81f644bb43f11c7ed56d1fe0f7ca1bc19cc3acb07795a56d3c9894fe2bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


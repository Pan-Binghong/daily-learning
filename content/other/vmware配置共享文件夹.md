---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665537VZDP%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T033132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDH6Gwjnd208BScy%2FtFYCfpQGXTnh0MRxDbVP2lwAYjPQIhAPreMuDmriJ5HxrF%2FZFsjbUNOa4gtx9gCXc8k15luDk4KogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyrEz7omerx9MOt0Xwq3AO8rqpses%2Fu42AJdvGU%2B8N4fxygYZpJO42yjtv%2BsJvAVGNZEXWTNo1STT60c2%2BgEEPKkYf8MOllrxrC1TC%2BEgtDAIJZBjxN%2Bv4aDrKbRn4tCgGCIrWU9RZ2qW%2F15xLBBzUHIeiVHJdKf2eLhltUw20MnJ2oXO84I6GUr7eXEGQ9BDbeWernnFD02S1p6lcYmzG%2FUAjbjMg%2FIJP2WW7uXAdZwpGIssJvn967erBNSNd09MQshr8z70y710VWw3nP7hqrCPojBWAc9KbQXO4T%2Bg3Tcpd%2F0b1NY1FIx%2BjKsuiUK4fturHHd0fgSON%2FydfMCCMRNvb7mF8Bv7wDwVmljS7MhpHTC0dc2VtlhFzCJz9LYHYsVeY%2F8f8qx0OiVCxuRI1wLOKiajHFIZLI8RvG0mJRS2TV5fIac%2FfeD4YYRfn%2Fi%2FP2HelkgYVziEodzB2fzkXt0oqpTECcrOX9pTnf6wScWKEzlZgfLAbgnlfGeLxB8XMeH6Zcc0DP8VmpuwXCbXwe8rkWGLTu71iuhkCwHv%2FS%2Fu8BoZabO5MSd8Kla77jc1rwUq4Cwzq%2FewC%2BLROgDNofIi3%2FXyoZFLMnm%2FtHxdKWytYAioUP4dC1eSmiV8p%2F3W12PCnY2hvlk9mqlTDcyPDLBjqkAYWTNBa8Zb%2FXJrrmB%2Fmr82luXE71nj05fUxPU%2BxEnyJTD1LT3GbN3Y1Eay9beTjg%2F6FpzAEuCLki9sZ7RfYUNkP3k1OszOG8d%2FUPSmUS7eUe4AeLWPkyjgtucpndBNGmGmdYoP8MMLH9OFbMeKrlQWAN0ahxc4j0GNzY0j8DetY%2BUlGPEAfG9La0JpERx3OQTy3%2FxGWhlZxv7CTUVoKDBcqYLyaA&X-Amz-Signature=65fe21de6a2c6ce5f2719143881891b8474d39649de02759c5243b4501300891&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 安装 VMware Tools

- 找到虚拟机 - 重新安装 VMware Tools | 如果是灰色就执行下一步
- 重启虚拟机
- 重启的过程中，不停的查看重新安装 VMware Tools
- 当能点击时，点击安装即可
### 配置共享文件夹

- 点击虚拟机设置
- 找到选项
- 选中共享文件夹，按照上图进行配置
### 查看共享文件夹

```bash
cd /mnt/hgfs
ls
```

## 坑

当执行完后，如果没有看见自己的共享文件夹，执行以下命令

```bash
# 如果输出文件夹的名称, 快执行下一步, 如果这个啥都没输出, 我没治了.
vmhgfs-fuse /mnt/hgfs
sudo mount -t fuse.vmhgfs-fuse .host:/ /mnt/hgfs -o allow_other
```




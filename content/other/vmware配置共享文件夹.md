---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DTQ4I72%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030423Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtEwmCcmbXGny%2FTQP0KNe1xnHeKQEmivfK5lo0cIqpsQIhAOO3So3sGTLn2eArmokpLvG02pfn6Urut2TQQuavb38RKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWN9KOtHg1u9uTyocq3APJLvLeHicsV46U5ykfpuu0YaxEU5UZh3jld27OCl1eCHaHapnhRzb9qlluLulDYUj4RvJrd3z1ksNuHqLhemVWgATI4Ka5eYxzjqdZgq9PY29A6r4%2B282r8PkwSBnKi5LB2bXEmOSAbIG4oR5ZCkm%2BtyZ74uwOymoT3HW6mWcba9OHAdVpuYjbyqJWExmdecyJ6iWXmBFnpG70NYLR%2BCg9%2BlC95qFXWnYYGu9VDwm7jrV0Fw75SfxucXaOmiVIFKO1RhEnh1XPImvQwZiEk40%2B9C%2F2qdWZMQIt0Sh5SwKCMDuq4CbkII9M3x2oXtx1mzUg11RBldax0pG0BKLR5SEKKDDBeBSwIXzC69iC2Z71LgkCeWj8b%2FlHT4BALi0FajXoQ%2B5%2FTRmF1%2BvD%2F8AXVJbphEQ4SfmgLMHJoKXG%2F7PNsx%2B%2F%2B67TneeV7quiMCcKqr%2FsmVn7%2BAc%2B9tEqHq971rEw84KKACEO%2BUdpS4v2Dhp0hwBV%2FKHg3hIpdSMp1r%2F72wpfV8oXuGQrCmD9XN8qJ4Z0r1XymMRbi7jW3Bx%2FBz059ofDc36IdBAHEGw6eTnzQRI5OUT6DXbQs%2BIHW23en923hF24tU5wW6TJj4WCcPPqNx5Rzo8BeeARlvP9fjDe2MDLBjqkAavIiWNo50aQCBECKy0JZP4LaGkXCWjKWvcDlwx4HDhWIfsdIEWmmxHSWuBccjb8spclcvxaQpu6J%2F1wB9ykTogAJLOGLY7zK7NG%2FNdhCa0GK6oj3zLYzGPaB9W2tzmid%2F27fp3bLb1RI2AFFOa1GByMADXcSJI0NKwm%2BPvy%2BfvxSPaOkNpLw6dckkbFkxroD4%2BQfiAbZNbB40KqrqWTGzSNNuBM&X-Amz-Signature=f984a87199aaf5f5e102fcff3d885e436ba8ac357030347897ba8d835abb5083&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




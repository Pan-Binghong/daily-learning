---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIJKV7PA%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmB4VtExx6t953v9w2t%2BbykRCzG8k8D9QpBpWgo%2FMMtAiEA3XCFPyhaJMcb423r4jVF9mIDK8iv5dIAj7e4izmXmIMqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIPAGJ%2FC7kACaGgkoyrcA6u1apWoT%2Bki6DdsrcTV3foRs1R1hYrhttqtYBvvkpYCa4qhnyvuJYyCr%2B2ra83LnEK2MX6OjgQjakdKJJDrU%2BrP%2FkLPZRwkGQxWtfBB2LRDipM0g8H951vIwmZsn%2BN8xtpn%2FLfJgYxKNPeDsQGdx3gBD66b%2FiQ7mYMn%2BPmgHzAMM1Xgu2hifYL6w34Kvyl%2B3Ctv9XBXV6aYQwUlBBMfnb0Arzca9Mzchl4X6z5A5ICi9Fj%2BUnrZwQramaseFaPt7s0UQh%2BOzfYnVVQmmKAiHsMiX4T62AqVtkffqq1GsbDX2yGXn3hTnpL9KZwy1JziXmJDSLfSahJe93g7K6LHZj1kbUMUiE5WbTdunYhUB7qSEe1pCQgNtgJq4NMSgGec4B5XMl4XDfgx7xnciZ21os9LMpa4EBMpBSNDg%2FPZotfoMhVm7fIawihkmEW%2FVnRCVoLeRDCSYznIR0ap64n%2Fy5HbQ%2BKaTiEvggiZi2VNtKIIVRiy77z0WONuDk%2BuzIraz%2FC2OIlVshkPJl2seGC7b%2Bn1dLW1kh47rWZKmhrim4RKB8FBFOYi5ikKGSCo0dXqF9INob3UGVHbZyQ6CILpfLfP%2FYj%2FKbeKK77XFZZ7x1HVWlk6KrSqP5eL0DgBMMbxr8gGOqUBII4nfzq%2BIAzXS8%2F%2F7OHLExC2YOq8MvgStDlPI7lG6wi0em50Rotyxgf5vJQvyMtvJTBpODK6t0x4jq%2BFOLGjNaKpQt0RpbBFZETTr6UQ1QwTnnU6CIt7cZJgvAdDEoPaNCGb3VuoeoIR8ylviu5%2BoRGrvZLDr%2FlgFsX75d%2FV2anEF7u3zYmJRZjhYt0bpGzZC6%2FC%2BNlOxkUL%2BUKAJEeA%2FpQBvwYE&X-Amz-Signature=cf2b69cd8bb98af69bf31e692a58c23550afa619c8bb9dffdbb656f9b6660527&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




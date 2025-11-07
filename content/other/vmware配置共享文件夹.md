---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCGCMP3F%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZ6SPtKCdjKynjrDZfJJ3EoE0pb4ukYNeFoe5NpcGTCQIgeeH40PVFVzPgaRqgYcCqr8sAW59eRAXNfhnTk%2F%2BqFB8qiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDeAWPLi%2Fa2zD9JZvyrcA5wUo8wlqTZduN897c7M3hDlZdp9SFv2iFERAlXfjSDgqOpZmL5Yh5hs4da2vHdQqlqVieoUafEojqzDqNd6tIDCqNq%2BFkAR8JFD4z4B%2BCatP6t%2FHRlnOcBKXcdHbbwDz3dfm8Xuo5SFt45l05TVAlCJ5J8kQzJ4qWWnsFYiYwTGh4dT1iP6Yx5en%2FV6B2HiESQIThg5c1uDKl7LOnHDy7qLIQ1omUjGOxzDbHdSXijnGa3Q4kZCPGM4KXKtPjNLZZn1dfYuidezhORBcOOewrwAFxnH%2BbH610YwGycOWiPoS2T2QDLSj5b%2BNnDP7Dvojzf0MQtIjY7MgWpS%2BNh%2BJ2k7C6eybhPwo22Jg4octDVfHk6WjcSihJqpowcwO5F9%2FWJR5ZnleC%2B%2Fn9oXMJXPRhQ3%2F0itJmtFXuIi1hhyUiW2pXOVKbs7eXFRz1l7fehVeQ5dUcCWPzZqYBuEB%2FdAsqATnJrryS6gtmN%2FgmHuq1NtGulaqD29YWVNupVwG0k4YpA0zujbhk%2FcBmGCKg7%2Bk5wE64oOe1BIFoZlvuAI2dDPiVFF5FUUaCGLjTxGWHaGLi3HP%2BDVm36frS1qw8oQT7nSlluXtFX7RpwuMzXmhPGZMpb4g13Vb%2FGXmGU%2FMKe2tcgGOqUB2KF1VMqk7w9HnzI4NMQQWP76z0NphnqPCBP8dA96Jv9macNeyb3lCCAVgz%2B%2FNv70bXrzlEB3I0gkS%2B1Jg2QPkyYyIL5cpMC1325bWUt1U3w7zZVO9JDZT86l%2BfAvQs2DhvygalTilmbCC%2FzGrkpo0JTJTWGYmDSxbNPT1wJHOX%2FEwbyhoQWk%2FVurUXci3PAhpWVhj05oVvasALxyjm6kFyPOCi3U&X-Amz-Signature=fc97af8006416c715a198b9c455fd6a19dbbc05a015a4db825211367be425910&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




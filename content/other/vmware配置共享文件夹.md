---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TSE5VDX%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICBWM3WkJ9us6B4o7duTyPac8yhAUVrrzW91ggLvpTsWAiEAnFY2u2ij5bd4hjohhhGsMw3lSq6nM7lWgp%2Fbq1M5wqwq%2FwMITBAAGgw2Mzc0MjMxODM4MDUiDA1vC%2Fu5t9tyCwVEIircA4AE4PNdgsnxImVEOwWvwocuTrKp2b0inxj2dpMyOmR29N3BTrRgN7iVsY7z%2FcDA%2FiV4MzfCVCLf0WABdYdBbG0F4w4oFW3i9uk6x9M9cs4R2TL8lA9gAUvbgog6n2p2lsWgpkc0iW23%2BUTV4zC37iETqZSIhCcr2zlHk0DucTBc0kpJUQ0rhvZ2dDLpqXC2sePJPSRArqJLLGlYCe5bBeEMZAJ9HvLylrgpXFK8t6jUR5L6cHPpOi%2BCZ1q6iQ8pALkMXKDoBv9FZtZuSary35pfuBVHnfdyRIdMqw4eR740kJcVdcjOE8B9eO7QNA5OsHcKczk0QIaMIlJ0ZvnkdDfVUSX21siFb5CWiwNOHy4lh0R0NFBHhj1G%2Fwj7TRVuq%2BS5QIg3IXAw%2FeSfmNLZRktIHL7O1d714tM7zhZbu3bez5EIcYdw%2BINePhFwRIVR5Gh3u5Kej3wFtkR6mjxtRnPyb9DYxwmghM3gGgzDe2Lnm4sAQgyg1qiSGDcZUNVNNLAoFjnSO8QavC53rYYj9e6vLm80HIHoyPx9CmNuMCGgvFCDxlyL2g6Oubc4SUL6nTZQWfhlBc0FMIiEkbPdU7noQO4qpdbT4mhtKCG3fCUlHKs%2F%2BCLhvAo%2BtozwMOXT4MsGOqUBFwbDsqrrZu47JmyUN5Z38UwGYl1g1Qtl9hIlZmjgk7jPyUhxEa33dECufO78SjeCYkWTUgLU4d7lf46fq0k%2FSWKdDOaeGNMw%2BvlZXdJL1EKgVxVM47sWZhAfAfhL7q9hKTDMZB1wcUCZH6ReZXYgiyW6KnWBOOoj2SMujvG9%2FO26k2gnwE9JGtt6wEF9i%2BgpGwoUd9%2FoJFNwYlUtDt%2BNwQaD0kkz&X-Amz-Signature=b7fef072e209f3ba11e89de812455c819c11becfc480c9f2011ddeeff9b3cdfb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




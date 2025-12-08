---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDA3IH2A%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEbPyJQdmu0M4J92hjNGhDeh8G91%2Bmu14TUSiuzf2XbfAiEAzIuEr%2BB3xEPM1BjEjdPK%2Fqwi8IpADvTHhysGvWIdwxMqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOGiH%2Fqf5uLBwcKS1SrcA%2BPCe4q70RbtH0HPtLIwYLNRDCmKRLNtaakPDQ78IYOY3dxNq8bGtk4x7KMoC0LhFbmyyQ2%2BcWPoLnUc3UcZGFr487AbucuYev%2Flr3LcYNaL07yu7w5QwkTTpnMgAVG%2Fs8NeuaAmAhiBmjYhidVW%2FfQhvPoxKRe4GnFhDKy6mq0ZHYtnu8SjJG2uIC6bQ8%2BsrlnfB4jsa3jHgCLdj3tJ8uo%2FOsgL6U2hGDGWqUtXHOHStq0R4YJf%2FCCzV0Ar19mLqxk3P%2BGWgoBgzQ4bKRarLxZFuTkEZ%2Fq038zQ6%2FXSKdANiP4RARZBtbshMFUjnYCw3T%2BzLXp8xrce0ir%2BrsuEfZHgEh0cmeI2cBaKQ7pTMLUpu0mlyKLkZEUmrPdbqEHYpyti0eHlpePf25qNEHQ9JJ%2BaB%2Fu3nn37vAKBlsHc5Gm7rbX7pa6%2FSPfDG54ch7pC9FumBqdgZ96W%2FIzKmhNF2SUX6GDZWOzwFxYB8tdDP5P%2FPSiul8wT6iLtC7TTa6aEl51IDh5Z6Hd0C8kL1eYLIP46bEbmlKlShpd0ViqFgOuFG2LXAPQe7dWwCv8iwt%2FqZAbWvtW6I0CoFhZvO3JmYj13hnn%2BkuvNs9MMN6gEou8zXeV3JzmQxRUt2KvgMKDu2MkGOqUBt7I6bhJk79mmzgVP5AHpUkBXdtkyiY6c0OgedLxAvsaD5taYgzeIABW1uD3JlnVavBItNblQnHa6ru2XLA6cAPscoPwIpsnwtpfyvbod4CB4y46CfIrFmqNvLjquJCM2D32tVs4xWrY60cOoR49u3aWyu7EEhO6I%2B2ttfIKyTB5MlaXeyg4F3Ce0T4Tma6LpviZHW64C0%2B%2BjBaORALhX6onpY8WH&X-Amz-Signature=abe14059f1bd34633f161c8b079f30402b2d2a13c25b4b7b46e7f443151d9e60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




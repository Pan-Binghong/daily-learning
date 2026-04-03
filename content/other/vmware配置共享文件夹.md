---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLWGAKZP%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDDy9mQvEFsqkaNoymdQYihI35ECPa6vQ%2FccIFl4csKdAiEA6VfFMLrwPG0aPyGsMp8gGnw8htODOgwsAAaHFjP7yK0qiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJpRzwIJbdmc7X3mbyrcAyX8tBnCskmT5ZkealziwjLME6VvwHGLEOZAc7fSvMaOxUsl9swR%2Fzjz9BpkVk4opLIYY%2Foghkkn5DCFTj0%2Bek9v7MoCHJNkGXumxhTvXQvUGCIZnXvI0%2Bwixdhrc7yReiWNSbv2QSh5dPf7bfOhDes1Jzsr3ZRvVtxbGOF%2Bx3UzmCosuzBjpqhvEVIm%2Bpfn%2BEHjXSqINEbo2LrqG1tKWW13KqMbgBJPQj3IcWByVymVzwexOIGN2VyWLnkVf9B7YPGkwP9Ih%2BwAjl%2F4tLCZYztt57hZY1npIJckxfGDFvfXlAObkViCbDv1jNH9HOJvkPcRVA8sCEArE4J87fyi4kJQ%2BYcPuMSKkR9jiQUrBpq6htihAUYxMayE2hqDPX2dFkAjoaE51S11suC6m8bkmjRpF1NtDPXVU5s8aUozPycRvnbhIRlowtILzQy1fI1ZTrRsjyBeo41gS2KiHTNKSKKtdIkIcpXXOusk%2B7w3KLz%2FhekzG7UAJvJxlmJGi%2F9gzODgBUsnsrPfyIX91p1eu26n7cWpBbF1MsAmiUdnhrQg3lYkMdq88kaZD7%2B2NfoxiXFaYbYEMFmAMc22A3ZL7zDk7j7U2YkzAdw6BFBD3LuyG6rMFqmgIyzVAgX%2FMN%2FQvc4GOqUBW%2BDKvExYq2FqSmCkjTHonNWudDEhqQ2Qja2agsqEtyCYesRFZUY0Yv6mvw5URe71WJIMiGwcO7oHvhcpIi0GDGlYZq%2FEUvNSz84%2BconK1eEYnIt666TlEImnX%2FrdW7r3Rmd9CdB6uQoLhjYf2BeSnvi%2F7MzDTQ%2BxoGq5fe0hbG3TQXSkolIMwUURw3bFEbrmabi5mA8hIGL7QRWlcwgotVaQXg81&X-Amz-Signature=1aa86ee6b78b19ebc5054dbe2c75ddaa55275d5bae6cc90cd7d9e9c81e5f9994&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




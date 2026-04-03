---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FA44IXJ%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbDdJUx%2F0QJU4%2Be3z087oD4JusKpUTzIF4hL3%2Fi4AuJQIhALt4owCIlxeAdIivtDS%2BGvTU7mVqK2UgASe3BapQRj7rKv8DCH8QABoMNjM3NDIzMTgzODA1IgwdXIKgHcBthMtbymwq3AOMcAYj6xdVx32jnFujqRUd7CMSIZbfezjAjDAZOksLfuKa5Je9swCMkA%2Bm5dUtZdyOgL%2BOgs2efPo77nWaYcF6ZsJRWf%2BfZy8abknxwMyWxLA%2B0kwm103yNyCwSeouMcUh9zHCf2E985yLKYgQPXumO6RAVYuhssMvhOIamPQ6OIXnb5wFAhe%2B0SB8vWphbYds%2BRLxhFh5%2BRqig082NBREBi1QBKqyrnHB9simVBt233tKIvgQPhUTSykEFiwE8lQwsCQajXRSB%2F2gd73frOnTo3Qtq7IezEqSYt0nIS5hD5yn1e6wnBuufN5o568zbvY4O19m9XMc5803hSP7sQsjHfiNZcJ3eWEhw5ByyIokyIuiUHgwIq7mTVrXXlne1TWjIdgEaoFirMyWz0FZQ%2Fbx1NCutITgLtKL8gNQDXUpFOla38HZS2wXYlo1PdsTH6glulpJ8wNQPTG8b2cUCwrno9PST0GNVkMJuxwgSaOkLHqzLK%2FaEsGcw5zF5Q%2BoH4fJhVuReGmuBs5uVPAxSdYvIGZQLuzJCcBfg6sXjys1FAvhAQZcZq4C8quElekQ9p3HV87HZK7k%2BLtdPcXi5EVrEQWGvF%2F2vV7Hb05StBdInQlbr4GelGafC6LlXzDJrr3OBjqkAZjZff2mbJ979BDLSyuWHoZ0sgzLHyDoNHQMHmWPHtcrvokpjDhJ6%2F8KTkcZOJnCp5U5rIuurt3qUnSwK%2F4WqBueqJMWTtkYzcgKUZ0%2BE0QJ82kWZ2yQdVzFwYTnSFaHsudofx1DnjCN%2Fksp98FfjdicBC3ZI%2Bk6KC07Z2hMi%2BMqLtksa83tdo9jtbyFzZVJ9eMUGwyStpz%2F9VBUbB4ZpFO4Xtgm&X-Amz-Signature=bb1a2ab6cf8e9d6335250e24cb7c77be412ffe018289a59e5918964fe2ea68fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666U6VOL4B%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIGtkVHlMoJlfIyEdzifmn9zjqHsCYSJk%2Bb%2Fd75LmSPlWAiA0EtFmlKiF8uUUQJz4IKHbd8Mw5PX4QzyT%2B6mer2OQsyr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMS44%2FDq6r2cQzRndyKtwD1w5INndpLOPNDcP4zPKoaez%2FgqQ6TX%2FN1vM%2BWGzq%2FGMYEtCuSnFPCtLRYEm4CZ1MHGuUTTtIUCfITzDD7HiaGmACKqiyDzR1%2FER5%2BGW%2BDX9eWhRHJaTdQtEZ78colzYBPosrQVksEGqumxiAZ1LVzLuMOX8A7TCZ1o4Oi%2BQ2JKIitP3XqR%2BoNYo9Yll%2BALHNr4HLF1h4mu9mMc6XI7PVk1TZ1yTQrcenFLP19tsjfby0KLhRQsSx5crU0AzlrU5C3Gd0MS0wFOhCYJqQPSbuvD5aGKYwgqctC4T%2BlHsKOXd6XiefzbJf94JKGUylKG8En%2BMGcyi0Su2qEWLxm4KxPKFSb5E4d0zauAdH7vHznPiOxiT3CV1VZgEPIs0DghNGnThvl1AvPPKBdZ9gAioCsMqPPxBfsOe%2FuO4BIbajBlmAQcfsQMW9JXB9MpM9aAndh8X16GtQBjl1v%2F1DqjYzAy9XmWtn1ZyUiZaeXv8zHI2SNUl4Zf1ekViy1UEZvkvNhzaUQ%2BtKM71BIc7biFZG3jAJXfzsPcvSB8Gl0E3Qy3dD1nGr3aUefBtO4CsujuHY0HD8OWNiApnGTnj0QnCZy7SfBmrcp6ZqFQAbG2GHOv9tb8pN550lzMepBQUwlr%2FKyAY6pgFPM3a6z2V%2FXyYPvetcLbBxUIrRxsXIhadlrudGY26OZEtWnJxYq5Cwm89tb3Xte2bqXXM%2FMaEVlKnaAXMWqkd4akQn%2BU5iE%2Bs3wPhK2yDaHlfQ%2BynXvzTzoXz2hJNP23fCdVzae9pPGU2vPJcKTr9%2BgPeBJSE1eiKBFAfk%2FvDnuBKRy188dnhJGd8UPjxvNNJ0zycAkestgKOakI9CGOKkQuNZNWNU&X-Amz-Signature=1d4c8168974a34a6708329dcd6f5fe1c36d4557b0ba51104a04cccb8daf9aafc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




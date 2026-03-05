---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666F4DBOY2%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlJs8YZQf3lTe9iKWTuvbeCWD2wGTVElpu%2B%2FHWcd%2FMewIhAMmc7JB8uS%2F59SmLcJiqIqOuXhXUi%2Fwnke8sKdiR0fnCKogECMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLWWg7uOYsR%2BUXefIq3APGeZ1yK18aqvN6HICsnNDaVLjTWgeBB1TfG8BhbfQgRaxPsPhpt82JpYDIA3C%2FkmmdJqsqt%2FzbBYbztvyG%2BxXG85X%2Fqk9c9MLxaPyhUm10uul6Z4lxqLSshLeqZG6TXXFXQ8TBTiVTC8rJYJvnGQ06X9Ltel2TRcmOHB7y0hOKEiP%2FfCZVQo8554DGbUYvodXLRC5YYpqzXavdryo7WTTtIpe6P%2FDCB8ua4btnO7LvvpN0zIprz9cjGUvUforXqW2ZGkiqeLen4%2BPoFC91kB4uuHF6a1XhrC7%2FTapWNr3MotS7oDHMk4mQBa0lf%2By2evDp5Zaui5tgm2we4mAvQl2drUFrCa7kZ1EsBP9nwRPhMf7Rdr08twjRlKrBnbE5Ajnb8L0Rmupnce%2BFhJKnD7Id4FPlR6NuLEupcHsGnDsjOz5bQjsfNTz%2BkCKT34jdxknZmWQNhza0zHqGMG0BTkz9LUKVwRNGzHZvnYHWlcDYhc74t7bo5GtjEX7SzLU49MUXOy0QYcbKbliGOZWRbDzJmtcQ2k0iZKP7UzLSYa4yNEDsbcfAwIU%2Ff0B1t1dkFUsjVuJ9GHSWS1bEPuk7cNwqvbZyfiTOkY4ySi1OaTN674WaFAdAo4G2Ol5M0TDG4KPNBjqkAVDKTJt6MIkr3m5TGyhpjUEePkG7Me8yQbpJXOvdUXTg8LX%2F04fuRTGAxFN9vgTQ1QmQKhPn7MB2rIRFRwoMl5HM78O8Bq30fYtGhLybVLVBG3YSarwlTZWWYbM8KEUbhcU6fYazSNGSis75aCMRBbza4Rkb71PSumJ%2BKrUNB7%2FQcZDp4dql%2BF8oP0JGxuWT68XhYqNa0KwN%2Fdnj0Iz%2FMCBOTdOv&X-Amz-Signature=44efed0a9f3ff26543eabfad8a4fc5847a8e88f826ced2ff6187cfb83710a6bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




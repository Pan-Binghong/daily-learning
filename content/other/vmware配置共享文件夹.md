---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QE4P25ST%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQCEDwLtAZZNI3CDk0jivnSNT8yYpQSgxThxzVlLemMDAQIgc8RLx%2BeMQeHfuntKX3K2twcN8DMPNT%2FyUWzOTwS%2FXJMq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDGkFMVza09qDzyvgkircA7Hv7Mm5SiazrELpdiYmSh0JagrsdXwFKcAldxKJpabMLO%2BOlWiTEVj4Ac2J80ItpJT3%2B27iebstSbthMFDSwmluiofDPusgNIbN%2F0UcUvT83sPbegrVmpsZSS2N8amZDu13DWLnLjq6AR%2Ft5U%2BYExxPi%2F2NKoSJki2cAg6p6ALE4eZ%2FiNcUGs2PvZwm03BNGSGvew8SzgmCHX%2BBFHdvP5f2EFz0T8spbylddiTusQigjqBmgmRIGJpRLuaqm4rBchughY2K%2FLIDLYyLLbJytLOGttnIH2Sq6iIxctneA%2B59qTBebX1XeaqAABIdi0k41ZCg00uNSWz6flo14GjQ4BSsS3cWuCjOT5q0NsPSnm9Ma%2F%2FuuESp3ThXX%2BOPdMo3hJcV1sfX3NIPlB8W7mopLR6%2FbQb6vUk0SDMs%2F0dIuhiOulBl%2BGj5I26z3X0mPRl1EUcRe7R0kdlWzaF7rhbHWqMdBFkOu4y17KsUiV4nzn5znyvYqhhzn8w9gwtUdt7yemNDYnLYsjg8gzKpdPH8COwFlF7Vx9fED078SQ18yrRI2aAyRbPUCmR7xFW7X60lUvttI6H%2Fmq5gy%2F%2FOGpjy2pQLcb3BMGssQbsLp5%2Bxf3C3mXhrANFCHRw6APzLMLyhhMkGOqUBSBzqM45722q%2FrpmpT0D5dawfemeOGwfYyLiJBIPnWTSXNApLNH8A5A6%2BVRCXyJBQsYfCaeXRNsaH9%2Flj2yRjsnN6%2FuD5sPvzVJxktUvBX1sWP7%2FdeZvQJRcFguLsKJa2kFPfBzHljpjk2IQIvlbg2iAVTJK11c6bAmIIAOzObdbNwTj4S4v2NzybEwia4KYDveCMYcqeG1T%2FBp9Z2EP8EuVKr4dy&X-Amz-Signature=75a2eee5eb7a2e04a0d9cad786cd29124f7e4d4a248b12103adc6090f75aa3f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




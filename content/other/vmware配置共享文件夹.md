---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMDYIWUP%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG58sfOqogHuEODzIQg%2Bc2N1mbbLIV%2F2G8RimmCK3kFSAiBymAtX04Sb8NBCidr2j4YlY9eB6n6xv0zB32wj7Sfm0yr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMrfq%2FtEKDudtZLFW%2FKtwDduh2kkml2UvF%2B4KwTmrWaw%2F%2F%2FeX4WCXd5h0Ms003%2FDIKj2XZwsexXJ%2B5UtflKVHOth68xh7AnVHmHA3afypjF2pAoP85OiKMav62utABZHqTDQMVuiXzR64dX9M85WQ4YjgWje1FHHzahe4i%2B1jSD9pwYNizPOpKGGD599YFrPG6lAZ75fEXPsCKy2wKx8d87f9OlsYo2ub%2BhTJp8p8luxTYJhXIYTjOUG4rDaoDmQtH8ZMwGkz0G17PybikgFU%2BvO5zUrBq0p5cn3dMDLsyhmdBBDxrYXF72kDvyq4xruPMZNMKnKcf%2Bb5JRMsmWyE45Bi2bJee%2FiLD6iizHHW3ZMu7fpekGyXMwSFdB4DN9X%2BuknE%2FOyvQVSDHf%2FuIMO0acnqU1K5l34ETmECekLMpMlPI6dlswxkoRaFSwMof9%2BTJ90xsVw4bPCJURkyK00%2BhceLoJRsEeCzhMRMELgXD56uJgaF3DfTq9d52LgAuWyH2A8%2F36Wb16E%2BALRSNmZki2qtWMTwj7ztDRNcmP55fuOq1sr4BeSlTHKRCuNeHNEoZ19mRKxnhD20tb9G4OFbClkUo7ik20T2ckOUgbC9XBBDOElG1gJeLKuIwtXVM2%2F1BEyHG644cCUB2kfsw9em8ygY6pgGKPCP%2FTd3p6Tfg8wDew8qXahNU6RKAzRr5zr7z5ZYILhYs0veDmDpkcq5XU796glGOQAvR1wXZsF%2BH56CCiPU1lpsdIBNDfKouOL8seKRSjg2O62uQ%2FU%2FG90w6ANoM67yJ%2B7Z7zkS0huRCZkNIeravzgpgdcuPY4Qftitnf0P9by0dT4fwh1XDcvtkwxyWyAHKXPo0nbdoffn0TsnJBpRRxzHbUWy0&X-Amz-Signature=d1d5377f40a926bd72ab583d45f14fe408379e445f3b3e99a1aa838247846926&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




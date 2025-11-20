---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XB24M5PI%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCICth6iP1UMZNj1vzZ0cDrQ2NxulMu%2FNgQ5%2BXrrQgLvqdAiEAjG%2FK5Lx4hcB%2FZZSdlf%2FC%2BW3WZGNeVFhxtCS%2BGTI8fxgqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCpW2wQqHxnjZKjaDyrcA%2F1l78lAb3PBU7onJdfZA6Ascd82cLeD22iKG3FLvUv%2FvNWowpM0TZpuLVV8wMb5zWoYWC5H7aVeJxyKsS5oWlV0lyclBl%2Bth7ZuiQg86GHiBJgC0LJ%2FPt1D7GOY%2FQ%2BFTMeTvWgIAcM5W%2FjasUHLfqfgnNaRHqOaqv4bIcoD8MbtUC7xeJqb7vVMEN%2Fuyi1zjYESMi9wdl6Ojs%2FAvZDt%2Bc7%2FA%2BkeXLGokYPK%2F%2BRLE%2BVDZeVmreTP3LjUDovvBviRYrzw3C%2Byf7nZZK2GGykrQ32MmSiLEr1lP1L8ahV2VLrfSl14nzNDvsE7dM%2Bl%2FVgeHDfBGTrkPRmBAIlLYUiFqZhta9gJxSgEteprBqjPTVzJIueR6SZBhoOxovjHqaG%2BbtpZpHie7ZtsrJ21GHajhMFN%2FloxFEwFTLbRp%2FVc%2Bm68r9UDWsMWs0b1B4c6r0Lw20tVMmnfYAQ6fWHLRs2bZZqGMabnZY4IYp8EzJ92NBhif4lK1of%2FKhZODPUKfNJe4FsiTel6uRxestbuDQPQr0JWlqmFoSwNVHxRhl9VuANRG1aVCyPtJU47BkMtn%2FTylF9dIYRQhPuq9VIx%2BMGPH447lVrwmrWy4SBPOFPqzWYNlQl6y3QBq7ypLKDvMKvq%2BcgGOqUBSGq%2B8XBhg8Rr7kdV1m54S2kBvgwWhBo9QHVzfvYAS6AkPqOMLRWaazb2%2Bypk2KEN1VxAyMF%2Bkl6sIReFcApYS6sKer7EVXjE9JVUHQSSSRJz2mlD82Vp7A8p9jdtN%2Fx3YN5ByxmY6zwNnM4j7A4Slr3tmU7eJLIE7fwPI25AyRHSTIaBWkfPvoH5qfkKUdEJFtZ7bZn6%2FJEQZts9%2B%2Bdkzd5RJUNA&X-Amz-Signature=99dcf27b3f3e3e89cc9bcfeb06263c60996225c4bd1acc8083c5c75fd3612b08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




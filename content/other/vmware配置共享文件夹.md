---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WT6G4J4S%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQCBg3SD47SRsPIGVjLPmphvMx2jjScipE66weBgtNpQuAIgLyZUskwsoYrQtEzKCH4VOqMtYpHFE6Z1cNBEStlyULsq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDFb8u8F5fqbG654AOyrcA2f6k8MnHORnjKeb3hBiJ4yFuoBB%2Bd9bcrscw6sNGWCBSDm0lg1SGF%2FS0EkMyC0yOJ2vOYDSoJkvBV7%2FWCqOlZ8g1YvqiIt8J231lpPZCehHAjlpStwo4Cx6gAblThuLkg34ed1igU6VMfZD%2Fi41Nl4Q6xqo9VPpk5AiE8Tz8kBXRv1mZaiJhkE894zlrJ%2B6Rd6nTwp5FV4lUS2UJ4pNRRxFfxkekWDnAvB6NUdFJ2gcEXdO3AnJ6WsX9euhPbusxTuZ%2B8EwyPyI%2FVRu%2FePLU%2FobG%2Fm1wYF0HlVqoGaUHUkhPHFbJ2wC5zAyXe83SQTUte5vdH6ZdZcreEta5H%2FI6N4Mqkdvss5N6n51MFaoC5ynIIObC2CvUUBElPQznVrbleGlUTSy0qbYiyULLVg9oXFVdF1fZoDkrQxNQbuRCDVjkHTBlulgh56IDPf%2FDH9jcf9ahyeg5GZt0efwBaOeLLRreQlgUeKDexLzL0%2BMdDVAR8ImFZMmXaDkWwK3RZxDoNk%2B%2FKm%2BZO1ttecrS6YkVJnmoDi8AoMBY6O4hDCQsvYYikEb9SfI2kmpbnZg7ZbxWLU2XY2AMmFTUwS7kG7TARGp2ghUipMv8dytDCcNbfVrYXZ2b6CDnRwG5tKMMNaXls8GOqUB3lFu1wixnpDHGH6CymldigeBFYNu3%2FoA55MJODO0XqAfIJgnZtcLmK3j7dOWq3tu5qcsEypizqYwFmvO1I22DJEJjjVTEgpNga3ls3HEn5Vwqm0%2B7pQyjfFF6Hu6WuIxv2Ck3sV%2BzeOIGrXDpbRHO%2F2YFcXMyqPoMQayUVVzvBO0YY663WvRCl69rJlF7%2F%2F8OK7UhssaXuaCyI4W9S0ANU986%2FxA&X-Amz-Signature=0e2ad24fc78de31c7e437b72d2dc34e201637902e09af4d24a054c0e91e946fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




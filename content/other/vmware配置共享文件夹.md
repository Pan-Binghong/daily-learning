---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TK7QJQYD%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCyqEH2rMYys3MBLaeZ171cbKD0iRauTerK4twnOYVTdAIgWQCVi7UoA%2FWqctZDHDTGeUfhJIzllevotOMSFVwkjCwqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBs3IxWLo4BG%2FcaW2CrcA4RgDhmztAZi77oVsZpS7V4jRdsFcQxFMmznPqFHVww5sqCUgJlJmddLEvZ%2BQ8Mx5SBjsEGO8I%2FjYcMuVAt5jsCmc6JSW241HEyEmHgcG%2BXb%2BgkgMgM7fBqUJjfe%2B3FkqN2oOcNEVjC7Uebc0oKcs6B4J609Nh9AS8zB6jJptTqbHLCmgYfUBWDuNCbZSIXthOI9a1pXT37UpmaX2Hwe5Gro2cB3htbK6VqqRhxxF4rSO9wXTPFM8PW48TlB0Ae4BctWKgrIk0owSbJcLt9bonu3uAKlmknufeIhWrvXxrfHJc8xnYrM4Asw63tVnsk%2Fp0t2Rf0%2FgDOlKp1GIQRfsCWCnquJVrfJ3%2BTQzUa2HLLxWgzx6x4IQmlzQiOppZRyZI8n7bdnCJKG6oSRkLonNRSJ1GYYhaRKG%2FVRxMwGAqWt5Rk6WAu66ujmBv1W8pTj2p554O3HJe08jFRItll3PvEo5L5JGVS%2BoqL21J5t7Bk1UeTFkqAjI%2BrVTQnUdde43A19iCCH9HMn7yweXCchkbUn8Z5hB9yKWX%2BRYVufegRserbZ2%2BZ8wdNh09IePB2e4DRonSrW65nhVrZD9LaBc4%2BLuvpkiabWx4eg3juMJi%2BVrCTCreav5AjPtyb2MLe23MoGOqUBZeRsH%2BsETFsG6Wpw0ijTkEdgyAc8UuXb2cTvH0E2kmg4FLeHgNu32TDP1ryIfJzJlCuuv8VpuOZz%2Fk5iSPnxq7cG2Eucxesd9Dih8fb8oAjSRmuuxORdEmn%2BN3TffdElDDNQlozNw45iG%2BDjHMAsoM27CWTWEGBz2z4PBh9r5I588MMx6FM8m21yiz%2FFD8MIaiV0%2B%2FhoS%2F%2Fsw08tuCyGe7tkqCtF&X-Amz-Signature=52a7f497445865e72321a1889b4db4468ef504d41e0ce4982b9c1ab6e7a5d20b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTOQ6RG4%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIB2mSP4TDuZiPqT9u4Ctbhsd%2Fv6zjW6BQxsP4y3g%2FhctAiEAgD4lSlaOU6BOqhKPEHA%2BivNX6sm57nw6WiTuYkJXdfUqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGoqnuPA2Fw7PDZfYCrcAy0E%2BQbyub2mDhL7VrcPz9Q8zbNwTBGRFTRdqOJhSf%2B0d3A5eq4Oeh5unax7dsNIW5BCnwsyrQqszosvuG4lxjvBcHGhDU3LrtzR5KrRrDZcmo2usH2s2c6all7baj46K2nK9UfnuWN2FtF3sf%2FfMAKCwQ7tBLassyRMJZmoxYj7JZQB6Kw8IZGGe7bH1A%2FpsFgICRlomZQProe9NcCRTL1LJsL4GzgDCFv8%2F5FgKjZfskDCnCDUzVBOW86GapM1h8CCLDEI7KYRRWor%2Fbu5HqobWMkargJSyMf8VP1ukxK5oRwDxII5MzyaEG%2Fy6L7cUG7GgHUmRtOguF8C3SseGwM2yIiyuGNWfwfKoOo1ziKd5jWRkhwGKRTJNa2QeEqM5VfREP5x4DVMIC6ME8kTK%2BNuLfikCofQA0HfCJ2%2Ba%2BChuwBLvWr34cZbpqqiCl2AnZxEPWUbOiRG0gOud7D81tnf%2FS7Pt88lX7Jw8A%2Fvs8YU%2FXDGBmIH4oDwWYHfCYkWJ2kAb%2BreRs8OYb9VHx7g9HPlJLq8kb9PCUSaxVRKzuA0sdxskCFr10elReDqRTHp0Kq41n24cr37GVO0i3LRisqt3fi1j4hVh6GqMspH4lzMX6Yh4pDY0SW9HwmFMLfn4s0GOqUBggakqM8sF8DXK3vLDdH%2FgSn9QW1ithPd34ORJHJAdovV%2BDaKfyd7Kj8YVoEEmbGiN0jxMX2x1EFgWNantxatizlkgAihXzbThgvmwJKlG3SNVwQBVoJH6XP1B7CCpOUrEOVwAFli40Y%2BYCMuRiBc4oK37mTlVUcvXffjGM6a9crkzRYDmH7kppt9%2FJ%2FYFUg%2Bcz5bqsmcELJF4vTfgbGmAi1wOUY0&X-Amz-Signature=e3d1cdf6917eb6fa765f167de7c8e9cefea85e24ec615cd19a981dbcad2b0587&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




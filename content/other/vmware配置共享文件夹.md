---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DIYZIAO%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICFMiRo6H0YPNZib9K3Q6IuvIjkcnfyKKEB3M5qmWEChAiEA%2BBUtxn%2BL6vVq4tvFut8T%2F6VV%2FfFREGFGJQtvq2rpOrMq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDMM7hgIdu%2FYnBpK72ircA30VOOZ5ZMY7eY2jwCaqjNTFgs1%2BWA6p9qxDJ%2FILLg2z1eBDAn91hgHN27BgYknAKvVpZQrRlGC7TZJ7aa99G%2BTSpXH5xW8A7%2FTjuF5ioP3UP7TgvzTFNFUEkqeE5LqZM3%2BrNWy7tNnKaWqYBR%2FKnJD4Tsna7%2Bjrebn%2BkZYlCXGy59mwXlw8H06fIqkFE9ek2%2BkCVm8rAcsscCwKrIFdeDPoGkqqR7jI69ZiuvJGHWaIhyolRHsq20dAcKCeiO4pbHOjaV18ZjuvIQLyjqXJUTv7jRKDjNXDc7WsU6irGDDgnwupz1Eo%2FI0Ivy5prbqnBaOT00wS%2Bk2y4BnT7kjbhrpn%2Bex1gbSXyFukCcPqff1UsNZetIJjvhQPX53tuMh5YlwSp96E2TW4Bpr%2FyIaD%2BWNUy0ly%2Fa5jtsS42igAB6LeCKzSIRW6JsIO7iSjzw8%2FMM3MpAIbPFedXQKOAHOKfTzrsakachjTaBUSsWnGI7ahBmdS%2F5%2FygL9VZ7SbXey9N6HNLvc2B3kEmHh2Xze1uxXIz0xEurDHMcQlJIq4uwoQY8gaugcKJC%2FvFW4nAQeAd%2B5GC66ouS3MH0oLGidCkdaVVRgbfSk6ZllQIXy5gvOTYgN7M98sMp1zGgAhMLLkgs4GOqUB%2FIPDLLBEgyFPADG7qapN2V6pxPCVW3jxqbb4TPup%2Bf5WWWnn4WFZtzoZiJB4OvU4VqnBDX%2FJuN2%2FDJG3d2fKLknJug02opv3AN2EUGNJu5NTpGK1iE9LdXRGatWq9YmfRajdFFtYEA10L3Jft3dFaMYW8NUx6Txgy4LNak%2BwaRfbLY40jVyHV7%2B3VI8qsqLMTWTKT%2B%2FuCxi%2F1ziAOgWZL1Yr8aiY&X-Amz-Signature=54a62ee058d00e2baae6b3cc536ab9fb715e812c2ede72ba330b9709a0e6485e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666QQOBXJ%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCICgh8uWbGSAsEAHm9ZdDSTDNHV%2F96XMgdBs9waQyCht4AiEAuZ8W77TdCYPM%2BwS9ccOM7bxgFgFdxgtJuzhGzQ2oUN0qiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObZMo95aUQ0YlobqyrcA2LKdwKwT6fnx%2Fe11xGKVfBn2k7ltosiYJ43NIHkkNe6TG8r8p0SRavgDGMVJywjmRmx%2FWdmK23cQRNxvBwXlkqtF6iksOgrP5nprPPbfpWnBFWay%2Fb6LXDGNz2u1TKxf3RdLSdl1R8PFcpUSENf6BhgzLbjL5FDZ7od195ChvAR75JCjkmSuvEVfobBCCk9%2FF2Soj08gn6mzyPAh76FfV8X5kEpSQ2q9kgbcoxdrcMXTmG6khg4YptjHZMb3et7BdrHjOV5AJFJzbHrV0ft3%2F9vaXlCdAWzEsVNv%2BnbRAVe6GCKwl%2FG5zzL07kJMrUprAxADtccxFHBV2Rll5tRn%2Bh5oTxESKDQrENojc07MYlN5jyJlIHFj3Mkzegg3ShPF0wbtzdIr475Vu7b%2B83V0VzsPt8f9oYikAD6WzFpvsX%2B50S1FsVs0DvtG3pt3E7zKagUavXv4McqFE7ttg1tit2gMdiCj%2FRq8fNk7T1HiA%2FFz%2FScV5AiasF8FE4OqstrDbUTpRb7hEnzCnhFrkL6bVVAc%2F%2FJVJLpwS1rknue2ejLuFfZ8bgGcoK58JS0YxIk5u3qiz7%2Bz1sl3w%2B1ZFp%2FKiGaKuxFo9A%2F%2Fqi3aGsjrsXV%2FaNJ%2FvyNsiydc25eMIjdkM8GOqUBCGi2797tBsX2WyidXxGTKO3Ey1In3jx7z8PUlzm5VgFp5QmLITaNZefKWR1bRV4olKNBIXU5a4LlHhhxRhW3mL%2FN1arc4frA2QNB56Jn04glCXxzrjxPCzYnh3ERGZvyr7xiuaD6OWKgkZJICmMSmNaaUN1CXnEws0AZIbw8ioVpzludgfHC0nmUD%2F3AMNjzfaCBw1PsoNlY3fqdqvR0i9jsO7GN&X-Amz-Signature=797e3363e97a994b55f625f74adf120233265bb813222100e6c9ecec8c4a4d2a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




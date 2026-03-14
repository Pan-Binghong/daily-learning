---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6FV7DH6%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T033110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHdvAX1rMv65%2FRFM%2FaYBOtokQg4EMwEixJ%2FcI49pkQH3AiEAuZj06I3rmXoeSSMCmOpVvfJ8%2FD%2BAw0O4%2B7XGlrwdFzAqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHutDyoDdojd%2BN82KSrcAyZT0A3b3zGtZQUwOfTswsBGz5YXxtOJvh8yyO40kMaq%2F1rKcUexAkfbBYTOQXPo%2FoQXmFdcBFWPRJovDTmiG9UcnDx4F1Tw7EjwRTGHatV5KIJTYW6Cs7G3xBm8PZGyuraZSA6KheRphu8FGgVJ6c6o0x5JYAwTGmR2rf%2F9nqAi4%2Fjo4%2F9%2B0Ed4TK%2BpB3ny8Pqlxr87DiXU3NxAgK7meUhRBwUuOdYnifLlK0RWzVZ8UF7jcm7JmE70%2B5d%2BHqeEL8gt2g9nIQixJ%2B72JNRbFsFlhhWEoqe2FnI%2BANAIP5BlHM6xwv%2F16sAjNijmaegMYW%2BgIuDPtn4gJsnPXXt10P33KrXl5C6MWUej22pSMyIfDlM4nxaQfjq%2BaV5O2732acEpH5TdwqfRsQfXj%2BvpybTpZu3CJUZ309c7xzFoRaatEMk5Rp8lGVW3myj3RW%2BwiwMuzmNoVVkxpE1hyqspNAFE5vtJeQAGc%2BMGV3ZcU2ggHkhrz7cIbF58YAPV1hymorBmHLMI6xb1pTrlMSnvFBpMx%2FCSwiZlaSaUlL2axiFLftSdS%2FYt0BtrTTsF%2BBHbK9obl3%2Fu%2F2W5FC2hDuiaKsVcD8H2z15KecNylum0etD46dOE%2FT65JumKT%2BTzMP6C080GOqUBuBhvJujOpPjeeomkGHXL5mbDSuYtOravgEu%2B6NfWix6mhPsxtgtrP0ULc5WTyIJxXYo%2FShMGmDPzADsA5bWmC5QwfqYZn7DctyLlpOFpv18F6zqHpbaoUHO97pOJeVAzd%2Bl79CnGF%2Br%2FDTqtl9nVoQwQHNBxEcjs031HkSKNPSfz2Vu%2FEU1SQNnXfJJfh5fx97W%2BWzn%2BJFf5NNiKKhSh69pa6X%2Bo&X-Amz-Signature=f42efff5892ad2168a544751913ecfff7fb3464dfd7019f6c76f05c076ee3bbe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




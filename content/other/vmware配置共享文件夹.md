---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYS7I7CM%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJGMEQCIAUOoeuvaTvtzh4fV52cnwLF2Oo%2F1sKz0UPy5x83CvNmAiAnVCaLFwqr%2F8kEphhhqcR5D3qUMqOfpf0Ak1DHWzin8yqIBAjs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM58VdZQCUJfSYIrxwKtwDJVJAz5dzprG4FBN767H39Pevf1I8Pn3P9kk1Sw6dwufK6vTRDNy6q1RPV%2F1%2FLj3pRrwYlc03nNA0A7KAhC92n%2FLncdihGq%2Bbcf5k4sET50X6nVhGiF9Vre3X9IqeeEzjPs07boXAO0b2h3uvyvCCMlcNOlOk4qZci8nXX%2Bv%2FkdUzAAWjaCiwMXDTR8UD1uhBjT98Ee527drWAWKKGU3mLeXdKSbQrERNrd7YewV%2F3n16WfPms7tySktelO2b%2BvurRG5ycrU1tc8EvKFX98686z22peaKzbOB0FlrgUdgdHyyrmTfXnIY8EDkMgCA1I2Xke8qQ52Xbxxr1V%2FNBMnRCHhA0vTemVtOVIar9ulvJKB5Hy5RJ649yyrsMAlpddz0GCfyYAeUwdYvweJvMgot1mx6PQ5trs4ZqTd0ptPicwNZZw%2FX7dmM83KCFuH25nJladzz6HYhkUAQD6LbdSDgAQOUq2qt9gJP5c%2B2NEdgxe5kNNMHJ0c76F5DqIpQ01X1fxwAaeb75vwPIQT9P%2Ff7P47yUj9llRajJAk7r%2Ba0o8Sg5udCryWzCtiCEkzlgHF68z99fG4YYs%2BCmOX%2FktlaqGMw0eFceofhacTPBh%2B4eQsURbBswfmSt79UyCgwseWiygY6pgFGZJ5O7PUifyWX598130ykgZkzVcztY38PEscHElkgXpVsNzf5%2BRtBLgq4GUZV1Y8c9uRQay136UUExDpNV2euUTy2RGsnidYtbxt4oC8WmRfkFbcY%2F1N4l3g0PmOZf5ab2Y2MMWTaPZiccFOfy0XNKadSBKaOayyxuESkR%2B%2FAflWy6Mq7FhrDagFRNCwGxicH5L6nOrF37LrQ0uLvdCqSfpOrxYpu&X-Amz-Signature=66080c6ae9deedb1f4970156901fafd85b6c971ad4241378ca589b8937bad9c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




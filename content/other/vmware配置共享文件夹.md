---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDM3CIRN%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCqx01lamQ%2B%2F36VNhTXfmRsRvG3QVEr94GX6qYATq8MdgIgd2VL8m4oVGAfdrV8b36GCWdxQRER8LO58cK%2FdvFLVjEqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMV5or0JT%2BEjbkxRCircA5K5qO93zmldpjvRj9fn1xezJrOGc5QqwawzOibK%2FqbyW1KnVCalk8NL3jxOQl84GfgFBSJ5iUaeX2E8v8RTYfMhnHvP0Z0%2BSuwafad%2Fzdbp7qi6iky%2BvyWu7AxSFZwY2uqr8R79wFu5NwqlzM8opJutKTM%2FJnuKyYfn1g9IZnRLIeN7Jn1xs%2FjpHABgp0xvu3lfOdgt0tuOAxX5fAwIghGSrjslyLQT9BGcE9x2k82peWqHaB4wJkKBE55dFxAKuGtlpp9O9ef21agFgN9U%2FMHn9DGcWfUeFjPb4%2FMbIlf%2FQhddnCfGKzo2UZBjkvhA2xr4E6B71YcXVXae%2BuefwsH3qyrLQzvy7JDkUT5W793PNep9353C9dJADwdpNQRrAxku1vC%2F%2BqjVUunJ%2BF07oPlNsYwaBNklm3TFc4Pnn6XAwxDsOsN5a4sX3rRY2ukU106GwPE777l5IUx%2B51F8LXLQoGnp1yvicu8ahRjOBf1p12cpEW0txoAWX3uT23YKwt0sZD5r6uSW95KPSYHKYvtTI2eMn242KXaZdq9Y%2FMnhSCg%2F8A2nw7zXL8hv7zSTaMt87iAbz1MNxosme29RR%2B0H%2Bp619iaqMb5UkZmyfbLlPmMOVhxrfWB4TdoZMKuW%2BssGOqUBVSUYLm%2BMl25%2Bpp7PsvodItWzdtOhnsk7GRdSIX0MLM5aZCRyo2VbQykU6QLbTntn7EkIAvujNd7JjUxLDApkR5mN91f8UF6d%2B1a0mV7AOYD75RRak7TRbCwouWJoKSl%2BhvKFWgshqxV3XL1SYqrG1limi5HRU6%2BXv1mqtkPGgkzOP%2B%2BtBqhn2YtRGGSKP8%2FoFzH8GSbX0Wr7CeKGthg84OU4%2F5yr&X-Amz-Signature=8764bdb5eb81f78f25825055d0e477027c2e3635921745a9235ac0df5f9001c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




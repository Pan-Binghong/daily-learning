---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BPSZGCQ%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIG6CKZqvvI5Kei0ulbCvFZE8osIMiXSCcuHiafT8JKOTAiAfaxqqoaz%2FWKmasM0oeEQ%2BCVeVTeFYwbhHsSt5vivE7SqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1eBmZuKoFiS3%2FGpuKtwDuUUjy%2FQI6fyPfiHHQ83phoxXaVOzGKjtsecRunSzJ7ORwDoHZObDiGl7bVQz6zYRLJh0MEbv0hVRiCC0BMbdCxqVm6DLMo62tVVNmA2F9E1unibNsK2v%2FM85ocAcQsxZ3ZW7CvRba9XN3L7MZqQ4RsN0PVmaWTPp3FrLyspUGWcxGvpN0ICkw4NBxbq9dPCI4Gbd2tsszTdPj1JQU%2B2vb3FxAtHE95ZRGPOFNqIs%2B2cocleK%2BVcR8scryCPmHwBquXpCMASWtWE%2BOpmRMQqP2UJaJd9xK9ixF22WCh8w%2F5Da66%2BcYy6bpCYkjKaxwxc9ry8suhQM2NcxS%2FfOvoCHXhrJugrOkspcvOgPzw4A2opUsHdUEkrkjqju%2B0NgP2wjmgUQcyvt7AUAK58RTSwgj3Y%2FHGnaLi9jGrgAQIPD2gaNaPXRGc76WE4iFw4pbiMW77FDqm2WIuky0vgSCvb6r0KSWDk8mscZYbCABVRLEQRz3E9WjgvnNW1ODlHSVucBChiFRKGDD%2FGPHgXrn6nZlUMoNCrI%2FhEI%2FewOAnj1sNqBWc9p4hLjLg%2F8YwLRKV5hqlSf6bb%2B8X9yK7IHIYL0BGDK38AtBwYlEJI3NSNkdAbClCS2oNbRr48Y%2FL4w2%2FeQywY6pgGYrFX0M9PWKUXw99ley5TnfPSs738YETkVBV8K8K7kNH8oJG5ybDpA5l7GCFJASutzJvTvqgn4zE90NlB4P6Ql%2BQKMytkjAVr20RwI6vJpNRnRi2F13r61Jfxd7Ni0RqVkKcVBroZl795QK%2FrFcOejebrqpQVbdcMusZuh3xBal6cYhp7DzxFsGL4NGD8GRQck8nrQwfc3alYZ%2BvGaegWVs6%2BcTJPc&X-Amz-Signature=581942da178a4acd6d0421e7fa7e2bb31545708124670029b611d613ea8d6c68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




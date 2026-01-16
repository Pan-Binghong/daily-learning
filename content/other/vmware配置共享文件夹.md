---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OH3DUYP%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQCo9BUBIKUPvJpCFNMGYsHVPJjhXRS%2BifrcP2VTY67IVQIgPMNwKnoJ9CEtRZLfOtD3SdQJOm%2F1LWmYBWJlZQZ6Zjsq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDFbFpCnLhupAe4DROyrcA8rAd7UkyPnNf7EzZstbPnhIzwPQRgCMagFoYcRobcCuQK2tN9pMi%2FwbsA2N0s8sQU8PSQWw4I97MSqxTmcm9y0k2GYsloB9e5ITaCgLMM3y2CQuh%2BU4h4IW46KW1He7RBftdsihwegI%2FHdzrOtVUTjgc7ozrxYNGiiB%2BIaEdgT3FJE8w9J5fiIomGGPfhGG1pQzBYaeCGDMUlkr5mM8c1r3g3qPM1HP9cNUbwf2RbgZe1EUf5HqBnerwhkQ5ADOwNPq5cImBfajZC%2FB90Bt9yOrdA3%2FQWpMLxcrmchp1ZxtokcQdxJkTbTzupz7tUI9jr5VknRuzJ8ffF%2BYYh43JOHafzSQMF5KuVrlaQoheV33FHuDOsGXdRv1dDaB6oHWtDYA99%2Fj6h0gRf7CPaGhK5Gn0btBLrQTjxT4GLr2lBjsbxVBbwLT%2BvrBgHVpwKIBv1kECiWh9buu%2BqEJCRIisCpWP7GNshIodF9G9nnSlYy54UPDsBWG9rqAXPgNNca7TSxwKJGe1cSiYE7EY488sDIbyQYFDxNaWhNs6PpNDeQNlkP11z7yeHY0XnpzVMUh20fn29Q7e7LtzPBuW67xrbyAFkQvy5eDJkrj6vLC%2FW6%2FbzsPTH3ftuOqwqDFMIm%2FpssGOqUBHWmuXQ8AtDaFsavieEhll%2Fl6NFKHm38Yi0RXBPzD07aKl8%2FsDq9087g8m3K84C3HAaGwBA2IhN82gIFcC0Ip5p8o%2B4nFXrVIm8Du1MFd93AdzuOebI1tVJLIvs4jDSSmkeUjtTYjGhnk%2BdVpewUX%2FhLHQrP4dVyyQ9nj2oZzWQwmg0zTj5CI8FXcPKimKyPW9D7ErIXTb1sgRjm3ULSJQGN%2Bx6aj&X-Amz-Signature=7ec9cccb725c7401b99f345568f83bc4bc095fc3b745b77178d62f1b368a4796&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




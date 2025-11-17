---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTKPALI5%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFmeYBE%2FqO3ZacbNbdpX%2BJed%2FMGU4ouuk%2Fyw5NMs4FVKAiEAtrZPC4hR69GTDxIK%2FvzlMwxcML0l%2FLSh4T8w4aq7IUgqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL4sHsn9O%2BYGYcazgCrcAyMXTEuUBFcWVuUVfnp0%2FG1CCyDz20x76%2F4t%2BurAHnNreIMwCWIR3itdE5mcYz6G63xzdk2hqeX%2F4y0geGOYXSQlV3Q2NbwD4ABEGgfeb2ZDwv9MQgVZRPI7XF4jKBfhK%2FUMx%2F0nZ%2FSF7nPu73p5KJkieO1mPG45ceXjouOm%2FuT2om7Efkj9D5PTa5JittjBWiCP9FrxNJO9FqdPIklIVTBzfOQBjD2hX5%2FtTHFZNMbsRewd5f8JsOIY87fGw1pvbYlfBXnsFj6%2Bd6IXPxD6UXg8jXoMnkSjHKX%2FKJy5BuWuvkuVN90kohQ0nwpqzZjAdDq1HWXqPlTeyugQRvP%2FmbkvF8d9ZY8WpefF4eAvGlGy4IiQkjX62gg1Wqw%2FXmm4KMYn%2Fo9SgjPqujzy4orBLVwFHUUF%2BqBlXu9QC9uq4Q2WI7OEGcFKcNuWAc2gYi%2F0zbR4ujE7qAjEyLiitZzfsNE4B6C3LwzprBfXlf%2BDScMpVvStB010iSxz4GsilLG9qP7DcfWS4db4ZP7s3XrC%2BxVcf5%2BEIOMSCYxiGMw3B0i5J1oggAUbkvDAVvxmUOyDVGjYl6WmrcyBqRgDyH7cCO4Ll94o5Bs800%2FXWqMXvhDvs9OBiR%2F%2FGNtaQdaOMLeH6sgGOqUBTDh8J3TCel%2F%2FK7Mt%2FlOxuEp6925zrrcoQdSpp59igvmVNTq%2FmR8vALF7fgg%2BCQZi5Q4c1SQ2ujsDXLUYa1lC2uLWMFgQ7IksOmaVXj0jswvRJmCUkXc4eRdAJ1ytaySkDnrlcMQw%2BcQaASuIpocym6zL0IGNPyqt8m3QKxKae9f%2Ft7kBN0v6foejl4m9camsVF3lMMlzDqBdnReK9ZZ9azwSoB8E&X-Amz-Signature=b0d472e9502e354e1b3c5661fb282df5ddb889a77dfbc0fa4b6c98248f9862d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




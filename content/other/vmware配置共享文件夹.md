---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWCNTEGI%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHdgx8c2SZUcMNKLEIKjevcPb0AdW%2FfLPfKHMtpUrRvAIhAIw4H9Pvqw%2FzZnY6gBHZc0Osd2Jb2sK0By0XsN2cGQR4Kv8DCEsQABoMNjM3NDIzMTgzODA1Igzmz%2FiBY1Jld8aRImYq3AMO1z1F3kdUCQX7jSlxoIFOQbhzEFDY4GVGABlGciNrlS9lhjBCgvD9RAe0VQMHFgcweOdUSfsTXsAllfkOxoiZSfVmrYHBysYCc9titeT1823fZjwo%2BXYIyiYtNpzp0kyRl1nOTe1cOFvW8NsdDxYX0SniFSpun7lHn9NHzTD%2B6SXI6pEfEBlceqVhirGzI7WivurWv8W%2FXeJz4oPjBpV9QCwrTFy1T%2BvHFM51vg%2Bshfylk0awVpWxLNAorjMzLnr16TzVqAAgHX2x%2BkDLyvyzgn8Ug0IBhLFMaw0d2T7Awe7bxNnAMUqXGLc%2B3xrNDNITXQ2bBSO8SKNjU6T%2B3gNLmv35dzbPq4sItLrGG3HnUvdL%2FDhIhAAlq8xShV9MXj8m9ItPHgoO%2BJkVHlnoEN9XsHIMiNnJ%2B1UBnipDWrc7C5UbQzgOexQZzS5gugml%2FPjNu9iVsFpMX3lfp0%2B52tCzGKO8DINl0%2FhtyFa9RZsb9Mky%2B3E%2BXC0D1FuuUDiGznzIjKl9tHYI9K6zDocDYKRsohjrW1fYQ6tnBuNYq8yIsHkksmxnX5RbXsk%2B%2FaEwQL%2BX7pvYwov6SK%2BLMdztMgZVuL5IfaWfy3%2FW4EiwVLdV5XJUaEfNaRnyTgJ2%2FDCrlonNBjqkAfmGUs1zPPmvHwaAHQj7h681ZsElpLEaCyMkfztcViDjAFmwctRx2rkUCw0YnG6bXlA4xlFxp7hoLFzZg%2Fct%2FQqIo5T8t6iMebF8%2BCaf3DOsARORxX9a%2BHERE0I7DEFdq2iAB0tjPnULVpBeKlN5JyQ7C6e7Gesgh0NadJ0MWXWJmOZhiIlPRRKikR0iEN2pw0m7DZGytzfrBieI5PV%2FJovIuUmO&X-Amz-Signature=9f0815820cc72ffd962447af1f802b57407cc757d42c9fc7970e2205ae854877&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




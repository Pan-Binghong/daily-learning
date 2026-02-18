---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RLTJFZJ%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFhiH2L8sSM8lknugipIZiEejMgDb2QzN8bPoOU26n5yAiBy0Jfe87%2Fy2SNsS8QE0ysTp6QfKrt2nZzgWlHss5lOmyr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMQcX%2B4Aou0vI3%2BWFsKtwDhAZ8R%2B27Ty8v7RZdrGjnBTCU8GkUjC3KCIdhua4i%2BCzDQjkxW5j0NeH5urOADjMC%2B06ypwtHIALLCn1gi%2B%2FAE2eJto9Y6GaC3o46R%2FsEtSo0RKdR5iTaalD2QOIjNPePPUmVNCft2Gu%2F6DnJIy2tehULITt7MK0qrB8vazrIiUckwedDv%2Fj6Y%2BCh83gMMSdpq1GET28Gh6wBtIjLCw40Fw4IBCOg3GHYolV67yhaJPYAZmOJKatuRLyBYvszijgmojscW2eVPjKEnzQGsFzI7lsToV%2BevYI%2BL9KKdTLZpfDGNWQUrzJ9WWLNeOxT7mcnZ9MIwQ9hyXUOa90%2FIVbc7UXZ0eFpY5ioyEAbptT3PkkFMtsxaaFS8uAE7vD95UwAoteUbXV4R7XfYPFMTKW7Gcqpr0EhlaP0WCX7YrgwHmKWuIJpkrtAfPuELvEFW4s1a%2FVkw19uhGiMKub5MYrB8TFXl71OC8iYy9p404rlxP3BhOvAuNF3qh9UsAWq2Pl9nUL5E5tcHQD3%2BIGmLwU%2BVddo%2FPH%2FWfSUWlq5gthYlOVKfeAYIU0ETg1CKUOBUMZ62SdJyaJHzhKYsJJLquKS1Nm1xHNY9Ggm9N8xODHOUjlHBBtpBo0CXdYO%2BgYw0Z%2FUzAY6pgFVTPYyHtG%2F0n2rfxaY9mp3O211extknk%2FhEhc%2BuI3Dq9ybdtt7w1dVfGjbG%2B96o3KAeI98U6RbWB86AJX8BKeqGhKMBd7OnA1S09osQOvXpSlaigZtCXE9cvhJhLfq93MCnbGinFgrBtDKScr8Fx6u9fhtYghnWYE%2F%2FlNnSpfu1a8OteVqQJQRnKywGnqsSsqndGadrnQ3Lk2vo%2BlN0LcmmwQm0XoT&X-Amz-Signature=95dbf47254145af6b65a9f3eec56d112267c826aa96259775fbc2f3d43fd0c7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




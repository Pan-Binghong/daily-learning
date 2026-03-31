---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3AWI6E6%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQC6AsMgsce1c4YzImcAV9irUz6AiePVrnGH7hggkrW%2BOwIhAIHAHsPkPStI4Uh1yqkI4TJGO88bU4qbijBG7UKuihvSKv8DCDQQABoMNjM3NDIzMTgzODA1IgwAyv1W%2Bw0whcYhAn8q3APldAbOmFmrvTGpEvwdXZ6y8bYEHI%2FV6RzRpxp6UhlhD0KuEq9fmASnRmTvwFY55bnDWI8%2Bt1%2Bn8r7uvd%2B2m3QMAT%2BwkutpPRDM9ggFxh75ShAEAfOVFjy1yILpWFadCXz26gzXsBEoiCiU2o%2BBtZTnjlJUg%2BSk7rJYjYQE8X4EAzGTmjqk%2FGWOu6t1ldbA%2F5s7tWwr0uQvqrOmh9gXalP%2FvibTmHS0N5%2FXqNVkZpbh4%2Fwj3lYm%2F2vIetm95vTtdtLOI9JAKwK5GTG90V%2BpC84TCvN9fN6x3%2FoJ9BwkUsf12tbiI068AJvmFt6U4aSyLpZVV6ohsdJ2vpe4eRGhZWOAZx46QM6zHKUKTxOXiAiIWyicTXNsbi%2B11KAVO%2BeTfZntNpFacyYNW14bIYljnGYsP1JtHWJy%2BqWKMQ9ncMN8mmzrMf8IzPoMfYwt5Zyp7INzeD8M9n9hH9Nj56EE%2F5EGcsN%2FNbksiYbH71IBfkeP2XH9kXv8oru2urw6kisiBl3ZnmsXfh%2BENaLSE8VwUSPgfFX4IgVPLeiiAYn8g1QBfEfxMI3i4%2BSy9XeGRR7VUDIqS05czzfebjIOnbOlygrAaC%2FwuO066QHG7L9SLpMKVL9D%2BL1DegKIhlm%2FIzDn8KzOBjqkAbPiuBz9JBKy1BEGqD%2BGkR9I8LfBbysg4BurinnYgzYNqfn2ihc0ZBpOPxeM%2FsrHHNc8KGGSP7tLAUGQXWylMiUkDl6iKmSEs%2BueuYvmrD%2B4VUY8uWSBoRx%2F9%2BeeMDgf1YEaEv7Ea0hsl8TyqvZR6ymtbGgw2aEUQLj55v7OkcZbmchmgpHZldcTDPresPABEumKeN%2BRWH2FVIOyKgj7srpPsmXQ&X-Amz-Signature=64b86bc6bb85b004d22d595933cf872a4c7177f25cd82c5659c973a351ea015f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




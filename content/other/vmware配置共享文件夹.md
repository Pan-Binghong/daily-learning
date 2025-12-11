---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQWA5A5B%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCBeVhmIR82QWGINziQYnuLCknheyu1OEMyilwwhMmEvwIgAL48mEIN%2F0JfvIsgDiA%2FMJ8M67sMnLHjiNRuEdWiHtIqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP1ltWg%2B0QXUTpaZryrcA5cuz%2FG%2BRUeQCGA8D4MQC8UqylSKbLCfiI5v9T8QeiZDLuV%2FE1UKl8SxMA3fOjOcjh7LsVjQEUDxgR27bwIPtBi%2FqZz1Zbcn%2FvKyKjGB%2BSPFo7YVoZV5ogrpvtrcG7HJFARExch3k6LBFb6eRV1QP9SN3ErvnsGAi5t8sxcNLvk8mRwuzaK5TBfFcckzosxzU63q1S%2FQzKVM3QYkOiLobCHYAGPOi%2FxCRRRvXD6x3z3aJv5Dwalse9KVUmS14bJvs02ZyRXlQeoMVOjK%2FGHP7rNPh0Oh%2FpxWZWYl3l8WvuzIvPro3qhYAIcjUh5SAC%2Bcmh9oEm19%2Bt%2BDGW7UUekWkAtzsqiyF6wy8MeSbtrKHze%2F%2FjxHTPJstFEK6Kw0GpGdQPplmiKxLe%2FUTkaDOvn2CJjHUHois3h38PDTNpOwLxVv9tHdfq5aeKFLS3PG6iJ1FoKQRHiD0n%2FlTcym7is5jiWd%2BmXfullEI9k2darMonwZzXkWwCb3CQtK6lC7evUo%2FV%2BVFyGBlPXCGWZchR%2BpDpmOkyOybJEIIqLQSyRKRYEBp4pIXMjDC57vYNVYGG505AA0PpLfCaLwFkjXmsChhmJEFiljcDq2o85KhNMP%2FflFDveeaKJjOLFG1vB2MP%2B06MkGOqUB%2ByVQFBhZXeSz3Zq2Wu5wK3na442iEYZZrPpyAxqcjohO2zgfM9VeMMC7ohv1JMvyHoRGbrVwCAAgDRYgCPakoxv3oGNvurWqMSWgQtJH1pgQrhfs4YnrImP57va83UaC6e5wRjOUsYQjuO5WtgxkgiPwGewSRY9jHjUn7zt2ZUt1I2pH2zw1cSETajWu9ByMBuqmLbhEzXPSbrf2705dcULdHh4r&X-Amz-Signature=cbc86b307b989a03ea6da575ab612ffcaf66a3b441935990e086529bf964e34e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




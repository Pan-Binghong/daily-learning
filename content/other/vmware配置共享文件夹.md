---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG4IX6MW%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGNF9ttWYQnIiOMuEv%2Fvyp3rOxt%2BJIKg7lQla6A6I9MZAiBAUluDhQbkV%2FducqSxrhGp%2B%2BxlMwgyN4l14dJRVJepmiqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTuM7mXy6P6dAK6FhKtwDIQCNCWMYdwcEngwPPYtUt68S66pg7%2BDA03t8ViuaNdk7L%2BREViEGNTReYGfDVSW5YtDnO2aS%2FcqCNzPYzZBPgUXANh8xClnhW5QN4AkdnbK4ndKqgGl8OCs%2BL63SaswsV7zgKP%2FAL6%2BHI%2Fi7CPyqx%2FqJaiPD8lZR2ti7v23rITWJEyZLom1qlRqSN71npkKeVUwQQGS6zdzm0zFsQZYfXTTHXWKYbbyCV8qWcfYRap5OFsdB5UGqjL2xB76jYMixxZZ7zn32pdqVaK3cgzk%2FCiMIglzBgnUinvCtQYEorMoYq1TROcPCEHYAnDopBfEc6eqSqcU56Xm9vszlAo%2F9P0npeMcxwkfJ2YRIBBivcnJwTLR2Hb0FiC4PBosV%2BIy%2FTgTSkw5Yy4jPvmmtPrRujWfV%2Fi9b817xyiVKOrmfOozZ%2Bg2bbTt6oD%2BBLblkYjVKfwCi5xzF4dyNN5hejB8mFvNn2xLLrBdTvZmU2Kmi4sp4hFroXZDJD8jjh6AtCx9mrinKJfFolJUhZ9YRpk4ZCsVSP7AHM%2BeffbLfGmJAG3UcZ7nfVxWtfXgsPPoQ6SmPxZo%2FWXx6h%2Btms7RTJxYzmt5T%2F7%2BQGiUIRI0mmdtTHaabPxVoVW%2FgcEfa134w%2BsmSzgY6pgHXA%2FMqwbKEl7LxW1ZJLEI7jCqPo%2BkVE5lSFOX0b5ca8iAiEX9Z7qodLfaJ%2Bi87YZqEEB8%2BQtY5su2oSngXzQ%2FuvYEwrOFIvC0iMa95yeAqWo66C1omM1SElHhXVh3%2FWJdBtjeZQoHvLDWNWP40OP7D1JPLFhoeaqMw3SYkhq1iy2k4pGndQf5t%2F6OJGoD%2FBw5Y%2BV8KcbT1Cma0uOlydo%2FbE3onxT2z&X-Amz-Signature=9b6fc548b5e8f03f5e0c0d36b3f735e8fa2913cf5b9d9c12364c540e1dcc7476&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




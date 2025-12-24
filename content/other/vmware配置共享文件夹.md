---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZADBX42D%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQCQ9xMPh1SFzMR741QG2KnWPQ1bwfXiyfGW5jEEByPh2AIgXLGMERltdokwyBaA4JYoRXeYBcBd5kxRLgTrmL%2FQ270q%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDLMXVyj4cDtG2%2FzZMCrcAws%2Bv404ikaMlyD9QrTrT38tLKGIeG3XGSA1yHfeISQLqkV1vze%2FJa1JSi7J5J2QO%2BgtEQCidgjOnWhnXUkMzlTb%2Fp1Uc0uNvtGx84E9rthXP6BVT6J5CM7fm5GEj2oXvYUaRCSIkZp6o6NRRoAEnGrC15rToPNLssb4GWJQt%2BWUtxMZ0wur1eeYnSkkc499Y30S9uwuTlSoaB3HGCh0rkaJaggNFlsCU5oc9HAlfL2HITZASW7fntQvu1ia9aFElIV9cEHnTSwcgYl7QEik%2FyMgLsmpSnMWwYUDrtmoN%2BLf1iYYzlJnvN7CF2Pgr0JKXjqYgF1eVKlxOUBC1Hr3PR3ziOqJE0I4Lyao%2FQ7poZqkBr2LvZ2%2FLaDHWHb1egh3n3Hata7BkGjuuWg%2F4ZR3%2FtsOOsMEusTg0eEHE7N7W6x590Ml1DU262JbBIWP7op7btarx6BfYnS9%2BS6SlUwI7NKfjiE0O5ArZEl6vljM34glQq0jKpLo7NvvApNhcWf4ElnnCsYWiCilMARJOoDCyMzbDboRnz98XOkY6Vsrp%2Bu93SnoEeEIxARQxk7IZ6yHY1DVFsQ1isG%2FKe%2FdyuNuh8pdJ5REVhbW0vOhJSmTTm9m980AkLRUqznzmtUoMNvgrMoGOqUBm0H%2F029D6LlQ9BN5VdqTvvXUmJujFWTVkmsOxyqgJRGrArpgxUexOFNNTeyOqOm4FUfWtAiVN76blVAlJKmB%2FC1r9hk6BN0uQigFhB224SgBg%2FuV3Z5FJtlFIKOqzI3uA6axLnm8GVVADE%2BatMIPoWQ4zv0TNuVMmqR3KZoGzHWpNI5CmlCNyRL3ukxKXHztykVjQh3kVZCovpT9Lek2IUhiVnet&X-Amz-Signature=2b179ea19451f6e58e0212754080eb3a9bc76fcb5689a521ecd99adda1026b91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7LESVVT%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FfAkzZJHmOsNLU56Fa0IZ5jKRmeu6tGqcuSrlY%2Bg2UgIgN2u%2BWSbTk1cGDYQY7La1TJ55P1nVbFfWxIEz4Hap0rQqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDrKSy4ya9AfdJ6KiCrcA%2FvFZj%2BYFCa%2FWmz69v1zJh%2FslH4vmWQ2xen3t2mraqM%2Fz25S9KzOmo83G8%2FqYoLVJpdNY%2FOEW3k1ky6xSdSNSHiQHtgTWUXNapIXUeU%2ByI3fyI6q%2BYBPOFFeXS1Q9HziaCeqbpfUCnLAyFnzc38Ugt5SgXg7%2FvDSaNlXCmKKNVieV0%2B6FbWZ0unFONdVWTzF9CGmQxzUpfv0oh1eLEAe0a9KkeUZ%2BkTyYROGZFWxL55AQwWOlQqc5wx2%2FUzLdBwB0qVm2KT%2B1iWile7Tk5H6QgMeQUGhVowTsxsv%2BJknrtQa1xuQ5nUOA%2B9Hxc3xjc07xGX4olzdO7KYFchKiacreuF8%2B%2BddxmVQ2jPctMuHI%2F%2F%2FeWV3q0kjDro4in8YSRmumBLC4nQUUq8yKgzpMQ6XceKbKUG3U0oeZQAAPCpqEZqFyxus40ZJza2KvwTSGrh9kpOxt9QeT06reMSYY1wEXZHEhakfnLvXIwiIA1uLAZGd0qAXzaeU%2FNqg7KvV2yo48jOdl%2FBgfdmFrOHz220rmLrPqdkVcu4DfeNppijuOGm7T56uj8UujyAkh9iGKm04Ehk82NjGQ%2FSEW7mSp3Xhl%2FX9U8q3Kmd%2FdX%2FP7qqXm2jncM3KSfn3nOwJWYJaMOviksoGOqUBQZ7JzeBiE1XxolKFa7R%2F94kTxkvuNzcUrDo1FHpsc6PXiCotH%2BXUh0cYY2pzHaH4mskEkuDS5PhXup8wky1UcPTRGSUsr8lkFCLV8nh924olV2nZ%2BEu%2BYYtaAOCXGNbbCcMMEHpW7GrNS6JUO94Mzrratne8H6%2FjkbDWjU%2B7h4LkNt%2FoCHbAuXVUCzvSrOt7yn9HD20mg9So9P8DyPXEseiFSmMG&X-Amz-Signature=d980cade488b81e689bed96a38d27a1b96e9f0bb3c784b1cb6a3ce87d302c904&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WWI6III%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB0RTehpa70psv8zVghKJudIFUq4%2BrtmjyU%2B%2F%2Bwhi3pMAiEA9StkqJvq%2Besd2dAY7WZm64VutPqTACloFVDrSA4WKAoqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNGVdpyCjdGNL9FxECrcA6v6Zxs1O0W7M%2BbUsqkrjFI07wD%2B%2ByuSaLcUNfM%2F6KzDcWkrFpPFM30Rgyb3cLpioG9E0C%2FMKOHkavEu6ks7CPtEldTbgAKNTbh03T1Ju%2FxeLYc6yU81gQjOPTptZfb7Jc7tGVhy7viftLfvkeG3buHMwVBt5Hg%2BPNga25YVy6X70WMtVls37%2FFpSns7rBNZ92RQ7XNVL4yN7QREt9ZJhrw8fmobDEjNw6aLJNuTRcbUCQiuzrF%2FojjBe8T3yN0YqGYNp00DSp3HP2awjIBeC1O%2BcUC6rtHlFjPZUgJSTbMKEcxZlqYVwj1KweF%2FbC8h0WBWkQm%2BY1HXiHgQR3uEyRiy3HJaBvfP0S7hBIyqsd0hl2URW1FD1m%2Fytzy0%2FzG2yVN%2B3lRfbO71oAhxqehrEanNeLgo60nD3LKFNn%2FU6bHGA7pVKIN8CUXY1GVQB%2FCyHNBkSNx8TaDQDSOBJM3jl7CJshC4j1B%2Bv5QMTZfsH1ka7XNk1Nnny82v0y7%2Bpvgh%2B%2BCbr6lqFa2vsz1XPgMpMM9E0L9wLwYAT%2BWada%2FSpWQGMRQedP2EPLn7REx7kIEbZQY6vDQlSHEEM2NOTVC8H%2B48TJ3djQGXriDLWV0XAzuqyW9jvHIVAzIM1mkIMMmFmMoGOqUB5sh2FQ7FfoPianDe41P5p%2FaS5%2BaBLIHzOhcUGUO%2BgIpVAB9KwN3317iyEouBhEEUuKFsLIMGQHczgEA%2FRhpLj3lmFcedY8AH%2B%2BC1NDDJkoszbOsS02RCtLgZ7awhEGfR9EraTCE0UTW6Kql5nDkwJw4YpV8vKbgdGMnUpOxy2TnARKhPYONb2icuFE3Qof9iPxXaPiSbRzq40fWUYSQNjz34uVFd&X-Amz-Signature=8cc05ad952151aab07306cdf1a8165d70e1d6702d2fdb27b049740e68f5564ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




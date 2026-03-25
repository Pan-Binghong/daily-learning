---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRIO4XKO%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFCUR9ICfzPaEG6POsqSEYWMFwhud9cYlI83xf%2BHiNYcAiBvSaHdi7h%2Bz3ROBoJHmMrVzTxOeatQoyygniBL2ILCiSqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxONrmYXlw3isvufoKtwD%2FfyFH1qW%2F76KGW%2BMuD7UNrSPHUqN7rXgzRpK0JqxzRUOGNjDapn1h%2F%2BrqZRFc4y1R5ThhYwxpIIT8CVtrCQsgXv%2FmZx3sieziAGLcI799ow99OJAUzcpjr5JU8Et3oCBwSQA%2BUpBKnlRbrhzZqKWfdrFqpKAgRv4iS6AVxfkEm6uf34GtB0i9ykecgf33Z9IzYzQuob78Uh3ruIl5dub473XBIxxmPTWFIrrKu513rc05oJ6f6xsky2Pfy6axQzrsJDi%2BRYjyoSrkL3RvGumOKgReJn1%2Bap7s1BG1s0NBZPHfxfmALCH4M9ijz8D4eNevvwTX0OrJ5j6d1u0qDum3oZPQp9CAqFEJ%2F3KYNy3vcG0D1tBZR1pJDAZKVSaRhmKivvn6mIT8ZVhRx7u%2BQXoPuAO%2FOHttuRmFSGg5vRMDpf17WyBgvNdW%2BA8LXvftqs5srg7M2WXIF%2FK4lakDaaC9lD5fBU%2Bfb7aI7PhW%2FRHK3qb5HawvuCmLtZa3NUPpyOOKIEy%2FECFphemvL2ADZXpWwP35wmwMGlRHhXqn9stVODl303iOZTZPiYM62mB2069hA0Vg2CoaTO9pccsDVsa1eeUH4ryrnlFh7nesYjA%2BEt4JHXqEeop1U8VvgIw3qSNzgY6pgGoEB%2BbIEk%2Ft8nbNc182IVmQLnnrOEedHilbBCMcWM8F0%2B%2BinFXXg%2FspdEjU%2FwpYZefBdNRMvxEnGl6PmwpeCfWF7VIjUDfimtUqOFIbFmFMbAmG8%2FZ5taw96T84%2FkhRUbch%2FBMoB4GFFvTJpJcgJg4ooCrJA4OAQY%2Fc%2FLllDBvnNcguw4f%2FJISPOjgQzthI2%2FTmT183uUv8LBJg%2F7r1K0KOMAS6yz9&X-Amz-Signature=7894d6b57c8ebeed845063d58732f4e31462f613cb4740a4a63899e03d08b984&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




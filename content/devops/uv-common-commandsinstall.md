---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBKTFCDE%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIGRRwKRLy6I8UjQQ%2BbXVB7ZPT1NGpi2vHyTPB4PX0IzNAiBn71wC%2BZ2CPS%2FMhflWsbs3WFUq7Vj2OGq3j%2FBHWQ9iSyr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMsfDX1zJByiy%2BetZYKtwDNYr6gQU0PhX7jLYK5%2BrBdQ3OdTRmOKzFQSpvjBa2pIOvsnP6KdNnQjW73UNfXqfez9pQCR6IxnC6R2Ioe5yAS7%2BFMYLYzedXVWXaCNUbci67nk0V1jt7A43fV5zlqMSD%2F9hCwX29w5SIiQ1nm1k3vqJexYkhWkhbX4Ga3TYSkjNqvmBzkuq3RzaSStjIt9ho4tnZifM7iLMineBWPHH6BDMc7sR1YuBSEkn3tNGtHLhys7qqgZejunLL0%2FPRZLQ7yaJwFhGxK9GFDzZrSKpMZa%2BhmRa7HZDSKJCxu2C1jt9aK%2Bewhy6zNn71lU4SXvTNYV0pGGTpoV%2FsvBIypD0c7WIA%2F19ibBSgI7oh9fIRChOsboPHVfWWZMqq2ZELsoLx4KtFgalLqMfg46K6dY3kU5nPXqE1%2B%2B3V%2F0t81J26wSX4s0y13s0v%2FsD2emoawDhb00hciUV2uAaq4P80DgVhRBWtjTPKzD1ti6thY%2BJxbfsjICeGckmXOHunQ2kfNHOevpq%2FEy76qDRCmWLphMRtKDNWpNFtEbJFHIJw2tu63M%2Fb69ktTcJYA2T5HyGcYhic8nRZA7gWBLDZ4kYWc5T4HXZYUZpwuYfe%2BsAOcJOH7HCghovw74CVgulVVVAwm5TKzAY6pgFxUM7LnGdesq8TQRDrtLygrquKbUNZNV3JTpaptY6n7xqj6N4gRRAru5mSNjPUc08UMmuxchj7B5ywWmvSgH8%2FLIg%2Bb%2F0hEHuYAvrFvi0w70W%2BnDsu9TTYryYJ%2Fsk3U5Kbvs52sqZ2Qv%2BTSn2SV032Be1UbWj%2F9vxGAu%2FazUnEwW7tAPRxEpNCxh4qXFuNU%2BBTRJNAYegAuTd0%2FRtsQZ3DoCxS%2FHNn&X-Amz-Signature=666d2429381b87214abaf917d8a6f2af8800d69faa51474bb03f2ab5d15c06b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBKTFCDE%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIGRRwKRLy6I8UjQQ%2BbXVB7ZPT1NGpi2vHyTPB4PX0IzNAiBn71wC%2BZ2CPS%2FMhflWsbs3WFUq7Vj2OGq3j%2FBHWQ9iSyr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMsfDX1zJByiy%2BetZYKtwDNYr6gQU0PhX7jLYK5%2BrBdQ3OdTRmOKzFQSpvjBa2pIOvsnP6KdNnQjW73UNfXqfez9pQCR6IxnC6R2Ioe5yAS7%2BFMYLYzedXVWXaCNUbci67nk0V1jt7A43fV5zlqMSD%2F9hCwX29w5SIiQ1nm1k3vqJexYkhWkhbX4Ga3TYSkjNqvmBzkuq3RzaSStjIt9ho4tnZifM7iLMineBWPHH6BDMc7sR1YuBSEkn3tNGtHLhys7qqgZejunLL0%2FPRZLQ7yaJwFhGxK9GFDzZrSKpMZa%2BhmRa7HZDSKJCxu2C1jt9aK%2Bewhy6zNn71lU4SXvTNYV0pGGTpoV%2FsvBIypD0c7WIA%2F19ibBSgI7oh9fIRChOsboPHVfWWZMqq2ZELsoLx4KtFgalLqMfg46K6dY3kU5nPXqE1%2B%2B3V%2F0t81J26wSX4s0y13s0v%2FsD2emoawDhb00hciUV2uAaq4P80DgVhRBWtjTPKzD1ti6thY%2BJxbfsjICeGckmXOHunQ2kfNHOevpq%2FEy76qDRCmWLphMRtKDNWpNFtEbJFHIJw2tu63M%2Fb69ktTcJYA2T5HyGcYhic8nRZA7gWBLDZ4kYWc5T4HXZYUZpwuYfe%2BsAOcJOH7HCghovw74CVgulVVVAwm5TKzAY6pgFxUM7LnGdesq8TQRDrtLygrquKbUNZNV3JTpaptY6n7xqj6N4gRRAru5mSNjPUc08UMmuxchj7B5ywWmvSgH8%2FLIg%2Bb%2F0hEHuYAvrFvi0w70W%2BnDsu9TTYryYJ%2Fsk3U5Kbvs52sqZ2Qv%2BTSn2SV032Be1UbWj%2F9vxGAu%2FazUnEwW7tAPRxEpNCxh4qXFuNU%2BBTRJNAYegAuTd0%2FRtsQZ3DoCxS%2FHNn&X-Amz-Signature=483d806e723ddffac5bc966be4119c8fff31848456524ce4f3df26562f5436bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBKTFCDE%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIGRRwKRLy6I8UjQQ%2BbXVB7ZPT1NGpi2vHyTPB4PX0IzNAiBn71wC%2BZ2CPS%2FMhflWsbs3WFUq7Vj2OGq3j%2FBHWQ9iSyr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMsfDX1zJByiy%2BetZYKtwDNYr6gQU0PhX7jLYK5%2BrBdQ3OdTRmOKzFQSpvjBa2pIOvsnP6KdNnQjW73UNfXqfez9pQCR6IxnC6R2Ioe5yAS7%2BFMYLYzedXVWXaCNUbci67nk0V1jt7A43fV5zlqMSD%2F9hCwX29w5SIiQ1nm1k3vqJexYkhWkhbX4Ga3TYSkjNqvmBzkuq3RzaSStjIt9ho4tnZifM7iLMineBWPHH6BDMc7sR1YuBSEkn3tNGtHLhys7qqgZejunLL0%2FPRZLQ7yaJwFhGxK9GFDzZrSKpMZa%2BhmRa7HZDSKJCxu2C1jt9aK%2Bewhy6zNn71lU4SXvTNYV0pGGTpoV%2FsvBIypD0c7WIA%2F19ibBSgI7oh9fIRChOsboPHVfWWZMqq2ZELsoLx4KtFgalLqMfg46K6dY3kU5nPXqE1%2B%2B3V%2F0t81J26wSX4s0y13s0v%2FsD2emoawDhb00hciUV2uAaq4P80DgVhRBWtjTPKzD1ti6thY%2BJxbfsjICeGckmXOHunQ2kfNHOevpq%2FEy76qDRCmWLphMRtKDNWpNFtEbJFHIJw2tu63M%2Fb69ktTcJYA2T5HyGcYhic8nRZA7gWBLDZ4kYWc5T4HXZYUZpwuYfe%2BsAOcJOH7HCghovw74CVgulVVVAwm5TKzAY6pgFxUM7LnGdesq8TQRDrtLygrquKbUNZNV3JTpaptY6n7xqj6N4gRRAru5mSNjPUc08UMmuxchj7B5ywWmvSgH8%2FLIg%2Bb%2F0hEHuYAvrFvi0w70W%2BnDsu9TTYryYJ%2Fsk3U5Kbvs52sqZ2Qv%2BTSn2SV032Be1UbWj%2F9vxGAu%2FazUnEwW7tAPRxEpNCxh4qXFuNU%2BBTRJNAYegAuTd0%2FRtsQZ3DoCxS%2FHNn&X-Amz-Signature=d841ada2de53dae27737e83ea8030cb06f8af9e37ca5ed514ea375365bceebdb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References


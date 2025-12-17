---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WWXCW5V%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGdWC1kReLuouY2NdS5%2Bvknk9vGyq9Dvhs9DFdZDA2nAIhAO7VrwSwVezoD%2FbvRlsl%2BHriQf6B7z40i0mKlCTqbgcAKv8DCHQQABoMNjM3NDIzMTgzODA1IgxSGR%2B6fltH1qL8x3Mq3AO%2F%2FzNbW3LWVfBuh6vnBGu1gkDrE%2BtTNJFK8IbMc3BwlTQXUfRw%2F3eqiH1xVhCOzkQkraIzFuwFtKilyxvmjWr2cMCEykhtmyxXge5PFU2%2BydjAQ3ubjL6uNvlPLmFECDIfI9IlJsRLUNKCyhV5tCcAOFWPwaKMKsQXvflfB8Fgpi4qT9E%2FIVANIFb5FmKy5oxdyD%2F%2FwQDjL5%2BEbdKuwLpXPKjRCtm0sxSyRi7zbKbPmOulNoLASPtkaa0KNFchCTAupXNirlA8hwrULaCN73qOvfDCWKWKiLdDzb7lDZ1hTEnehT%2FsosbrqefUhkVG71W25xpn3tIMUbVCgWYueROSBIE0AuBXFp7pzstFyn06s42h%2BSaHgK8UtunDgqJuWSeG8YrE5kNXQBJEPNGHh5BZx9ylv7F3EN0Gu%2FCatdZ0fXTSIy8f%2FowghVpo9AbERIVO0suzHzvgqaD990NGp5svTX9AycFmWMAy1dbOdwAb3InQ9W6snXMBRt5cR5%2FJdtT8PFnwnxp26awjxLbqpaxhEC2H5vcVB8vxYHFVPP6dCgnfMbUhgQ9UepCn8%2Burid4zbVjp4RWIlt1qZCQcEv4uylK1SvzXR92zHTYVSCTvoNLvgiBPDgjpacEoNzDOsojKBjqkAYy0gcWbbIfE4FOiULIK7yvGXXWAVeMwKpkir3VWi7iOHoDSnXFCJKAF8EUf3RNYulDc2PFHLAT9LGinLMN3NVFouIN4wVkBFBaXd%2BAaxv9qv3w87nbWbis8mdFtfk3LfbyxRSMirCM0v5NntEkk0JVB2bI0sYb3RaFP4lN8ik3xysp8%2BNhTcZ9i8YcnOF1lN7GC5wx66MtAeiffU2KvkEIiNmon&X-Amz-Signature=7c1372cd892466735053e4259526be1e2bac219b5b522c72b4dd519c66b93e70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




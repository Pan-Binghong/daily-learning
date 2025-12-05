---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD4QUJBN%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG1GLRUUU%2BcNU%2FHl4jFpWn3Mt22S5iy13HE9psxhFZU%2FAiBW02rnIx2EYkV00f3pDmCEdEzXNV8SpZ8MFwJwPSmvoyr%2FAwhPEAAaDDYzNzQyMzE4MzgwNSIMJLbA0YWNWX6G4AQEKtwD9IVOrVe9%2Fl9IcDu%2B31ui23H8B4H6XitbaWXeyC5u6j%2FY9PGcASJP6gTEJkmWXmMyUQFy%2FR%2BF8vp7Z4Ov5ItFuNek1cLMyse5TkiLBoLTEOVjCahfN3paRP7IAX%2FtvGZ6Ox28mBAJbRbwXbpKP9tzARw%2Boy6w8SEnPNGsGxr0c67zoYS2lzwImllEVUHnfliynTchZxDKYzGDL0ic6NyKZI16r6p4MnavBhyLDmoqvtXRY3L0pQt0eOHsuX6AQ3m78i6XudzTxTpkDwaub59e1obF8k5jXBcfMTU%2Bp8f9mmOpmNo9T%2FrTXTvYXeADYD2C0Wbt4Pdzw2yOntKau89UAbu6VkdeR7efrSUSFeVkpCWXaxbMwpfICQuzo8WoRJhT0SKxLoye3EnLlk830O2A4KCCQtPbBddqYw3sCo5vPbXqZHFcV9V%2B7n6A73tquo8gYaHogfuC04kYi%2BJtAn%2BN7Kd60MWC6gpb3tUWUJlIFewG1RRKSooO%2FzyxfmRRh2KE3aTfPa%2B2fCyN%2Fz9IotGBfSaU%2BPqRSz%2BAeuqVQ2Sdv%2Fa%2BxE2Crxg0WDgOe%2BM6qWz7CWHkUQqr0buc5HZTW%2FHMmI4okMy8KwpPZ3ujK2PufZ%2BOL%2B%2BlGU%2B4uPVL2Kkw84zIyQY6pgHJNzBBWAeLIP8cbhiF8YFbeQfgBRO7C2R5Ogbg%2BsVWW4SKSyyyqAGP7S0bC7apw3V%2FsYrOrEfhswYafxc9YVKRNdSdAYCoT7LiicZhT62wUpCIonFueqtKdTkAuc3aHi%2FrmQFsf8jb%2BStB84xZSD9pzfKDcEu1%2Fli1tY8VuBXTPCEh8MBk9rY3K7%2FjHwk7l%2FRq2uybwV1EX5uYPcCRt4MU9ugaQh1e&X-Amz-Signature=9631f8867340d2a9fe9422b726350313fac425581568f2c90fdb6c7f039aff8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




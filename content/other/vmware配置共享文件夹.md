---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2RIAQQK%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIGhzVvIuve1A%2FSajwkqqUPKpTDBbq5ApEUyXb96u7S49AiEAgTHoYMTSC88aZr4vy6vtGe6DVriacMK2ORMqNwS%2BUuEq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDFj8TEkpqAA%2FoatfjircA4Nj9TsRh54A%2BTK9FR%2BChrTiYYK49mk9wucS9DhsN0kYdnhsYOyn56cUJ%2B3OMrP0HZ5HwqNeoTY4MRe1p3PfQGwOr9LB%2BQy5MJRuiPa5slUoyoDd0EFLQBwwwMZNXhycsoD2xEugKKULm8jfxF5U0Cx7IfSgYcR36uE5RqLQIM9Q0adtxuF%2B%2FDi%2FcZJ4OAtE1ZQYkU7jPkGPqfi8jIDt%2BZ5MsFdRfZ66mYkbKhkRNeVBTdtboKr1052lNO1FjOVZXIY1j%2BMh1%2FZrjKg8eB3qQ0LilWTTh3L5puivoPhrOFDTBoSCPzGCGuelFgnAY8fgRC7rKwozWtYP3dbU9hwfpMuz%2BhYoHGG1LDsmdbdZl7ULolOTtflgWMr3InLgCu82PaDt42TaqDgJlbNGpZ2em%2BnWCKz4ZLvi1vZ8ppt3gYpgQHF1Ph9FiGM10Lk8qFpyObP%2BByI7SON75MwAyNzN8aRQG5l%2FbY7NviHjN9qANTMb9Wzz8aJZGiB%2B3EV3VxuaaL5oibdAqHGCBYu50UjGys2cEp9NdRuTugxwqR9heLwvFN6ziTeH4Nk%2BTmF%2FACybbedNr05CNDs4YcLNrQkO5%2FKz7q%2BF3E6nkPk0bpztgawce%2FeQ3EvSflEMNhKMMIGHhM0GOqUBZOFRZcl6aP%2BBreU2p%2BMN%2BhBHZkTcN2J8iQpmuSPuS07qxVkKETSFghjXzH5ZguTuQO9I6D%2F59EV7lbLVLGImj7XZnOWah0vfLLXJEFjzWwr3tDAzQLsQcuoPFCzqQo8fvNUSDDxDhHehuxexJMybCuM3C3SgaBvZ3xfXCY2S6yYkOFZfhETYOgwQTSVIZ0xm0eUFWZ6g6iyrYGodDs2Kd5DoXu9x&X-Amz-Signature=1e3eb12dcc9643678e5853304c1812be3181a555188dac8b86a9ee04a6524202&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLMH2JAC%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041506Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIFjlW3aVK3Pd%2FedOIc9oR9nXnqAiemXMGLyOw1PiAQ5WAiEAs3Wot3%2Bdnl6dzERLji%2FvsWkdprE8M%2FncS8%2FfxftPNc8qiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOccVXlfRp9hXazbTCrcA1pNKfdggxd%2Fg08xWvhaQabjVbfCgKVlqHh1P5JsHcf4JoT%2B2Vb7bS%2F0BShwidYw9b5bi00mw7OjTlqbwLZlGuvh9u052ZRc7sEd8xjHw%2BIhmNRYK3ONxpSvtQPcr8CydkA7a%2BjQvwBql%2BH8U92ZYnjyVGdWASkGv4e5dy5DXN7Aw3qIRuD59x78a9QlRqt18qSDY1CiS%2FYFQVU%2FGh2gNJxMYD736%2F48QcRNitjabCiBpCUfCtZFF1QB%2B5UvrgzR0jvxl4YGyEQe%2BHpwDhX2tYwaTF1Ox4CF2WGhgaQ%2FbJ7P5jGCYWR8Rozmyy4K8t8QmVPIpnOBZ%2Ffcz4WuYvKdXbuAPOXvC6nDFIw9I9QeUXCtVZKu9dwQoilIo2g3aVAhzxen4XXmmMdiGnaBDlQdkNXDq5R%2FxKIvJ6X6A9sYdEIXju4d1stf3wc4cENZ6l%2BYcJfMFkBWUattTn9HIrxjb%2FU2o%2Be34y74MNoLMsLjj4NO%2Fju16QhlUUpqz614tuJrh6ZUcVrIAYu7QUJMsSAbKU3SD%2BLDQCmArR0AfWzFa1vdfB15yLJAuuweGn1%2FeYK3yOLOLWSPyJdcnmNKRyeUuz%2BkK2nDJuciQPkblNroeKcYcnG9vH2Su1yn7hqjMKK7hs8GOqUBRFEGAnFJ0T318B92sErZ11QBy4XpgPrhGq6FJL9gWFB9mWcxuoWS2Ritapnn8TuYpm1opGwr9P0fQhfGwLqYZT6SQ%2BIJ2SxgbzLjNgXcWs%2BN%2BTAPlxGGMWXScOjKRQNcOIzHHEbCuhEh5%2F866lpiSzXK3%2ByeF76e2C%2BjH7fjmI07EFwIMifu0eZf1LPPcJaHI4My1wMX1wuv3eAbaTnmkyk%2FtUn5&X-Amz-Signature=b69fdf066453cd22dd4618f469c57d1e6e9eda095ca206b7d2b597fcc728dbe3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




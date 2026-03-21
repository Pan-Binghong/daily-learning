---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664772WJRK%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDgvXkqBcY2uMG6iDH3MoUt94U66jQ574WxRoh40M27bQIhAP1pnCkD47Z%2B0XE8L3ePcDw4LRtgFH%2FywJx4fP5dVeX1Kv8DCEQQABoMNjM3NDIzMTgzODA1IgyYQ8M3IxmoGXTqf4sq3AOT10nsg1Qd1uTxauKxRQeSkuq1BViXOm4aCgDDVUn7tUYozP3wcZQtUp7S6yXuPH0LXwG9erMDHxxLAY4HAOWal%2BeUaDlDmip9gKk0Q2B7yP%2FYHTL9yPX9%2BA%2FKYY4SHWX4WvT5Ruty683Hx9QafxsG9LDFMNIOEGewnzqO3X8LyjIKspHSXHbUCBWY7NK7xUVt59RvMUOTQRdApAZMhVc%2F%2BeplGTGVuoYpjyGNBUJtAUQsEPNqM865Wyqp0nDgZyCj3GkOTtg2CnCXsDcxNBKkOI9plF8MjQZtY3PwnZom1Ts45gdujP8%2B9TOL08KeQPYENpD9f0qNJMhkzo4jAfDL3MwJz2sp7NmfhqDj4po%2BbJ%2FoF8nPDCgh54jFKsoewVpxy%2BlaWfuT3oVK9B0QLjEHLWlnrMYFefoYq%2FfVzH%2FqVzSiCugYhGEqI6fAMShxNlZOviSF6d2gD6tjtdK3%2BOaTqaoQhjVbXH14MyuZS7tb2wA0Y1HoutWnlbF965n21iadRnvc18zy7xFx8q4PcslXgJibuDtvwuIhT2OtQDVqBPfRWd44Hyxg1DwKdpYEPxw%2BBcNDPbT70fGpZWrmgaLBVdMZRxo22tSbmtdo9WyNDZXdlwR3BCWTMxUv0zC6kPjNBjqkAWe%2F7U2KCBgv5tkzutuOIvp%2BlRlU29NgbrhA8Ieo4T%2BTb6Ns0wUyRPiIDFzp6361H7CudAWHKQaM0iK6022u15EiNUYZKuHB72EIRcQLMZUj9j56GFGqmHe9mgV9Ol%2FkRr3D4uO8cTTsjY2CIFqE%2BR0OzwhaaD%2FAy3dKfc8wb4QqQOdv8wjUYS7PgnFh4MUOeEltbRqiwvThxoYjXtjhxan%2FPa26&X-Amz-Signature=ec6bf8a58a91b44d2c4afdf0770f5997c34a80fb42e7b31a438723c0c3826620&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




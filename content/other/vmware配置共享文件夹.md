---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XAKP2AD%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQCynSAmEN6GRzpPxd3%2FysHWcuLywdP4URtLEaG%2Fp04M6gIhAKkotv5Ci%2FU1n508WV78YhAyLm%2FYLt5zIDNFLq1JTIpPKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz2HQ5ykzcFXx2MhDcq3AN7mdHF8bPImIDEm7%2FYLMLUEFdegzoEdHLk8ykdNnoU%2Bip2bt3RTyMKHVuuq6AV11ty13rn3MppwBoJkdU4Dii78cG42QGRmklN1oMB4qVrBhK9CXnKwtdMK0AeTJEpgjxrzxLf%2Fbf4PKC9RBTpm0kVaxO1XkmztHw0KhmW2ouPaWZN1U8UqlqIp1Z8Fvq%2BMr%2B%2BJ%2BgnQuCa7YwtzeB2MuF9KWUjlvCOrHYLTz1kYu9rcgrTqBZkzMJ5AN1HbUrb5jZwH0SATC4ALPmREQaoySC6RINJ3aDhmPQGJG49a9Z5a1OpipTzv957J78xXWXjvTTNnnHwFZFcQJP3jyixYTd49Gm7R138wdlr8YSpVM5U6V6T0z%2BMby15GP1%2FDNukFWP8gP5JMffRVM9VNUGGtllETZYF1y%2BJWIueOHtHJ6KHqIUPYN%2BhAUSo8nna0mMI2yLwE%2FXXjCEb4MkEdCQpUonrkX5%2BM4qfnNhW%2BrVwQsyww2pmr5fhNKr34yS8BTyUDTrOLiqTgHQV7EiNwJ8uB0qvIj4y5g7MHacwChRk%2FsdR3synocjoMu0S6FsL0sAZaJx4rcx6PxDDDBzNpRS9Ga6ACzWKnMOoU7nTQ2scl6MGgwMGI%2Br3RjB0JFCQdDCB1q3JBjqkAXGC%2FPHo20Hp%2FUYPKHiV%2ByMRhYAL9uU9LqMi8yZtDIOT5zRdOIBWdXbWBOuNElM4D9%2BdeRie08ZvcKBr0oi9mzNJqxBsSnKfs6QMqPMYVb2ZYKx5UFUQ%2BaKbq6yNdifkEBVHeGifKGqu9xPnZnm%2B5TTjeGW9XE6Tgwo4uy7T2mPNuTb4kxfkx3lfF1ZFDXIjrDUNrBGT9wQGzprmBy3G5wRR1Cjr&X-Amz-Signature=70a37db398a8071b594a2ac8f900d3b9d89a2b8740118d9b486222b33fca088a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




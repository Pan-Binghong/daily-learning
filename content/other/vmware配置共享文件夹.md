---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZX7VL7U%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtvrVuldQOFDqBnY3%2FUQgC5DgxN53spPqyqSljDdUuzgIgPmRkUsM%2F4DGX8NPEQH1IKHtppqZWCyta%2BoWj5zxmvcUqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEUTZWRBl6O8xTebACrcA%2BB9RBWIvBBTQ2aieQGZUeYjTxCOG8RYkJG46nHWqXR19BaRY29ISrXy8hv4Ksp8zeUjnoOtAfQoBpgWkt1DZnXl0RQPw%2B84FMqPwGxvDoUeLwD1%2FkwBdz501Ml8KThQuW%2FMRRYV9JjyMRAYw%2FYAZNGAf7z1bZig%2B1LwdBFcUeRL10WcGjdd%2BCFzGG17%2BkBGiV268BQH3Pzc1aTWq6C6NE9CCXiNwVSgqhlIwVyjKdBz0d4R4nXUVTPCiUrVvoVX4kXFvZtlHCRRb9nh7CDEtTouLrdQ9Vo6O%2B9gyHdCtUB6rlE5MnlCDFB4KFn33NRyJXxwtSJKG2yqWalIcA4f75HdNDKISRDIGksqmJMSwarjIt4Kq2GsaX7BtaTswWzRtQrY67Dnu9F0WzlVySTkk%2BQWve9YLKlRhqL2wTpQ1SDjAc8e5%2BnllsucY0Wpyu4lCqClse6hV9e4nKaHBw0mN1Vnt4vjZ63ohL6c%2FbHw7%2BKyXYDXB1ODkxHWjGCmm6pcAZllLG2jphx6hTxMy9olqas0GdbTCmUsa56S21lRlNn%2FS5rN17o26O38nuTd6WWMLdc7AMUWuJakLfo7gZzzQRyQX055afIwl%2BJOAseXIlfyQF%2BkRcpaQI%2FBbGDCMLyjrMgGOqUBX54HiabpmGLfQzD45xNvALVn8O8kqfxOQhMkBon4%2BCmO7xe%2BcB2vVYdj95fHT0KcqXWWDcRfWdvnwc9quEAjqcIW%2BzPr1BWPpoNdmTylW9%2BlJgbaBsNWrBrRMwuwhYzqd88oSnIYIp0WoLXAHPpXeSVwv8ePQ2gBiHMuWT53O0WdHhlkf05iTO7An0qik%2FqiLg7S%2F9QXFjHjiDQTvtKkwwMbB9WF&X-Amz-Signature=6630c606cb40d360dc6ff8f6596900e076208e0dafb2ebc5f90a7204885761fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




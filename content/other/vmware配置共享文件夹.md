---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2KREAKF%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033841Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJGMEQCIGblovrhl0ZWcTiqQ%2FslMNOnMWgn16IwiF5tPEr1G9JVAiBdlvi%2BT91ASZaAgnflvjY8ACJPqOT%2FeP2zYuHOHeg%2BKiqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM4v6IENfmE8R0GfIFKtwDje6X31V8Iybwqbzvlw6RB%2FnkifsbWuNjQXQiNOcERoTDOKfVaD0oATT3mkOQTpFE%2FZhWsVAG81lziDHw6q8L9i6qbJ8XKyR6VGcqT2GDrtv%2BCg4IpZBkRydGqJMNdWW%2Bmn0Njsp7M4IXfwQ0TQJDS2hJiAkVQkOgAg6pDKkATy%2FCyokd3p4NLIpiOdfozRwqHDACWuBzyOG50hcPafimeYDEsj6qR31CQ6srVtKZdAV0tdxVagCTJUruS4KfkM6a%2B7BbOoyyNzz2CprhziHB9qbeq%2FTY1MqlTXlCj1fw8owg%2BpfoseUT8QSNuC%2BSW2yO7LuZw8ps1OLaVG3uPAOQZjtU3eQPOnLffBOZ9veJ7vQWCN9sjOT0HPE%2FLiHEcqCfXAwIHWjJEpJylmc4D1PrdlZfmZWFBSoF40OOoKccSTX4iA3UewbAU1Hud%2BdRkuw2RVcw1y5wJa0IWCB%2Ber9Zb59%2FrByf9KOmnEsw0G2rgE7aSEEPALD5PtsOsJNtAgAInhF7kjxg%2BFtOs3m2W9zG5MXfJ5CAJ%2Bp%2FFH0ooBLYvWCYtn%2BCVaXg%2FTNqRIV6MGmqtwDjgPu0vKvvE%2FrZxq1Ce1XUmDeIm9S5TyILsBD8JRa0c4%2B6Kud%2BHcyyndYwhNiFzAY6pgHxuS%2Ft%2B%2FQZ9%2BrU1q%2Bllp2e7ls8eHqVKAMMgf5KITiRtORzW%2B6y8unmPxf5GehwS89ghr2XVx0Lo%2Fjl7eMxNA2I%2BwjJYeopNqxldcvjoKejVZ8WZTINcSJWsqGaOZayIRcsEPGTLc2oOg2MT06hNhnV39zgCKi%2BMTlEysZdixCv4dw8RBXfqInoSiqYN%2BqYG6oBg58eoWuMhXNkdQBouEhk4Tne8BG9&X-Amz-Signature=49dadd169b2d400783a9c3da76194300ca5458f064e8efe37a1da1e14373204f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




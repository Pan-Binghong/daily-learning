---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663E7NDQFH%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIG1Y21r60zM%2FCZdj1W70U1T34zPbFm987Zh1HL1oBYyXAiAvIN4LQlaB5vXPv0CM1GAjgQanF24Sq6HhoUck6Gfllir%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMleU5DAbHxILPPv5fKtwDSdKxIdGjO1HnXvj8oQopPFJ74fg4JrvewgGcCJ6oszE8brtOb9V0JAI%2FTFIiHDXJspX3iWatYWZ1zKg1LDkwSa%2Bj2y2S7PQI1GBA4%2BAsoyRYIG%2BN5pICa26LxZ8TnHpJBJU%2BLBqkXRoclV7Hk1hx86u4G%2BSHpnBy8MtqK2UsTiJPU5%2FsPUzj9uDF8WFo0bQEAkyQV49%2FX11QBTfLDsxyX8pjrktzVjlCIkpIoNLKsH%2FyFnKU6M7c3zvMm9H759ILFLztRdLY2O87Z%2BwGgXYRSafveUydbRA%2F6Qvre51jPhzIJTrLj2muxC%2FBQSyD%2BjXWhp88SvM63JDQMZZV2YX6E%2BBdobB7wzmiWflT3OrtVY9LZQay%2BmbDP6TB27UzNCdkMz6LNkSXC4YqDSz4K4%2B%2FRS6nrhXqsEVG%2FxDPvNIWCirzcX5rj5ZBXoSFQvSekG4RibRe7Q2Y1evbMf4PRk38%2BVFEm4kSl4k3%2Bkv4wM8MDseX1HQ2SOVSmKzpk21b4oLoDw6Mw08BFqRpOFr9Ut9kTLrn2NhwQw%2BEtPByhAlTuyH4tN%2B%2BDZHhJphbNw85TGkdBGIOu3L85U6A0su2Zmg8QBSvMANImFNeyabIWweKsg5EtyuBagTicdYP1VcwoJ%2F%2FyAY6pgG8cxEK%2Bci4ANl5KS45lpnf96A%2FlvMpqIPuJel1YKZ8%2FMU%2FRl6eT9gZFNvvOZ8vDEqG3SCTRzU5mJaL2DdtgP0FVqJyySVRhQjyzb%2BWBiw%2BydUUpx7yVSnzyHYrWwwYN0VSvEIuYYdTmAP1j1kv%2FP%2FybF9qhNkGhqZM%2B1QpvzGlsqeXJBa7a2mqqjw6%2BNZFNi9yo2h2wDHNolLrCdUZ9uhpmAjG09P7&X-Amz-Signature=678d974d5d72f5faef7f2667ea0b29c2c7a9fb220a61fe89d54d2d1cb3cdc2b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




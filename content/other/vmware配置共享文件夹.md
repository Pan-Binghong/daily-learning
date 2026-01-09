---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636IDBF4S%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1fh5fr%2BVb9i7vyypPpX3giDwq7hk3sTGuWQ%2B4xsZr7AIgGmYacto1%2FkfrMu%2FCgqP9GqjWffGWQkCl9doazKUrSkgqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFMWaJGQh3zHtCmWDCrcA%2BSc0f1Hwz2zjlRh3PX65DVVh9fr0Ypq2Lx1g0lTEb%2BLLdMuKZR0a5NfYw%2Fj28ptRAx87hblCaHJgo0PMSHxY1756TLSGC8u0sFdxgAkh7%2Bjcr9%2BNVFF1PzK1c34OiLQPmXhE%2B92WdaLbnQvjcb%2BI69H2x5p00SQh%2B5c0ON06pl4w%2B%2BM35lSkYOPDf8ffZfbs9fAC6hiDDtsS%2BoiSir13TZCxSdmNETciwX8GmzjfKlzrMnYL9o0We0vJM76GnWmbYovmxnvgxlh4McCwn3wocV9EZqWOpCIxYObFyBuDcZDTYDUUyQXBrYS80rFgBQrs1F0DBFwo%2FKiKE6C6VQ4AzZVJODtgIcJa79HNgpA2SPQ7z8rb5hprn924jGR6U2v%2FTDxdQ32N%2BEU%2F4n3kBSn3NWeFJxIg7IKFU3lt8HoAURC8Bh5HDP9mgjakLqVf2vzfP5B1%2FIrZDwX4PjHrF2mRMvdiK%2FziJm1RP3zN9xasCGuFVZg%2F6HnuOohrks1Q%2FhtfzeT9o%2Bw9%2B%2B%2FfGs%2BenTHL5tTzJV4FHwaeUageWuzGroDMoSfUHONHJPSQPTGuPWAI92GuolujyTjSowVrfGOwavPdWDRr1pzZaXMclSyqA1uWKfw6Vbox4%2FX6iPfMOPEgcsGOqUB7jq8NyHrPFb688W1y69iynxx2pfytMUbxo3cnDGVbqoPC3uttxEfy5gHLqbB%2FeVF2W1950u9NTg%2B8EMzK3IiA2xIgNroKnAstgyfmAR9RAf6vWoz%2B5e%2B%2BWPtltpusKq3XScRELNooA5raC1M38LNElATjGllGjnq79Yn2oxOhI9QGvBE6Axc3aLyj%2BwS0yCLZc7PygLCR4aP14CrX4BJK9PXwcB8&X-Amz-Signature=360020c75298c59f26e64a3580ee311a6bcd62afac3573a068b303703040f51f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




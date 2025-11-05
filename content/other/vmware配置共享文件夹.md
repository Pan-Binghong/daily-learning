---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZUMWWJ5%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGrnbVPcO0u9EED59ArY4uBEBZrCNIqJoxBQcEq5G3UWAiEAscCc%2BXdFLha83cjITHj3rT5Ghyg4m0bhqGAWoqD9zlYqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKJWTxokBLXT31%2BAYCrcA60TwrrHIQzzP3u%2BznKYY0SEyXNBZ2CzRlX83uqZTQnkMyBhPvynDMi05fCyvcdMwKc74de00UkNi3MeLz75FBW0xGlVwmktr%2BeLf8uTYPnzfnaMBiJPyfza%2Bwn01gPANStcViWR6pUgf%2BEdNjoxHRKbJSZ3%2BfkL0cfs5dEPQlFTq2r2DSigl%2FPE77k%2BO6BheWWktZRG0j0PBSGXmKdX0559OgOytLAxOh5fxccAEbcxLaCXcgvugzKmbDM0BSS46yzZJFyxPtAK1jx6qh96vu4hA1oC9LbjiKreycEY%2BVrcPn5fNRqbprOvOBaKz%2FXjlf8P9ANFjT5MDmhMn9rcvlDMcWjc8imVI7ypIYOSYiS5vWdDyO%2BVmagd%2F2SQPq%2BmQYh6%2BsN43%2B6%2FgPXXTzkIRw2W5R%2BGEgDtfot%2Btku%2BaAJ7ctn5f15gsXzCKIlrRaUZ8HXv0eVtKyoxa3Zkewc4bB9vPJv7vcLcFOZFwRcUgCtIK7gS7x6Mb3UgJ86ckRnOe38W%2FP1uieUh2g2eQg9qPPblA70zgKjl9QwmxpjkUFryaScLF0Tg5gVcPO0KN5EVwpeibs4iroDbZ%2B29xjDXthfi%2BSSsKdgtuUbvMvhQKckPUtc5pAcoHANsmto1MMafrMgGOqUBgJzMH8Bp0%2BGWABtJn8s%2BAuPS%2F5akGqK4WF099ZQIMYgpe2nb3G8zbKkMnoBaogH34GEvP56FUo41V1YfR00e7Neu8LAxYGzvfKrWhXwOJ15ydBiKflfHGRH698Gji%2FIVGA%2FFnR2bCaBqnGSmQYGG6onViA7jsSTF38xYQMkJIgcg%2FiQcRGa%2F3TGM8zdJ0JjUCPH3%2B0eov67ItamKHlErLYGA8pWA&X-Amz-Signature=7778dbcf56875148b0821bebb315fbb3d673b00cbd698c449601be25851784aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




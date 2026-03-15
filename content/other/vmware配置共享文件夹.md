---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OYG5PWY%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH46wOnEp29Tcjzf8xgwE5DUoTIwHBC8VVxqCjQl9Hr0AiEAqS0ywmXv4AxTxrMnZOvYIPIxn4Fh8b65L5O66PfrN%2BcqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOey2bjIwoXmaTg0VCrcA%2F5hSV3liOMhYn9PHsrsyTLk%2BbHi7jqrMNsimtd%2BENgdbUaIWp%2BeF4UHSB64zuyhyrVcSxknWwZEZ3qBiJCItg8Z8x25fS15TfQ1GkgXm2yXYj9v%2F3rhKuPaU4RPtAMTAFHjcQfWUHH8yI23x1gSsDBQxleaWibpJeqWarzgaonaYkrNagLOx6RLD6Pz1px2INlIhZaJSk3tOVEWe3PdXUDWUDNALVvUTtGYbPA01uGQ85DKuceKKQYi58gdwcA0BGlwlLkEgqeGTkFMU3kIl6Ye0GM5c049B6ycitW6ugqlECOBBoucMJ0cKDT355VYDB3L75X4YC0qf%2BYgnK8nqBog2nGNFSOqvegz1OaF4WkUadOjrZSbeCm1%2F1oqamfRrXePxOZC%2FUL12FZ%2BRjaa0mUZfTP3QYPGlB8wr7o3CKjKMj9SuMrPQynN%2FPUBKZIjhn8UQqw%2BkgmivTCoehtuJq4v9zp%2FmkaiZ7YsExdlAEWBm4%2BAz%2FV%2FbHr5YMoTY8VssDgjE61uwuD3PFs5Bk5t6NpT%2BH3bvgJbCpWZl%2Bl9T2EzCbWCZSjtQZOuRO3JVX9PM4%2B4p5%2BhG568iSsgvzD43ulXAzmu8CbirpPYybWb%2FZ70MZWOcxnih1fAVBDOMK6R2M0GOqUBIgrwWCcs5iB3KaeCKtmaOCdAEmpONNu%2Bpvrx4v4pFx1l2AosrtK3RSNXJ%2Bycs%2BthUIdAgB5VajYCyGDO1HkUxOTt1%2BQ22WEG5gb2%2BCYhlSRW3Jm%2F7jze0W1%2F41QmqSBAXKgEP4%2BewmVsB2Le%2FHTHyPoEEc2iTivT5U0fgGcKokT1AmjOnDOg8MOEQEoTcCf2IXsmbWNFrFD5xEAaleLeIMD8tTxE&X-Amz-Signature=cbabb6646e0bf3cfb065f84fcab193494afc75f8c0389b6f1735b5d9b248b077&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




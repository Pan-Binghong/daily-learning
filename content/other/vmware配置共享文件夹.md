---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QH5OGIW%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGytjfxQncdeZUtUz4zQb%2FfNl54a0tazQrD87SUv7KqAIhAO%2BkbhvdKs9KuoC9F9YAIpbmg5NVYnQoydLqYy%2BEfeTbKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwDBH00NwPHL4fS%2BGEq3AONd8IPtb8txU8YTqLStWx87l6nAD02qrVDFkH5%2BzidXjjlJMZO3v31KLPume9yAyXzJaqCGYmbYktc8flUa%2FmK4iFLzLU1IV0klhxeWRvm1QWIFLqHQHkJNpRSlR96%2FAg7iA3tcaU3slBXRLK8ttXvUGcWSV2aycqg9DzkQjmmoxuzGL7pbLAUtUNC%2BTrvrj8Dv9FvzAul%2FpO5jI8u6f%2FlbbtVrKjJgKT57yPgFwU%2FJga1fsg4zhVzYy3JYpRGV7BAtwHAXgEVM6Q8MLWD3Jk3s9ntSdvFUKf%2FczZxSx4L1zsG%2BbSH2QnNM54WKxDpbWVph0DJIp0D4ehOu5wTwthKS%2FvdDADkxtmEVbkTAQU3LHeIH4LJJ82ztT1p%2F%2BC3j9SL7po1eUH32egp6ZxoNNqz%2BK3pL3j%2FvsKXAZrEI58M2TJIUiQHWUZf%2FoizAfae8Z%2F%2FlzsMzTv6r9inq1XaVktts4tleRXWRkYfUtNNyhb9hsU5mvJQltIuc7UlADaBOGI5K%2FzIpkRX6BC32YuFxsE6klwSmC8wh3TaN94dD7axrgIz%2BvFFsKp0scuQB0DBbpJp%2FKWAoUmhQhokg02YG3FPQCimsRNzatgw4FAZLY9Fmc628GS5xZub12eFKzDE5sHOBjqkAYgOT92eBA%2BXogc3lWnl%2Bsiew6fC%2FRaLhZrYJHIK%2BAdGWtr5rX0CYC2EQiNomIRI36HFibpww1vZkrkaZ3TH6MVxRiyQep9GTAOYpXNPuxsBGTu6cZldDtrToUs0v6KxaKXLpfVDsU4D6Dv1x6dm1NXZpQKCjALHN3WXupilyBplCysQaH6no9vvQjTcDNjWNKWqzZnrr5wlsdi4sWqNkPS%2FFf5m&X-Amz-Signature=9a4dc3ac65b59f8e5c08610c9fac86f69a163dabea08a9c02c4cb36ff7d6240e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




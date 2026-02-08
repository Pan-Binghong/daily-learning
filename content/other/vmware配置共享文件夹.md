---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662B4S6MTF%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID8WiSIk0nAfpghnWYYDgfVUWAxG2MUMSbXs1IfnGAkBAiEA7kXrJsJ8AkI4FJB8Be5kfhoBhXZWsTm%2FozJqTHU7pcIq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDLvy96IFpQ6HiBb0OCrcA%2BIMeNJ6hj0xzzdqOccHUoQ4jwjeq6z7afyec5vvEnMC4%2FzJd6%2BtnMWTC3Q1Oz26daajuYlY6cDQrfSgSF1BbNBUyLZeb14iFinoL0MjxreeUYIvTA5QlR%2BVeFHfBy9r5HcDJGBQR2ST9iH2yRwva8g656eXHSXbzLserwf3DYnR%2B5xBHJN%2Bh4%2BXiNIl1LqZ4X%2F6T1npPbkxUZU%2Bm0MXeE0XKEdnwHaenYn9xM1NyOsQhqGOz5soOD4sl8mHmTTsSYem3pYGu43M7NeIWqodD3NE5qvpdMVCbvAAVgTWIjcWEa2ox4U3IOglv%2FwviEX8Cx7E9ogc23Stf%2FtQCeMghDo1z2J807wnBr1913KEw8MOZvkO2dQn2oqjW8Wp9cde8mCcCdlML1H4n%2F1yox2LmRAaVzRbw%2BkHnpIv7Nc%2FWM2IpERIIah2TeQHPS09T%2BPH0qOHrI4CzpoHFfb%2F%2FNXx%2FBuficdl7M0UrXIEmw6mtFVPuw0PbK7O3SMXO5zafK9w2gf7JKHLN9xOXgDB6Nc%2FEFeOy5eAvugVpn0tL%2BwBSHPATxm4N9wSTTk8fbJWmA2g%2BMAfzxhDSa4XQTEgb0XW3TzEyJ8AnnlwpoaYNxpLWTeEsp%2Bi%2FfhD52w1vzRiMK2MoMwGOqUBkPMdtlc%2FjPpE2E7jTX%2BIpgNVi5tkZfW6OpyDi%2BvTVy%2BlvspmndFbRmiyw87aWWevfSow6rRwAu5u7sYEvjsLPER31E4rjDXg6fo4L6up1CXbZh%2F51fMAkRkH%2Fdf5AInYbjVWHF1J3dQ2bYgKssDRWjvwrlKiH3qmbtccSiA8XwZ5X13HnlHR1xledX6HDEnnqQf5cBXKll236U2tiTSAWDXR16e3&X-Amz-Signature=5bbdc7a531a77e9beba1ec85ea898f40a40878d01be681ebd17398909bf4df4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NRLRMPB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG1VG229VK5jGQF5xJiwjD6sAL%2BpVHjgK2%2BCgEt3zOgVAiEAzGAExecOfX3O%2BkYDV%2BnTXP7gqO%2BmJCFlZq4uK%2FSXG6MqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLBSdmunBCcWkfZIByrcAxzWcJvBucpvB7Sokpg3xq5aWkoTT0vrPwTVa%2Fr7lJOz6466yvk1Vh1tCj7UPhIAC5s%2BW1BfL6oZ%2BvpZpKfhLCd7Bo5IwdxXCXrVXmRErPnn6wqyFPLle8W%2Bz48Uuxlsf3AUfw2HjescWDmmAkbGG4r4UbOdx1iOdgG%2BCXuXO150Z1Afp8TIVzdNhg5WPfc2J07yOe4NuiwB%2BaLL%2BdhbHIr3d5PqrHn1hzqf0Dew8x73yTRqPT5IPH7%2FR5wvzBs%2B4sqQJb%2B%2FRzDh4m0O%2FqAqf9z%2BI0BSXQuZI082%2B9mYEi2%2Btu%2BOMulbh96B8K2Ap5QRkjylBjf3AKHG9wMQa2QhF8%2FQwJQtmuJlhtn%2B3NSOHaG7z1GZuTUJl8F8p8hGTRjqaIDugzx%2BT8Vr74K2QKzOSN8itndMPBZRZjstU%2F8IHv6dzZmX3li7FcI3MVQ8h%2FtrMytmDgU%2FfA%2FXa%2FTv%2B2MKKPydleg2gBXxHld9idLRbmkdpU94yJepqH3sVJnasoVy197fkZHRgAZn16qrl0ZnuCcUndUSgbSYi5%2FpvFVKPpj395HKuH6rN%2ByXEylSMCaqhCitvmQsWKMSi8XUTgJGYK3HnPMizUpx0touD%2B8etEPWpEs3xcK%2BPJGfPwLuMOrwr8gGOqUB1ZLlq3Jqcp6h60uwqC%2F1dDs3DGCSRk%2Bm3ohPzRhjGHr1g6V1QN2aYSj%2FKLSqL%2FkO4iOlkYVuTeCH7hLR6n5cC%2BLUSqXO%2B%2FPNOiUWyidGWB5fkyUBV3W2uADqyO5wmhttd5i%2F48c4kVdsUslx7pArGK3HsH3sTDaHGh9JYHGiiTfLrfvx30HSnjLaVh6JT2%2FirOCndF2nynjLAqu9hkAuae9se8Wk&X-Amz-Signature=877b454f15a37e1e3e826bed512629e119b6e9e240c0e7bae87e87fec4ca16c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




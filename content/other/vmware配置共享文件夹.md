---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5JNUL42%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5FF%2BKl%2Bbal4do9EL5v3sGiJ06VNv4rWefch%2F2Qbda4gIhANQxmKBbB1NPBzpxh19Rv7qhKFCZAdcY0UUBIgHfowlFKogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyAQ5KlYIwDpQqKj50q3AM%2FHTHqcRzh3MzTsADsOh0Pvn%2BEookfesTvwJnhWH2wIlcsxCal8qV0mDkVtXBJi9PdH5WZ0wdvYE3vYDYEA8w7D8FLQS2ElHt1g4EpgHDybFf2jh6EMToDz4yY9dsonHoKWcz%2Fbj%2BaQ4sjJKFtZ4s1nplG%2BHAcZ0Dr9cdeztrBaNF96V0htv550o%2FxY4j5eOKD2IGh%2BAH5n%2BFbFCGVByyxxmKivkiTBQzNYoD19X8ZXSRans2QFfIL1RA6fozfqKp5YAtjnHgHHkxb3oerxUcSdSigxyt2Z8HfPUuuGYKB4HUZ383C%2FgOxNpnUp%2FL8J91Y3aYRJF3ABsfjOVziQid6CJCBimzezHelde76GFUzlQVdlc1dUFzXPcpTvWNXdMX%2BaL3ZaLpdwQdu%2BBt7qy3MAag0jq%2B5HdCGNPLQjUfp4XT4XegzUoOCwO6B7w1%2FrYzvg8VVQKwAtGxZnEq%2BAF3bnyJu0Bc6nhpPasW70lnRu4b4nagMoG3WeK8EmoPfdDnbAcXDUEjBJZo8M55WfFB1NjDT%2FoBk52DeZepYtqxTKyVms5DyFe9JxY7ZnSa2nfEyEdb4NvRboxWzQWDbTM2udB0vrq89mSrg8Z4WKHVFFFarplsvv2QW8nnCqDC1uM3NBjqkAYjRgY1oVihHa8LJCxVmAnzZYFKKwaIN%2BedjJHXwZ0XE4M0cLCw1jVlgZ2R0LPL5NSHs843nh%2BboS094hGtY48nrhtsDSC1VB5ajWAvqFUpXkt9RTUyF0WEFgvGi%2FYfz6avu1%2FTpk9nd8hq8mnZ8gQ%2BA3TzuASghYbNpiiFeYVQabhjX8c6mwbnRKZp%2BqSICWCoT3w14g%2FCW5c6iZV194bNhVJNl&X-Amz-Signature=09c6a7d84ead98e3b12e20ffb65fa6033771dc9f06508f442fa853366ed82ac5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




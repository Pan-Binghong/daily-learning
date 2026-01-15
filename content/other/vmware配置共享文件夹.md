---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQKKX7JP%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCgEI3eUXIaoA7At96YMzhyW%2BHxSL83ho9r4JWv%2BlS2kgIhAJbBnAMEfo02HakNCrnfydvKExoz2IxZCQiP4gDSDm0rKv8DCCsQABoMNjM3NDIzMTgzODA1Igx8PGnRKMGZAz%2BGAq4q3AND27KHgOgoOlL4cAwZaTxaMW2apQyvWrM55SwxsqiZqQljcMGu3A71uAVb0etLNJChcSboDH1HMIj1R4ykEEHfKt8Ae5XfpEfA0hKeFTszeR3UYo40MHUiS6LMn5UViw2c4XPST3q4%2FM39BhHz7IChrd2qvj6dsPbw1prGQ6fQaw2vpmI9huGIuYDrZTA%2BCRvuaGvMRCPILDghjRYMmbN0RLLDUKgH5w8iiLsIy3ig3zn9CTlHW0cWoBYasluylkljn%2B2ZTd4nRFq6MhCaBHbRkeu7eGpU3jA78tNKXHFPZIFbjG3KdZbjXS1WRaLg34kFTeIKKzP4i%2BDyx0RuPVvsC57L5IoMAUcY0wHm26nhD%2B7a4av1okByEjpckT6PQFLnETJiUkxJyAY07IC1N0PGoqcmA8ltBvgYLznLiVSia3PtTdTafn5GxnMYIrR3kl6%2B4ba5DhmKzD6oFr6sZfCiYvv6J2VMVVn3%2B0RMdk7q1HxJMGdl9nmqcedhuetjmwrBq55HUjgGokxVU%2FrV%2BKpnUo8dnx7Zu3IZVpsna1TPqN50btxuYtdqdi8lRWaICFiap1ekiTspZHWNE47vacEJjka5EMfhEfb3Wito1g7BjbRdkxIctKpeMxFtOjDTm6HLBjqkAbt34x9MC9gDHVqOaJgdZaLMEktiLU8zZ0xxEUT%2F6mt36Ym4FOIJ6VIGlkPN%2FXfW9O6cqEcdR9LUk4ckZkvPuD%2FjQue%2BUzV6NgSFgkcAib3SYXjink1qM%2FhVMYuJfeqYKiKXwlBVsCPJ%2BEuL8AYk6p%2BBPiQ5ZWKUjDsFSLemx5Cwp%2FZRx8YL1uixyHezuLryTqF7WfUNMFMogHwTVHtePM0xr%2FAM&X-Amz-Signature=7fac7042343e08ae465a8414dbd1042a8ecd2628a22f169390ace5a2e3f4d014&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




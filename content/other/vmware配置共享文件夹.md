---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMTBD35O%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIElDE4C8s2bH94hS9%2BcUP8%2BF1g%2Fe%2BHo6s56dgdGOvFZAAiAtk2Vu7lSq9eoNjlHZT7ENWGKZk%2BdcJrLOrC8X8s1mPSr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMlbKj7LFLFVmJcYgnKtwDtvgOqR22s8gjZSUqbNZPAdkIDzNCdzQ0sjpnKSpcvqUSChFQlqsxKe9DOyshlcmypC3KfrEAYmrFcPiTZoi587o9Pnkgi1oVI9TJLT1Ad7RkTjndJcKZ25aLciNB6%2Fet3q6TxbnMVi%2B1fsYeWNdHMeMY8eB0inyaBLClU8M1zJXESYp%2BObY9u0C2uU1tSqTsujRZF8eUohaeUYRWYUuIs6ZQNQWrV1Fs3oHmI7YMdjWklE5b3LMa7KdRrWDEVJtIeS9187TnsgLV1Db3ElbcwB%2Fav2WTUSjjHHFaguzRNJgq07DHEhQPE7J97FsnaxW9bXewBD7I%2BdKTHfRZaZzSGYbqVR2L5wNvTdRBMLNq4ZfbIkj1njQRJbDVXDrZOihJ6TjRFJZow%2FuthHPBIDOV%2FXray15vE2GR%2Bl1hFXh2nhYuZaAPtbzM%2BgEx5qoWcSB9oA5v3pREA7j0wYbvNuDMEMZHNAWcIahrStcfgE736O0%2BthvlRcZ0cM4rzOFAzaBsOnC%2BMR0%2FiCDVoRlcd3qoUJkGb8J9M%2FayYCL9LPtyTf%2FJqmdZ51KI1jxSKakIQSxkX%2FqzV2wDPQdxUFvVplkxcyhLce60touMFcvD6sPKqNnURfjGuxsOPpqjBisw%2Faz9zQY6pgH3RZRYegDwH0sTyLS2rsqToNHrjizh0EX3tjvksDikJygDLLMwiH5rhTW7c4I4KD3T9guqGmDKZw5qYs0V44asDV5EkPoGMi7wGtGc8oPxHq%2B6kXmpr3X0K7GJw1zgO1pmtMXH18YYDzDnzL0XX80DNFpl7BuJ1W3QpbU95trw2LyjJQupZKo2wDu%2FeEIgoDm9rD7PI0jJN2sDTmc4Jvmx8wRqDsnI&X-Amz-Signature=13dd9359b4638b1c107cbd4c80382fe670ee853a7a38c7b8c3d50d025511c715&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




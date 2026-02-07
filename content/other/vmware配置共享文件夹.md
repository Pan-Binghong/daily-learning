---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VA2SG7ZB%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCX41nLxrcIwr1yS%2BkAee5V0t%2Bc4CcSsNxvaAxuyfx5AIhANWqZouPFfKlOv0Cb69UTZmzLq6nQlDy9a0G35zLwUqoKv8DCFMQABoMNjM3NDIzMTgzODA1IgxUSj8mzmKt4hY5meAq3AMz2op118QHevLLZkFgH5bo2PullfSEzHrWAoHDbv%2BprFi0Ltd36DBGLZxvKgSirJf6xUlvVrciUJI7qtFKL0yZml9Xgl4Ej1bB%2BMTKUxdXRd7ipGQv5YzZJXdk1gZ568%2BviST1H%2BLWg1t4eITPHUNDQBua0wUfh4hAe67nyxLP1BCYufdKKk2HCuxkLV681YGGisRtSTPHTNnEmMw4LgAqBSoRNtMmdwAHODfaULJ32IExbtWesaq43b59Wh2BcM4CK9WDqhAs%2Fwj%2FWYk1fjMjI84I%2FkQuNU4%2BqYuddmz9txqEWXgz1bl%2BQj2XjQQheyhr5CZG1pmi3tqgNVNh%2BBVTUyGzl8tTkHa0VcKnUZ07fwDJguK3hSyPvPSsQyLl2MQOQsKXI0YmGRgK40XiuaXf4rxazB3yVLcBgYBaG0X3ta6j6rf4ssOgoe%2FoLY5iA0ewh2glO9kevY4wvwaMxxt4yDazRmTqAkErhKSjlrPwx%2FX8rogoXLEgy%2BJ9NGVKZtfGsBqPn%2FvXw%2BoJ6juk9xQ4aMg6b0KaGvfb7XV9HQXWSnEOc35W9QxP887p9Jtocs%2BhmnMZv7qAgYYxnfEg%2FAgLCc%2F%2FmsisMTNeWX7sZ8y98oT%2FZRgoCchNxKW6iDC4xJrMBjqkAf9z5tPfqOGnPZky5GjpI7iJ0KrmSQBD70IXIUXeTHoX%2BreApuOmpGjtH1KvdZ1ZwY0zpv94z6e5EivyZs2bQuHbcItM3wEzYM3PS0vpuSh%2FRDHbRPMw5rfiM8T5q8zpJ8yrhmBIYMea48ciI5cCZhz4a5ACNVT%2BnHVyWGB1e%2FmkdQmBb8TkmT3V4IAf2OZEX5lx%2F0pqPnhfy43rYHUWyuBzLW88&X-Amz-Signature=5a475b908ba1fc9957d2c1f307b115b3fa802e91f50ee0854ac13ac62b1b6460&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




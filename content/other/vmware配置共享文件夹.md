---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y47FWO5S%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIHMC3OCILKF%2BHvQjfDhnpr0kLlWZZMmig8AYDqfdWe45AiB11sD6vjdIWYsejaz2YWsA1LnGdeuLA9f%2BQEzSk%2BgreSr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMQDTY7Xz5rlPXdC7qKtwDjlRfD9bM4RZRT33gRhnrXnYqeIW91iyr8erjGmJVK8y7C514mWRDL8CwnDJE3iX%2Fz3xBAzKiFXrm2L%2FN0ZS3o0xdZy7D4xRLXqTDliCIYb28rM1raCEGsPJoZLw9SvZQi%2FdEI8jy8FPNB3AAAYO6GHpEuRf0Wt2KD4I0mZtMMVEJZ28TXvcJa9WuyTTi5n83J4vgNWB4nRI7TcW%2BNbTh5ZMmP%2FU0OhwBm8Nl84r1OkwjKcPtXPKYL%2Bim6T0644ymLEUKhY8XmmhmgdR8jCQcVCwp6DCSGZ5Ao2IuJKYmr%2Fr8xxV5lXnRicqopOi%2B2Ti3fj890EsJ%2BNuu0HDltUyVWg5xiiERgpMpC9R9INVoIzkzK05JNaHdhfc13z3dq2N8s54nOB89ufHADSoeoJF5WNrLZ%2FeYP%2BQ8VMzxWoWxP2ECFA0xlNA75fYrwfCkXf7V4aoY%2FmCxipQiTp73e9EfsDFh19KVrmhESfeu6gr7Sur27QLYwG1nbwq3stuHEC7L4PoJBaTonZkE%2BzRocD%2BifCjEc1%2FpEyVYrvOIkGsqF6pj8aIcFatuTxH9TjcxJr7L6d4QiabhZBrtcq%2FmGz3g1tq0C5CFr%2Fkf%2FwnMowwCr6ljurMmCs2jt%2FHHhcYw%2FrqVzAY6pgGcE1ZBvBBGliutOnJv5BmfHNLadnRgNq7DRtUNTIWngo6246pA4eZv096Ucf3pJkMaDqEPVIcdfvm8MTphuYMngTSKDz0IuMB6p8T8glJ1cm2inI%2Fdbaa41ek9H595vmI9nZVBMWUVTAtgaX9clzEl3q6HvX1pYRXBTOR5DZqV360xf9P9XGUahkM9GNOIeN%2Fq7DAZLNJpI2Sp7LFNswayI5TOa689&X-Amz-Signature=98e895f616a27a84ad998ddb2f9558880e321f63b9935be869bf53048c0408cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOLLZPZL%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9ONfhv8bOiXbbb5VO20J%2BgIHCAj71XKDnrnDj3hPbCwIgYqEGwENc4zTUDt4TE%2Boaa62Vrd1THiPRSZhFNxV5dToq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDNhQfmamvy1EL1mK8SrcA5kBtf80Vx%2B02mOccJY2iq6QXJRleSe%2BD7bTI9tLE%2B6t%2FWTgiy7JpG8TtsLUMEqZ%2Ba6ySR5ch9KcsyhqgOKzzaBE6S8r8vnhbx69Xy0oqFS6diuf9aLi%2BUb%2BY083wg9sVT1bqJAcgvAWD7Vy%2Ffksyjzi9EDv%2FwSDeEZFmPFoF220DkiBgmY17UakoUThkChaBCE7xlFSOFKoYhXEUp7BAfPTp7PLxuxLDcSbY%2BFY0XaoXGaXRQIfdTuoo740%2FbAChWmJebxtNqL88cMf5L00AD5%2BYLRxpL6SwSkhmmpKGtb2etYYF8Eqw6Fu8%2BzbIOP0lUEaiWzqeZkubgSfVbaSBvOA0O3FmPNsB%2FsQeQNfKPZo3ZWdpiJbjQf7AZE0jABTYs%2FDzYg02xiBOEa%2B8ASDoQ%2BNlSAs5wB8p5HIGtC8XJv3wDwIZLUMZNYLUJ%2FaQARpu%2BAWYiIybG5hT6Tqvyz414c4fjRiMmURc9qVvNsn7vJFJFTyIt6C7ZRXEaoX5k3KfR39rF%2BpbSGTzirAv%2BmOPtGOoapiiUQOiWUqgJzqtyXvd9nlD%2BmTAGVvpM%2B6UD4Xm2y3xxlN4ODs3alRPgZuH2x8zEIvMWrz1zVRxOaRNlHjBz6mfIP8%2Bte2ERd5MKOwmckGOqUB48TMhxKajnKcuBWnwO8TQJEdyF53IYGuri4t0jEMOI95HJaB418L%2FGFsqJ21X9bl%2B04i66%2Fms1KPBdvQLewCfTJwgfAR9pgYUV95Go%2BBpK0%2B1TkjTkslMtfxRRKjTVnjO0cUN29dD4S6mGOrsirbN80HLupBvnFV%2B3p3vQUTN1Pi%2BAk0LphpqNx5pgzi3eeMuwaBN5vtEN9frwQyt7LpzQPmA48t&X-Amz-Signature=48001fd495d77139229e856d89a83acd71863670ce946fd1253426866239491a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




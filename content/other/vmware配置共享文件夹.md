---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYTAUBL3%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDJyd%2FCBWEPZ%2Bx9%2FQy9lz1OEOREpySThR%2FaEoFn2Ci0%2FAiEAqyiaPLLxHxlP23A5NTgyJIbmvV7mbdOnzUYKZ7OOsTMq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDH0mQoEwQeSP%2BTEvCircA6MDYCNVw%2F4iQ988lxlXQCISDEF1d85QIw97is98dCkMJrzeNUZrvRaOuzbppBxsQkmWod2Bwf1Kh7hIN5x408H773lgruzX5koFzCeHvogQIbtYBTP6ahzGv3bkURYTiQyzn9GQrt1rczTVpv%2BNGKupYFAPYPCutJ0B1nJsFo1h%2FInNiVezIEnAup0XUfIqOFUhUuVyHxZPHsW3dK9ePtJCR6RF8h53YVP7UcpLz7zpIBlMuitUNTtvN7h3Sp3MJHtrTtMNWwzlMh6QqlwuRNCidIYlcoPgzGg69sxo0KlG4tkGRExwgAiwnn2tiKz0Dn7b1psiEgmxhtbgrAe8b1lQZ4GWuWaEC%2BvdGW6j4LoDH9k%2BnsFkSnbQeQ%2FJgNElrtTYRt4eRgqW%2FKM0WvBHTrgOfZzAaCK9fpDrE1%2FhXoQnoh7kl3dqfkvyvD0yl8mL93v925eMmlSStHM81tSsH3LczD1PSNmZz2cuucFLLW%2FU3ijFQw5yLxYFWanERmhIsKnqDsOHG09gQZsz5Mb4jrBTEjVKVU9wCtCl54vhBVfsenx%2BlC9t7Lf619ukfH3FlIZ6bdYl2QZ%2BXXiL5xg507MZuqVzvWaQMYg58WpjndWlsAgEOVj9Yb47z37gMMmNg8oGOqUB5cp8n1CtsqpfjDwTdIDj3eaUTou%2FHcFIEsX1kY0WaOGgFARAjEUMZubCMTVagJHD0%2BHBoTCU%2BSeh8YhyKBZFlmSkVcgulvSCLKAqE1C6XPaHD%2BVO9vwjskL1wTsqVGpsybTWAMVrKY3yvYLPS8HyYvPJDh9KUR%2Bt2ZMA%2FLlxWl4jjeG%2BY4aZxL3YXHwhYEdwLJb12IHNOku%2FA%2B0%2FI%2F8ojDlhgRvV&X-Amz-Signature=827dea093c670dba9f7b3a6974e0ca7ed484c8950ea9a6cd7e97d3e677d953f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REEDC7IW%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQDDOxqLvos%2FnL9hcq6cAj50X2Q7ZGou0yOSqzAzN6TchwIhALAewFASk2HpLnyqze8QxNRXr7S0Wl7ClF4Nh5kFzcmOKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy7iQtqrJTRAdNoo1Iq3APlnwQFvu9dByLV09VSv1TNuoxQPO1LeTv04fpVURMwIfPYdKMmBRW6RcLEQXL%2FGEn7Sb04LC6EP5ZmoqKObE%2BXVluVXw3yIMjzux45gT30Yka7wTeixWXjzXJ43Kb6GDH1ZvP%2B1adQJLws4Xu0ab7E2oLLZq8dl6Cb%2Fg1hKrr2v55MBZ4snTzMcrltCMg6on2%2BK2fUOLTHdydN5Ve1wugyFzOBfDIyXT%2FJGDQI%2FK2ThMMjnI359iZCFw%2FauK19Kbu58yJWtEcQGA6xjWtf8YVKTvk3AHF2nnMUo3v5CCZJ03AKJIXquVNPZVPCgYX1nGXk4B1fsXWLjZT0G2ZHM1uznJWnVCX7cFfARkmrncJFzTPcl3dmr%2FIVH3szKxZKqtxc824YFHaaSDoyk8xUaeUwq%2FUx3lgo5odtnJCwUdoKg66FEQ%2BPe%2FDkZ9p8W0N6hK4pWK2lJGH2if%2Bl6E47bGXVv7dJhq%2F7%2FDrNb3z4WenIPnOrMTCyXD2jkKeVnpuY6bLblQwSfv3b8OxAuf7n4e%2FaCJUJWg69h%2Fb8VeVtyDE7hu1%2Fc%2FHUQHdJk7XXzerRyM4rOX1x4lHaRbzZGOGtssTENm%2BAQzLwfkxtP6BQ8Mtp4wRXndcsdbsAXrdOPDDG1O3JBjqkAW%2FWLXMTKUu56Lj6rjzC3g8eB%2BGEUSd2sVL0J780CyBEBSl4Ni1WjPGyxoMA%2FLdUFndW6OD3Iwnhg%2FyqS8%2BeZyDl0SUZ%2FNtXuQCpkxbsClHB9w20Nf%2BaaIzrArOugII98ZjFuUwH9wDfxKvYJvz2xP314kObqhu9z9Z3aVPhkjIEKrRJC15NOPngGtkqN4vJVjJzUTYWhN0fsKaLVeIuWDjwCWwV&X-Amz-Signature=1c1458dc55fca2231f848f2ecb5cc311bdea1832537b228741767fea721298a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




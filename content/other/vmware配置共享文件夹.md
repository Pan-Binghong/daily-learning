---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HRK5XNT%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3O%2BYbfmZRUMyuKa1drERT21tp9Id1SDXVfWm8JObxYQIgUDCApwlPh9qSoW2vPdYY4UEZsgEPJiUyCePwQq5gG64qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBqBPSLEwWxV2ojoKircAy1hUjCa8LaEJWb4PElX1KOMVaABUUf2xuaV%2BViwywuHcyJIuQ45PsfrgM%2FD8rMBOI9kWt2OFRMOqAkFInZD28lSbQRVDNST0TG1a0Vp%2BK3jLxMPKC28zWQjUvkzDqFLnUH0Rfo6gExbik%2FkrJLyvIOy0tptnaQXgyhQKqH2KAAj%2B3m3V%2BOksh0iReURkK6Hti4avj4RXefPd%2BftM1snGt%2B75NEBoHZBCZFv%2BdgRjC1YETEosobnW9qXT8M9hheyXFsmErrsnQse8nZK50Qjw%2B1fmULqUvO6kex%2FvGhdumfWZGkzBVHNrnXCCwxkvAOznJv6mr1GWg2z3wsSkUqEqJ9fxIn3PAMLlA6kV%2BW7ZmZWU7mI%2BuSmaeKnmoztsGt%2FchUjIcb4aLeWESGqHS1Ly1201HwXAgx1ikQ%2FQuor1cvwSOHBHO9cJ3EThi%2FCUVHU3DIgWayLk61FNllwcCOMeBJq0141WCUdFOralRYUm1gzyo17zVKnM5otuXkHsDHTPVu63zzFRyOJ7GYE3bPl40ubx6b%2F%2BaXICqrWcS0Mi5CT7zJhh7pPaDlWMQNOdXOuxd%2FD4KJ8Ylio0Sss14aIdP%2BUL9hw0TlH9jy5P5eEPlC%2FlIjF45hOXsd%2BbdG%2BMJjDqswGOqUB9GbAugvACLsf2pxa03CWiouA7Pq70Sz3KDecNdrLjC28XBmeATzxIZ%2BCvZFLjHC0dSN9we94vA2FkoysWeydogXlMJsW5uzIMsnpr70RDHMrMbNCnx%2Fyf1QukP2SvVr7uu2kHDzwCVccxvytb4AYci6j7fZklg%2FjEK6b7ifeNiNsMu28S1Nz8jcD6SDVNaREu4jadfAXK%2FHUjnGwHCTfvzPK1kNR&X-Amz-Signature=730cc90287ce6da449ba128683acd7089ceec01a2d8b117f5c7296d6c037616a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ADGSSJB%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCNt0i%2F6maz3cZFK%2BnSjN%2BuBsm4t3IaPtgomWqYYivcOQIhAMwAwcH4S33CibeBDxNx1095tOop6cI6DVGtMkbMkQAcKv8DCBQQABoMNjM3NDIzMTgzODA1IgzziVXo7YWFK6Wb57Uq3ANTSsEAfMcOp7ds0G%2FW8fZbi6j%2FySPdXs%2BYIDLNdGq6gVMH14N0W3qA9dDgSxNqK97K7Vn5Kwztqu%2Btymw401NpMfQGAYHoYwyS5JAZkNQ%2BPveRsOR0LQEoeseMn1pQHHcby25CAkSfYLWySJiyUzd9eMrBCugnn4KRCN49GHbJW2oTgL6eJ0K25U2BKJkzjwbk2u0Rn2lG8E6SGT99DfxtaA45%2BqsNNhM%2FNSt41OjoskE3MZN2mb2pSwyxuV4pM6%2FqoChR%2BQHrSQalrU2xlD8XpuINFj8ffhlE4yyOKknIbzR0ubT2srdpsN7h5e2z7ZzdXES%2BU4uRPNU9oqSeX5sxCxRx%2FXO2Htgp%2BNQmbOMi9qFGC%2BUgtRYm%2BUuHWmUpnNgBe3cI6lXVzTcqUQZoBvgRJwTJ8%2FIl3MEgrVXzrp0acEI%2BP72%2BJqYMBjvkjDd1Uxj7I74po3vKz%2BfLDdCqerjDX%2F48bTde0TnP20ddpx6O4BD8vbk9Le6iL4qe7pUOw3FWvmyWML9jZAspaEDlSK4tpKnkJ0dMUheatNbghUo%2BwDV8xptDETIQNsZ6oyG70VFBRkDIDb%2Bkjf%2Fxle7an8eOcVU%2FTYGn4Rc5aQQBSOOuGYq0yNPxvZ5poqERFjCWkJzLBjqkAf%2BS3yeFdK1WjTb9LDAW9JzrJdsZlPFPMPcTGGbVPwKHm6aJyDNAeMPchnNccbqUPiuRdJqJez2ShUr%2FOdmAr3xzMgGGeJ894ZnIAWieBlXSTgOCw%2FEXbEExy6WyyKqUNVWL3FoYMPFblEGrNfZtQ%2BvRgYBvuzh7%2BSoSq8d%2BH0IL4nAg%2BtcFSnKhDq9aOoNGgJi5hdkQosltk6jiNLJ5xA3Qn6pJ&X-Amz-Signature=35b90cdfb8767706c3ca99aeee4ab96c99861d8152fa7d4482d56db3f385a0ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




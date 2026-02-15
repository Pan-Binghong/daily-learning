---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGTH5JK7%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIE3J63x0pYO3T2rQMkidLxt%2FXBTvW29mW96l57etoYuHAiEA1wuv%2BGA%2Fs7bnKEFOoRv98cG3zCV7ReqthXAL49g2%2BYwq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDDKIFek%2Fq9LQO36nTCrcA%2FSzGzapVXDAkS0N9GV4hclKD73xDyRyPcmVpqbhclVPcA%2Bux9KAbk0ABcpSgTgQAgFIpfjcSHYQWbnFn38506302gOnvPwOB%2BLrRnwPpa6fh1ReYgFytJK%2FSPGdwiq6BN6TLrSxSNXs4lvBvuSqz88vQ6XAdzlboZNcRzPwnx3ZJMac5kmoueeYsvuzgCg2llpKPv94ICnXaxqSIzNUHve2jFzctWt6slS%2BmYPf2Jp0liepYi0e5uP6JCN4B9a1XiwGPmY%2FdhmwmYKYrAuuaydszcjQMsWy6QehAZpT7UldfPO8gNe6gHbISxN5mI3ciY4VX3YLiy%2FHb4J%2BBdQ7hEe9AkLH%2B3k4YV%2Fl5Dh56zumSgrRIc7I23vuRKksEpwK8XR1ewzPh%2B%2Fn%2BU%2FCAx6sfz9uzMNgONflvBFDWIOZ9J2SSczduBFew0dhVd6NUSQX7T5VYMJRh9xoMhvpGmLeaDclArXx0vXmS3az3k%2BT7Zg519gtWIlSorW5MKjobOuEUuu5dX00tkomJdDvvGstJJiqpmp4RlEpbykXcRyWE3aNdl5RDYMnYgHyEeLPGY8aYa0okcTjLErQy%2FmrLBVmavuvvW7%2FHUAbM4V8f7GuIeCRKZng8x5qVqLScqwRMIafxMwGOqUB8d203vuWz6UhQAB2fhT4EUZjmp%2B4Uyn8fVZAwt%2Fr8B%2BrP%2BviZmhfBo%2FnIqDEsTKS%2FiqfwStdk1o%2BICrPo%2Fmdopiz6x2nlFLNVL3APdAWw5IJ8qv%2FedTFpSGmaCQYu72tRP03C3N9DJ3V4z93hsOM71%2FfQDVWurQa37OattMfcv7phF89HfsXA83JYBd9Aw9yclV2FHSbTyVXHttyrca96AHbCzBp&X-Amz-Signature=cedd0edcf56761e05ac8236f8c528264036b4c64c734eb4ebbe028b8aed334bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




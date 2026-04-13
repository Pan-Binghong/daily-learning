---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T73LING3%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD91bNocPsCYtNMBwzMadtnz5HcN9XMI81VYLunxxEQmAIgE32wo8OI4CWgf2b19PKaHzWg0lEK6yp0ckBDFQt1lV0q%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDOfHseox%2BgiIJ%2FfX5CrcA%2F%2BGnzXiSfL3SA0a6nK3ESXd4GvHtkVkSjOxzTiREKIj0oG9WVCqYFgsI292h60KYWH878L8irg8KCkwv2Iht5%2FsN6hgP2ZeV2YEc5PF8nLn1VRv0S5M1P7An%2Flb%2FncwDolr5QLJ%2B7%2FU%2Fx8hyyPtXWqo6iP8ZUTOGplQeX%2FtDPt7SHPyqL5hbsXfdexj%2F%2FsjvnlSoTyp38oWMRQz1W4jt9DaqyjGXkGXAkIKRHMR5%2F5Qd5fJfw41Eqs41eNuCM6b3b0vMnt4wHQioZ5Zxy5r66ytjq%2F0nlORUyxEk4jOaFJvoQqnW3TZs0qzbGRxrMDJwZniabm%2FJvU3ILLiVXfuvn0m4mM8mg1yTo%2FLltk34XS0cJ%2BaSLybIOpdOlfzkveDRABvPD5OXaGQaaTLbHU1xBp6CyCYYqbJW%2Br6S6ClawlR3uUB%2FoqFexxPcVOUweVlw4y2YIyiAQf2mFceClNhnnzCdKCSTpei2V2RfhZ0p8sZZ98IWJSccY7nIFBwx1VlfrZuICZN2%2FdOXLK9%2FPj9Uks6YNj6f4GNA0RVTVUVP0xacnAVc%2BpU7Q598gMq2tuo7GxBlpzAx6yidItXKKokLD2NZhGeMflHW8Eobbm6mE37Vd%2BD%2BIkjqNby3aUEML%2Bw8c4GOqUBB3PKFaEdM%2BU%2FeNzRkpPZ5jP2L6W4MUXxUCcTsmpnPCIxbfwAbWv74zmYuXdKh6yvvIiOKo%2FusWHympFE4gVqTm50McaJq5rRLy9RLPJWQGi7whpEjvkCXtCbBbbViSRJHVICHtjHQrHhLnOJO8zZkyOeRgjZP65k6dkzgXXs7yjkoErR4mv9%2F6xSlmk0d97ViyU5oPG%2BcJ1Vhtu85qCsYfCb5rQN&X-Amz-Signature=132e673f97176b40aaf0b8dd3eeea3a249499edbb8669125185a43946e333196&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




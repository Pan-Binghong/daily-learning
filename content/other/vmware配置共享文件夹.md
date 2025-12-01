---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMPZATU2%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T031130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIH58efYxGzEiix3POwSIYsrk2zBA74vdrrGLeQ%2FSaQ%2BoAiEAsGjI8HG%2BbQUV5%2Bu%2B5G5%2FfoA6WdPEeEey4qLWH2tjCj4qiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG0HCzW88z%2FgVI%2B5nCrcAzUtOrV5cdcz7Gk1XnKespPRSRQEtbF7M6aeoT%2BUDQxdbXZKNsC0sJPDq1rGuYZDQ1mEpQe7pTe1ewOEjU3YLJFVwo5k5FYq8TxhFslxJH6XkfnxVxhA30SR%2F4C8OczmcbIL7I2aPJ0ucZJQSlNbyBwWl2xX2SxtbvZ%2FWNhrNh5NrcyoC3sqFpFS65qoV7l7LkfMafi3LSsFqnq6%2BZrUFQsl0l3bXiP1rI0juoZum7vMRVrmSKvZOmY7eG4LY4Sy4DvHgH%2FRe20C51HWLIu1Nd6d2BspTnO7iwndiyamZUra9oACWdv06zafUJYIrKfFJbL51PXiXmrNfCK63%2B8ur89TAd%2Fzov52jy8C%2BoBtCIlRzRRuqfcf3%2FNi%2B%2B%2BzGRq%2BBgFbD38oizf7%2BWgtYaiKqXX%2FM%2FdSpJA1MYhdK8vZ6dN8y1K%2B%2Fg5CUFjspFceyUUkz2I%2Bx%2Bvhqji6JXoUz833XtPpidd0PnuywzAYfRLPdFqflgCA9rHff1YaRfnwRMNbgeFvW9b9Km%2FEiv%2F8LMQgfVeYleblYcaCRximhAB0KN%2BzUGGJtquLF81otAJlWFjOWa7tosuzaQ4LX%2Ff7ovPCpUd7ndSxdwkR4p0GmmaqqYOLOsDtIkYeO5yAk91%2BMKD9sskGOqUB8lvhKrUWwaUlYX2bzWMrCdgMR20dKp5%2Fz2K9Jcsn6xP%2F05G4zsUYBV9Ki8hP9NqMt2IKuXVdMQj7J80AgwMKs%2BvIO9iSVOYaeqU9OA8uSNqZVKzRfqoitCMGNT7PHncoUU4WC%2Fnq6bvOorzuesUk3aZ%2BS3rkL8s8z%2B0mFtE7UJv2oAAw7Cr4IYGPNiXuAYhf8P%2FQ7x4p6%2B8efjUHDoJlr7fiDVuB&X-Amz-Signature=0d07ec5691a825e3fab3f5b07d682a38295c3ba82c23f40f9ac86e15b9b157f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




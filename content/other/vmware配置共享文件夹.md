---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MOPTRML%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHh7qp9qyjyUgN8jhYEOZdhNqn4Mrd72qWAz%2B544RcKVAiBEf56oPKivIxPxQyvP%2B4yZB5xmsZUtCQ0bZlPrj87hEyqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWN%2Fpgg3favxdokpIKtwD%2BxWOXrEvNTjHHr%2FUC9exl0MoYHOg9cDwSTbvmDDO3%2B3scjZD%2FUnyD%2BlyzaX0KUS0Lo3xHeop24%2FzgRSsUKU9G64K0sA%2Fi2xwYmtV9eQXd%2FqyEi%2BOG3QpE1csElb9RSCuozmf81IjcvElDYHxLAAJ2WwDeldqRq9ateRf1eoASonZzXxVwx6FOOGxDC%2F79AcV073yGST%2FjhVDqzWdTgFHcNt3sHOHhr66%2FrpUuAjqX8%2B1fgIc29zQ5f4iPHtwMT%2BO5mssslM0Fe0x0Npf4wnMbskOrk5fN8K6sqi%2FLr%2BJ1LtIU1%2FZYj8k4erIf0ewY3tc1D3wNZZXFJLBc%2BubFMgQC4ltKLiP4N3d3EGb0x1S6Nc6j1eEZF6iFGJonjOmTSUUEMOYJZK8QAwupFkG4EjfnoAXoWgAMW7kiqEASlFlwnQct0GkdcD254yhS05exgOamGki7kkSmLWcx90Jtit3%2FkefzFEfGNW2G3cdy8tCN%2FR0m9CwAtSlcW3UKaZvEVeFd8HvHMZSDneQ019d%2FYLkqoJCHkDzolzR2CQmj2s0cxXISVO4H%2FFvwN%2B5hZ%2Fi7D2GMBVKTOeff9JlYQVq6x%2B5V%2FMBsN8iTFssQhLm8C%2B%2FB7xaIyKMELUiLE4HNBswgsyvzAY6pgHscbw9DVJcO8b0Z7RikRdfG%2B7Ml%2B6GYHT0b8nYkQAV4wCf0wTak0SD5xigqZOzU6ZSu5Zt8jeC1DccTquEW7mbTyGaDuPjL2%2FxgzQvQS7mtwuptYrNDgPHwW%2FlIqnqVizXTknKFKdy5kR2MLtZwzJhq2bkKiNW3Y9AzFTjFhX6KRqBCMlpeJCdm%2Fj2nQ8g9G%2BB4LqulFrSAbmn0s2ZqRl%2BKJFoJ4sP&X-Amz-Signature=0f58afabc426bdf10eb566d62e6cb1f418a18a4f290669658633e2f59ef5a2b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




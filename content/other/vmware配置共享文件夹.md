---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6BCYEHE%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIGGBaQG2%2BYWKCR7z%2BZ00lOEIMHcS46v%2BgRJkz57cvh8gAiEA8onyw%2FuCAXfpWqudXGAhXZNKDRd3%2FMhj%2BKBsdXk3WFoq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDEbcK0jMthSBUyGk4CrcA09dRk%2Fd6o7nahBoHRVjcOvLA60rSAdU9IhtuZ1NpQS9vt2s2sAswdzOjpViPd8ydGeVlcTT9hSfYme7hMvhH%2F0cgWLILfUseXr8LBeIwOKyaw2eo2QEoEiP30Wi9NeBk1xoCIOpow6u%2FcjKi7lGOd3qm8wZYTiPTqxeE%2FkfKP4HVcaAhTfUh7qSu6FjSBC1IQb64SkZO9xHz4F0iTQlPwFV0XheQPVOgI03XculdZQJj1K8DtXTjqn3BLc%2BgNmKa1DnawZcCl6Z0nQC8oatGJQDTnznHIb%2B5Qik5FlIhZGEMIHfrxZDXG1ihiZPTOljApxGzlawwSf9zUMstJMl7YmkLjqSvxPT8JonHvjYlwnkCitDfksN7oJVpQz2s7QjAD8FYzvLhD0VZoSj53LbScs87%2FpuXHFaAlylmE9TxO6ADOxQiFvbEiURkeR%2B1dBIjuHTkzEQhRH%2FrGVVvpAxUHp7BmVU6yTVm9vHn2VfKa%2BGOLA8YRw9%2FnCOqcJUzklM0HkgJlw9lRJNvjwusU2%2BPx2GZ6F1vyoYNcJ%2B7m8f%2FVvJddl8lTVMLJdTFUt5KtTV%2BEOwyal9efTHcOqNEkbpWQhrpeWOwobtGKNNsZmuAlSjBmZ%2BLcVRKHjHQ1k6MJD9p8oGOqUBE1nIfBuoxy%2BdZNkYKggsu9yg3%2FeqDD1GOmcw7bukRDxo0sCW0I8Yy%2BrltRj2EfVO%2FSfIezgR8QMs0uiCNEv%2BmZg0NOhwEHHsxvNVN0B7F%2BBWco8takM7Ms0sajeaxl1hEwgmvLVnb1amEyid8VOGjRmxcQTnuORDTwRjKgtrDlsJ%2FAiCGwvWbiMyCkdodOJJa79w1OXI6T4SGtIMmJiy%2B0wQcFgr&X-Amz-Signature=5a8713e27b647df1873b2eb23ba2ed1667e5e829299c265a8835a28f7fbb6aa2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




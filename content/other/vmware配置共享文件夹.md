---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGKE2OSB%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQCM11q3QJC%2FrIhQ2RerQNhKZSDkrUjR9cZxc5MvjyX5fwIgGFoHcyKGvrsl5KToTcV%2BduTOND5CCQO29HAOQK4wQIwq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDF2ZwO6m3TDW0Pb1TyrcA5D824UArSm6l1gYiP8eQuCKlFHuI2QC6%2BgrmmI5gFmqqcA4dMeeWY4kD4AC1YuL8VX3bC81cct28zv0blJEZhcXteiOty3xHp31XmJRta7im7qtUy6NXOmTW2UGE8xtAQeLPqRlGgKPieim0mob3HzsKJsO%2FcBKUlawIDDMoBkOHLeCJ2n%2BCf8q31eTHXb1QP%2FvdnNS8c2qM0H5Ue8mM0qtgUwoUURx6BU1npJIgalX0Zc%2FjLJ7wa5UdjrFVSHdTZ2cppOpJ%2F7beeOqRblPUwlQOPo4gqc4Wkr73Z9ViIqdlzxRlZ9%2FbZIYDW%2Bazc%2BxbjHzxnm%2FPOtXw66OHgfEZEA0FroT1JtZ8sD6NzRIVHGn7QzcsMxmmVv0Y08W%2FtkycPyTDeB9Fx0Tj55fDu5wHCSdq0M%2FauF3yE5HpDw6ck1xFZoWNl%2Fx2pUi4j%2FQ16zRaFQF8s2KlnRmkpWhwGVyON38EgzENm6F2ym3Hdniv8PwkoW0%2B0lfqB4jXVBN6%2FhrU9FeYv3B4hnLo3FsTPJ6FS4SYEEFsCKrY0ugK5PzOyCWDEdhohlpzLatdh4aY522ZKqTThVv%2FOxHEcdYno%2F97J51PlwpWmoMe%2BxhKxXdC4vguVC7V1d%2B8hJlIrrLMNzNp84GOqUBiapXwHNwEEDKmZ%2FE8ShCw1%2F4%2B%2BT6q8JLxq9dNSkN%2Fyu%2BFs4DN8CoAKStCofPqc6M7Ktad1kf1ZBoAixLzObdXqoEYHj4rjMZp2BOTLB4tXpDMt5iuxhcTfUIJIha25%2FM1a2%2BvlbVEVBBfp9bRPC4E2uLCQ%2B373nBy%2BU5rbMucZ%2BIKXT%2BiDCPzVUov0ug0%2FXuu%2FCz%2FWotW824yo67sIbE4CJFrDCE&X-Amz-Signature=a728e2ec17706d45e3f09bee1607e9bcfcb3b52f56c6c73d2bb06cbec613d725&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




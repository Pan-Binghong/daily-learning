---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IK6LGCW%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQy07u3bWXUoA9%2BjA6ECeCD7WMYa5CZGfPKxtUFxzoRgIgOZ3pIrN%2Bm5eDc3iZ59CyWdAqkcmzp6kueLi6i5bjt%2BIq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDFSmNg4JMr2oRujJPircAz%2F7lP%2Bd91mMF105%2ByLsGpBge7ljEPxBmxZ8OzuTTZVGtiX9oQJXCzjmu5Fyezk9eseYdr7YIldN60knvCv0bvWQLWiOF2432F11IZaGmaWqV1BAkHdvBKniwnH%2FRexbOidqYcJXoTYAcB5L%2FPSNK05eqMNPPJex9ydJ28tId0y3NvmiiIFTwu%2FdYNhSvHS6uLNleLS8KPhHixjwzlbXvOh0dRUKfWdA7RiuzRVrqqVf%2B0pT7jxH2LOqyuP7SQmpWD%2BtPLw6JVOqHsDFemsDGPkTX2D65dUVGBVBsY9Z0PmU40K1pkYAOJ4LdKdtBww4%2BA66fFuLXdIYF5aVHmIvA8GckqQ%2B%2BlVuKXhJoI5Kt%2F7qwPsRMKEKtRgab2xjYIudZ609GTxkgEacaKUK51DSb8upHgNxwdVlxej46rkZQxaYzTMX0mdJmN6qFimCIrx1mFj0UiONRvQprlBPHz0BAbQxycTne%2BY%2FEQcII6vBRZiMUmRrfveLNERfiEKNhXWskxRjmOAcwmQ%2FFuJ2tQp%2FTBIGB4DEFX0dU4P4qUxLXUjxIg4t%2Bx1XGKrWajkD9JxqXqgqlKIJTB4rRMVdhzo4TW73qm14W4PJrnJ1%2Fpsg1fXwwA7T9f1JBlzg8dWdMNztvM4GOqUBqSxdTcBbn2N4YaUTd1BdOGdDOviWXthUHW0fztuLpBzNYImZ1PGyFHojeDKxS5Bn8KtRh%2BVKu%2BMGcEHjvH7eqz41fI5K3jVXZWMTjhpOpgyfZW6or4LhtaFGn39E4skhMWXFXi4O4LjcltZpbshUrHbdxN%2BotBqOwmGCiM0VCsOJicmP9Th3kNrFpZtH516Pf9axFOxbfP5a%2B63Sf7CJBgxLhZBx&X-Amz-Signature=cc0fedbc93d0f32d4e9f908090e8eee7f8aa8f68f919e52cad3521005ff6d331&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




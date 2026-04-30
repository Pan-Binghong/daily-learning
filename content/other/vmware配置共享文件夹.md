---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTCVERBY%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCICvV9CFeQl3qXYwmGORI8R5ynftTS2q1Gm%2Fc%2F2V3ixUpAiEAodsJVGt1WejAqEE5cxQsMIw7mdsX8Itw2F30zRPqV0oq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDDDQvXfrRFwF7oF3aCrcA13POgRAfG1QFJEGW1gN%2F3Ris3cZ6kIK4%2B5JJvvAjU2VKhIbidFW8jEkf%2FxaxXKQCUH8LvKH%2BhsfnVLMkm1jsbp15VJqKr%2FFHqKoqMfvHCePKzfl%2Fiv74EwY%2FMFapysBkcirjR6rmuYDbgbcMENjOpsWgj%2FAYCknDoI6Dwt1Ijx3xNOUGy5SD14xxghRCgYhU5l0lKdPlkN%2FqWlKWmNAwLEonqAayA84Msvyz4UZDJoZVZzt4Ao%2B76jGie45wyUrK4xfotrpsY7ekehg71l8Vs4hAXdV5aBZsFW7kqE%2BpexqwDr709vE28i25%2BEIwyR43Da6%2BX7lClfNQtuzxsgMXPCeyySEevwps7yBL2a4arlnHfdO8Ze7PmsNO23I7TYCDz0t1zySCpVbh%2BAGogYcOP2HhnCx9UrLTTIo1fWUXDny00ilZeXbZiEe%2BURyKwGOBMnYpy41uvXYlBmUDVSlniU%2FUsqUiunsGG%2B3YeA2OH5YrNBNsH2mjRNXE25X2oDUT1aeap%2B7iQyI7VFuASksOqLpvP%2BomzJLG7KAAbs%2FX%2FvI%2BLIPgfotiHbgLNxUPBPh79QHSAzUg6rzdYRw5%2BPJU5Zj2IP3OFqJYSNkvbXs1ReLCJjr2LGzuDzZkDyxMP2bzM8GOqUB9wfMcQzc%2FkbdlAowSA6Q4I1g5s5DA5Cb5a1mKhuKR%2BaI7Ddal1Fo7tX4ewmZInn8Y8SSA27OjktVjGOMI7%2FtvsQBrCSXLEHPuRzTpz4FpuuyrP74ke%2B7%2FGZ32WKEE0MQ1M4OCeKs7rA8fqgPOjZNR8ROxook8e17og5DdS7rrpO%2FLPOYtDL3GWPyAUKbzjreVzLy%2FEpeZOE5uFlFmOY8M9ZXQmMZ&X-Amz-Signature=1d56b438310d78ed99083502a1ea54298754c38b69ef3bc4413622585c04f764&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




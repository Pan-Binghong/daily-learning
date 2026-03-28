---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623A6VJKT%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQC3XdU4rtEvNl3%2Fi2A2nakIbr1GdtOoPnXunippbHln9wIgJIaFvOJN5Z7n8yzFGHzaaisK4vkTSuq3rpimKVIxJrIqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLqCXftuGDjRzf61oSrcAxqWjuMsp3GDjbmDkvZds4yT%2B7NQma3auer8NBLk37VIwD8RJ5D0eRdZyZRxuhJnQitCNfRhbpDKK7hjrq21J%2B2bTDdmj2QsdJ6zeq7w2Yl4KnA7UrdWptiX0CFFFuEBr0Y173g2wJZAlTMQvefx7U4iscU00NdpoCI8vc4Gkrg25HmdktUzd8Dfb7VPze%2FplaRoeyz8DYZXc%2B19eQB3NfH54iX9HYhcK526VRSlk2Rl7eeHy142c6rvWsy%2BgRzIIQIP6tPBGQkNvdTZTZx%2BGWky9lIIfnY%2FxFHmA7ws%2BH6q31YRz8KubiZevMuXGhKDK8IaxoipoL%2Bb9RFx4DXjuAjc0q46Iiv7LK%2BOyHzh3Pd4vnn3CMTYLaBiI3%2FPzUJEXDqVUtK6W0p3TVrzZ8%2BwDreOdAcf1%2FxC0lYzC6rZ6OjV8ft4l0C1BVrus3qi4Y73ZNWsvUnibsI2PPODsGG5fa1%2BCg86yixzQ8Ejr%2F%2FZDu48Kcn7AtrbiVcMv84KJWrA6kg7A4gaUMXyTsiHQMtgpwg6eHdK3HX3fSrIVszuLxoIs0FGKYianYKfRFCPhjVkjY5QwWqXBS71Ge7y94dMGa30T2d5re92n49VIhxXEmjHOqFkOzXdiEKHJqSXMNnsnM4GOqUBFw8qJbHo1aRrn12VqmwzNHpEGyaEcZ8Y1aLxSPV8QLiO0gpTL63NfwZORQTgn2NN8xF8ZsDYlBbwfTJA0VNJrTd85LrAgXgdTMTjRlK5JZ5kbdsLkow4Y0sjiyDY0YeD2oBxqTGDRaF92PtDxcWMFIN7K448Svg8fUMU4946gZuYmpgQsMoLcgFBLSvZFeWB0JdkFGC%2BkKgoavyqykIBeuXoNPmr&X-Amz-Signature=e0d4c19207a43307fbe4c341f1c31874e32a9cb40075290f036b9404c6f456be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




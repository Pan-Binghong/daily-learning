---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2UQJVKL%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIBcoWD%2FCYruVsHCnRfFolYwZ6CTTdT1SiZk8LsVbY3hoAiEA6XIR54wUv9I3HqP%2FipclVF%2Bb%2B9O5FKsYGMXlFmVzCdUq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDAhSMl3nnaE6nkRSoircA59YoEjMOfKrHOYTTBU23M7rUpnKsEtQODh48iHIjyd4txuiSOrF1m7zIQK2MOeDFVvDm%2BH%2BbhnuZt%2BmgP6E8s0dMwJQUigJJ7iaoAG2Srl2DjQgLuXw9c%2F2j1JVUsW9uIHAJcJfeTCJQjPltxUigBEyapm9NaZLchQTsC%2FGEdwoPaKqHmYT7GnuwW3Of0t55xARkR84Ya4cWK96kOyN9VOtjLSvbqBM461mzi7d6aMHdDyBwWQ7c3%2FKuNOh7hwmlqHdCoqm8QOWCtbSt9Qpjs3%2BVcrZXYg0RMXYe1ODJKJqxg7JL8zVuEKrr69LzVE15789eWqVd50mo3aze98hww3V6Nxe6fQjFUfWASU%2FYKLDVEdhxyT2HY%2B4QmZawVcKLqoswyroNAEt7aLzX7ZA%2F6jcQoE%2Flfn8aEqOgI4bmkxn9V3w8BExg5UyuSqk5uDbzEhfXcM7ZVUPJJvAR%2FVFP2xg%2F%2BcgcARcTgZ45kXN4MtDXdgJaCGygHgRljwKsUpe6CJvm1z5RS8EKF0YTa55CoFJ1VdthPPUMsuu1yTsp4tfs%2BPur69dx11Ee0k8gbNcdpo9bY6cR0eg%2FCEymWcJabtPpEMJgV5a1dVFkbgvOO9wV%2FjW9TAUzuGMdlzvMN%2F9uM0GOqUBEWfmDghblKc9byTpi7HUSwIkuO2N2Nif%2BVRoJsrHHLbN%2BjZBlivz%2Bzex0ma55bh2IViltX2s9CFeWXuLWlenLUT0DQsV609KruQpoMltTBu7VL5JS9DIEEkvd%2BrwAszGgGN5rg5EK46geTUExWOOWril9TVd7FYWJiG4Xa8Y67mojXP4AXh9225DL%2Fn8TMRGQRLKhNgJBt%2BPFiQX5noazc16dzvS&X-Amz-Signature=7ec4dbcc8ac515a2aa6a6b2ed8d78b62a20c68404dd17edf4134ede610b512f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




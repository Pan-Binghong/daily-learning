---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RVO3SUM%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQDVLH65rC3ZHAyObjrvi0jmhpY3nZ2%2FkwlfqTCJNhyb6AIgKceoi%2BuFCa4UUm3rLVG4cUAau%2FK21Q429c5SVTliXuEqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAXSgDO6%2ByUPryGdLircA11fGWPeg2oXGxlYBrgIAgm1XgvktyPf%2FeIbMspZUwfgzkdY1DlyXDsBiAZ1BTB39FCd%2F%2Bm5i6cHDbXHNOs9Z7e5vC1eaR8GtLwm1vyEyIA%2Bik6aHRVM%2B4CylrNZx%2FI0yDqVa7K8cZW0L7FAQlhr3czTo%2BIfnnzHvRhe%2F%2BZgUWGuyuW4VNbQpjqqgQzw9jO6NNz9Upv4bokGWZEl4xf0NQOOo23UO2xZ2YHLSpLWAy2XZBVIWTFvosTzMvpxm1PTE3FssGaUtbnTIYjWpQcLFaGqAS2HV50XeQkOcfW24LG57k1Ztf8zAY6kPHIUK6vMlANO5WC5XPH4IAwChpSF4V5kDcDNUi602qdJMAVxfKdBJlrYhvtSxslP71EUX9bmMDq1lJrFVMCP50YryHzh5T4S9hXY8XkRGMFhnm%2FHjUsP6tP8Xhd7AVDFgQ4U9vY%2BHLfoJUsUTN3V%2FER3qdVsW%2FEYQf9cyXm9S0cfVyVMR907j6%2FJtRzfF4irfxS8osLbD4XwKw9ZaoP1gq64Sia24mUr0o122GwIWSXakOpw%2BnaGiXqihESCZF27c1XIvYml5YBUK32leYEla4uyOmwqgE01lvSM2n5CwBUpPNo7gSCL4UssiQ4MZFj7RApnMMPL9MgGOqUBOh6oPpTr38dLpUNGXIEMw8YE1lZesF01VsO28FrVq%2FhCyNIBApq%2FLo37dc5GxQ5SB989dXmWhEiiY8aW6dNDqvZ4S41Mc1yvKS6rSyrkezAL8uD0aKGySbEChXKiF34t6Zl3kD47O3eWZFWYCc7MGDaVrtUnivkSLZl7w7OLvKqLoA3VgFx2Ra05OU2jHLM1z3im7GuAUKcQ2FLLxOtNL8j3zSax&X-Amz-Signature=b9e509c376c48ca3c8834df4ac1c514ff41a1ce1136fad669434823f93a50b6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUJJAIVT%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQC%2FoT92TwB%2Fnzh%2FnYU2L7FwWcyzssBfkynm4ziyvt1tWQIgGWr74CT%2BQl9v%2FWXAh%2Bl7DJTuIMN7tNk%2Fw9tsXarysIQq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDPI2vIuk05qmyZofyCrcAxa42%2F%2FtCK8JawMHb9GV%2BNrF6vBRGzJY9WxPmqap80rg%2FIDiZuz1HKYy3AYK9UNGAMLFHfV6uO%2BPT8W2%2Fbh%2BBevJ2cRsvBfTDUr8eFP5L%2BWb%2FNGXN%2FGIJNe1okR7ehznlO5sTwsS6sgYS7i%2F9axcT6NLCzx5FTjj3qBzV2utOnBxn9Jh3inqz0o00nQkpa%2Fgx8dr4Fh5bZl%2FGaxyUIuhFOqQOJVRGqM7kOmGDEKLgsOu6q8HfWYLHcmdXiXZxXW4iFbJ8NsJAaKuMBIXc5JQYttriFHYMMvnlCGqgXoTHoDJlEQQoyLuf2iPJyv1Hn65qqgoorFwbkk%2BctyWFfgJC0RGpu73vWurH6Pn0C2%2FaR%2F2%2FfmCf32JteZFVk4YlQvnVQgVaaAhrkBQtn1p%2BgzEKnQv5OUR0IBb5BaIgwasH3uqohouCmzhPFdpqIBZhXK7I2Ht6aQ017PPnsxAmpBVHnIXD14E2eVzP99V4LAJ%2FfnPP9%2FmUnF9zmB6FJi6WDGDnEADluEU9KJ%2B5DtQd8B%2Bzn3%2FPhZMFZkKPd3WyPwcAoNIAUA%2BcFPc5KVrZQ7onoTTw4wyOT7dQOFVWrDEFqywR7MmlctDSen82iah45FRYBWsVV0U7dgoJ7aKNaAUMLO%2Fos4GOqUB6rwAXYQyALNsnNajvaXUd%2BI1O6KWRBAEm2RABP2EBpLtbDv1XPZXKXZMarGxxa%2F4od2pyrdcnWId5y1ZetuQywVIPU8hCqkyCr8uztkYaGpNhFhUlhoCDycO3YTVr%2Bz%2BHbhBZRXGV1n4UFuTY6GRzPIsKU1s2Q1epCfNuHi0zK%2B5%2BqZBGvpjI7WXteVEHhesTbwm9XjYpriw0Cf4Av9STrxYgdRT&X-Amz-Signature=e67581bb28ced307eb14b706dbf2d2eaa925dc2817dd68355061ad7f61e3de3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EEICQBA%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfgOzv6H2IdByaVOMBN1EU%2FI39aDlFkd0K6XJGdRimQgIgFOzVBytZOECySQuXq41fYXWiWqs8vQukgp8J%2FWI0GBkqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAWtJGfGIjzsszJifircA6vmy7TGoGohc4O1CF3MQdtMkzEgpVpQqt82ddtAK1l15x5Lcz4V5lUB286vK%2BMtkvsjZVpdvLXoQFXrYWieLQZLwR3b3LgfJQkwbPzso%2BqnwxxcFHOgP2haXo2qBip6NVY%2Bqb%2BJYfeSyYi0sas3HtRi0KEIOuWuleRj4U6T7yui%2BmvA%2BQatufep6RCbpmEMGGL6wH7b9zl1OeI9IcrV%2Bfru0sJWpZRt3xoqg6eZd1Ig3l8WiYz%2FmhP7IDQo8wmzm0AqFY6OT2Ltxp5xtX5wlW7cynP5pf8iOVzstWKRj8mC06e7XE0RonbOfvIveUbxLm0NwbSuRFJBjqVt70jCp0p88VJ8rVRvI%2Fe%2B%2B8fnOgRZR5ppdpdBlw0QhKXsKF4eETv7PBPCjHu2dRACnh%2Fqctd3XEr3Ee20CV797rtJTOYcVrmZJG5Ao8fH%2F4e03HMaAwD3wUULx%2BPA6DxtXE7hlC63CLVSwx1dcCXkgcWAwmoVEQRSzTkbwMcLIzBjn%2FOiPwQA5GxVfqVokFPUhf9l1iMPPsQQY031kC4vmOKqmxtLaGe7VNrxUZze33P2MnVh200kFSzZ13piWdd%2BvRRWjHCtAhV5g%2FauZqsIz2O4XgpWrbFkVtyatdHJw184MMe95MwGOqUBh2IsVfhD6XZ%2FI21w4N%2Fnjdvmt4BO8%2Fp7whqDa6jfRJX0GtyGXpwXFLb%2BnsjyP%2FPPAAagS8AAaISGn9b7F87xCuheTotvIy4Out38174tVQD1XgFwUK6oV8mYUsWs5cI4oZFuucj1dQr1ldjP%2Fm3BJ82RrL0X21i6pk7XrLlZpkzVUVppfWaX%2BRtYFcDKHhFd57RRd4A2XWEs4m5KUysWLErdXk1G&X-Amz-Signature=bf0d936f0449a5aa824fc82877478e660b5aa5a191f916e69bd1285301a67443&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




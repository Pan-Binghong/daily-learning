---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663V5EAT3J%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB1bh%2FiuQ6iL3I0Xlf6c9QE%2Bj%2BNplfI6aK5ExzTUgnnHAiEA%2BaegqWJdpLkavoJT6iElPc32QAvnZwYFZy%2BKqdVhzHQqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGCr5cmArqTZd39ScyrcA54EZbdHZFnb4WHkQwILSQQ%2BwK%2BriB2U1MV%2F1GEfjWmdsh9F3WH17AheN%2BAeDvuxP96TvgX2NtPotRnZ9B6nmKTrj7iE20TVpdjAJay%2BqN3X2qP%2FYmZnpufNi35oQrcF%2FlZIiBvIozHS48Knhm9wE4jDhyA980AGvOkwoMoRYeFui2XmubrWinKPm4BGXZLUZdsmG5aZbZD%2B7jb7%2F9457%2FJVd25M0ew7NH53tkbs4f2nepRndsfaPLlVstx20En1srDRFl%2B8pORlrP7BOlBnkS%2BI2drHdhaLNwCHUv5iOCxTb8TEMjD0SRJtYKlX1WXUPTBlQZ0ZmOmiYi%2Bdae8nFy4M9U803bUPTYCmoyDkCgYgQ6F3XF%2BTiPmcVHmzXAK9bATLEv%2F%2FtCe0nxzUvQEIWJBxd7EEY6aLzEel1e1pfoHOSAMOGyEb0XLrQT%2BdNjlPyPK5Zw%2FAL3n7BT7muotJ%2F8Rf8OXOrSfflJsdWsji77WPWu2aFZQb1zOJydERv5ycn2iduUg4nf3mgM904F7L2hJ1odXg0nCHGCIgxyFCv6eftnJiklvUXe03ZBE37W%2BqMkL7TmZKJATDHXT5VtyEViMo6xk1LAdLz%2FhIYOK7waDfCslL263kIiQ0rhyzMNfxsM8GOqUB6IUcuxC8IrU0Q%2B0O4n8Y3FA8a5trto7PS5SWF5L%2FvjT7p20ikUfbTs2oYAc3pqIlqltBRj4XocsbsAHJdXx74PW8JRzxeWPHbMmxIXCQvz%2Bsz6dhiwMfOBgwMhXUaLj1MXZLSZRBnPrDzVq4XBhBGraeNsOOMicOR1uhJe0p9uSCeeYQOGotAokG%2BuwgJ6ecvZXww5wxLTwND5%2BChny7s8P8D51g&X-Amz-Signature=958201c35acdd8e60feef892d07912a8fef40abe66a80f7ac2501da9d9d8aa51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




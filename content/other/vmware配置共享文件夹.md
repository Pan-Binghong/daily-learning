---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIAHID5C%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T034042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIGkr7Pnf68NNHT7CZgFroTeUVU9hzCRC0ASPyIFSjdHTAiAg9A4AmtmusRtd3EYyyxlZsr3v4mwy80ldAi7YPdE2ZSr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMcrQLv0XQCvPPvFzLKtwDp8JFMJ9dg8aH44D9DSnK8%2FT69Dalk1v8XnB7tzaizxdANv2sI5dYaRye%2FpyuaWmbydxdwZj1z5%2BBd42WSMATn2%2Bj%2FH1PNJW%2FTxBeLLgN4dqAXLznLCeb42fDurU0RBDxLwQSHx3ebY5IfsRwzibgaoLCApRvczqCYfcvqiY%2Bo2jYuu1Wub9ObjE%2BvszG0Bk2mhJMcDwjRZ4nNDRrZy2OxIvqy6Bz8t4EgWacNlIdriAS5f6Q5VwTYuPwdlZ8mBRm6ktC86OqO2Joa7ixCihqmI%2BoSnQeDfcF7sZxxWV9pvX%2B%2BDFU%2FSiVXhVB8D5fAZEcFXJXgCi5No%2F%2BaefiMi5M4LPwIO5S1Gcw2ePPvp%2FlGdn83zkCgCZi3H%2F7bl1cRnik8saAVgMf%2FHkwxBYOyfD%2Bd4bbTFF0Liw%2Bho3KSB21NyFanhfbGvm9mWb5gyRNeahCQfJULZQAZwQC32VKjtHZxxJnCEmgivJ%2Frh%2Fh0pRcim%2FBYv8kHKwIxLT5FTbKY9F9N0vXIZVGaBUEqnTY24hApMxSY5n7LpX5si6n7BRkMuvoW3UriUqBWpQQ6WZ%2FUoNcaufo2wozYzuFyAkaWuXXJFDI8GRYJoYtbm%2FAJQsJld4JlW1DdNA8t3VgQNIws%2BnmzgY6pgEnvhOhSwQhV%2FrVKHomDBe8Do47bmXLHXIBMVp6gyG%2Fuyhv9OIoGgkIq7j%2FUybwWaCc5kZqqs6mqHr%2FAQx0ttk1ElscMYv%2FkZ1wCU0A%2Bu9z%2FGa5nyPR0VBnrlQHFO41sr8oRL6Tl%2BtPp1GsBtbnS1FStIauBP9kJBFCfGpFFNOBmNkD%2FHVMZfuHtZTpRM8GPuFPBciBWuWumpqizVJdmNGyA5z3OUKD&X-Amz-Signature=bf5f68848e3c9ed526aea71a59c68b86e105c95e78acd64c6d23cd2b44386513&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




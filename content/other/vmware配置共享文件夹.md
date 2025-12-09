---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQEF7KEW%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaWoIrXVlf9X%2F%2FsYQE0jiy58onWYN59x%2F7yfUgkCd%2BXwIgOBNt5q96Xun%2FE3AGlXEj3EyoPSOJl8CIdYH3%2BtvEBOYqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMzy6RdZB654NH2LfyrcA0HxQC5NlxDU6a8kaQZmtYyzE0xU9bcIoawGj91ico6c4aERMqyBIGo7%2Fr0s1%2BALbMT1qrc1uNycHdIWTug%2BCijaQyroysuop5B9NAgTMDQHXUNOta0fIAxjLBWl9P90Qd7ZvceuiKoW8fCYxcG9B%2B2jtpmeBzgwz80r%2FIQw%2F760g68ay2UHa7xYPM3UkXQa1TPg0mFz9CSTMX9c0Zuy7Oel%2FxHLnm%2BZ2R1j1%2Fc%2FKlB1bHGLRUYXyYSiG22ii7nTN4Rb8aZR4%2FKo6ZB1EAfEWG6fF18SktsxqrdUsCZVyuQsVoZjo%2BsqxX9Ld1RcDEiPT7QU8vVyJh6K9uim0YK5A%2FzdGO%2FOp8qPDNttcKrnzO7njA0j5BnynqPJcT7fItAw90rPieyLdgTX5EeClDk74K440eiC3OsLOSSvAJRvsO5Rp0gX0JWC%2Ft1uUj4F9xHnoa%2FQh4kZLY%2BSIHYlSQm%2FJK3tsEOaW0IDI328r3JfqW7KrPMTjit%2Fcvut%2F5KCv7fevauWlSQdhadJ%2B4jrLBU%2FXFvlKBQxyJkZeYYb1WePqHHeuwpN8Arg5osVPgXVvegELaRXPy1m%2F4DMDlZzXTpISy3wCjFdC82VAys6NHCYRGlovSeBQkhQEzcFqQolMMCO3skGOqUB1ILXza8ZSuzH9Cgw3RU9oT8uPMu%2BG2N56FWMg1%2Bl%2FFm75touur%2FM%2F%2B6z1kzzbdNqzXDL8I0sDi3AYshvAY2%2FUPQ6sis69Aq66aVCzYrsdjEaIUL%2Bhvzkp8%2BywGhDUe5yR70VLwwptv7KEnpo%2B3CNyos2sdeDdhID8kTspHz8Sy%2BhCDNDlMg6S1qz1QOS%2BcfzjqLPPUdgGIG%2BzD4tyCzoeSpHLYrB&X-Amz-Signature=ee44948efbd37f2c831bc622b41079bda7bc2a1fffef1e282a6c2d44c830280b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




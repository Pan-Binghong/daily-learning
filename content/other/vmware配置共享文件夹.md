---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEGUXWBP%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQDdjLc6xYwyoAZaff2I6TPpa2Sug5QP8yLgM9ex5DozTgIhAK6WpzWStJc2Ve3vfQEOsA0CmxZ%2FZC2sJj%2Fh1XKFAmSTKv8DCCwQABoMNjM3NDIzMTgzODA1Igz1f8ihU1h0jMr5nwwq3APDz0NJ3TBB5NAPF7hVsgzX2W%2FAN7Oci1aERpCRobA99Zg0mdDdVg7dDpmV%2B9Dr39udlPGqypXzWVtZ5%2F0%2F24EKFmlx6s6BqLLEgmw9XBqJxGMgkwpeVF%2FYMNLpicAw4UxmBHwnvrFPYp2Ea8fomQvsR0mFz5nOUCHlEqVfqln0Cc2K9DtiuZyfAkecbwYLnpV276qOgPhuTWFDGp%2FhEXWePMr44eblog8AdxHUCX%2F7S1huGdtmBYzSOyzObpAuhmwWyrjyNM6waArLC4BA%2F0fdk9Vqrz66%2BLmjKHYG4nN7WcnxWIsXpBGHLOeRxswS7slcsPnlMwE0BV9GiQxz0GkP6YzX2ttcEFpPWXRC6KiRbSnT7q2v3R%2FvPhgMhQ6zb0Mhj8ofFQxk5A%2FLa0%2BXloJxUSHexUJIArFUZv0DH4kP%2BlXk%2BkxLofyaC42C%2BAJvtTEQ3mT92lUYTB%2FLOLRJ1uRXob7cVefvgQW%2Fji93eful57LxlVKB3Z2MexDWSv1CCOZ9fdE3JI3kugYpeZN6FuA1x3H6CKzpGzaSeRt7yeMo1TZNrzdksfSi8ILuTuslW8q6cspM%2BM7GqCSsT6gpru%2BpVgtMwR3HALxgeX%2BXL7nVjNXEgas6%2BB%2FPAVSIeTCr48%2FIBjqkAceM5jMOw%2FFpXCXiBlkHMnlelrmTicOMqGFJGF2vhKPQcXnU1I4y4VfK2nW%2BaaRM6WgX96lIkVeQfRwCfsaQv%2F8CludcsWExwuIT8%2B%2FohebZnk9zIZ%2BGe9YPtmFFbAJa9zF%2FkKD0ZsBlnXvIpwD6PS%2BHKCWZEc2cqXpIzMdonUS6Fd20Xz4dFk7C5OAHGQYWnhXsxxWZkVuJfrSq%2BTBpdTlKReJf&X-Amz-Signature=c1793ddcae4b422586442f154f3bcfb90b18664d6a2cbd3cf358fa85bbc779c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




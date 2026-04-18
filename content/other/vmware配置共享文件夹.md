---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UJ4ITUQ%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T035042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQDpNz9akFBqQ5VCyT8tLuAsnrKE%2FInQ8Kr8%2B7JJ0qpoDAIhALC7yzj5XrfhdtRvTfy3PcbLOMyQP050XX9TtbLf6XtuKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyNmRClCo1KI98tbh0q3ANDd9Y6iTBsE5Z3%2BXo9vgvoPcBcgKzjMUZzS5S73qYRf4VoqUywWzE56SQbGgnLctV6isMYymhyKb%2Fr%2FFBNW17IhxRRv6bNTx0r7AbbfART0YkN243zurN2uyhIH%2F0EtLKwdP2nEzkrl8MkXXY4qXT3aaFMo%2F3VgJ9v18Zdb7Qs%2BwhmQPxqz2SB%2FWfWHL1IV%2Byew3hsuOof57PAp1nJADAbyZACByOEcJtgbvgKYnb3F4Mo7fR3o%2B%2F99f3L8rmP1Ek%2FtZ8hFiyGzrvAwvOgjEzA33eJH5tiGN4RH%2FSbiE2dgG0mvkE%2FqLRbJEB2KbDp%2F76f9jLc5mFH2GKPl4KnaKHnxbNmhtygQrmXWIGu7jwueE9Dn9RiyFZpqClFbdPlvtN7FOVW02p5LasdlhyYIyBfnXgHlIEZlHiXGR9znvqPA7qDpKZ5c0%2BRcuR7x0EI%2Bgf6%2F3HaigmTq%2Bct3HPAdldBJ9St%2BiXhCCv%2B%2B0hWtnW%2BMRnk5Cd2RCqFjqWEYoRx%2BUolLFUOyfB3awwYuHW6bhEIEER2H2j2CWNSus%2FwZnBjOoYKhbU86xC8MmHkI4p%2FUyAkNJoEj2jps%2F9KYIeF1WTGSEBx1vZ%2B70UYocdFvTVg7eArLlaGinc9TiddCjDnrovPBjqkAbatxuFZH%2BQ%2FSj2gEqDitwvvXnm9ld7%2FcV02KNmGuVJld2X0P05tD7PUFrxIQwEiMIr7SwyftoI8Cc9QwHzkgyO5cenKKT8K8ZNjXdar3x5mA%2FZ8jiM8BTOWA3C1EzNThQlUxVXdM8N31p5yQ%2BtdAGVzvwvXKbS2kqGgEiIP9dxAP7bP5YXIBTPlV%2F8cn0Xc449Fi041%2FesVp8RZQoFBRGgQYfoK&X-Amz-Signature=b91998c74383f386133a54fd5551a57e1eefa50be2f207cd85b4b603c89795cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




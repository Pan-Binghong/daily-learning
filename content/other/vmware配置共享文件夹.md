---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7LOQ3ZP%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJIMEYCIQCpM3Iyz3A%2BhKriT0zot5xntaHtSqhAR2yKIuQxQsOm6wIhALYWpxY3twymEe2qYsotHb9dR7yUknl2qOwbb%2F0vYYhMKv8DCCoQABoMNjM3NDIzMTgzODA1Igykh1%2BxVJqeWqn2ZUQq3AOQV7JooMT4ZUs7LnBS9RV79CnI2n1RACdkyM6Ka92pYVcZR7FV3pG7oK3utHNc8gNapJTuXownnxu2TnEGMlWoT8Y9gzms%2F8HW03qCODa%2FUaFP2%2BY9DRq9%2FmoFMSoWWBAjI%2FaSsm2E13MJd4q2apAXXMX8vp8p%2FquqhZjrh%2FBUwgeMfhwT4muTkdOPksfrXzFgRiQOUktBuuTG20JAfH%2BbGPoO1rZcp%2BGLHqyuHwZhUgucZK%2BUW95YGebgQiHFYKCvmWmba3W%2FUd7IGxmOwq1pbrBUu8ZuZW2kX22ZLCIHTsO%2B6INbtmmZWMk6lAu9Z5DK0tZdbGGwoUyTKdyU6TfZCI64iEVj2VanbW7O8Kl7xfiEMfD4IVHuKmaoZYrWi7Vm3tVgPIZmg1u6xdqIdNMdnlmd37AOxdSWoswTFeDfScuPsYF6gOpm3Cvhk9zlqvoqetCv3dHt7bvCi%2FVX8OqXukmuVnkwepoJXNHhnQLOy3h%2FqO9RoCMPSDSbw4oVldycigZm8sViqG2%2Fb05j%2FODUluS15gYp2G6QgiJjD68mIhemBqxBppsP6PYkuLDFaGFf0eTUd4pF%2F0W%2FR6U7EaQ%2B2rT31Kt73hV9LweRM0jjSuIEQDglLQvZa9bSvDC9ufLNBjqkATrItkWnaKSN1P5jGd03WxxiQmK3upxosVL5HUYnpgoijskpNl7rsRpQwTTd1RFTyjm9lnXfyqBMyhx74YmCrQDTQrDbil83LlsXOL6iR5%2BbpREoqajOVOzQBfx8QCuvQs2YK6h4IMy7%2BbdsAuUCEw56UZQpCk%2BxNEqtkDaAiOCf6B%2FrJTBHLnr5hbi75O7ujEGTsDJ1LDzxhK%2B4gkuVN%2F0rqwIC&X-Amz-Signature=3bb13850ad3e4b63587c4f5c2c0b2ae056ba318d724553d765f4b1d08cb99ddd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




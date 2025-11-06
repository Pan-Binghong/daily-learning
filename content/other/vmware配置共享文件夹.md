---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHRUOHL2%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T021001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsyTIv%2BwyPeGz%2BeMGfnrOE5Ls7488aeCx8VU%2FoIUuUGQIhAOIVYFu0wVF%2FbKpoIIceJA214BWugax%2F2SPzEf7CVfDDKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyJyh5CT4KiURda1QQq3AOqRpafxjUNaDBsJtb6GrH%2FmzJwWfwwmv4d2S77mfBXoxIkZf%2BexBwEC8SSOvuPE%2BHh4ZdLQ9XEylXhzO61GGMTgjOyGsia7DVP0vy%2FolumxmxqDaQru9ozUARt2LO1Oy6IGV8CaY4vZSkMFdm45VhuyINe%2FPplavq5uOR61nSAbM9QjqUT%2FoU3%2F6Q00k2Fy7V6HWRVFkEzfEBP1i79UjDm72jyEUwOu8QGDr6PQMwIVOl6LJFQRKMYJO2M3MtU%2Fqcf6x9hAAjQ4sjCr0dSIZor8ZnELpczIVYoWTDGUmUAe5%2FisCth4%2BweaPYzCdHonzhch6YiVuKMzwrGDMAKb9%2FaWKc%2FbARwDU2kktTOmnLQDyl%2FvToYA7llO%2B7%2FCogKoBmJhD2Y34ySBFFjPH5J8WUUOc28ym21c9DAzL3Xrp6%2FwKmmzY1m4HOLfRUqxI0OPnljNmnZT9a8qBEcWS7Sx1p%2F%2BfmSkcgnpuZiumbjvbIEc5vN4PH%2F3SJYuWnGQja7YR6QqUHYZxBzIm8iYaC804hPxBgaGr5s6OlFt6%2Fim8EXlJnj0nq4%2BQFWgnQEmbcZEH02htHadhVAyJC%2FVGyPRjdy8iezjPPepYbUON5%2FhMjZtWsXjfFyvdG%2Fx9ypizD08K%2FIBjqkAWwNx8O9olmNERzkEaf9vSeWU0X1pTwtRNCb8emOBirULHxc9SeGYrxcTp%2BBLBW83YXJvTNdmh3c6EZQX7shoZG8ihXp3TraKaqexbY31WhwnKZ9U%2BT4xjXmvRoBWrtGeCi68EceprxYSXQXqAb%2F%2FQmt7S%2Bbw0ZytAYJKRZw3QhqtFRbRkiRNJhdCzQoe3EE0qYq9SQenM0KJb4Eu3P%2F2qSPfWTy&X-Amz-Signature=aab2e4594590ae301897d48c1631c2b5f96f56219bd583d306ae9f84253678be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




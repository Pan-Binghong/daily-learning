---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657FOARCL%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T041124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQD597QdBQVLT4%2Fe1yyW9s%2BUGcwfg7NPtkj4IR1kp5MvNgIhAIi0OQp9Mvy7zYGV%2FDPqJoRSioeIC99lvbR6PVccDEXrKv8DCCQQABoMNjM3NDIzMTgzODA1IgxDOLQBbvv34DcMU54q3AMWF4HJF484HyTobGsou0GQsyeHKgEqE3ZVm9jRGD5qVyAKCND6bPUNn1joroFhCAkJDIdCkynse7F9j2imBL89lBGH6NC8cJTJNjUJMuioVXadCtP38yOFmpyxV0%2FJ0t7pBS%2BkvSGpQ4hl9mIgZ8EqRhWmCWTDp0%2B%2FL5jM%2F3%2FCtc8xpqGXy9YKa7KUcE0F0Zj7HV6q9qaTvxZnfmKkQCz0s09N53hVceLP56F%2BzgnDVWhV2wf5c%2FUNcQL%2BYOyvqzuM%2B2xe4YvnBPzKrusZENPamxSEZiJ81uB0TOpUX%2BUNCXH4SFhoc3jzb37EnNxUFrT3OVF8%2Blo5wwoXH6Z%2FzfYe8MdGSKyjVv7NL%2BTHzR9BzDFEmIZjBNwCnfElpH9Gyvi4xyDO5Ca5sAsakLMpbC3G8eMpvzbQ8rOlsLf%2BBJuIW6YBKHo%2BNb9w4sYCJ%2B%2FFbB1K0NzuPmEbbF11gz4fNQb1jw%2By0ULFUr5U0SR04t2aB9YufLCme8qeV2lhf6Ai0r6WkaL7QOIT15ypTjJlc2jcass8CxeuXUJ3SYEBgFuWSbz8jmbuC7gZil5NyuJb9yVfDA97hNY7fBc26X0CiCE3RHhOvI7K4Hw%2B708j9cjsXMKoteBy4z5WnOEcSDDXxuHOBjqkAbijbVHyEy0v7c%2B%2FFRhdkhgGHV%2FBNcHvHSxCosz1yQ9nNq88D2cL3Hz%2FItP8peWNUVJnoIPROMhjc8tZ3AJg1IzJny4ePYAIGXftwFbS5hPxahQpxH6e%2BB2kx%2FpEFfx8RxbZ8JK5TaUuFgxWFZ38i%2BMtf7MEgxuj4UcPsI4Vej7b5kNFrTMbFllXqSJro3s5SSzPzxsJYzR9imOaCi%2F%2B0hlF7FVz&X-Amz-Signature=60759cf77ce03941f13343cc8991e0b621a81c9050288cda5f0908c358182401&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625KHP7CQ%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXfkvZfuB5c7tFNaHq6ZtE3WmVCNGYyeIAzQ7QueMzggIgRKYrNLOUCizrsczLJK4VrY9q%2FyQkcQQ6AklzRYqfNFEqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0%2FuE%2B%2BABhT9oBV9CrcA%2BEMhhImqIKSH4yF75SyYy7LctiTnxKk2m4h9qlvyFOPwA3DtZJDuSZVurcfk3Bx5Nx2Ge8BsYzwoQrxrWl36wM%2Bx9CVaANniWAQ4yQvXmDppnoHfcQDXxyyoEeJjygq2IcdtI3WdWAafoAbfhEun6ykptl3o1jGUl2Kmok6aJIc86JRbGWUO2IkXtUbf9flSPUa6FghUYBLqflFGooN7FN6Qdc4G1TK1sIMzIZW%2Bj358a3RebSFXwhDgF1NDpJnVinZWllKEfSSOzU87VdFm8a1gkWLu6FnEo0e0IHTOSJVxxYCRibCLIJ3ZVPTKTdAkdQW%2F176e1hObfTSgIvcuAUu8%2FA6ZySjmrK2Uk49NS%2FPQKq%2BUHJ3IAsnLsQkhE%2BIrvvSF1o6rax695gfNvWK9%2F7OLCwyDA%2F4dH6N5ju4d2K8GZ6o%2FN6her86%2FUpuAWUfXO2RgVmLDsF6Vg6rMZpH2UnztD%2BNZ8KzTqsvhjYYq0R4x947SR6Ul7SjewkQxEWd2gA9EQNXlVqOESy8J6SRFTGvJCuR%2FJ%2BxcyMBcJTEs7JgSg56e4p2JAHMzByH6PocJoO1r512NC%2Fx%2FfBcNgQNNYsIJaHMcDI5mFfB3OxtRVpPIWV5ithhrBQ%2BXiYfMPWOts8GOqUBEGCcCSBt3TlEaD8EKfzMJqHROH6rnNNOOxIU5BvyHYMtTXV7ym453WS9PhjZtf1RUc8Hw2CtBFX8Ig39fR7nJCqOj9A4R7oIpOG64r0tnuN%2By5ju8SphjPW6tueFhlOxdlAPaSQFkQCgtEZZThPm374lB1bp1eI1v5BhfJCXkSuyfaADPaVrSayH9oMqe9kSQkWXFnduHu9asDHM5%2BIKMub5NZEd&X-Amz-Signature=12200c2608f4bc36d43cfb8642269bb9bbcac82145aa03fdd197483522b573e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




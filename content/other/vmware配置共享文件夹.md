---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NUKGXWL%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T030117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCX8EJgYFPG1%2FYogtTfXQY9l722f3292pRnnVk6a0CKwAIhAJMCP%2FXYeM9wmTpnwvHIikVmLQe%2FaInwAnnkryXWHjOIKv8DCCsQABoMNjM3NDIzMTgzODA1IgywdqMVrfnS01fcnw4q3APYkU7Pu%2BHzccpJxawDP7KuqG2KF18kfZ0Z3QMDfsIaXYmc%2FmTqMDHSn%2FzclJEIIBWkzLBKKLooKKANoSpntquR831AShBmU4PjBJMdGw0MqdH5dP5iDBX9HaNucPDxcIkOWFZtXe3vaGQfGsOv6V7RzqJ5jNYZ4U2qL9BWGCK8rvfE%2BJ%2FVfb9%2ByWwro7kmEtimabgSIQKCcCTYsfedH505ysieuwCSfyE2iUva9zXMlJFCS72%2BjS4gwoXBf1fouvqaXOcFXDxEKQSHJdz%2BAvffZrmpZP%2B0fLtMDlCf6prghrN%2FWUOVcdVTpNpTPkKaViK2upZhl91J1rm4Y%2FPGVcFt6673wHzaHxOqoR%2Bxf17aHJEpOOU6FS%2BMtHe0lmCFsti8QN6MbONSrcZzGcNdI1v9D%2FhWo5IK9Qe%2BgFuKLg02tqSnbp3kUM2KZL6A%2F8Q1AHt6mMkRHH5Y2rlNOVvTKj9q3UI7yI%2Fmp5mVvtL55sI9KBpL0vJJWmNCBrv8VQNceb%2B2HLDN5QW%2Bly3ooLmuDnjt1Hggk%2FBWI9zf7HYpywApZmqqu%2FKjgA29h5hc0lHz%2FoeFXRyFbvjA7fH0ccYGOu1BotI0uqheZ8EBmIDXpE2ohYDsQSAypjHORcTWGjD8r%2FjJBjqkAdiPfISh%2FAWD2phKkjZCmOKgfwLCpOulJuFD%2FgtXY3LG1PK9e6rNZPlRW8ThrYqst23pHMuCMmhORthf4nNNFjoWEE1gxZznqC1NxLUezYzCXlwhNlD6jckG6DbjRDQ3%2Fj%2B6OJGL%2Feuy%2BxseCQS%2FkUV33X%2FyVHWbcXqGTRbAeKc%2F0rHZrmFCSwRfIDmKSsLeiSmLsxhUgGGJ%2FdXleZFh4AkiUqzg&X-Amz-Signature=9a479fa143818381a3765dfa1c496ab5d9907e1e842101657c581461e8d2192f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




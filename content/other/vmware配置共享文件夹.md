---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664G75Q6YJ%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIDedhtwrCmuygO2VdCt64PkRIaAoW3SQAbW0Z3qVWawaAiEAuF7flVszSq1KeonQt5ixO0%2FkvhrUpgpcwRtcp7niQvEqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJQUsSoHQ8ySzRtTdircA1u64e4CNnkTT6DAkbtZ8y773xOsWSsz6Va8%2Fy9zRTwHS2ygDGbHSUMcC4RjcQBPO%2Bjwi9Tzw15%2F73UB%2FID7xLIXeb0PyhSq6jQxO%2FuRw7dzjRJ3Z6ATDcO1Ll0t6zlxS2bemmdFzgWqCBwd04eCq%2Be9fkCJ8pkTgeGxQP7Eu3tGCM6hzuj2WjoQjvnWRbBNzwiG3NTf7spyOnvayh7zX5b3VDYfEpShgXcxES8AdS5UJ1mGTtKcX8XkQtMhNuNlnUYiHSFBgLv6DojSMcU0TsPQvpfOQl1puOhDuwla2eVWUQj0sJDOMmHX0YPrwD6%2FhVkQIKzuenE1aBofMzaAgVp488CqNCl3YbZlg7CBbzSW4d0H5vR5mgw3a2jHmiX8FFfXZvLrrm1gjJjAvtLCUX3OU5j4CfFhcj6j9Riyvh5VY2mGpaTooMfVCRZi8tue55uxqBRXCloBdYJRycHnP3FfdDzoDN1bPjDfnQuEVGM9Grc4DwBJlcMxqnJrndhtUuAwLaocw9fUkWm9194Ys1bO6lgfpzsAZo0e04JxxjBFthRNIBkJRhrPM6Jk6PqmouOsoh0%2Bt5vCFCj6RTwm9D7WxqMF6LrKSfD%2FpkXboIaD1wkm4%2BVSofNetprLMPbQusgGOqUBQLKomb9bpejyPsZNqeTs8mEDgpzLtaxFdIqQ%2BAISuv%2FOAKTe3WZB55buQKFkcEXmQHd4qGnx02J9e7pQczjnJGIG95lNai0SKhMly1JE5twD5IgqEL4ypqR4xJJytO4UJN7LsVd5qTyCnrMMT1XbXcvGSf42jEBA53E%2Fkc0bO6HLGpdM7UmYDUztNhR1sZVsQhNrt5BjLdeQxaQ36NLu2DjfF%2FbK&X-Amz-Signature=5536cdd59a8120222aaa6dc1d8b4992a23f8075f4cbbbf31cc39f3fe49946821&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




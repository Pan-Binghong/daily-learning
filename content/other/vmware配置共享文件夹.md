---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MCUTNZ3%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJGMEQCIHppmflv8i18R4sGCRDU%2FXq6BVspER70dpMNvpO56fgbAiAeANeMCOWkEk0lZgdeTpEilUthgTLHHd%2FFHHfR%2BuYISir%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIM%2B931Q97DNKzB%2BT22KtwDhUU8dG3QZbOGLP5Bwzjt2kLlWkpXokWwMouHdcu4ZNsZVCB45jjiIDw7QQYOiC98S0a55cM78Kuge3wdHHYdL5doZi2kDO7XmKBCSFd355k8c8sv5ZWSl10Ta6IZCuPRT0pDnoKaSj0f23RI77azt7pp%2FNJ%2B6IUThQ%2BVYo557VbMNfm%2FsGALckVmAqZtDZey2v9%2BzFLW9e6Dcbyy7dOqTjveOutJ24auTthFRSLDZJzf8wS9dQRMBZgrDluwqNdV57CF76M24wtH%2Fklftth9RhtfyUfcrpC%2FxpUSZ0Q9PGd8%2FzaOs98BTjERSmC7CG3UIdhKLWrBYynat%2BujgMX7PIOJ1c%2FF00FEBzbqRSZaEssXCSwOnY3KXe4ENwVzVIFMztkyM4DVpPTQLgnmJ40gGL0jF16EosQ3OQYIWjNXHdMfMXSaTM3gKXdCAMTWUEZBewP9EK9HUMsFndqea3P%2BrDDp1UHVcgtQA3EhP0uBMwTQ%2B%2FsWuIrLZ27hbDr0JS4Js3RFZMcGt%2BBSt3LZpqFmIKsQ%2FoptolviCKYPZ1sSIrfY%2B9EUVb9%2FMPw6qPsSvG9%2Bw5m%2Fe67i7sY3k7pwxKUfLGqX2TU328PqOqFg1%2F01Wg5RXRcIyJuMiHkFqiMwj6KyygY6pgGh5wWQvpl9Cx0%2BgiYuby7HDGjdCi8iubxaXgwd%2Bf5KfSg7EJo5EfQ1Ro%2ByEKiOyGy3I7NEGkj0m9Aw8nmx0pzNCozaVuWMQVDEsAygJWHAaFWmK4NZ6lXTriOOqc8E%2FcaArRGycdtbE%2F3cKscaKnvLJmGFuTwB65z8sx7zKc%2FG9LwVk0iXeA7WP7vrnimc46OO1qPw0KC9Bz3%2Bgdi6fHPyXzqTQG36&X-Amz-Signature=1df38d11ba5d2cb49992cce87fea398a4d561f1ec2240bdb53db87e4bb92ed8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




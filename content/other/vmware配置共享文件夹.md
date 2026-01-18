---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6WC24XT%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICJk1JFY2LJW3LMxTUZKpeElfZz3GruQZzZtMb2%2BhhQPAiAGWgkrIbKg0dH9SwaZKs6ewXJxjtxYAmzwGl0kOqEQbyr%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMEKZ1hDmop6aZrJT8KtwDDku5oYmkupHSH2SGM7et%2FxpQvhqUbPurrT%2BO2pTEA1MzhlnFUpcw2a%2Bn8DHuPv0m9T%2FabfbQWILRadUZhuToyTHD8YpA7dvLDPhbVXQDUjyWmOpnlj3mrc1n2rx6eli%2BQ8mqmzZRrFMCE69cR9FGuUDcWIiCQQ4c5sF6Uj%2BXA%2Fl2dvfdSpJj5Qv76Eko518j96g8yiJDTxNMS7hwBquGXEJ77jnsVGDNDV3PCsiLyNp%2Bo9MY3D%2Bqk2gRsP5s7KLHArMxBdn1seFQbRJeCRjfIm4OMHKew4ngMLRJ6HcyleL0dRfCcY3BbPvPmyDBB3Dstaiu1bvn3ymb%2F%2Fnt2u644Twg6lRVOFfWz1PaoWl26%2FabK72wAYD1WMcxztyrSfBmkSH%2FjeeDqvxPgZwbR1D6ZBtVq91oy68jav622j2BKfHk4Q7oTu%2F7Fx1x5RmELYwYX4IvYA8Tcn7onKsPjmZs7yGkstWBG79oyQwpy1LxmfcGifmSTm55qFg84WTPjCvoF2%2BEw4w9rrLxn%2FNsvgkG2MPa2GhsTK2u9KEMYs2mzjKYVJF9nTjzoWpcy0NWMhfPb%2B7hHV4SO0VkG8nmOlc0WcRJzFBXx%2FpmCDDElxeXUJG5o3lhY1oPnBnBzRIwy4GxywY6pgEVliYEo8omCsVaBXeH7v6bKq0IU%2Fn4%2BJwD17B7oH3%2FkwZG9n8snNGm2YABLgSlknbxV1O68vegXB5PU3kD4yqrafpT%2BMOmnveW%2BkOcSwcH7M3X7%2FXLRBuwza8UO8raKb6oln5kKI0vlcBv%2BWpBQIwfpvmkPHKy9ZUIJ9pUiruQgkuaf1Il7zWAplYANMcEW%2FPl2H%2F1FroNh%2FBqjg3jhNy2DZReTKjJ&X-Amz-Signature=a74797cce6477a8d636c49879b2beaf34e3b49c09e3f3d97115c952a4e156d13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




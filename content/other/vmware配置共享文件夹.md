---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q45NOIEP%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAZ9qP0wYya287TXY3M3My68SgVBkGhZGcCppWb8kXdQIgSG5xbpzTw2Q7uqLl6CNIfMpFZKz0REoHl47BiNtcIakqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJzyy5VLvOBTpZalOSrcAwSK2xXpvi490ptwMXhm5OTKzhNTZmpmZX9tE224kd1EqwtXPP0UkURN%2FPR59m6l4X7KRMJFnNC2gb5wXk%2BHYYvAofJwFUEB%2BRqaAQ4nXq7DlAonFVJLVPpf6WSi84m4EKwBu5zYZcGmuEXnkYxJx94vEEih7tKiyFjESkGHFvhtrMo%2B6X7RU2ksKccDr47KF1f2inycGronVh6cKGxhVIHwFVCQR56pwGCNX2OEhN2Ik4Nj64wA8tPJ6a6GsceS8rFpnRhXYwC4vo3CXx8w064kI6ppixxaG5yqgW%2BmNl1TcJqLvE%2FpEl4x8CXtRXhLTyJXoC90ju3viDdOsq4qN7Uk%2FjhZ8k1Di9EwtG6i6rpao71DHk4tJza9cLW908jSsBxYbM4r1mgLQnx7VqzgBelty3VfLKDd3ARXG3ro6Ocl4Zk%2BBFT4r1MA45DXKelwbWTgo1R4%2B0BATuW8dsTnFIwlnbKIfRvjCbnoaE9M1iCoDItLmwpuJ5soLwGiLTF5n0WtkLcCqihLlKt82fCTury3wwgPB16Vxera%2B4An5GLAKOONUum9qRvMBiwUyZslkibYMpnp4XhmCclTRrmMD8tdTX0zsc1X%2FRzWE6LPuLmrIJJ%2FKX9OdDNSroiHMJ%2BZ78gGOqUBSHhuLyj4gQlWsQ6UR3dydAnmPaO2ijmxd0mSzxV6uJvoqHFv3gQ%2FuSdQO40RcdiYa4%2B29SmtSYGWWOc5pjBduF9u80%2FSZp%2BXjm3gHOAoj2iLUsDsA8WQfGFD1AGPyR%2BNNR3tu3jd6EPuEYi%2FMH8UWTQYbpof2dWqkjTKeMHWloFJiQL9va6u%2FaPPCvlK8MdnPf890mDUR4q1KX5B0IFgqrUl1x6I&X-Amz-Signature=9ddd4ab6c690f6384d26cf6b4ee3081b2f6e59efe94fe0a997c5032967e034ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




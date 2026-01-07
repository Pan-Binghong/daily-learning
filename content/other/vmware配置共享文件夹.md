---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XBUYE7WW%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T030112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICRQKiZuAv1tLvYDSUzubxai8by9DmMVh4lIv2yVInbYAiEAvgT%2BXzk0laugVvAus4%2BGVIh3GrTdElln35qF69Anlkgq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDATI2NJoa08hmhLPFCrcA%2BpjPFaaFMxv3aNhC6q5ETIEuKxVcqIJ2ZMddCdlTJnDdOPhWjmiuEMDz5aFL3JJRYG9P3qlJAipXmY6X%2FPrLLlxPehaLBpfCfEYUegZ3qSMGO%2FftZG6qJUlEvM36DP%2BZx71TOcsK4XC652Sb56rFbPum9UV9smIQeIWHRkIGBr6gQ09TZipWN3XHkx5kfn2ONGhvI8RowmR6sm6ot2U%2BuxjTnOCsFfYud5mMxNbwffba6z%2F4XKZmvBHot7BoEkPQrT0eMcrvGupl0s%2FSud%2BOfWNhJyydGb5AA%2F4hVwtx2TeFSkF9kAhgko0d7EQsq54rRNb%2FQOLdmLyzrAEdJ4XkzGIiBHBXJU4N4ZX%2Fy9XgeauriKP7e3aFKukvs7X9LcAYm%2BHD3gzGCi0k4fezVXq%2B7woL%2BsNvJ1S3hVx41Mx4Fa7M3rjreX5aLZ8MMJaa8XmLz44u3zHddeVBC4EFlSQ21YC0OsvaWxtMzn6%2BaFO3POnAUik5ynPfQ7Y0VHVgL6w5TvFBGeNpxfSRnJeuP1Der0beVcgTIBeZPDK4ZWiE9FVhe%2BgPs%2FFt%2BKUIXUd%2FezXXrjhjPT24EAQDwbphBz%2Fj1tkm9KWIWPA%2B4YTFY78NZ5KSG5INjQ3vGmIcjjpMJCP98oGOqUBwDtVru9dqH9O7gBYRj9r9mBDhvd3%2Fig1RAyBBmnA6SKWFK%2FM5m7Le5655N66bjxomTi5li4qvkIzWR2V1pi3Oaa8rzypsqXESIwbLgqMIotBp%2FccvL6UklV0qzMdYhXxnXwNJNDJHLXYy59BT0lqYJoYmHXK1LePaqduqM8Oj7DlXZwvAZqJQnsMWZKy%2BA8yxMqCozYY5hMuKnbmKFo2zuU9oyTG&X-Amz-Signature=9ebc238acde3eee90d2dfcab697ecbc3c628759d2057e90acd05c3854ec68751&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




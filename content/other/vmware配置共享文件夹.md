---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RT6XLVHL%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T025058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsvPw3yu9CP2O3D%2BSjQjiRwQawlU4lGXjZL6%2FTF1UAXgIhAMqoIx%2Balwo1q4cDgrQTSSuUc3qnGdZpaF0cghhrfQvCKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWPZ9UVycRPlSw6T4q3APtvk80iLXlwaoCOF%2FvfUyCp3Q7STHteVbUzzDJUnVkLG%2Fi3skLBSUoJdLAsquxJj5%2FlYpELE9lQhVfdsPgZVTEivR37uTwAOSmbbWjYxCu6Wlj0ZWgofuv0NN3onbvQS2ZPMsgamHjaPnHHWaVe96EEbxO0w3y9h%2B7Yimdfs%2B2mXTDFVBiSRIDaWyqRSAZRN0Oyateon9p8t0%2Flgr3k1dCmCUd2kE7Rs2XaB2rCKSfHDLc3kxFtnxtAb%2FeYnoocAPc8ol3sIxqUvfVBHkDIa0%2BftAOQWYFjGsUKhMQim2H8Y6lAzZtOonFAmR8kxBLK1iC9uwcqDWydvauLbfhH9OsKbyMkHXhRzQZbHrLOirO2Y2RbPCWbhOCP3OOVdVhVTJ9gs2csJZCUbpB1sGuRS3%2FV%2Bo%2FoWB1vThvxzd4tThuF%2BWgmgbzv29hMZ6hBi9bUt5FC83OcHeWSs99xQTjgk0DZuKdnBGLk3VzjQGSm%2F%2FG3APi0lkwaTVRovv36H5T8maz7fIs1UpETYBlym7%2FG29QXa1mwm%2BjHDpYBq7Md7sz%2F%2BnliDwhU95x2ZUjUevaQoq2mt3sx3%2F7nabQgIwjYurv6ElsY8QKbQYDPcWB2Q5mhx7nt1eIzBy8WsQuqDC84OTIBjqkAav%2BeGuusglkzRVq%2BAiX97g2ZhDOp7zJoGPKDb0fOHWaMK54K7fK2KKMeBxcsDG4Cs1bSukt2EIU8yKQGkl6BpXY0VQXZKci%2FyT96WaKpSXCbS6n3cbHlaMT1n3ZuN6J%2Bflh6d5RR6%2FV5ugk%2BwP%2FA6NObai9Owvetp6aBZvzWIZSeyX9XLWEzW0TZ0lnygzZ4TVFqj098PQNo2SWgWzzjmgbW5DO&X-Amz-Signature=74b3ebe7b1a33a6b18d9c3be29162f9aa9e8c64001900da01c0e2785e4eaaa6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




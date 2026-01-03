---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQZEPEPH%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJIMEYCIQCBq0Rt97gxxorr3woUROojINo0uw0gwzJAdIxOlfCuMwIhAMCtBV4zzlwvx7TfTQPY7Q5ROAgRGrB%2BgX5tL%2By4jAKYKv8DCAsQABoMNjM3NDIzMTgzODA1Igyp4jVb7gPWm%2F8vMhYq3ANdh1Hx%2FdSCtlmx8kHnFBVN3pwOE%2BBwj5ufZfPT1uxFY6hvYH0owXTvqBzwDpqZoyiP0Exxava3A%2B8hLb47lCkVN%2FL0luEekbU%2B2MeJ%2FD7EB4LnoarISQ8waCz75oYcLfEWqsHvsiQtz3wOEvnPRPuSMxmJ9bK24YHm2bApdymN%2F%2FZo3Q8dmhCCLzqWAGwIJqaUTg0wGwsd7tn1KU0v2DKJM6bsnJAF%2BaHvkWf3LYmrNDJTvcxy3%2Bjx4MOox8ByHrcQHa41U1PXYza0f10wLJsjQjXaI32grmMIQHu3nK29JXJcDVvNkyGPY4Dlk%2FZlaPjkf4pQfKoTuivISK8eyGWz3Kp%2Brn0GNHTY3oQ8y23UrgkXAuUi8q9aOennjDVxsJDUgIQGugdvEJctT57eYpZF7eMwdNeXmnx2FzLColMK2O6hD5NX%2FWiSfBRQgZju5Sbydvc%2BPHJ9Tl%2B6%2FHmoPovfz0g22McriKNy2DvGi6UdzWMLTX5V%2FZs%2Byc6ERnpNeEiRpy0Ieb%2BNKe1KyUGrFMjudVnQ4EfrwQrTnRgh8a2BBbn4aDOFgSRN1zUyQp%2BkKFraxdCHlRsinqI2JVlz6R5SeeZ88jN8xXrwdvw2uL59rexah82D8bZmOr%2Bw4zDS5uHKBjqkAXTK7d7zdVDbBt2Li3sBQl07gu8FebT%2BAigctv%2Fve7My3OnpmKPFp4w%2F6s%2FTWkyyEc1vIh4erLvTCVqS5%2FpmX6n%2BeVtdvfLwKQugaBs7NkOIa5Tjt0Vo5obBGuHapZkWBxccdxrXcNZhh2sHOR4MIfUgClOktZGZBANuOdOmFNozQjbNIkVOfEG%2Bu%2FY474VW%2B5ENNyQES4ciupcE9hEdbyt6WqLQ&X-Amz-Signature=cef827c84a103336167a5280f0a30fe8bd569578e4be9cdbe7cbe1ea31f86ee3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




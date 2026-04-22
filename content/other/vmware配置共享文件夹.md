---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SNXQDBO%2F20260422%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260422T041033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIErfqS6Y7tkFDi1ctVeEkN9jbSzEL%2B%2BvwvnSzZV9sureAiEAksdnaBIh4h41ykX%2Bbpc6CBKHezzc44%2FBjoz9ZfEsWOcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDO17tIAO0fLaZC3PlircA6c%2Bwe7QxYT1Dzmu%2FDQKlw2UutYUyH0qvR1ImCDImKAorw%2BIbLb7H%2ByKS4N9MBpihxEpZbzn0lu3P6d9dxehuKSgRplRtxxDu9nbqjDgzOAjkr%2F9RzcXmhq6qQgpqEjvsiHWxHd63IowD8gbauvG09bktCkvzbkHO4TBaXqD3DghZnc7tTrwD57lGUqbyY4GL1KIE13624lhvEwrIKMuwbnZSek7LRBRMgMb0Jhhb9LfyLz5yKyrY9651e9WZJv4uFuexUyfQ6vZYcTLT8hr8%2FQk92VyQFgqcVuLC7wLCIlorguJnawB0m%2BWJR4Kfrko6Zxresg%2FhMiLw03Bjib7UzAt1JEsWLfdXWojI5z4zhmVLYPSZQ40rW8VavAEvkoUNG1vcQhOPtqE9kxMu2v2dOiZrtmGANPTc3Rnj9UmwkqZbjfgNB3ZDgVzX7hl6I%2FGHQ1jrv2a62iIXjQ0TNF8whu0Kg3ovChJ0dbSkK3gu6OtGeWobtnXYfNP1vrpaTS8L2YtmO8%2FqQsP9sUZDB13JvjrKVp%2BrFcp7sBqU809amU6LAQwCVmgL9eg5OPfgZtQ0FeiyV6f%2BRKvypq7BJprf%2BxWhE2TP9Jq%2F4KmkrLGP28XxDh%2FDjS6LEsiQnm9MNX6oM8GOqUBvqau0Wk4crxnvaPTNqhXw7hg4KwBVEy4JI%2FNkB2CyjF3XXLMwjzJLYylRSASprKyx6xF%2FqksZH7X3WCg1Okwz6H%2FGSjTfCpw%2Ff25BGBAMXR1R1n%2FEiH6Z6qZXgLtj3udZISNUlCdr1XfNLgun4WHe%2FTI%2BRmKbT35%2F9np%2FX1gaW15PpdHpJTPIkqe56QePXsMK8LgHUdnAfYX%2FHJjvb1JrqgRKbwn&X-Amz-Signature=6b6d1c2f1c35e8d99b5befdb63d682740d756f053b819efc5e40eeb0173a57f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




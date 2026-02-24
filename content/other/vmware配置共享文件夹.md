---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCUO5TEG%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJIMEYCIQDrV1oC9M%2FwjV2A4lin8LfLEFioDmG6LzCPD4oZXqktsAIhAOER30cFUVHvwxVBg5dH3VzEZ84Q2wdy43RXE7YUkJZ8KogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyeSDM01DNSDdHd0b0q3AOATntSeoYY4u0k7MI3J3H6JD1ph5Z5Exds3PPED0kIF6bQQqN%2B2t1%2BDa7qw%2F87HP1RYejpfHA0oGUVDLd8CxaNkWwUpxuVaDsV2aJ16%2Bkk76X3mWfjZlswNNkVa6KYwWtJ%2BlJE5LDKCcrKCJ6TjJLnjmrqJKz423GaCYuKEhty7X%2FCjrJfcwHPwUXYmBwEQIV25zgIwhy5eCQAREZiGiO5VeuQDbiXR1u%2FRU9j3J9gq51Uu%2F9iUOey0WqhJ%2FkcAU3ub7U333Eq4d0skAe1dO4df%2BkShcbe9iG5pbBHiZVr32ojGKqvS3VffQHIpWD%2F5lCjZ5%2BREc96XVXRp8VU8PZv%2FjTAYLJlJxvnzoKfr1xVhs9rfwYxnl4A2yrkGaC2vp0kCaFMLUwLn1D0ta7iIA7aPEuwX59sjC%2FhPp2xGx5aCpo9qGduqvpxWNg0JL2xd1hFjSE0mV56giRB8PIXDQhpyhjSiBvpnl7nOMgJVFXUSdDDo6yyxYMSfKedossDL%2FIC9XT3NK3YK2Xdg55CXNRYJkaYZfEpB5y172xrK5J%2B2RndLQKiCLSGxy69JYVrWPvvy4klT1ufFSHXAqmYsx%2BfEjkj8Qea9zmeB22JWGPMuMgH2pkcuafpa8iPhTDmtfTMBjqkAXoc%2BbNuJwKbvA4OSkW8YLu2sITm81k5%2ByDLK0gEC0T2qceigiX6PESaL9hDPRBb%2BuTUn3o014BbshzWFAd8veQA59gI%2BeFbHx9N6tlTN6%2BxlEwRVwhfA4%2BJvlCC91ndwW0KjIT281C%2F1AW81OaQ6VM0WuFQGT%2BKnk9LsHsm2QbOXGAevJbTLQykCW%2F8vRxdIfNCWMcx1PBvKZQOgEU93rQTmgKL&X-Amz-Signature=1d3d254c8f04c561bd91e6716626c15111957a3b1fa917060a6184609525a2e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




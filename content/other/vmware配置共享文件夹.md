---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUXEVYVM%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHpZil9oL85Sf7oq1VaKX0ZgweWNsGtAVSuU4VfUCsCGAiBpuagD0oN9%2BbfiTeihdgIpkvOh9fVbmaTxoJwO4%2FXKNyqIBAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMN2Qb5fEXrDSFibSKtwDLq%2FMXSX3UIna1IyTLtg33r4YWv9c1wSBptCr%2F9pnkUVlMnizbzMvHTy%2Bayc6nCpFAFn%2FGgoDZdUHWHBrEVzi47JmB2rUm0oeajEVIGhc4KypooWel%2BELRJ1S87hcXcyoCYWEN4eOXcOIfRag2PIPSkxP4w3cTONLNruz96Pg%2F%2FyuO4XrfR%2B0MIaUc3zbaXok5JzD4j%2FBLq%2BjNFYXW%2B72GbSv8c59tyhzLKHDcZo9Gc9IskDjaELFi%2B4ppH4KQKlEPAtJCsTOqPAuUgIzARqSVeYJckXg%2FMiSOZAMUH%2BV5kPews1xRHufahM8HW2hc%2F9rLTMCKYYHfTDtdTosveKrymnSRsYyNTNnlUGdIaWeUYNHvJS06OQQCHqlk9BgK4dDAmzZwEfr%2F9RKJy0KS2s%2BiGSt16rhygen1%2BqsFRK6B5yNAXsz2UvJcGVc6%2BJDcolxGW3g7cU5BI%2FjWN9mypUMAt6IpAHM1KwccT6wl4YaZ%2FxKEC5yEJ5MtiQ7TSXKOlzhfs82qjyvtwSndATJgCOZ7bEqpsxAGBl8u92TdstKKmmRJiZQovAO0cI%2BZudehLZl84EBmOi%2B7BQndJSBRAmYxBm%2BRxiG8UW%2B7G5jwCYwkt9T%2BaihJ28QlFIN0WswjfW6ywY6pgHd2nTPWa%2FRN8IIsQkiGHZJFwD7um9XadqFBbjpEs%2BHRv7AxozwBQKsiL8mhqcmn82dHFKvzSMu%2BEL2nGuwYvl%2F9bkzWB8PGxOZC6AHRzy55K%2BhSKAvSZMgNYxwywTXDbWFsSMT52PHFSt2xDgVY5K3G4euj6F3S3rALd8uybRN0y7TM6noF5HvGJKEu%2Fc%2BANmbL18G9Y3VrZEj6MtsLUDEcSwPO4C0&X-Amz-Signature=766657d33125b9604b9dc6abdb9647c3688aa1a3821ee6c5d6f3c3af86a229cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




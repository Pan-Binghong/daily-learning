---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEV47SFW%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH7HVf656yfuP5uQutg0IuUHGAkq8wi989MI5YBb3CqLAiEAsNuNMUxGlgZW269b%2Bz4%2F0Kx94oQqhg8xARCZESE%2BfUIqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDHhi4Yy2OwcmF1%2BqyrcA6rw%2BcdHzOtYuVqw35mRzCbvsFVV2Fzm8FxGYxm2SciNnIp1WruQqFH2PSlMW4%2FQY%2B9rReFSuODf4ar1Mx5VL1bHGKRE2B1bEffmMw0w97PZ%2B%2FN72x883W6jNw%2B5vKTsoUs3arZ2WnVfK6fcFTI%2BhKoBvjpaFusYQpNogp%2BmtiUfVL%2FPwWK%2B5EX%2FLYkTl5pn2jjNj5RJoFH9eWDcq02aHr0IEgmYydkHOKy5kFXMmnPAM6JMsXERDGbc2bnL%2Ba4iyqa6amRvcDK%2Bx%2B%2Fbp9ndzIlF4b4h3c4XveBF%2F8Kaqf%2FkcFN5eTsO6WDrRYqI10CY3UMqvOowYCAtEee4oAsPPN6Q0D4DKllCh5EXor5Exgx19aNxyrvrT8gmSIbdG961JfykDoE%2FHvpXaYM9pyc2tYUfCh0qvD0kbsUzIFUqxI%2FInkEFMNUr0xmD4uZ%2BBtMxYb2h40xaRueqstpfG1Om99scZr0SL67DbtdHrA8n4rg%2F2JU55l7KdIY960Pvl6qQtecm%2Bxlbjtj7S1gmGBqnhfKazWF%2BYQwhWmd1yAfZWn7%2BNjP9CDvmH%2BcQXHTVz7o%2FRRYddjvulNYAQ1mdNZaUjhNqNSAlX3jN0kcafEtTdvVBCbMbnJosESJ6DYCCMLHWjs4GOqUBgBjEK7NpW9M23kTfciuDaUXbPVFGYXmi3uxrhMi1avCJUA2s3dl8zYzF9L7Z31VtEQeVsPCZWFE32NZGSGwQyv5iLRD3ziZPdrYKHrF%2Bn2xo4F%2BdYwH%2BJj2S%2FYqxg63E47h9LSHOakLFIJWU%2B%2F90fSVTfx4reMRio%2FtZbSjpttuYzHayT5IzSR6xIOq%2BJcGw3JzPxRVJlGBGa9g4JcCmYgoMfV99&X-Amz-Signature=307ca48147f39d0a8932ae2b3007c503c8f22d8f5edf18e5fed1930de40bbb6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWPNRS62%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCkOJ5LdKom3OIMyvzMcCZ7Q%2B1wokBoTv9pKao33NU5iAIgVXEqLqdG1oNLNHZLoepp5SPvxt%2B%2FwPvrS%2B5ckoCmGYMqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNCaTbP%2B9UAgychCcSrcAz6v3KZ5x64tAcW20gflefJnZyCNY8X2halleKbfsE1PNLalgX46S%2B5YnjliCahOdxwnojT3%2FmxJzP2p%2FYfe0BEriVRahjLki60ql4y2vPk2ykrtnzpFNGrMoElalkzz7tBtgTXQwlmO1A3kgQ5EJGy0uGUKROMQMswm9RFt89VdljFmIrQEytpdTpHSdDDNkJTmulOUEDNFgtSlqTdO5dc8vJ1%2BH6gYxNY9AxJ3MLsQbd3vEG9HPsrvAmzv73rt%2Bw5NILGxXt5GJSgpiAczFub00nkOHMm0srHxyoCh1sJVDSsR%2FyVRx0xy46Hhp9yn%2FljWxxD8%2FU4iJtZRLvoZLsIWKYAG9PzzOoobIbKQm7hxcxJhkdnImkzniPMtyjhzdbyAU0VWZ90AzLh5xboagvX4yHmjulkU8oojV8qmt253%2B5dl0kKjQH9Xaf%2FbMvgqXlgqfJ6afaWOwftEDppY8mPgb8IkEi%2FaUbrUV7DrtMOePcheJPcNY5eG46iwEkViCLH%2BD4V42YUx%2FBmGpRr7fHG8Zbm0FCXi5PoWpLpf6PoPwapf8NZa%2BVBSYjfsmhNvVFGI%2FkzHeq0c0dQ3WkzjYcUqiyMoUFyu6lz61hhifm6ediHs4rXo7OeWn9ucMIHvls4GOqUBNHcZKFacHdnONtMyM4I2s5Zue4cL%2BjuKtf8elInYieNY%2Bb53MBhBAxSJkHFGY0gmnElLEH811ZgmslBXAFfuxf98L2fBTkSxtzcBoytM6fAm56L6cYRWMo%2BT%2Fsh3iOb7Lkj6WfFPkCIixRZam06X3o7YsMEWDeHeZVMNA4ae9Kf80Eaa8JI6jR30zmw0xWCfLwKSrhsj5apsxMGB3QyZH9e72nQH&X-Amz-Signature=475c3700cb298d1dde900ceaafd524db3646bcdde7c8812ea343b85ac9277860&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




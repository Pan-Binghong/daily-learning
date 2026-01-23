---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YL4ZUAS%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIGYXGJbmzl0zH56NkH7wsZ9iOENNcJunL9EfLXlXsh0RAiEAyMuLSJgA44lXtq%2F6CdLfgvccqT%2BHaM1%2FE%2B2TGL9e20kqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEcZhsNxcoo%2Fi5ygXircA%2BTRhGyPuzVDW3ZsuPZC9mwcRycB2vZMjGU8T5koWrD0dJpsFTvkUo0mvpbc5TxEVrGXywN%2FPyJ95baNeueUVzYPjn8n2LhzVyOpwRLzpkgzJcdAOYxOQ0uTsEL0mvJXusFWXHIkfFQD77a1QGLqcwUs1ahs42JeQweqpXghwZ1xU%2BH32HGXMX5t%2Bs4%2BeiHSVnYvidDfHBH4D3YHYlXNpM8bPOB7RH1xFxKLw%2FrXvNyrDKzffJ3BHwGpU4OASHi1dlp4%2BhrJv87vtMHkMIqaawBonU%2BywB9%2Fhqsp9B7BcBItFMNUD1SmBwu%2Ber4374LnbvtmrZgYlEtlmJMPsViamZ%2FaI%2F1AGXyZU%2FmteuIRqe0i6YStEl1EZnD2KXCUP7hAlXFx8bzvLFzE2pZDSKAFAccZha4ygFjhjQInO%2FYPAvwdjZ3kNuKE4SgAadZTAVNLx57h4UHZMXFeGbYbt5vU0kJtGKmSDD4PBNvsQg6tToKMmyzsxNi6sstbd%2FjSIWsOqodGqBj5cFLOwinOM1zt1UlwNnE%2FAfozQ0mL%2F7i4uMywX7HKzfS1YqkHnCBLctZFjbx3kxsfOtdnZOfuqkicUF%2FDP7VfegtTL%2BUE4gHr8IJREBkZuGv7PPd2hcd%2FMNuuy8sGOqUBnN4vnpX9HCrpUALlMClUcNVp6oTOtQsDKvl0pSsuA95v8ze2KiCeBR6eYvuI7pYN5bDP77mlrecK3KD3zo7HhhXNX74zK8yQyG3gOSrhb5FG72w5SP4ixZYC8%2BO%2BbhA7VT3%2BzT0mhDzcR4nben%2Bc5i8Jpsl%2FVHSsmvKr2cofID047E5XDh2TeA1b9QswYUstgpkkV2AvEDCz37mkuexWQCUKku0F&X-Amz-Signature=ef5c7bd2e9d9df40a66aa272a284f1c43c81b765c7156632a707d33bad5dea35&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FWZ4EKN%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcJPV7QayZnsczjFlNlqqCPhf2%2FyfSdqA8CaLcjJ8iMwIhANy%2B0pefcW7v2njhVdUentmhoAs65hESBBOmGJ2ykDlVKv8DCEoQABoMNjM3NDIzMTgzODA1Igy6h0O8GGr9%2BV5Kvp0q3AMN%2FfN7%2Fm%2B80WO93qsY9AteeGG85cVEQResiN80D02Ds6A4xS7rpVL9%2F7sRBCbJxluaMK0rkSjeW91ar0yuL7Lm0xfE5jzEKgyr0lICA7SQBCEz2%2FRmlDJdiVKxNUrC1r3yaSy0i4VosFLAWb2WhgkHsa4R45Lz47rn2DFfE5xwoQjkslFBfAHhftDSPQzWoz55L2AhJuFYKFUz38CN9oI%2BSnNfXUPDO1x7kg3dF%2BTNuXvS6oHay3z5cJrPTZXS7wugUIsyuCLmUlr02xq7E18dU8N2DrjaPQ17mlhyxkILswnHuEhkHXUm0pDEBQ6b6bCCdBxU5ZfLy0mfuPcVxE7ewDN6isukovi7e9L3K5oK2J82YKcH5Xy84qTs78gV3pnb8ryQisa64UM58zolQNR8CGHXfOZI%2FlAuMIoNWzidqOKw9b3hNDjLYaSnwqhXKp2bVXONRBD68aAx%2Bgkrfnzd9k4%2FEItQD8mOyjNnI8MOEBJWnPC3e7TUAQnakiEWUxSa%2B0EntCUYC86wtRiPYhN1u5awkib%2BkqlyI%2BB77jNub%2B5J9OO%2BqTT4%2F7mdDT%2Ba%2FdS%2FmZ%2ByBOs9kVCrg1Hxeex3cUGyq%2FJxFApWMCw1MRUtYg3jsMKN21M%2BEpX8RjDH3I7JBjqkAeJvh9jeLovEickh1fvY%2FlG6U3QYk4i2YIkj1b5c4BerDEWKxc16yfRyFMUwoEvfIRIHPn%2FH8vf5bVhDg%2F9ptgYoNoasqifedGO0XlQoRWSh6sJy%2Fo4I6n4csu2rF0EX2A9bJIW1A6Z19pLIyXxoEvEK7AXvGj59uA7maFPaMQG1uDBY%2B5f2kJu%2BWvuCSrQ5nyqV9%2BfK%2BYLyYA%2BGjEjFG93VwJS0&X-Amz-Signature=543597c8c3e1a0b1e7f987846ca52ffa7fa8e3c98799a55a108fb801a7975f83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




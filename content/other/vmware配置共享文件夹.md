---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645NJ2NB5%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033853Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3tspXKNf3CeNHmmtFt4UPN0UfV7RWgyy%2FV9Uy0SSKEwIhAMGd0Q1zj9ZVJkcAhzFfV9OKw%2BAS%2FZv6vTXGUpYLj5GwKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTQn24r5cHrz7ZRIsq3AOJy0j7wd90V8dadTBedxB%2F22o92MbNG6%2Bnrb2aWOXE%2FlEuQxicfo%2F0YY%2BAru37AAWBNRd%2BHNd2xdN2%2F2hN4gVIUoacJ4vBuHccA31O5v6Oew%2FwKhkEHEXQphbBjS8CI2c2K0cLCOG3yRMIHvS22JqRXE5AOjb%2F%2Fj30SrystyVLQT8q0%2FZu5LBb6wH0NpyLPBf0%2FRMUcj4zX%2BuCguUB9%2BK0fegueT2VD0PNtYekl9PAiT5vA0Ym8m1Zh%2BUlp4mYDxy2Msmtea8g0HFNhXB%2FikmlMF%2Bh9TcPp3q428CzJTSUBFKlOGrqFJGlfRscfs1LIzwJgdMgeZ43Zy8cM188P6bRnnScAsZnlY7UUwg3YAVUSsQTCaVFuQJlDwbtS2hOH3hiI8jmvF0EPJcVESf%2B9pFs39L0BLIH%2FJYNT1Dt88RlaXOFuPR9EI2nTFExmbWXutO7%2BczNrrfxa3iiqa8ZgWjGImUoa0JfAKeIA0Tu2eN9%2FcTlCWYVlxCDMgTxeIRdRkqff7IMXlc%2BpacCamR%2FlWbHqws%2Fi2r3g9ohu%2F%2FjLYgFKruVsmJb2cXQnRbxPURTxkpt%2FNvNiyM60ARUIjSieflCVZd3LevECfdqFwxSEhXpfRE2mPy7O9ulvHmemDCctZjNBjqkAVFjJxIV%2FdmREIut9%2Fhno2bUYklO2h8PShkCTwrBln1N0Hfi53rebjgRI%2B89xk83T1yMC7t8lVJpDJaiqSj7uzM6lxBtdo9opPzonSisSMHsW3lZvKqphqHkGyQcsbi7ecBsyaF3svfnYt%2B29AoYmVRHEu7N%2BjEFRZbxYxij1bUaLNBsfaZ%2BO3NE%2BxS4fljNH3PVyyD8ct9S8cywSWBED06JUWhc&X-Amz-Signature=05dbd500e99fc5950337749cb104c46c582c5b3e2242ef5140b31ac70a2cec7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




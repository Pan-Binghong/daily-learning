---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MVEJZ73%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBH%2Bdg6Ohz%2BULVXn2gZknkIgx%2FEBwfuy2JeijVimA23cAiEA2kXyvplVXW5%2FlY1ikAgxZc6Jab3%2BqlRS2n7kFjMfsgYq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDFh%2BC0vy6aMfcEmF3ircA5%2FVPahz%2BMlQuuX%2BiPHpVW4Yga1cbs4Cqz8Pe5MWf0er82SpcVysmEwdqxIEwq%2BDXezbvYddy194ug4u6%2BiiRnQc7FqKOl5LOlN4UeFWBnJyeHGmlu6XVxxr7%2Fd1hqEnZJqHsmpCocehixnX85WbOBJf25O6gv3AnSOMEXB6cXVsWmZjlQToQRr8i%2FxlF8uJTHpDGToEZ5VibnWZGZYkX1RNdWHjujWgoIB5G40VzJi%2B65ylqYKY5otcz8eCoI70IYpjFRaPneyd0UgwPEvg25t1Jdt4Sl5UiBmiy3XipJikuqnaPcaBOAgrOeUAeMo8uJuCfjmu%2BG5Io%2BZdoBbY%2BEAHJoVPyLOvnQrcNza784nDcfccmIBh62u6LKnKOjNVviXCsHK%2FKxEsypKLpfAbZ3TmFJuZ2EkMPc7d6v%2F0qbEHCBwX%2FRfUW0zSUjxxfND2SG7fECRpbnlMmzFsgOhNgytSPSto4j9dIT99iFfvOywdW65mdNciSo19%2BzkccWQb%2BVPgSVP2g9ubl7trgEVmYDay708qXvTMbRkBUw6xFFNZAYQqFDdLIo5MEgXLVUSfSPc5yVcE%2BXNgCA8kut2%2FVlXI2O4BKYm0dTWQbftLVWeEDQzS0Jb%2Fv%2BKT%2FKfjMPqtvc4GOqUBpYmSoiTrTVoxoBaNJeG1i47klwIfHEK223yVxbaZgy6%2F%2FaHKNuFpA5V3GmmuwR5bhLAa6B9PK70xGaU6SXGg%2BCKt61eZjiwZiW4Yj0V4Qi7s1roj5xZxp6dNMDnGnVD%2B6rut6ZD7LNH2LnFJlojrqzS1y3SIfPb0gRQSYk%2FqVHmCfinlTJ3pzTD9T1K0RYcpV32IyX10Ld69rlHJ25U7w6GoSVnd&X-Amz-Signature=336d0039f8958202d91c92e1cc4d9e6a5e1bea21ef6c26851847a7392a6bacda&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




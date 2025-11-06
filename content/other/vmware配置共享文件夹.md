---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWBLTXCQ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx%2BpAWv4%2BWpsguZ3pVeFe6NDvZ%2BoKOp7Ekdbky3LBKAwIhAMQN9O%2BK1amfZ5UmUsdF1qkT3DaIePqzYkugX0o%2BojaFKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwRL8MSV8Baox6njDwq3AOG%2FasTizEPBLgBLXwwfbBzDcbG00bJeeqoHJqTwdIRr250bSOGjYOm4STmhI4yxepc7JKL46z2prr014kt16Pum43wr%2FVskJxONEi5eOVvJIFIX9l%2BGSClS1zGsp7A3AaB4IguxmtA2J2daGLG4RXxVaCmGyHyya9hCa3RrMRUOrJBjxrKohyRdJ%2BWeys8mCHnSnhOkzwEfNdmxqOZEBGkTE3eCbnuQGKHxvDIM738g08ioLb6gBd%2FMWcgcKvlWR%2FQx56E6mu2yHaE51pJaohv%2BS36ypKgB5mxOVoRP4fCjKiVdwUOMpgmhK2L9xNxo%2FOzbO5StUhwJMzO2nW1b6TSZbJdUPm%2BQWr98D%2FIVimBGyGFchZ5fgwdY%2BuXkA%2Be8e3IpurixbKLXiRKL8wU%2BS1y0%2FYNIFei1qGeQsJ8SUiQQgI82Gp7sNHSVCJY93eo%2B7C3hs%2FOqdEEcQYllDKCr8hkHWGbx4od20OkIzw%2FZt9ltoJ7Tgl%2F8QGxn69n30EWa1X%2BUxGmYvFjNCSZUNak3wA7%2Fjhwyq18LOBofXqhyQryNmZrRTQYjm4OZuyMNqRm4fVD9o2oSivor7yP3PqJRBywr3Dphr9C9oRuYfOqVCChndOzSi1xJXR5F6Ox%2BTCklbDIBjqkAeDuu3Rjvv%2Br%2Bw1oNhucBKau%2F68qLq9xvEIrom%2BehvYwST1KT6%2FtXjwnoqzRVpISOungU1UXDf2TTc0Hb73iVQvdMCYphkyvpXI%2FJarxeZWcKT6X96DYDOwiVzDsWbqMDqdOejTBzul1mwFgOiexYFmCCQtqx9B%2B0uwYQ8ESiYfaIQx0QLRivASN6kiYSRPXEktSFHzrYgdNr41%2Fy0irghfplmmp&X-Amz-Signature=97403af79903357cd33913b82c13e9c2056336aa14e5fc07805f87fae34ae86f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




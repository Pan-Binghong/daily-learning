---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXUZ7LXK%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIAG60y9RLdDOTb0rU8AoJqlzaBVVxuIDJeFfYPy245R3AiAd9v84d0O0LfV4C7Dqua%2BG1HOf2C4F8rtYS421D9PfSiqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMt1DO2bv547TI5GsvKtwDi7qdBxSpwP4byac7k0N5pvZjdxZYef9zMCKF2HkjY5S0ALUZ7IG4knVIBYGKmaw7cXPeaKxXpBoYBtCrXJipZMG3Ceg2Cw426bx%2Bd40f0a3wHLEmu8rAWvMREZvnK3usyFmyhosbUvAM40tpvkDDq2fwqiGcGcwGitB0q8KQda7gGgkZGpiscI%2FP5lnBMCNiDNI%2FmxahHp2jfhAgN5t8EKa%2BEXloItW7hTrNKZtNrG7gd0XPED8mFa9tj%2F%2BkYJRYTkeUi7lZEuL4HWEP%2BOShbW95THPwN16aFnUGV0k81bMe7SzqudOM8ByUORLDErvzQLtzEwfgrBB%2F2UnLqdjrzOiI1BTUPsBnTL519ZzsQvz%2Bdi3U%2FtB%2BNvClLVqY3XHhCMnPaGL8ImohM5NFJXPkduKHiyd214%2FMVQW0FyjfCWJRe58Qbjmn71oHAmApJysbr0OHNOy0VNA8rhdZxtX9j7qq5y01icVcCb3%2FL6vAU3CH5mXfm08bNl%2Bk793onxs0Eceq%2FjjEgaaVRf2bj2g9%2Bunfc3r%2BEu8r%2FUe%2BTn0m4K410t%2F5Cl5b616ECABz2iBVC7kaWDTHts%2BT3dG8UY64f3iXb39DEcnVWKJ2iodpFwDOVfMB30vOqvUIp6ow55G1zAY6pgGzacO2A9BCH9zIv7Dug8AfTsZ0ByPqB1ui189LYyDUy3ioCLsjLxPTAMgq4Nhl3Zd4telCuietbrV7aKQWcd1Yqu%2BJjnaOUZnuwwLwlQOPHEsVmiy51cNoE%2BS1KvUpUW7%2Ft2gYo0azi54x7R6GQXcebxD78XMvnJZ%2FTc3fjBpBxmiOG0XU18FAWHv2YrR%2F0%2FBso9PfKtHfPw5nj2iUd5seNBR05KLf&X-Amz-Signature=e3d166bbe212d87ad2feca93227380b2caa50425b9f51bb3989d26aa5f14d9d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




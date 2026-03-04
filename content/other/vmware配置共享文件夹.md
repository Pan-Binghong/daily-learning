---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666N4GKVZA%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGJofhws5aXwPdZfokPgxVjwVfJ7cY6M2f42D%2BHcRjqrAiEA10W9vcrBY0qqEqsHjFNGpQKNx6Pk9AGC0mDNvKKeyb4qiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCSUzcAOTOtBANX0sCrcA%2BHNMSNcFjziZotcXsr%2FjJ1cHA1jF9KUK5GrBJswtBf65uLAdqhF2bU9q3KaBdBX5Ci93uqjxfK%2FjuqZriqKKJl5k8i8zOXvAwxtO4GrHKYfaEU0sPHulIFECMg4QNxWNlpEgnx5muGUaFIWMYF%2F4a7hboa11LqoKTRfMCglmZcveD4iLLfwpql%2B1EKu%2BkwlpN8mVOPc5FcKEWSWKhfcm7NVJLmU3R6jWeGoccX55i0DIDOwlseiTZF6w1U%2B%2BS%2F9guPI6MfOn7CtXmkI7vps4J3cRkiW%2FzLaN5oLWF8nFS2j1VnK3d8fDTud3pp3ZT9sAT8n09GkWq1OxbQjG0D2syXOSHcbtNyLSmFN3wInYYalXsOGtE1LowoE03yAtgNzDHwsac8%2Bo%2Fvb1NsXjr2b%2BqiK3b7wiiuuewxzqaAGkWK3LNkgttACjcNECscdmjY9z77APExAO0Q7RliVKDo4ivPgO7q1Z7dMCRMqF4EyuopN%2FF2%2F%2BFUng14LCZ4OMoZem3hk5RVvoHRKSME0qGOTddVCeEtqvOEi7ECyNPy7W88bsR4xczlkugSgR%2FXXezSRQxo88vTu4vldbukQn%2BFZXcX1q6QFxNLWGqCasMdCRSvHIp08UmlZ%2Bm6W6Q2YMNeYns0GOqUBHCbEIPo6dGHFiUiKtK2RYh%2Fw1qp%2BWvw0bsNzGjg2qmb5r30T4PP7WHnC4BgJlPEnhtgK2ymUro2puUY0UmSptMDuqP7gAB2V8fkPi66vSJSm97IjQMB38ue1UVHvpDdzk1XZDFNsVpg9W9Z73%2F7qIIsos%2FGhbn%2FqV7At7nzJEW8m1gymSN2Kpr3LK8JDkCFEzjPKxFUT%2FiTog2XJA1BXbJSpMQAu&X-Amz-Signature=f25dcfe2d99253f9c130def8427307a332e2378e0db3e0400739230cb5fe5aec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JDSCQFJ%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T042015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGMtyQsMDllrFLyypGCR15JH%2FdcmmLOJV5re030yM6njAiEAhRDof37iKwsVPO9SmBQcKnBGP2RF52uhhnnnTkZwEAMq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDEDDeW%2FjgwK%2BpP%2FaaircA969M2qHNYTKjyxkDkZogdB10gQ%2B%2BrTNY2fKMM5qIF24ZLzcASG%2Fqxc2mzQb23lCkYSpQTHdtOZgF5BXUMNHdcHGRJ9baHdmKKas%2BkgxtzAkMhMubYiCRbzCR55xqhTDf67BTic4IP2%2FjieapGZuusRFn3PAK0S5xU2N5Q0ngpshFt3chI1iPlVPQXniWUCd4uA%2FVVOikTu7Q9kIbv6QVYQv4uscPiOesEkp0rW6ysQbK2hK4KjC8Yx7hb01diSY1G5ABkXRJgEikcjIS%2F07sCrRCgVFDk7mTCW9hvjlyml1t%2Fl8RKE7kqnQazDoYqitCwhaMojDShTbVDjpmSVWGWvpZRG3uCbzfpKkZG%2FMBGQQvEX43vad1AH7SP7KJ87qRqRxGBx9PeW66D1Cav%2BuHcThsfk6V5ILjWQ56IWjDFde1gCGtgaO1vAaUaKhVFpNUagGogAklEvLJHk5I%2Fnwdq3Pfqc5FBuCd3oQwYQymQA6HGqVvpVM%2FFIWK3TwvyS8l4FDPGHHvoZI77zlzGQQ%2FTv36phns91ErviXakWkRtwylLTLhNAevZWy1NEchmdWJTU67hUoHyM9E3R%2BeLmQC17UzSe2xVyMoZxvrZRk8xtlSl5m6qYDBtz3776QML%2Buq88GOqUBZqySZZry5Jj65t9go7DU%2F1CFs0GEWWzyRV6BpwzQXd3CgT3H8K3melssb2R%2BGpJ9XQmlYQN3Gtd3Y0ud5ugIrHcPADppXoiIkMHuHhCvFyEDtTvnbQuJObeBiO%2Fg4kYWuq4YdAfqNg2sEB7ZHN36k5iwNXwwpRxEBpWlvjnEJgkFdHi125UV8kSH6cs2ZK5Na1wKflH1HjbC3%2Fz2XSdgvKn2smqa&X-Amz-Signature=06c6d06c86a0bc8f9b13f7264dfbb7ff0865263b20ab722baa95480057c0ddb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




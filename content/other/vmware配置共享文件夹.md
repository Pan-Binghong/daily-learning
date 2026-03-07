---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMPLCTE5%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T032103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIFGmdA9v2hIwM76yvFxvIB1b7K%2FLP6dzQJ%2FgAzpKDVCfAiEAihXrkTERRMPm9GAZiaaCD3SGNxb1RuC1QDQKgumr2j0qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO8cixhdroC0suAN%2FircAxLn5VEA%2Fzj%2Fwc3%2FEReghaU6XT%2Fe%2FXTe08TEEMhRL1XurEZzfFEWm3%2BAa4p%2FD1ro8PeTgqNIbcCwo4It47Y6zjilBKC%2BsXdbAGcvLTlYlFmZoJSCynUtsGEJWWUiCfJP1%2FDqoKZce1MhNqkpgakgcoJW1bjPfrLsieGhmiV6wivHMGGUTqPHftsMRDC09FcsQVHrxbYnVzC%2FUkfpwvCHK90bo2kCiTDoCxfe6udwgQk8gjGu8FLlp%2BfUcj2jy2fkhQNTwtHQv2Y6GAo%2FfiC5W%2FE%2BjE4SZ0CJBvxQguUql2Jdipr2ZTXQtAkD%2BIYv2XXyi2zpV8Il652WeGKdvDWcVCsqhI9wXTqGruDfd0e2ZS3eO0u42cB6Vi7wGEiXvAVAGK%2BLDKdAV%2BFKWSAkQJ9kGIwVC05M06JzosJqCCshfUEBP1bo9mDpLrosImVv3i95SFnjeC5EHPwweh84bxMDlmIQy8%2Bzryf2q8AT8UFbUwH2pB2ua5YDkCj%2BR8pE4X2seR7oA2ktbGlg9peIU7B83tsfSykht0oyP3So48G7Z%2BmnKQPCROUjqlJFS0Bxm%2Be7RD0X8uE5VLqyapVrm4qV3gz75z8SJIO96IWNPfd9UjgMXMAC5LpWH7N21q5XMKaUrs0GOqUBun1hGvtFgE1Y7JZWjeZCBV3EjUl9S2shTGW0b0bo%2FrHrchfS2SRkrjpzqPzwMqPtTwxXhuZgBdvczG%2FSg3UaxHVXllzdpW5NGRmRKeBBX8WqpnIuSPmDTe7NTxk86OwFkhj%2B51lneAaY25nl%2FOVQvDenp6spU97R6G%2Bjk0yAsSRDPTpc9nhO005hRH3ZU%2BzVH7Wi5IVXmfTAXog3RlsTC6ZLdtGU&X-Amz-Signature=dfe2a2f67ed0dfa5e76296204bfa912766c42fe82ac2be683b7f047d5299966d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JPVXXMF%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T034006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIEXKs0cyilMa%2FFzs%2BOCKC5jM1HKrFIG0Aa11F%2Fv6Q2yFAiEAoJjfT8nRrWrhl6lWVzdCIQwrMoCtkQ9GXv2y%2Bu%2Fh0Fkq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDODpgv%2ByOTLgh2H04yrcA4VYHd7R9v3xyo8sgtGtBVfcx%2Bv%2BZUEvZydk3nHzsQC%2FR7KynobCoyPho58DHKRzUqLdfEecI7gh0s4HqBSR7SBuw2yfsokU%2FBVZrImaOG2HkP9zZomb6YoU7sEX0MfPKLnHl972SPIec%2BUU6ElZI8vB%2FGMTdahmPgUswkGxAURhrNlLpgIfrH0trV3sV%2BqbKCYWJjvRGTgvEqgp%2BGpOqv0wykeJrRki50KNoBbct0JmS8ZQAyfXhVcOeyngr9JYx8ivy9FrsOwMjBOK8f6a8dNyadJkw1HTPpEUwK0M4v%2FbQrrunMdsGCdi%2BVz%2F%2BOEoL5qyotRoKktLFD5BfMLbNWIgh8V1REvS59DVMgrscWZbMP%2FgUveGSlZWt2w4gTStvLxWK6h1BmHS28DWQKeLsxQiWwFr2CerHKl64f8g4%2FSyICkgLVSAHaoxnfL7p8sgAL4cu%2BzHkilR45CWeWAXLbRjnGNWi8kgM%2BfezGguYJgXr0IVLX7iyECv%2BceJJ6RWvIqVNDQjBIeGzKj0QouZTsr2Wppk%2FW30ZReHdpuHya0sRhtmUxCanFM2SKbAh%2Bus3KjZmdCkY9%2B7IiC6lwgXNCS3xQLMe02UmyWF0rxZ3408O8OAcu49ZCP7%2BWfzMMmE%2BcwGOqUBNZzkG1TP21uiMT9QO6b93uFeshNramrFGEdXpXOSSie8yKbyP0V0mip3OTyUQFdtGASpKSy%2FWi9qx4KMA75l5UO93W3wayhCrZEgW%2FUaMNc7HvpnU7cDYecHn5JFbDRYCuKD%2BikjcvfAOtUhHbrizSQl0VQe6UFFobsLhMzsMoHL%2FEvdJyXd6sNmQM7h%2F78WMercDXe1Wcs3D%2BqJRed7nYvQUwSy&X-Amz-Signature=f6905530490e29816e37ab0bcfb21fc17098efe317bce149bcc1253f52375493&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




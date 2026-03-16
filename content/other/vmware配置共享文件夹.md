---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663U5UNRB7%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDWgH2BNIhm75PoeBbtRe6H2kE7NnCTWUGH%2Bw5KZNS5ZAIgTcMFctvWEFxVcDKvgyT5fJRKFbRAswkI%2F8t5WXV3ZTsqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMPzG36nQGg1HLn%2BxyrcA5%2BkLIGcGjsZLoDU61mAoyePwzd9de5IKYd8%2FNwOo%2FolKLV5k1Kg2GeLzk2u4uvUojybCU%2BXUhZePyB%2Bj62bWsq1V6XwpFwXSEyq3FcuAopgWwbBwU8UkwKWB7eqBxVgbUGZOh%2F0CTAMBMJ0oBaMQZ%2FiLjRTzfVWqQej0MArOXvPB88Ybv01lzvnEQZ3SVK%2F%2FLp5KWVeWO6CqeMXuhM3IkgJhbpT5qknInOFSFxt1hgR491%2FTAhHUGi61RCQk8KNPzX%2FJSX9iGBWfs1LzoY%2F4aAPvnkrxzSk%2FIt0yVgPRqKqfwlLt%2Fwz5fp37xeuvBMQJkO%2B8QxqLcIkkDFNyPapG7DOo%2Fu%2BhEc7R%2FlJl23vQYDebJF8dtxKFwPsP3DPCjDuh48t70Y2W2mpjf3xCCWCadKui4954kG8Op3dcLzskvtrGewCmv61NfjsAumbr5qSWzfSU32iRqkDPV0Vc6EDRRJ1JzXO2lD9vUWu9PfVBTX2gPEPBj4g7Scq%2FYOvzArPMJrHEJ0b0URdH6UnefMm%2B2a6PqkYuV7lFHUhi3McCAhywS01htQb0ocy%2B0hx%2BXy4333XX6Gj5mPyO1wu77DLfVNaNbMvgWI2%2BszNf%2BXcUSgktt4wnfUKVTrMaP8XMMO%2B3c0GOqUBmoMz39d6AgbDscXsaJwstsjVZX2GcwkLZPjDusUydgu5i8BRCt0MQ7RutiG68MUr3Gi4y5lhGqMzDqSNL4IfTPH%2FXNZemzgmcBDGQs5YZ%2BP%2BfjxUApu5x4eplpz5apSZPjhUgu4MQODauK%2B8MOnr1J5oaZPz6y8HBj6EMQroBFCHAj9rQ0iq1t24bZTHhYmOumiolrZjBzCee0tXsqgAfLKITVND&X-Amz-Signature=ef160a99c9e94dbad8fbc739fab3849105579c3bc40bc02a6114b114332c954f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




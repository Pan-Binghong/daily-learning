---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GLHEE6N%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2B8xYpXXVlRZNesY7KQf2V0LawOohL4V8D2Fh%2BIM5gVgIga84kHoKPULCHRV80kT56jVm2LHZ1iDk0QBL5J%2BiLDhAq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDDHB2sHhr0gQ7aVAPyrcA19kbhDz4ZvO5BypvvXVYglR9sIr7VPZzq%2BkimfgVsqceAQoG1dhcPV8WKsLZNNuxoxjHBALcBT2RjZ2QkZ%2BmGA7TkKA1%2FAFETkK1iVDryvhj0eLD57MpPtMQlHrfOWkqp7pbrXSQbu7YuRj10CGIXnm09Q4qfiJs5FYUSW3DkpKPCFCDouh%2FgPPYdSb3A1MU%2FqH9CzTbs3UeIf4DVK17YmMkUvP6dSzuzIPN5Gp7SKsodLxpfVrSUDg%2BWS8WMOIY1FNiWUK3WlnqL5klQnw68Wk62eC7ey2VWl1ZjhBFYtpl%2F9ILR8pVSMXQjXsptOxYL70R5a85tsSa8pTDWhI6WLDQN8DGZmWBsHaO49%2FTmxkZPxtBgKi7RgOBQGHBml57MQMH5B1ojrVKbJs6OUt3vZMJZiaZIIeujNTACF3WXKCMpewKG%2FsC7EJxTAKQG9Jq7vrCNkmi2gVP8K0vGdZpuvnHFF42AKMlC3yzXg%2FuEgpWyDucDAJWlnr%2F2w9Aj8tjSgKWPCOjmkt7%2BM9FaoevfY%2BnODzU%2BPfoKnTf6vLwE3Jx1wE5%2BHSfRTDL0eFI2f8UbLlrlfRt78%2FSFJ7xs8cxhuJMX6Y%2Fo%2BehZ0gje7ry%2Bc%2FeKJ4PNFpTVZoIyH8MPGJ2sgGOqUBxKHtZwjvl%2Bqs5aUWKhSGuHxq7UCn%2FaP4zmtUa68G7%2BZYll9fyDsy1ivlydvi%2BTFa90P8RvKBWKSWkz5B5E2bOBwhPcGmtPHQaBkdA%2BRdxn7GNB4y3TbzI2cd2mHIWwZH%2B394ncHyBowD5MuJAMefw%2B6JCtD3kPZGmih9Rf1xOZyYNe%2FStudOy%2FgR1aq6%2F6FcvU9ltKHiScDSqdWl%2ByWonl%2BMlq5j&X-Amz-Signature=92d6879c2e3287046558277869e7f021b0c149e2ba2ecc756c33375bcd55b2fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




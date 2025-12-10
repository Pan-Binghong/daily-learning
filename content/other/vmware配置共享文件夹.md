---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QEDSVBF%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQD8M0hGqM7ItgFUqRtQ84Qx86XZU5Hb3MJa8Zbq1AQGMwIhAPaMO7TrL3B8lwmnHLZQ%2FdmwRVr1gDfjnrL%2F05LSOawMKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2FBaROjb98mJ7ic0sq3APDTM533fc%2BFaflo1K0jgoveXCS%2BcIEsVnYT1oNkBQv3qgZsCBk5n64ghXQw6XAwBjW0EkBlpkDk0xDPlCRtZ%2BRDGAY0XVzr40qFi147Tw200f3CYneK0jARbEIzxPWx%2Bovahd7i7MfVw%2F2%2FVElV9djrQjYMq833RNZD3T70jy0c%2FhRXsdTU9Vo0q8wHFt17OufahTf%2BGbE1U6wf2nX%2FleTI5XSfx8uDRCCDhXIVXnZxbMGlJ2rrCysSoog9ZUlbqJcPpIATXKBUHItb%2Ffv3Ic9s7%2BNNJzYARmhr71dk63SeRQjf%2BQ0Rm1QGtbfnHb%2F0zO7Yiy58NLH57JOOfBEoA8hhs%2BuL21TH10DW0PYaSCWHD1v2JRvBvgXHySFbvxSZRrX8R1k%2Bx6kRwJHZgCbVf3ojGbvc7PLaqIpFCvEb5Bo1cKeU3JxRaI2e2bLDtTqXvDuTizxZYdy7NN792Emc9LT23PDrCdJZ2bkvVfP340Cp%2BwQ2wpC4FMTD45Jk%2FzCjehmKNPDDwxEWD87ukVikU07LoBdBdox7T%2FbCf4oRml2KKTdZlfDMc9uDn631sG2mww6BpByV1N2%2BcVcuQSy1tan3adfvZJIsS8zNxlnGoivAlJEzII8eepR%2FHY4SDDyv%2BPJBjqkASRMML11qudR%2Bhrnw3%2BRjU3bVkL9K5JbyL2m7GtR%2FpVjOUNM8DbDODL5dXxg5tIH93ZlJ%2FS6kmnMzV62%2BBclMr9cEIR5eSUhHZlldnJormJZXGQw2pkePUyHOewPYP2sBC1m%2BgKXd6qC6PKylL28%2Ft8P05Eb3rNhULkwgRZTmm%2F8MWliZIRRyLx0Fhheicod1U9v0IF1ZIYsBOzh9Xaj6wRKzUT7&X-Amz-Signature=c3a3f38a6d03df68df674893c793f1390441bb65f3cbe0deb3f42d7eab09a4e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




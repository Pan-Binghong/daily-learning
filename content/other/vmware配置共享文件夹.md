---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTKCQAZI%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIAsTQxTDDPWL3E2leBOIC7hUUuNlw5hmcon7JV20Hd9PAiBDc%2Fl4EPZ%2FWtnk9kHl7R9hM2WUNzdy6Xj75TqU5k1hJSr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMR2%2BdmdL%2BaCzoQqJCKtwDuMYpL2LQL8zD0sq0fmTT1fFYTY1mPAJQ3c8oQGHmZuAVK5lG9gzq9ipTUCRzmJjUNDP6ZHEZOJyhLquOy2dmcxWvZB7G72aSD4bxdEDzpIqZbpf2BR05WNPTWB%2BDX6NVTLcTVGL1QFqIgfUstlCX%2F0DjJC5btOUDB%2FXTKRVGEs75HXgNneXedV4LBb0ekhcjF%2BU0l3UXqMvDbsYREqd9RbQvjM0QjVAalYrS5qPsTRR5KVT3A1GszN0d3vIZkj0wsvMHR7%2FSeI%2B2uyoR52zZkPEnTJRdaYnJ1wdmWdDOy1CcbrNfoA3H%2Bl7tzSxKwHcOs6KjSWdIaXe2oM9R%2BYkg7xOnnKl7uoH3TTJ6N9%2BQ2MW3rR%2B2n9%2FAW8N0%2F5Sm480gYjMHi%2B4s1fTgFTXi%2B7UCs7wYrg1OdOMTez11cnu0KEW3Zt2%2BiPH8GVTDrzp%2F%2BGM1T5R3WoSP3nPORds3%2FhhaBQhBxg712NUS%2FtpvxRH44uAD%2B1PsgBZPn%2B52%2B6deybWZMU4GWg7gt99%2BIPAQkZPBa%2FNoxZ0hxmZKKmxYee%2B2KcOF%2FLlOX0nWiNSsqGmVHRQGIYJDkD8TJKnjUyhzQY77YSFx6c1V97b4ms36Rcq%2B9dQb6xF20nV4IAPwDeQwhtabzwY6pgGvxeEyCO5PhwH8li0rsTSJrLtGF47%2BBRfsbxhs2%2Fl8qNFOzFl8EfUt4arfu7tYUjapyxWfSNU2pcG0KjFf5t0XCUcaKNJskdRIvULTgkIvovZ%2F040C4mX3NU9SznIquFvJJ08bW%2BImb3yhs2cVzIjxpFifMCQAlEYyHjsGaBJhDugK4ZsqyGJT%2FFrsjdJ2TtudSjmKzmeXiNWAhR5qn4M01HVxkl90&X-Amz-Signature=d8559c46d5d283e9ab5ccc2b3232401d9a0484e2310bade9298cb6bdf7bea130&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




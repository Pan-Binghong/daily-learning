---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTYYCPES%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQCCkN7esO9iXTLdMdwC%2BCgmRs6CQ%2BsI6Oggaj32fBj1igIhAOqslcZ3i%2FZkhMouqhUQcQj9gX1Q4nwrsh%2BNwpZidZDlKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwE89hsS%2BhLtUeZayQq3APiaM63Qg2H30H8aiNmVurwcoP5wOd5zzNtX%2Fd2AXWXBrbuPFZgNx9FUE3otgpB7WR26rfeFhLwwludIlUefiKPtUaFdeMhTq%2Bqfo%2BmCmbHVdlFyue5amA%2FT8mStAixn%2BsJEg0udUg2qy4%2BEZdmfF39T94yD1RKz3TXdOfmUfCsY4ibFLLo6BDGD4PkortL1j1lw2708cTZQodHtZ%2F9dFmOdRSNtDqSmf8RNfW9g8ZBOHOc656ds%2Fse6%2BGXFs4BPzQ76o9IygP3VLmp3mmMum8ztDWl68DEojNr0LJ0DG%2FpymzbGucikQAaaz6NjZZQTSSsnZKe%2FnkYwaQfDYl0SUakiGbDA4d7up5%2Bkgp%2FIYFuhRuZLWfnho%2B%2B35p9pmpwK6B4H5Y2%2FANqvZqdGtyxSbZFQhmXF4UZaFpn%2BKbpQfJZYMj1KvVP43MVyEbi6dX%2BNyWjYCY1rb0kK%2F9skLVaTDY%2FrOc0dliw4h2oG8%2F9jItL%2F%2B6OPyZGYJXmqDB9jDJqohg%2BRHw0dWdc6XW%2Fts28stq37DybgBkSf8NyQTVGev8Wbt9OHwDEoWBzBrMpDAhZtAjWTjz4edq2KixlhbrAps30GaN4M6kaHF54hgT6XB4LJWOfi3fEDucl%2B%2FUmQjDWusTIBjqkAd6xDNy0DU%2BnYHErvFoYGGhktE8R5bAhCE07DhsJTl1W3JtY8xlgnj477cWtktg3jWEk5%2FPZLaakWIscwLusd0wC97D14T%2BznVrcrWxktaYgn8itiR9qDlUk9Ilh0ZMZewlU4Ar6w%2FsT%2FCPP8VObJJVsWycL0kFIxYaBsL5k0dKevnmr1cixfYaQCdKkl5FWePixHnvlJLqLcfyyHbNMlgpSVlR9&X-Amz-Signature=e7a273d6d404fac392687978a148643d64f09fb4a6702aea8a5a8dc3e89eab45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZYIC2U4%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDiDmqG%2BGvOefo8roSOXTlh0bRFYChQXVzfuYTjpCj8LgIhAPq5vjPEUdPzlVX37gOg8YfNp9Yaq3OnkTSAfXbwzI2OKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwANgrb0ZEByQvFNZEq3ANCpBJTWmCmwic1Fk7HXL2ro5mXNd1E1da75bzaWhfSPLp8ji9MbDw1Zkx%2Fyou0AwBq%2BYkTnSQ0QIPAkskmNWR6mAoeLteedCHVjaZmBy%2BB%2B7X7XuprYwBJuClFsmcWXYVdS0R%2Bld3xxdm9go4CzaiG4m3eEEd1gcssRO32tpIlNx%2Bw3iWh110KsJXfvOzYBJw01%2BBIlxtGQnuCXwhsrCE7AZeQ43eurIwpo5Rht54XlXkRaDptgOkZqzhvboIO%2FHrxwF7mkOgPTyYZIRjhbgUGo4ONiPWs9bnDXzBOfvgSdpCQa6IxMRY3wyrQLhsnZp5lvgLtd4MZyjSsAIGduWmIDjIhw6t9%2FbEkjm1BdZt69HjoKXQmZgc33RqWOV7KUM4LwYM3HXznQ9vF2Tb5W1Z%2FwQyBhlnW9aEswzx%2BJNNwV6klm0mJ8%2BTbEdBnMQZzQODKOU23Q8Sn%2B%2F%2FttUx%2FoqbBzhWs7pP8STXlZhP%2FGoeD9FVzGA4HnJzRuZrRekJx2mjrs0ZHU%2BmbH1epY%2Bubl7R1W6HlYUaufZ76sfSarfBOFESHRg%2Fdoi%2BlO%2FlAWELz%2BejB1o1Q5Xje1eZ8U4gEDgK1nxWjFvbuknhRgi76Uk7oGcb0vPoBYqoELlPSxzD%2F89HOBjqkAZ0UbVSYzvUBB%2FOCaIemQ8UCsk3YQckrLlVgCURytqi7q8uI%2FxB74YyDx79KDiROU5eqg%2Bs40T6012jRawPdXanIdhT0DPBPzVQpTLO%2Bkas2fnF0ZLrLa2Wv%2FJwEWcFxr9KfchTM60nbjJUGEwclq7kLoK1fOVa9uaS0g%2BX9YK1YhwOy9icNlf5zDtNhCheWFUDwSihPmnv0JNooWIRv21MwaNl7&X-Amz-Signature=4d540cb3109e5423d839c58f5df0625b57c28e3181a1f426ae2e49101c201684&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




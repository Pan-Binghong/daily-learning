---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVLX3O5N%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCP54oflcYIiZ%2Fl3V%2BMt1QAC%2BApBPbgFfP7KcGTXdsSMwIhAKSmDZr2SDA39mj5EaN%2FACCqMZsS2m%2BcdLM6XRYS9iYDKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcIjcMHmnW1BOubxEq3ANpr%2FxhFciL0QRLMavhs0%2FVR%2FNU7e%2BG4nfmCM7JXd0dyI0k4qy03C%2BbMmfBr2dKVxUqkHN1vDkrvTmkpuaK%2FUtCO0m8MqcYjBsuoSn8akNPlqUAixMPx%2FS4nbmwtph2M8lz0A%2FauHOfYMIoA9%2FOwJDAELCmmmKJIF7HTY4is5e7982RlKPkWSExyZp07sr3RJY3KdZF3m6z%2BNwqK8Ojn4oSW5C4fEIeF70Zc5guDmy%2F2ZOuIQqrWDPo87bC7vpDqtHHdgl%2FJLbydFMlSGfc1ND1aLSuOPkPz0CL1%2FuSxgDqmWrPle8%2BvIkCy38wsn6TWT2P60aU%2BuDha8RxJJ1KmCCxuxx8H7KebIR7n5dFGoNgnCjgf8uUJbBXQB3xwW2V7J3Qm%2B%2FyBwfz%2BN%2Fq9bhj%2Fc2t7X79TIeRb19k5Bfuy5s0z%2BiEYWWzePsOGqXgSI3NM%2FqE0UACplm7vGJ6o1yLHiioZbiKkqrdmpb3D5wiel%2ForhrlF%2Fb4OLPztivQtRKCKaf3bUH5E3zMxfanbWN7IzigQcKxLYNVyRtUMTFSYkoTzxF3dVodgvGXs8Oy0shcpghwUw1HHbXNSy4yTXS4dDBdaW3Hg7ulVWc86WeSWNNm41aLkn18BslYprUevjCJzPXLBjqkAbH4SDRGkPIa4mZshKMNXkJny6JkGNbEN93DanO5rzRtMhZPVYx2cuaYrjAfnkFKXD%2F0kyg8MeMyW8RoytqeiwwcMys7wMH4b53YizllgWnbuu1W97R314SEcv6Nvbg015Ijr5qR69yjdQGvcY%2FRJA%2Fgzy%2B5KM5ivp0eTuj1RJjMusRhtpB326nfkpKBtZ2bSpsbgN4kJMDdUw871dkWOeQ%2FTdAI&X-Amz-Signature=5ce359b00a42f0d0e402dd9aad020ecac05ef1f6599aa5bd16a2c4dc63bd4cf0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




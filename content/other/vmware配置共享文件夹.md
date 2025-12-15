---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2OLQPBJ%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIHvtGFFz8Z5DKJoZ705L6qshzcgLZZrJnAvBwlsBD81jAiEA%2F22kKXNoQghlIPTJV8FMZXNhyHeOmhcJbGdbcqgnS%2F4q%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDNCFE1PCLlPPPUQbCircAxsTB0WdCiFZZDwyHjb5EMvCpzQEWlJsdBqtzYWuTJVTnqDCtvgOUecZTzDFR2cM3vvhVbC9wVnDmBuf46UhznL4PJH1ur4LCq1tQXvEA3MV4yG6u7wZJ%2FORTlEU58t9%2FM8BQd2%2BxCAZJEukBKxUF4asUIcmbQKEv7P3ESR5byId7aaPrMDvZIf5GVgmUIU6QPcjvU55ZyHKfzYmN2Fr%2FahvAx1Y2PTOeBgAcUrx5WDUIuEJaMXA3%2FHyGj0LCj5FdYGBbPVBLc6Gor%2FAFV1CBGVbCJ2Pxx9M7CTHsbyMqvEWcaFht%2FnDG9kwC14UeDgE3%2FCdicfRXLoDXhVNG0N5XAC03sSfOGb24m7LSMcUryWEvrpdS3VojUu91oCF6FF0sv2psvJ55WbomeSXKeK6G2yaYHwt%2FFi8a6JrsbK2z%2FdcZt3ZlbNf9Gpxaj3PHCJJRv028PUCfT3TXym%2FLsfcqMNUqwSLbkH0u5TSCNVRdX7X0KGOiy4OGcyf5YuQJ7DCD89gy7YuNcZrO57pK%2Fuugm5cXvM%2FMN98F%2FD3eGWwd6LPAxhwwzf%2F%2FcS0ESF8WUwDPeQxcf%2FokpM88ZMpI%2FekWSqynjK49QbqMQkDUUbF6%2BGhVLDY%2BU8vCdM5xi7iMLza%2FMkGOqUBle%2F%2FXcbuJvAdLrYgZw0kWqC4RXg5YhnGkQCzbECc2edvX7RhYTxPxliLQ1uh9COFL0TJenedj9BOjYZ4PyZWWPxWANyOEzFc1xLgyJR9Y38AhbVy2PV1TnYd6WTfpecgkQe%2BSRs04lPSyd5DGerMNPpByOJcRD5P7A4QyZbVQ04mzG4JiDTsaL7gJL3K67JqEvh69ymovjVtMs930iF7mBj55n6v&X-Amz-Signature=cb9e53aeddd3015ba99185608b331ef26686bc4f733eccbe1b27f79a28bb94b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLRVGJNN%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T024027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNtB3Wb7gxoPNumT0cKGYn4LWxuPqgRPWGsGf%2FoSylxQIhAJDr3fCN5ZfG6qfcII508P6ZC0nL00gEYprv2n6KUWFfKv8DCHMQABoMNjM3NDIzMTgzODA1IgwvXWobVtO1OZp8JLQq3ANvj8ZZrtkvi5L0kbJyJRD0wsWsaWC8pBpDBIE5vk5ltK%2Fnb%2FuP7Fxd%2FctXILnG0Ls2o%2FXyAgfhdsYIhpObkzW8MRLq5vP2X%2BPqKrOiJmY%2FfrWCEQTRs%2Fc7LOJzfihRIMZrxsoo2Wc60CJDD4hIyX5l2V0Dw47uh%2Bzd9a%2F2kQFgy3lNBUEUsm5MNCl6IfsX2rnGTfwRDlkhZUhS1HCAnmL4XGD7PWUNIyBBUA%2FSPuIznQR91VOTgGV3yGVjb1AhxRPf%2F14mZ1Hsi8P6TQ8prTgoqjVC%2Bgrng8Gq1UOyQyKY5fJ7%2Bv01TG1ft2eDCJjT2G94VV48SQYQJM6bI1IiZ2jTDKm1PwoGyerl18LNuJhk7I2YTfbMwzXWol%2FqcXUIlKX6Q3Y6CF4dMpWbEUSd06U9Lljo%2F5Y8AodwRhWY8OjHAhZEUEyBSHkHUkFzuRLDmNFBoZxA%2BKPGckXRNUqhLmLhzTu73Vhx3REY5Cywv50SB4eZPoRJB2LvoWwBzNj1t%2F5fPVI62kqhXPgBDg2weuAT20u91MbhXmpyCCijV1IiO%2BMUk%2BHgBUuxzPoNeuv6wKYXfyU3cxVDmN%2FwZ6BexD9s1VMUOMpzCMHT24NkEpOfXl2PvqAxWEESW65jnjCwwN%2FIBjqkASmoycGLyfW97CXieQlSFtALYAE1aO84MmhChRg%2Bbc92T8AvRjoophMVJQC7ZEuYxAsWT7rmy7T32DGnmt2x3DiyN%2B3K6QMonJttSDFUlQ99qMbFFZSasUmh5QzJXrCELUjie7Y4SeSFhs4it2EGG6lZYfAB%2FfHsFg1eQGPC8%2B7Ox3iujtoe%2B0l2gCFTmfH3yjYU4MBuo%2B2NEaDv2ogYNTI1PrA6&X-Amz-Signature=4ba7eb495a97c5683ad283ca1815dab7fdf73efcc0a12b716a5a4d2e10d847ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




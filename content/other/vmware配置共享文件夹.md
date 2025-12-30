---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZTSBMHF%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEYYIyH3gUsr79A%2BUZ8kxkt%2FyAMxtN8CetngpaZeWpZSAiBalOMgDBdt6C%2B%2FMwUubGExaduibvB9BVKSgxjGboui9CqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmKz9ykrbqFFcB0X2KtwDsTVLOE2QNJbrJu0Ibz7ZZeAaUAaGnoGK%2BVlcuBTmXltXH%2BPYE2D%2F6%2FHIfL9bTDI9jfvyHTI4dglS1dUd42jkIU%2BLHEE75fnbzXrTl3fSTreNu6wst11R7q%2BREGhKGWl98AkRuGSaaWm%2BQgRLGTrx04IHgbC4VyQV7vpls8CGpYnXcyZpNS0O6Sd2QkQbHPPiV%2F%2B0YFFeZLJlzhbuHgRlhZiu3%2B8ZL2g9XtD7AYm6o%2BYwheTJ3SUd7KwTM97hNNc8OBX2bn7KImQyFl9gSBksNT56%2BINnognlsY3Yd3b%2F43ZIFsKK0ZDSV5xsmXUnMk6Kjnm0lQkaqfHZ7Gphw90yMgu36kH28wDJUUqh%2Bcoi2QvbRRkoCfsmxWMUBCGCPZyZQrocuwLQoJO6p5jExGQQiGZfqsQqM1GndUB3VkdU82Vr%2BEAxiNwhexQBxETYl2RCjorWQs9vdQKsi0L88vpSaBgp2N2fEoV9WcptXAbJEbBIUPq6phuBJwZw3KBGFdz8Zb%2FX9CKAaxxzrL%2BRVx%2Bhy7eOglrChrPwaVPAjyiwbygSUtdGCMuHqCcMa3xNBjyHZwBLBr1R2ymkfAHkiBMR%2BCZxCacklIwu4WXjxMpOX%2FNwhusLsYNHQhQloQEwpt3MygY6pgHxGNAr3XsxNipjV0%2B6gHTIjmWHks0OHyTiH3VWECJBCV80UBy4mFWo0mluRC7mebIozhhMC9gJA10YQfnhinZLASFF74qq%2BGmoapAw1uCt%2BKB3hCQPTjvSnsggHLepTdgZH320iDIFitJgcYsvqOrzD%2B23TVa0xc1UpYl0%2BKAL5DzRAGtOCENzmkdziUYlZnuIbJ3AP9Fm96PEuK0ZJirWsvM7Zl3V&X-Amz-Signature=24a6b92b620dcabd1534f4b4767659917caf433e2d73dc35157ddc525f6b41a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YYAEDHH%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDhZSbdt6h3sUp7uwam6cWCJSvKxNXi1NqAZvsEJXYHOAiBwfKhPoNTiNdSNCJoSTqmY%2B5udziza27hQcmA74E6BESqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiaCtb%2B83eHaxoHkKKtwDFzvo65qtZvuDdahpyH2SvqdoRdHvUheEduzKv5fq%2B9kw6RoHZ%2FwKBZlF7wIERVbPF%2BGAijkKoSoIaCcJFDzOlpAs5hsQw9xJjI9tRZGR2Ek5kBVhXH9J3UiJ1LfG9QxTwWKPz1BLZMTiQJfBFF%2F%2F1zhOLq2xo12chNEQx0JJknQUUGbZaqi7OhmVZx6B1FQlLRyxy%2B7J0mttwDhIwGLeu6Lkej7goGA5zZQY7lFLNHYbwU4uIA3BUD28HFL7SElfcyMbPkcnI2wATkpf%2FKwZmhSgMDuvQK4G4DQiFE2XrVlZN9HAfemmMx5ykwyqlSusWFGqoPWHzyLHLKeMwyMjtcj7rjLDAdxuFyfq%2BC9iMU0SsOllxUmI%2Bs5ncks9y9zphTiju0DoNTZ%2BUAOdqFWA%2BqVUzzL3rgR53Xd%2Fh37zfHzOGuFrKddNxG1auUXFxFjpQgZXhypnLd81g8SED1QIEp0qWxNrRxsjnJC4qFlLF%2B8bKfKL3x6QbA4dXCuNVy5XTX%2BDL324AzxoHCl2nRCNI4J2T0YmE41Kmd%2BgljqriKXQL9%2FKXN867TdVXIriSS3Bv70rAbeX5K0WwAuGK7GhyBRSzi4qdGFuYMPPKplkYxGpZgfyBqebvZ4F9d4ws%2FCvyAY6pgEB8%2FTyalp1NNR0SnHTF0xq6o15KL37aU26zv7GTdNIIS7jMdYWZfna15MF9GWQPWfSUoxPvIzG%2BqIUV6AA%2BA0eJObVCx39AFjT4l9Tp7ckMT8hBZ%2F4t2jXizc72kvoTrXiuVmcgVZlUxhxKbjj7ThRo0rj68J2%2BNsl3Pw1UTiOzJQ8OLpsEB96nWlR39Ag9yOof8KIGWSdC6KUFNxUi%2Fs2wCVMcvLA&X-Amz-Signature=bd8fadf5a6636fa11ab88dda9f9ce64ccb31e213bf1ae5b8cc9f9d054e14a6ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




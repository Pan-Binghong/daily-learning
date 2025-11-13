---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UH6CATH%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024842Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQDOctZXhlGhxflaN5t7nrNi8IXGWds8NXkIaGf5u9UJuQIhAJEcq3YO8OjltSefklxzDxrdlIn3PyQ3eWWiJQA8ZRgFKv8DCEMQABoMNjM3NDIzMTgzODA1Igznvd1hd%2BVb02SZYSgq3APGbq3YpdyABQWlmJ5vTDxsip50M53zPszs46qVSflE5efI3J6YZMX5YBU4ES3nZxRWxgODMz8x4uAN37Sl1293GbwWB9bNyQPrjLWCdJ0OGaEfgYJ85KoRIko5A9MBaLvXY0McuBCJEwozkk9rrfSX7UpLmKlkhT3%2BEOsbF7TO%2FNq%2FhrmwsS%2F1dHR6X0RMTHtNp49oOuIl6hNKVSAiXHqISz0XUQ4rMAVGi3nJpboKQr2LMvmHM%2BEDLaJBNDEB4DHpz1x3WMnI1OCGHBvkFQX13KfesJSw%2F786PF8XytV7JFbhtc%2F2MBRxSgPvo9F9rpY%2BiYp0fqHUH8oG1oCvrKpBsYhW%2FxrC1r5pzrCL6Z2sqhGFkjn1s9IGVGn4vvCFsr8JNzoCUeqQXIqufRPB%2FuW30J55ABWeTDe8xuwfD%2BXyVbjRYc%2FA7RofsgNyijHm6ARj1n%2B6a9f4dtpEatzqQVOkHoeScpAx3IPsn%2FB%2FgfMe9vs64r2MdsFouF6Cuedd0DNyPjtXQIDwJeUBKZTh132Rk7haXo0cfr%2BbTLYKoyBJwzzfeRrkEGkd9pgxiHYd4AmadnMliUBwBPrQP3o6Bt6a0%2BTQsiNLM8P%2BMqykO6jnPa6iTtZME1wbA4sefDDa8dTIBjqkAfYClSR2IlZLGauONOemdE9A0%2Bla5gESXovHJq9QNvF8gD1ZsiUR24MA1Wjx5vFv5ZPmAaeenYfO4%2Bx20e%2FgYB3oQGNTx4S%2BFWNObxjILnEUvcMEaab8vrOlXBEoC7sJaB0EzGiezM6D90zz22YnXdaQPwo5aw35BmfNFESieWvCteSjkc7Zk8cNaRFFcDkubyrrkkfEVNFlH2yDEIm9ZgFuGd%2Bi&X-Amz-Signature=ca0cd3075c1fb5d2de6c1218c708ddc153e77f7e8f19043caf9db774680f6677&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




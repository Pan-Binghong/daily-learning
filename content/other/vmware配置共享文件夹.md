---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZHIXNT2%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025820Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQC6ojg0a49MFktmUGAew1wtgSFXG%2BNStR8BrRskBsGF9QIhAJEZ8h0ndrJJTXSiLqgi9E849LZbkRjfKzyQp7g0kXghKv8DCAMQABoMNjM3NDIzMTgzODA1Igw5oAkazjYy%2FmFDN6cq3ANWx20Qm4%2FVVYDrMGiF2dW9QZiL1jXE7I%2Fx4%2FgR9zD8fu6H3KOZcowF9eCkWosYm3bjcZyc%2Fk7xQlr8k70ShfIf8zZCfy5t1pCb1ahNWLKTY8W5LlCoswWryu%2B7KcT7ekJqqTtjKy72bH59vQJFYJRkVcb8ZQ%2FqgF%2FyLZJNrWkfc7QbyY7hed6cpppnyDux%2FoltRrtShuLVL0ZeeWI%2B9bsjIpDZYfgZgoA3iq%2FCSE2bdUDYxvidcFJi35OtxIp%2FdNmNZbysRrUOjFStKzGQdtyXLvtwLdcpnQgdGQrAdYvAk2%2F1slawI4y888D77UCxnA01dUmyg%2FSo3q%2FPyyoWws418mjmaZukQz6XuRDhuF7WKgPMuZuppyB%2FUOHLmQZc05bDgadjp2BtpZ1spUYqhSkrTSpHHBs7Vp3d6BgEB73fTh4VUfIpDs%2FIdwKr0eOCXOx2Kw%2BdIqMXdZ%2BECVQYh6lr8KT5iEKIkr%2BguPpyG4GWHWuInIwGn7Nk%2F%2BBLYGY3zzecW7YiocuTKvV5G5h1qNbUXLHT7NiKjFqhAh%2BEuMOFnCWLgIIkS98zpGnNFXPmftVpgZ8%2BUqZMZOY76h7A9GKEoSsKabFVeN6KvO92kVkeOUmGa3eDRAOVxdBINDD4ztDLBjqkAbyOaGJo%2Fv92S%2BrV8aGUwndCsV7iw1STmEtTY9KedRX0m9AhPr%2BY18CtXTh702QwZu%2BDPe6ipFx6K3CwfYXt%2Bo23RAyb1%2BL%2Fis%2FAk6igZs1B2dQUYIjyGXnUqXnR3vNOVFyivCFxT8Nzfu%2FJDPQeD%2Bx5%2FFRsRroueyFLtm%2B3suC%2BpH2IgX6zxjSU9mUwQv4aAlQycFrYWxTtc9CQVKkGXVCvgmxt&X-Amz-Signature=711829151f68143cff4bbbebde8b5f52b62dee4228f07e056ae2464cdff18e72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




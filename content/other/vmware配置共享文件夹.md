---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCVRQUCL%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDSqHAPFJyhe4g9h0tVJ3mhVynuO0gQ%2F0i8oylbyoTa2gIhAK%2BRaTWuvVr%2BR7fj7hRECJGXzS0YA%2BAKV08IX3a03lxlKv8DCEsQABoMNjM3NDIzMTgzODA1IgxfMUh%2Fc86DmOPwWM0q3ANkPPjYJRk0aNVU%2F5w1%2FADNfYpy8CpTrB53bA1lzQiE88LeDf0OEr1sND8xMkdKqaQVS73KabEnGggQkZc%2BA1kn5NxiDFPIcQhXEmS327cchMT9hs8pUkq55P9ehCGYkFzKRtk6wmKmdPXO44tsunYyVUkCmzj7bE6SH6CtwJk%2Bt8m75oKYSihoOgQKZJxvSxk6ODzbM42XaxaiXChZFH8IKrCY84xIxYEIBFBvJgHCQhJ8JQOEQI35JhHPYf%2BxT99EQgZ0XF2ak6wj7akloW2jxIdO%2FySF9F3lh2dLx%2BDq2dIRzqVUBtcfb38HwDd6IUcZfj9VaFQjcj9%2B1Qqi5U%2FHihg2AuuKoLG9XhIi4EKw4RhP40IRxc%2FvcSAMfh1k%2FLi7Ki7%2FaeR%2BPaImSznfhibFfpr3UbrkleP4ywSUHnKc8BK1M6lBDYFBMoKc1BDswKMNH%2FF%2FMexHfD%2B4NojVLqN89l4cayzS%2BOJlOWiBIwjWdxeyik6OZUNrR%2FIhEcC%2BFHunRuCwBHxwxTUvXxRkYs3CLlmvNvbeTDhiyinskZzFan339fPpw20wLexVT09W%2BG5yVIPrsjKvL%2FR1n27ExWnONHCy7BSK38kxdVXxsUhZtgRWYMtxgbrXODI76zDc0rfKBjqkAQ1dXKwF2CDcHDV%2BlL2MildLwO3E5zGLPmqjFVZ4FtS1hU8hpGVZe8ebLMognthV8gPmlnass9LnV9ttJb6%2FG1OhFjA0YK9NbCUPRo99%2Ft7UGeeZAdBJPQ2dCsL1pbotM8qFdU8yUnEOKAYqo0swM3ovO35DfOBy%2F0VRGLEKDCtt50wBVACIxXz9HOiJbTkE8U3KnGuHf89%2FCI8SO4Tlfmzz6PDq&X-Amz-Signature=7298419c4329454881e58e762651199d5bf5fda80726f092d22f159df5881b08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




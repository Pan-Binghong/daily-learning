---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DU6XUXL%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAcb2kq%2Fpr7KaowUTo9NsXr8zYHggwpiH7NeTZF5YoS%2BAiEAntnhuK3PtR6ii8yD8nrrtAQ1nvANgGO3rO4g5Rb4ZagqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHkofT0h1mtkhH5PbyrcA5%2BuNSg6Qp%2FnfADcIWyVIznQ8hmNemj82cUjz0zY4Mckmfb7nOu%2Bptr8UH08Eg8MAIFTdCmc6AAteK9JKpfuOfVsO0LYkNj2%2BInLlXQnaY94uRk%2B4N2RDFZLI3hwssIj7xt4mKVIdyeAeajP9CyizbLd%2BWTBls9uZ%2B18igQQ1Bw1DuyZEbEqAyB0KQjBxgKR17LZDenE5YgqGNEzYTju1z3LSwCeqg6e3td4ni96EC%2F3Dw%2BbqufkCgzWhKe7zxR%2FCGfOjNsL6lNcg99lyRZZCgu6pZkSOPEFx22O%2BJvI8KjGBEvc5oZhoUix5gTlx45ELW5RcJpiP4Jk5Rv7G1QeHWoh4amEqJWvJxlFrh%2BhYCnF46yvqRXXwt0jcPK4ZmLc1Ewst6X1YTS6CzxV1rUxXA6fao%2F0TUGUSdjsNNOF%2Fkej4%2BIdmmD4JNGOmP7aTPxsIBpyBs%2Fn2C2j8ltjc4NbXp6YMKer9XLOihVraYRI8e8se9RoX6J7C%2Bw2pTKgy%2FXM%2Fo9rardov%2FhOHGhln29VMM2qPc%2Bg7LIIsta1fyQhHIt15EeyrbXt910pszri4zUpKVp4RRYef6l9AUM4a3NkSW%2B%2BSHP0dS9t99zYEQxPgA0h0XlvI98EuVwTeimIMJadx84GOqUB8rUuc8HOtaWudRrOX0p2kYg%2BNF1vJFqW2UZbIJtl6GO5GT%2FG%2BslfdaHSkRmo2bCZholPwAZ9S40VrRKtELeigGpsnLZu%2BxIjAJSJaAPRcGiiGvA6VNxH1aWMJ38J5iF%2F%2FpFtmMVvm3GXNnxg7CZgjFkg6pwfLr6gcQG%2BPOyvDwkoT4d0ZTHCCqWnTDdVgpY%2F5MZsknbCsJ9clVVWxrY3xfXltDLf&X-Amz-Signature=b01f1d24fa5c766e748f1baff77891e0387bb751cf5b1d8c31f92d88f968144b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




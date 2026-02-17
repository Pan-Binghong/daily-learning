---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAOGW4VM%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJGMEQCICQ0ayLys7RlND%2FVyDOA%2FTbvHndpYktGT%2FLw9s%2F9jeICAiBnK%2Boe7fP6qrrl6yFGy0e6HJq36xNF7krYlDgosB6NWyr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIM59orobu5RJsdKCbEKtwDwh%2F3Wncf9lei7vk9SbKD%2FEPcsu7iLxPpRwMNpGRHb%2BJD5E704OHjVoFvoTj1HEFZlWjnBg4LTc7LFLEdhj6ifZd8DvxPnUhpAtoaXaAuHC5%2FlhGZwN3CXDZcgmarQKq%2FXC7ZxN8iMHsuQCckhH2v%2BCK%2BSbIDwPTPN%2BdHGx6cNxm%2FdYS%2FDbpxOmBcgzRwD5grN5M6pUsYlroldeYB5rGtC9vHtaa5ivXR8SjegiHWk0BLrBWwjqm8APs3khwgu5IL1Pn8HhDr4eSL93W2Vpuono0pOJC3T1VF325zj5XSELMasXat7Lrkwd3n8Skon9MGPPdPbGUviDTgW7xRtYW14o5DmtDiPJencUjiIpcfHyH3QZMkEhNL7ZfMLGOwZ5BQ6y%2FgQllnXpzd8BdJEEX87OhBhcRf3bV9%2F4ivCbAWp9cpmZPJBEdcfeLVCSDUhpic7VSlDFYU1xM1cYROzIZAeNgBLVCNMruv5PcjENf8OlN6T5CLZcL42UWUKNFisfWPQ%2FWLL8%2BtyQ5mgv6ki4AeckbY7MEGHtCoYDxxuKHMkJdXwP08LwzkOm0Ic1JlzYLGeQsdvXSv7eIyEk8MJhZ9TuSKeejkZCQyPxQszk9%2FfmVlMTKxDwzNGFd05wkwxr%2FPzAY6pgFbuUT%2BzUtAvzcD4nlQIdXL6OO14y0D%2B4nLd2qFQnCk6jXuaJNcq48vPPG47ukXjfjsKv0Q9%2B015HlnTpI5ZEB04cWN6HKP5Wq5WCnHXtPBjgU%2B2N%2BJrkngBYMMp7Yn%2BnY%2F0FzelUwS4dCQ5aSuPCDoe8shJcwwz0hX%2BU1glY4W1NdyrkNDSswWI6okKC9uH%2FCdBGFyAxY5qfJ%2B1zhgrBsYUyeYCVdj&X-Amz-Signature=169fe368712310dda76e04d9a87e8807a9b1a11f804f8ee34ea6a4008c67bc6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




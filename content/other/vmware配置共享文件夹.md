---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2G36GX2%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIHJmANzqhyfgKxJXvoR4SrUegQiEUACFDJiX9qN1tGufAiAfVKIY2UvXKgi%2Bmpvh757c7qQQDnpLpB%2FL6vq4M%2FCzKyqIBAju%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhfS5qB3AykMJdrf1KtwDVXUzcuYQ1tN0dZfC67npwh8xGE4hdCp853P%2B0a8bbgIil6DarlfgrVMhEkMXICCGUPQGHa7G0Kt3Y%2BjZiM41j3i8XGbKMs%2FliMM9cv3%2FR%2F5yeutkRr5pWn17yN3y5LG5Fmvn7FwEOoxY9qPG6tFyLC%2FCe%2FxKSm2O0euMYZo3fbn%2B1npNjP9sDUmA35muHPrVwIdb476heLBRtijtpi%2Fj5qb%2BseWEUH7jgumoL8qXy%2F%2BoX9KIVDDcrrljnMmJPBhKEQxuLSvLYkn3lgbtw8%2BgqGELGe2f%2F%2FP8%2BOSVK3XiOz3L%2BwiaKA38XEDM%2BbcfDy9lB5coENrOWmuIRf4paC8%2FKhlMD0E2tu5tdJD9qUmJrkjOyDUxBnx2I3sJUa5MjRmsNObwfK%2Ff8zRn31d0UmDGv8SVQJL0RsVcZVJH7PtH5ksoujpszm6g%2BJOhoYDUa4mYvl%2FZc7QAh5%2F0cns78inKPw6p3qZeAGgcq5FcCfwWKi%2FMe7i0%2BCamqWTkUFuxQTT%2BPWmaK2DOJIT29um4LSlbeW2Tqg4un7uEOhnn%2FVLNngdTTMGnWiAI0pSZ6w0mke6Azu7ejhC8ilvucO5dDDapZLDmR8UzQyaXJlRn5S3FWRvafMVy7Q%2F4ieTH1eIwmJPGzwY6pgFoX6sYQ3QQWIezDVm51dnzCxNWXxBS%2BY4XjkVeV1Z1PZHuBRTeWTiXoNoX1ijhIMuTfrE%2FD%2B56H7vDaC79lhsVC%2F%2BB93fAUxwgXuo%2FjO8vKZkoXYYlzFh7OcY4dEpcK5N3tFgaGaCqy1cDPdlOqeIKvdZp6QLqICpcSCP8aUE%2BeDmcxZ%2BokkBaMRer7uHdokaFUBq0kS5vRb%2F9AjzHoMcO1RT10RWA&X-Amz-Signature=cf5621f4883a8972abf264beb49c655bcf87824c3866ed60c84df6ccbf23fbea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




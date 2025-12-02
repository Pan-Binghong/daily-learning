---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEYZYLV4%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T025052Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIAuxZfdy3BQYbnOyY8MajWspgZSh3nbckl3kw1DyWqUOAiAEK6T3ZKL8i3kT72AQK2u23MHL4pz3t3%2FEZYObDRX63Cr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMmVvrhNWQJRh3VLPhKtwDJvyiOAAHuNGmBFLFMoz0gtZYONmMjypAMe3KymEKRF27X%2F1%2BZ49KTajR28JUKbH483XvYtiGvWUMGhxDAnJs7tlTRdjfvwkh%2FDWhxlXBep2%2F1gMFxRBZfzwZoAA0fGWMGuj8eL%2BOXdB6zzUN%2FrSOxCW6AI2nt%2B34hJQtWUzbyjwMioAd3XJnXqEGWI76SIG57xLXbdQclMd8iBllJuHD4ZYNhcBax9es%2BPyYY6WYtlsIgi0WAjJIe5u1Ru58N4E6%2B5pNiCS3n2PzemABq2CNjupBI4i6we2nPlV5xwKwz6JDaAlWZGms3geu7x718CnkL7G31tTR0Xpx0lW4dgbVPMEugQCVdY7ZPicyYUIeQZWx603pnYQhAstl9nDQez62lcyvehmuCsFjQVF5f25dXD%2FOvAtpGnwdrgucVnSmgfvR%2F2%2BWI63UYvdnsewj5WPy6v8cQsOZOj%2BhBXiRhumtD4MPSBreQ2UJTiHueww%2FTG%2FmJKFFOytWR0Gnf8QmPiGV4f8%2B%2FIYYjieVJOtEP5wDRQc1TaCkOGgO9U9BARDUvXw31O32G7056dmDaFvHLACAwGoS6c3MNp1ytGKohE2pc%2FPz0kMdcDsyC1GxViv7Yio1XLkDzpRNI%2BGHy3ww5N%2B4yQY6pgH40n8vJJ1KKAh9SBE1UAu33g0S%2BnjYr0Hl7hF0Ruxtso9zEx4oCfSNi6I443fIdPNQq2uwWFf0qofeDR19eibgjfnJyQNzQJFT2yVwiKgj33kF3tuT26o5aGMsNxqKnLOKzCNH1l7U26uFUIvWDA7rrSi9uWdWqoFi3ku0x1e2g7yPaQ9ioCY4tlkeS%2FP6m8AIozOKgucoqj0XL%2BGrn7HpxyvA8XTm&X-Amz-Signature=8205169213a4aaf2ba8c1f7bfa532a1d0b3f06db71e9df3c2c77a7a4ed5e54cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




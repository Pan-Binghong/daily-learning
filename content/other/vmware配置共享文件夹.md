---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EGZFMWV%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIFSo7Dy%2FMQ%2FB4HSH337bU4Qgv1MGow98OjP5e%2FDW3xiBAiBxvpT1%2Bm46iyPJeN0OyjtDoGyEwd2oKxpwxAogdn0T%2FiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwoueYgjwIEsHb4qqKtwDpPS5dkaioQoCK8zFI6WgafdLVbZGbVMTY6Xy3fmqws6WPA2oww5wiPfMeprjB9l7cPwmAI0zDVXfXt0r7gOJWE6QXVYh4QmfqZMfD6ibOwNNZos87fhcOeY5mgMjCQxjszWYRVGvQDy5kO1obzhk5QWLY%2FvLoxf1bbTMTNEsngGcp13nVzmQ2y91ughdRKFkgKEVcwcfs2wjA03Go7196KYXacd9h5pfi2g3JGxB4tPrYl5AIZptcFUd4Il2twxLrjcfsAhT82vZsNp49rgoM%2Fp%2FCZSBdj1oNTmEpVXp77hS9wEkeK2Li95tdGnsIE6RINd4M01jBkrstewFyPwMvSnXAa8bTdNe2He3meX5j9EbcnE8OE0kgCXL%2FVT1M9uBwcGxbnilAvoQ6DIrsgP5WInOaSM9o%2FX5IMPkAKGvQwazy3Bixdp8iJj%2BEYavRy8rXE%2FN1ikSotym%2FP7wGkV5iOblzq%2FzrFkQC5EMWJchzxg3tTXSD6eaRORB7ONkKFLcZdxjgJPEKomFu2ohAcdtT0QWhaVZtnmvNrEvdoZ9r%2FoXF%2FvT16fdYjlu5IV6NHpej6LEKcDj0HWtY69mfKfmGSteMCua%2F4d9ZC0qN4cZoUY1lNhZf8IU5NvafMEwo9jFywY6pgGtJYmD7%2BD7zUQPzHO4ye7zVkBCWCC2kq9HiCTcjyDQ0R8Whtq9dAu8IYS3HcnlM5YabhalqIEcutGvyb7irCwEIOxOXcHyacvoBCQiLWJ0jlCzovR0TMW6dj9rbZD5YSnP28AmZmrrc6cY056UvO6W2%2BqwGyCrJQUN7ahhKWli0toSPcBCnZZQUYQGLmcBIJVy4N0CosC4Js2Jupt4TTvmfbhXWVeD&X-Amz-Signature=3e97811845d88ba0c6e8d9a6b47ff2c691c31f510a7d5142341eb1679db90c9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




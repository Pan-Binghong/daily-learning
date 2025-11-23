---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FVGP6VA%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJIMEYCIQC5ECJho6xehnY6QNwJgIsYIUzTmrEgirVA4R9evh431gIhAJAWHordFPkWaGa0Mour8VGt%2FinnCGn6Rzwu3V3jV6JiKv8DCDIQABoMNjM3NDIzMTgzODA1Igwzsk5Ymrpyb7G8L%2BEq3AN98H5gmfusyr%2BNm1tUlpfgGZ6PcPwX%2F4tTjk%2FYrv31cot2oINRf3B%2F7lS6sE6tgko%2Fij5rhwixBbBzEb%2BAdvime6N%2FlAvHyGbf9ZUbd%2FN1ZOhyO3hTwZOtnN4L%2F2z9Dl1MYpAXMHb%2B1hOw9Q%2BX6sa6fJUWyt7%2FoYrYD3Xz656vxYci1tIhMKxnvNhjiFM9Jq4Lgc4AEF51C%2BgjOeNdhhfZzUSNg0NXQZ4Synbdkz0Bis4oanImdAHdNol44QMftQ58KoeezBwQ0KuGR9aH%2FOQlk05ol7PKHj%2FTD7FP1kaP1hieIobWuqMpqHyEVXBy4ltSTmtQNwaYSd62wSJgZMKhkIEaVakXTy6ywKUR08mK2TtqX7pA%2FMs0PT%2BfArojwkum4toLnm8X5nf7iCY09xtgbhs3j5ZKarL7B4v7LDIZts4GFWiaVBnPb4Zdxh5gGrh68FAGC90eo2oxsQls%2F%2Fa0hbqusIuT47V%2B%2BZOVcaY6O5zNKOrYqrJe5g%2Fs375wQ6frQQ2nUDiqTxWKgSk35nuz1BqTk%2FtxMAHNTDI5c9%2BMCiI%2BJAafb7zS1TrmTS%2B2VYj4EDYwRIWZ8DAulAXOPUjZmX1BfFHvub1clwU02c2hf2i98X1vqNHUtqb2yTDXsInJBjqkAfQpZHXPNn5QB8reNxBWyDBIY9Z%2FBwud%2B60uH3XHGpPu2FhiYqLvVL3lzVlaaCaFuTsx58Qv1szlweBxxH4rqtLxIk1jVo%2FFRkZ%2BydJ0hSbLwdB749Sd4kA%2F01r0IYfLCNMTDi88JPF1wJKEj9fRK9Owgap48xVA2zhCb5R8icj%2F1YtokJCi1Aa92JpkdusMCJu9YeK0RxzVbg5vAB6eXl11aQj8&X-Amz-Signature=f0d0d3f23ab1b7017fe81a6e4393ef7aaead35cceb69250c7b5df8ffc6302e43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




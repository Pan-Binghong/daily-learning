---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677O5ZM3R%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQCbTJY6V0Z3J5DFVH1ra%2BvMnNn5bNDqGsBAdH%2Fs%2FQtUewIhAPAqnROlZsKAyPRQL6xMsbHpLduwG6ukM%2BcXnYW2aLfNKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxrmC3TCsDOQAzc0L4q3ANeddUVnEd1j5sWVY5RT%2FDlr0uLNVCa3vQPxxbWvl7GCw0usQMLYyyIFRkTw6ujKZU9OZAn7BT55JFZA3h7ihIstKDGvH8OoIddGLV4ZsTtsVy%2FZxiFbBIejXzKZyFkWMdfDXfXgfLiFNaIKGsAXGMDV4EYU%2BdCNNzbqPrQ7QOiPjD6m6tzEO0I%2F4oQ5dTjMDpJhZTl8PPJjRgTtKwKi65WixB3K%2BR5ZFrNKOCoB5EfvAZrKnS2Hm9teaa0QGDGoFcJccirtzTbwpsoliXTOabQvz%2FMwp5xO5kqBKvkRQQQBOGNzv5V12P%2BXwsYId9z%2FL4TdJS8R7u2y9siyVNq03xvydXgKcUaKtS2A3uvXdYWEBIwDTiODHzALoxl3cpUFtFT87TWDr6g3S2MEsKA1IvyntVguNNFyS3VDsdg3Zpjcjdg7edST3qvAUqVc595EIU%2F82wbfDokADUOd%2BaP6R1n7%2FfdozeidWQ6c2BHH0mALrpYM%2FN%2FXWmCIXUZ8pP%2By8h9AF8zKbwlQ38d4KFafncUtFIkDdYUX74jyC%2Bk34k1JVoCUMpeOKrenE%2FqGEwB%2FhCCBTyJPfPBv9ED3CcA%2BSeZ%2B2%2F9DebGRP0q1v%2Fma1F5GzS6Cjzx5uBq31WKoTCYurrMBjqkAX773YhDWD8goZcrIkGnhcyhBR1x3oVNSvKrx5bFdfKslpaKRC2V641brYWrCgymKanQQNhkh1AvObOn2hNYKl%2FmwFxFSjpGeekwZ1q8IvE8msIhrjlY7JZXltBSAkngUyFTKt%2B9jdt4wmOEBpGdtX%2FMYY1MO2%2BO1dRYjyG58q%2BEjyJWDZFomPnKFlisiQo%2BoT6b9lNQdWUCNUfq5N%2F%2BTKnR0D7w&X-Amz-Signature=ab88471154dba241bfe0f728c126e60c8aabacab3ca90edd0352f053d4e8c411&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




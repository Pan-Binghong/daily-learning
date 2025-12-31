---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WUMUG5F%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEeske0RxJ7zcRSOaVFhIbe08mrChb5c3CzPudFsmOUrAiEAqGg5H6NrrDGl7Mu85QQqJH%2By%2FvCVDugeIoAePLdKFpEqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFjDyOz0gLlNnQD5mSrcA16hr%2FzJk%2BSqlUP6maWreQXEHI1lyA%2BT2tMvWnI4wVteOz1HXVTwneW5N5%2FHEV5xzC9uBz1DkkfKXhKWe99EL1y%2Bzuwg9PHyNFCubqug2YtS%2Bnfd%2BBkHaEWXwJgjwrbG1iO2gil%2Bjk2ozf4dSZTDBiXwChltt4hr3n7hfCEiecMSRmwqMnxa5mPbIp5ES7788SjKDuqfNhbXvM7fsaIy3ZmG3pWXqUaUFPcafDLLbgjpecVQJMlvtPIaSdAcSzfQtYV16KPU3RDaK1AetD3g8Z0r37muG%2FEuhkGUYn0WM7jLqsd5UDUi7e7wkPdXxKL1Uxj7Rbn750QLfgAx6%2Bm61NselQCUH5Pzc6mCWUU%2FDc%2BXXBrFVFftz8CUCA6u8UX4BRs3M4chqdtsQ9IgZAfwp9Y8warBsh1fMffJsIcqXFJZYbg8F3R2fhSk955C1wcHp3H8q%2FOu%2BhxkjgU6gcrDwpqtKPVDz4yjcVUvdBqq4uj4j7TibEgPuHqXYsXyx0wsJdKQVWzikJ7NgeJjXcODWy4aqQGtVRjbU5tBgfLhIrgrB283x2YMO7gP0h9IGiJafwZqu%2BTAHOvTkABU6ffz2LQmgEfykX3RoJ1sOuyyuQ8%2Bn9EY03i5V3cxzFgXMO300coGOqUBD1FBxKymFw8RWK%2F2WklYrocRDxkKjOUS6qc2i2jwKquI0R8lNEoS47VQzuEyDDaITHLjd0slrrnpJS3vR%2FZ2o%2F6HAk%2FpTpVnhJuJ%2FWlOoclbyrD35CthUhO4D9%2F6mD1uD1lmszDivl7vYXcjowR7RrZFpC7AbQ2B%2F302xtT3DgZI%2FMLcjq1h25a6P1YbVAm1YqbPwDpS3blK9q8QH%2Bj4QclsFnGk&X-Amz-Signature=df9d40c1d31529334cbb8ff67630cd28493916c127765b49cba0d0143e42fc1e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




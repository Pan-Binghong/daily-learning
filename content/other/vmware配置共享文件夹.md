---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVNG6F45%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICrUQVX7NrrUyJnruH4fnvYKe9hpKvVG8CnaIu4NTPoaAiEAszuMQYgn8NmX7zbP%2B%2BfTq1%2B2AAGNWGs%2FQWDijJfzN8gq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDB80qID0TK1bYALBJircA8Egcn0i7F2ve%2B%2FCBEXqt0sVuYTuWLP1GQdJNoXwmrtR9mRfuebwWmuhWk%2B9MMnLPRS4uA9Tw8pekGpoR981jxEBZqvY1RlnroNaMd%2Fhe6KVk0ch36HqWv3StOCaGI2rkCEV5oyC9zR7qFhZkLOgOn8%2BB%2F0Q4cpV%2Bt7SJzmD7U4Nr%2FMn9ITH0eR17yMxn8mOknQPyl0Z7GR2rPJJOlgj3gbuVc4t5IZlVXnDoA9FOEz00zUqZEnYtN8bLhaiIIFK9G7FRlgcobfHK0NwnX%2BAHuB%2F0BaGhxcyO1ppwZkIvOj2wSA%2FDJZqHcLkZBFNsKZA3vBpEAzy5NjPf9cos5uC68JBcEofab%2BUbeP9YYzQRU%2BsaVlQEl3ZbaQE2%2FIc4wuQaQgmZBID8cdUe67WljayoXWCaDE%2Fmk%2FrDbiSG5GkkCWT%2BLVJc6ukccWEKolzZwleunlz9PoBM987rVhykMe5pqTgfeMvLe4xmSj%2F8Xp4Fl4V3hxSWWubuI5%2FnBLg%2BX6qqyat6JUrS9S0saruT%2B1Cnbw2tnsk7HffPi2xJ1eWpPL1cyb8Ttpy8wTDc1DySzqFyRqi11umurFJxJQZqlA6kZ3oQD0zxnN77XDYYtGx1KdL%2B7gM8QqAQez4wjFHMITSq8sGOqUBosf%2BCFY7QxqdAIkC%2FEbrqG%2FbnciU8UFNNMZNHMofxZbTuKjFopo%2FXKrVLklvYrt7q7HsvBCCrpsmX%2FE9TRtUH1iCH1zIUMMBwhXGqYoyHrvMahr7pBhTGzlaGX8wnzPl8RgUJMmpJpO%2FwvpqPMf7U4ZKycb5RM6fWnyIS8Dy45q2PmZrgAXk5W3ngkmwyCqH%2BbfPvSSTKjPqo%2BHuoKQUOhzMR1tE&X-Amz-Signature=bb3acc476d4da8f725d472a03baa48f8d50538b5562e4daac71b4e457bb9a529&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




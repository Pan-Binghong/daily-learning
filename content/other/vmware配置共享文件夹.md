---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466325GFWCI%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpSbXTycWrZdvd8SZXjPab6XQx9PAnL90SVt4xV%2B3aNwIgFMQ5rAi6u463UsNDNzSAwzR2HHqZdRWvouSPY%2FAE%2BkwqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGRQ%2BvKEWfn%2F57JMMSrcA1Lj%2FGLZENp%2BfrGchfQQ%2BgPEEE5cxjC1org5sgk1JPdwvVWrFh9PDo7oCWBsuuScAMKqBfyfQNYwd61vyHC577BuNhmDyk3scoBXpLDTznbGfZc24PyZXuHYAdwRzqHgrzMM8enFjJXfNZtDWSnFI5Flbf5vD1fl82yfmSigb52QDfzLs3WbdDG45qn1KjDGrjZgqp3WbNbS8ulxBpy0iVD98IqvCWCdIEvI1%2FeioqbG5JgIWzy%2BpYyvxjZ3qQRFlNuBZz4W42o%2BJtbdetUlNejToX10MdJ1ydIw4YXfvQEI4cEZ6bf1%2BOOJDxftSFg0CV%2B4JwhKlU%2F%2B8YPdxLigmX1hSYE8XZw39YpEco03Oo8fDd%2Byvfgq6yJ9cwrL%2F1V%2B1N8P85LnvsAwLC%2BJaq6gwuPA8Na%2Bn%2B00%2B5MMqNh9LurCikQ2HEB9ycDRGsalzMqSrP7H09Ib3vC%2BMELnA5MjLfBKdsFr441p1kBYdtEgnhuK4MRKa0bMyr841Jo7fR2vM6x7Ki4gPbP7Zd%2FVoRaAgpN5idPvD5Aq5muuJ0xyXmwpPIUYhefNL4DEvZyy19gv70nzHpjuE9p7J5So2N9kBNZ5%2FllJObey9QVuI1dUdRxGniY35p6LY9U2HHlUMPiZqckGOqUBSBcoRtFawgqBD6ASp2gIMdVdCUBDHH1S%2Bx3rvq7VEy0V8PK5j9ZwTs6VefU2hg%2B9Vz11pJ0O%2FmDilt1peSCRmBS5ptaFx%2Fb5kbaUXbGmLFmcsbM5YxzfnHWMZytZCCFe%2F0rTngG%2FInCSqlLcjHhndkaRwgFiC8%2FatPy46IWQ8iMeSPCXc6O%2BBkBRJ1iXmsWrOpaHVkYDUY14G%2BSzmkjdW%2FwIMN75&X-Amz-Signature=d9cbac7b81c296f433c830f917603ed21171fd7294fbc0165706a0e2e9bc1973&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




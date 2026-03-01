---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466657J5DGI%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcW7%2FN%2Btabcjlem8kbpMuQNXVzW%2Bq5DBNeNlDILj6yjwIgB91B6CeEDv9APXpcUu8M29gE747TaHy%2FBV93LGINqGcq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDOY8F4ksIR%2FJ%2FAj4MSrcA7%2F%2BBzl0njmZ2ZqkpelIH%2B1ygMuuqOTvqLH4Rq23Z1PBAi%2BVHf5fYJUJuOIMTcAyO2lkhf6gq5OHre8MwhFUxFCGP65TpuAVk4%2F%2BERWtI%2F%2F8wyEc6ccERo7xRSPhewSI2099S4eXg0%2FqIl8j7ZwMQGKaYAG6a8j3A8Uf%2BKb9bC%2Fg4%2FHnImoeWihU7IUTgAG%2B8rxyoVZAh810o7xOpyH%2Bx5W9cZp4kfy3h1NdXNan8MuJAeYon2GCqbfPY8gpR3WR3oGEqa4O4%2Bh5%2FLzx76v9kFJHtYsUedkKNSBxqEUlEtvi6cvsdh7JJU5rUnaas9VxIvyclN7uhJH70rF8%2FLcAGMgmPsAMTOOgNVtJTRhG6wWQ4kcqT0HnfXmMt3blW5bN7HnrOT9YJL%2FzL%2BQXy5l00YQxcq3Wo%2FEJz75Fnte5ZmHIsh9bYsJ9Pfx4SPvO1RglulWtPImE1oRUzBweFccTrDV8BjfSkdeH6ocFHh1dElWWYdrACaUxg3UuUHfHQAjNLbtBBvTHLscL5E%2Bx12jAKlmkudPmYt8wimwhSWn5BAC%2BehFpYOlHB7xLzGSiHBb5xhw9wvZ86uwHK9yJDdA67R84IWU%2BUTuHP%2F9TcxNl1lq%2Ffj8wUhK7cAdxtODsMOfNjs0GOqUBaS2z%2BITyFR2EfA1MAWWSET9aVQpLCfvGIc%2B3cmBiQjRT9BoLYO1kmE584%2FmKLMZXMMNSkJfYn7yJ3VYhDQqxWllDM%2B1Z727hYqJqnacRKy6aJkdnouHZN%2F4zg2P%2Fx%2Bw0r6GtGLBPgMAOqw1QILMPgZmwwDaerjEZrqUICRbfACDDguwza380Tm7eIAri3guZTHcNEXzoAtJL8FDfjnEzTw3W7Kyk&X-Amz-Signature=d8d9176cd8b4b68042fa1c26c31f7f0ccc257eeb3c9d4ce175472d5ef79a2c3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




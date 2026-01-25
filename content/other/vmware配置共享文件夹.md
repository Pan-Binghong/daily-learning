---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673HJEL65%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQDBwYuynw5UKEkrx5gderhqGHBGGXdpnBf22tKxGcGXEgIhAN2aS5rczbmzsT1nGHLUmG%2BPS2IZsCe%2F%2BVrX4Fi6Z7bSKv8DCBwQABoMNjM3NDIzMTgzODA1IgzvNjHg31zvWGbUOLAq3AOxFa1V3iSd82KqciEDFrUY2aOIw9%2FxJta7crwbPAO60jG1%2BIMKsmb504%2BiuEx%2FdJSJCsFLAkK6W7tPwmXbPlhKUGXQ7ERFvWLW3J0HVSCfxZvNJ6C52lBH5WMKNIkxCzpLIK9M6KEsD6Mh8jn4bS9UM9CP8PaL44qhX5WGW0R2X5kUC6dusVvnaQxuoQqc3EYK%2FkfFRzkGB8HoWN0Yt6kL0LpA4jzN2zxILnfiKSkWk0CKcdDUXpPsfcYBXP5LoL6clGBWVL6z%2BTr16qUrgEZiOBiRDhf4ODOWrzbDqzISYdYHTev4YLsWMd3bNhbVqQnFKAZgjMzbHm%2Bb4GijVfI31DSZ7chgt9zPFQ07IAlgh0%2F50TgbnfAasA2NCOqeOYn3lyNe8%2FqDytWvZwKCWTm3AB1e%2BdtUh%2F75Ci449WOJd17lAjhZxRDAW6fKuqzRJMYVWNElY4rHbdC5unwo1sExhttAD0vOWncuD13jWj8%2FE9bhE9X2yV%2F6BetEFQseGdBc83ipRXHK5g3eEip4ScmZakZBr4OYj%2BtPYyMLh8hEZlt2gQIx5d3lajUgNH8QaqXNRYIIwx3szUrOUUzJrBMCl9xKz0zk8KIjDvIPH4Es%2FeoPdj%2FshO7SZ3IDkzCYhdbLBjqkAdNOoCSD%2FxwjTduFlZdbRxlo%2BcFBTfIy5aZE1F6qv7O%2BLBaicWAsMZhWjEogqqfpPoEWEgXuke%2FTLcbD%2FfSzy350kIVIbMyrqNUMCh00%2FIz5DYrAAlHwP22zkQEnx0II0WnYyQplhk%2BGyllRTQBvc3pLMKN%2BgGpIc6C66yHFvDDP6RAIjswKG9%2BITqGGwQXM6iTkDzq01FwecP%2FLWUDhfwpLf%2FcV&X-Amz-Signature=567b9f4d1f2fc08f24ecd2fe68380d94054575f8740cbd7280dfcdf96536c7a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




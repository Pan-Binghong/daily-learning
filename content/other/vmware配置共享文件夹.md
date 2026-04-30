---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIKCCJHS%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJIMEYCIQCxk7mQDmmSmNKvig8bXDhdHpzLa6cIHnrTs69budTQ4QIhAIuUIujJs2jjgGBTwj9Jv2XiWck7Wwi%2Fw299ZfBHcPGcKv8DCAYQABoMNjM3NDIzMTgzODA1IgxctPTOIZm9rxvC8Dwq3APNJ1YvGK76HsVaTpeuRpSGNxgYrkOad96%2Fnc8%2BtxLfMV%2BXjWRHWU0UpsJySiOvejzA2dbv7e1q3QM4SWs%2FcmLROxqwXr90FSidcouR99EuCbDiy2cohMg9SQxOSJKe%2BBdItELo5yzPKf2Vf0eHnBQIgmhVwTr56afkipNt4j8tBxUTY0gNJwYl%2Fz00QpRn16FF%2FBfBA2TvGDIdvG4jXVXnxiKjTeVlnmDVuPEoVyo1J52Yy5IxsFxuUXnPo5z91ZGZjbcO7zeTrztsZmHXT3KH75S4cH1us6neDcxAapJgSgb7%2FdB6Fzj5lGh8kfcZ8Yfm4dyz7D4PVCT6TzCmYUhJZHp3LHWwa%2B6ctDUh5HdKVTPDsPYUuYWZ8ihwUUd25jKFeONz3eSFQRLWHsz7V8ZwuGIxZ5hhdM0OFlm5j7r2nXaAqhhj8gw6%2BPMy3gbtITDtn%2B2JZ2DUiRPNM6iD6jlOL%2BAguMAc2QTswDTfUfj1IaVPrUGh6kBVKK%2Fb1BMNUWrN4WKsUCgGJ4uq8lN4bYgLXKWiR2JUJSFeHE8ob%2BA45wERciP3O0sbKX8EXo9DwhpZPPFwZNFhC%2FzrjWkhpTtnV6xEUiYciOZLbdaBMowlbXKgn5vZkpCyG1zjzTCTs8vPBjqkAQe6cAte31klX77HTBV5fPt2s5rcewbdqN9okHZYgLO8g9ej%2FGSGsIX0pgWmqx7%2BAQiFDt6SkFZ%2FcuziBN9O9x8EgM%2BYXt8%2FJXqEKyqaInbLyD351MRxeHzXg1orsklJFBh2sgfdCE%2Bva2W%2F41UWamrYnsI3ulDk0ygxSEzVf4Ps15OYNYT194e7%2Ff9kIaixk%2Bzi3Fj%2Fc6Vm41lsBG1QZo1Bz5%2BI&X-Amz-Signature=741671c22450f9eeb3ce5ed3e473c13eb84bfa879e148ab53ec0c56f6672ad43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




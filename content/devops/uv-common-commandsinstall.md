---
title: uv Common Commands|Install
date: '2025-03-25T07:19:00.000Z'
lastmod: '2025-04-03T07:45:00.000Z'
draft: false
tags:
- Windows
- Linux
- Uv
categories:
- DevOps
---

> 💡 Anaconda对员工超过200人的组织，需要为使用其默认包仓库的每位用户获取商业许可。总之就是变天了。现在大家都准备用uv来替代anconda。

---

# 安装uv

## Windows安装|

1. 用管理员身份打开powershell
1. 运行安装命令
## 更新

> 如果使用pip或者别的安装方法，需要使用pip install --upgrade uv 进行更新。

```python
uv self update
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/792413cd-74e7-4497-8bc9-a54b5dcd1fe8/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQJMI4F2%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCICmX3HmG4mabWATAWNt4PmzBs5Ztayy7YeEAF61ipe9GAiEAp6LE9STwjW8AGh6bzxKKdDzDcvlNKdIyfgTmM4MRW6oq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDFd%2Fc7lQ9p9%2BUzOCbSrcA2kfSPsfYyJYG%2B%2F1pI7MsUOXEMZ%2BqogWuN%2BdwWS4XmqYN77jV8JfNgEV0dXi%2FuvPkRk8QpMDwPb%2BTgEnv9VlALXFyPFccpBBo4I%2F6LbZZk4O%2BZUhS0o%2Bh9mR8MsszUtUJsM1sYO44%2B%2Fe5r8EbELevdkLXhM1jb5RXB2uo4BiDasLxZLAL5ieYlnoBEyTWRfwGjNxKXYEwecNVAvhs4SwE%2B9ribXdTPbF9nq4Zh1V3fEkxgCT1cDugTfRH1bGw9zqLrzHqjfmooMtr2f6vSQCQR6MtHSDXtLIjmkh8vBSeTOvZ5tX8ZgAESzui4oSBgRNwOP7Mjd76nA44x%2F9pquXp9NoqHC92lhLnY%2FOjxwbwCM7eY0YoDnmoP2QpgsRWWVWjTtWSik9BYxJL9SM9VrxxUgbKyzvBhg3Lmjb3x%2BRzCQ7riDoA4CEvVoteXIqrAMlYhWwYpDnsDAFqJlFZmR91W1TXcXlpa3HugYH724EwtDzV1pQ1Ddmr5s3iByC2hlS6O1wqzSw2LoFKCjfwS7To%2BGsUBeEYgji7fI8wqMzjPs1i7a5POgOJIilVp%2Blj4U6ZWNOn3%2BNaOtMDAEkIpyfVpMGPDLYHk%2BvU6B90E32nlI%2FKXXJ4qybPL2V2KxfMJX1%2FswGOqUB9Lz32BsRadSEhRkSOi6cr3j2xv%2BxklaGqLnN9Dga%2Bokb%2BHuCDyLbdmVi7NrplNYA4myaD0ZUYIF4U70Rojj5z7EenuhXy%2BmDLO7GknxYo2XSEDHdAaUxXJnelFg8NV2HEIvJPrDEJMmC8re1oKK6oQfYJc10eC9ui4i%2F2SXQhfX8oGFwSk8tuQIu%2BYsqTw%2BuVR089hCE2nDdjnJONlAPwMCBoJZe&X-Amz-Signature=1605a8248d80a4d620fdda8b727e1d21f2b1e1eda75d43e8ee9e429f1c397405&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 卸载

1. 清理缓存
1. 删除uv和二进制文件
---

## 安装|Linux

官方建议使用以下两种方法均可，但是我都下载不动。。。最终采用pip的方法进行安装的。

pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/362c823c-ff0f-4a1f-8401-871a82af32c0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQJMI4F2%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCICmX3HmG4mabWATAWNt4PmzBs5Ztayy7YeEAF61ipe9GAiEAp6LE9STwjW8AGh6bzxKKdDzDcvlNKdIyfgTmM4MRW6oq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDFd%2Fc7lQ9p9%2BUzOCbSrcA2kfSPsfYyJYG%2B%2F1pI7MsUOXEMZ%2BqogWuN%2BdwWS4XmqYN77jV8JfNgEV0dXi%2FuvPkRk8QpMDwPb%2BTgEnv9VlALXFyPFccpBBo4I%2F6LbZZk4O%2BZUhS0o%2Bh9mR8MsszUtUJsM1sYO44%2B%2Fe5r8EbELevdkLXhM1jb5RXB2uo4BiDasLxZLAL5ieYlnoBEyTWRfwGjNxKXYEwecNVAvhs4SwE%2B9ribXdTPbF9nq4Zh1V3fEkxgCT1cDugTfRH1bGw9zqLrzHqjfmooMtr2f6vSQCQR6MtHSDXtLIjmkh8vBSeTOvZ5tX8ZgAESzui4oSBgRNwOP7Mjd76nA44x%2F9pquXp9NoqHC92lhLnY%2FOjxwbwCM7eY0YoDnmoP2QpgsRWWVWjTtWSik9BYxJL9SM9VrxxUgbKyzvBhg3Lmjb3x%2BRzCQ7riDoA4CEvVoteXIqrAMlYhWwYpDnsDAFqJlFZmR91W1TXcXlpa3HugYH724EwtDzV1pQ1Ddmr5s3iByC2hlS6O1wqzSw2LoFKCjfwS7To%2BGsUBeEYgji7fI8wqMzjPs1i7a5POgOJIilVp%2Blj4U6ZWNOn3%2BNaOtMDAEkIpyfVpMGPDLYHk%2BvU6B90E32nlI%2FKXXJ4qybPL2V2KxfMJX1%2FswGOqUB9Lz32BsRadSEhRkSOi6cr3j2xv%2BxklaGqLnN9Dga%2Bokb%2BHuCDyLbdmVi7NrplNYA4myaD0ZUYIF4U70Rojj5z7EenuhXy%2BmDLO7GknxYo2XSEDHdAaUxXJnelFg8NV2HEIvJPrDEJMmC8re1oKK6oQfYJc10eC9ui4i%2F2SXQhfX8oGFwSk8tuQIu%2BYsqTw%2BuVR089hCE2nDdjnJONlAPwMCBoJZe&X-Amz-Signature=7a84526adf1acdb6ee41207dc9baeaae8249a4c771c1f56f12152978eb352557&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# 检查

安装完毕后，在终端直接运行uv ，查看是否出现以下内容。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/d2350aa7-bbba-455d-860d-34eee2ae196e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQJMI4F2%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCICmX3HmG4mabWATAWNt4PmzBs5Ztayy7YeEAF61ipe9GAiEAp6LE9STwjW8AGh6bzxKKdDzDcvlNKdIyfgTmM4MRW6oq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDFd%2Fc7lQ9p9%2BUzOCbSrcA2kfSPsfYyJYG%2B%2F1pI7MsUOXEMZ%2BqogWuN%2BdwWS4XmqYN77jV8JfNgEV0dXi%2FuvPkRk8QpMDwPb%2BTgEnv9VlALXFyPFccpBBo4I%2F6LbZZk4O%2BZUhS0o%2Bh9mR8MsszUtUJsM1sYO44%2B%2Fe5r8EbELevdkLXhM1jb5RXB2uo4BiDasLxZLAL5ieYlnoBEyTWRfwGjNxKXYEwecNVAvhs4SwE%2B9ribXdTPbF9nq4Zh1V3fEkxgCT1cDugTfRH1bGw9zqLrzHqjfmooMtr2f6vSQCQR6MtHSDXtLIjmkh8vBSeTOvZ5tX8ZgAESzui4oSBgRNwOP7Mjd76nA44x%2F9pquXp9NoqHC92lhLnY%2FOjxwbwCM7eY0YoDnmoP2QpgsRWWVWjTtWSik9BYxJL9SM9VrxxUgbKyzvBhg3Lmjb3x%2BRzCQ7riDoA4CEvVoteXIqrAMlYhWwYpDnsDAFqJlFZmR91W1TXcXlpa3HugYH724EwtDzV1pQ1Ddmr5s3iByC2hlS6O1wqzSw2LoFKCjfwS7To%2BGsUBeEYgji7fI8wqMzjPs1i7a5POgOJIilVp%2Blj4U6ZWNOn3%2BNaOtMDAEkIpyfVpMGPDLYHk%2BvU6B90E32nlI%2FKXXJ4qybPL2V2KxfMJX1%2FswGOqUB9Lz32BsRadSEhRkSOi6cr3j2xv%2BxklaGqLnN9Dga%2Bokb%2BHuCDyLbdmVi7NrplNYA4myaD0ZUYIF4U70Rojj5z7EenuhXy%2BmDLO7GknxYo2XSEDHdAaUxXJnelFg8NV2HEIvJPrDEJMmC8re1oKK6oQfYJc10eC9ui4i%2F2SXQhfX8oGFwSk8tuQIu%2BYsqTw%2BuVR089hCE2nDdjnJONlAPwMCBoJZe&X-Amz-Signature=c20ebf7a1e4d14300342881e9033c9ac742665c85510759d680239fbd5db64ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

# Python

---

- 创建项目
---

- 管理依赖
- 修改源
# 坑

1. 警告如下:
---

> References


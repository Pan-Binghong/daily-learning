---
title: VNC安装 | 配置
date: '2024-11-19T08:34:00.000Z'
lastmod: '2024-11-19T08:46:00.000Z'
draft: false
tags:
- Windows
- Linux
- VNC
categories:
- DevOps
---

> 💡 使用两台 windows 电脑进行远程控制，配置 VNC 的详细教程。

VNC（Virtual Network Computing），为一种使用 RFB 协议的屏幕画面分享及远程操作软件。此软件借由网络，可发送键盘与鼠标的动作及即时的屏幕画面。

VNC 与操作系统无关，因此可跨平台使用，例如可用 Windows 连线到某 Linux 的电脑，反之亦同。甚至在没有安装客户端程序的电脑中，只要有支持 JAVA 的浏览器，也可使用。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AWUONUN%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXNnqQOKv5ne%2FX%2FPznqLl9cxNLF9G7CXN6jfvlMBlhcAiEAwS8B8%2FZlPSyZbDfXhbf73C4BiyJAugYI37DjDkgXRG8qiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFt8xl0JQLvjMl8izyrcAxYhGqbkVKeyFHybC6r21wlN%2BUpta5Sg6%2F%2Bw24%2F%2BPzo3ei8ztP0sgtpjD6GbG42SHsUKff9FX%2FzSth6IFckTQfWhh61y2OIMVD3gBgGxT39Onw2Ng0wUcHZaiuH%2FcQmfGw2UGp14vAxwUwWvvX13TPyqjaE1ZzK%2Ft8lYePdlgc7SXoknSEdBrvWtsS8%2FQ4KOwgTrwa8T8KuwGAPZcLhSYR9crEpNGO8W8x47kQxs%2B%2BszT8mQZRWJzWcs5zypMdaf41eOgyXa5RvxGWObf%2BvkI%2FD%2BQLWXgZOVkB7%2FlkOubpphZ1fVaiqCxOnchycivCd6X6xjA8BTsLGMeAuYvKT4GyXiIVdxj1eOz8GyDV%2BrbEC3opf%2BR%2BVrR%2BBCb%2Bg0hTOyEHwZQUIMZbq2S02Q8jKjIGNf76AmTnFwFFlVot1yf%2BZVW7eBu882M7lNsLvGhKh7Msztia5uSZc%2FvSc5LHHbuFAQqBfM8pxW0l%2FOnTtZNdWlABGT%2BALSdB3VeXTJNv8nM0Bl2Zin%2BSlPv%2BOD5r6VwjJeiS17vqO%2BiyejiWRgHhsLNtnNw4WKg%2BClPL%2BbVsgATaVuqfnGTe9%2Bdz1HpdHAUaI6HDvktQ0FxT4Ij%2BDvLP%2BoZeMPkahiGt1W4F47MPDyh84GOqUBVZP7TlgZq5%2F5q3yQ3VkxA%2FOj6yl2z69EP%2FzQfukkINzMZgxo1nZpsuMgwj4zGjG9P4VgqnpQWyYNbr0kxTNSq6gFmb19LFP5Pv2ydFh6ldZ2tAOmh6HMdQoUXNM8JVnGV0meruCqw9WBh%2FA8V6Du%2BZv8ZIAcoFIqrHNf0X5dVxbRU7m56FKy4EMBrg%2B0b%2Bg1vwK75r44hP4L7%2B%2BTfbA7o7NOUD10&X-Amz-Signature=24f99521729a81aee89e956d71bd8b99b7ac7d7b7bb74966ff07bed9f9ced220&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AWUONUN%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXNnqQOKv5ne%2FX%2FPznqLl9cxNLF9G7CXN6jfvlMBlhcAiEAwS8B8%2FZlPSyZbDfXhbf73C4BiyJAugYI37DjDkgXRG8qiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFt8xl0JQLvjMl8izyrcAxYhGqbkVKeyFHybC6r21wlN%2BUpta5Sg6%2F%2Bw24%2F%2BPzo3ei8ztP0sgtpjD6GbG42SHsUKff9FX%2FzSth6IFckTQfWhh61y2OIMVD3gBgGxT39Onw2Ng0wUcHZaiuH%2FcQmfGw2UGp14vAxwUwWvvX13TPyqjaE1ZzK%2Ft8lYePdlgc7SXoknSEdBrvWtsS8%2FQ4KOwgTrwa8T8KuwGAPZcLhSYR9crEpNGO8W8x47kQxs%2B%2BszT8mQZRWJzWcs5zypMdaf41eOgyXa5RvxGWObf%2BvkI%2FD%2BQLWXgZOVkB7%2FlkOubpphZ1fVaiqCxOnchycivCd6X6xjA8BTsLGMeAuYvKT4GyXiIVdxj1eOz8GyDV%2BrbEC3opf%2BR%2BVrR%2BBCb%2Bg0hTOyEHwZQUIMZbq2S02Q8jKjIGNf76AmTnFwFFlVot1yf%2BZVW7eBu882M7lNsLvGhKh7Msztia5uSZc%2FvSc5LHHbuFAQqBfM8pxW0l%2FOnTtZNdWlABGT%2BALSdB3VeXTJNv8nM0Bl2Zin%2BSlPv%2BOD5r6VwjJeiS17vqO%2BiyejiWRgHhsLNtnNw4WKg%2BClPL%2BbVsgATaVuqfnGTe9%2Bdz1HpdHAUaI6HDvktQ0FxT4Ij%2BDvLP%2BoZeMPkahiGt1W4F47MPDyh84GOqUBVZP7TlgZq5%2F5q3yQ3VkxA%2FOj6yl2z69EP%2FzQfukkINzMZgxo1nZpsuMgwj4zGjG9P4VgqnpQWyYNbr0kxTNSq6gFmb19LFP5Pv2ydFh6ldZ2tAOmh6HMdQoUXNM8JVnGV0meruCqw9WBh%2FA8V6Du%2BZv8ZIAcoFIqrHNf0X5dVxbRU7m56FKy4EMBrg%2B0b%2Bg1vwK75r44hP4L7%2B%2BTfbA7o7NOUD10&X-Amz-Signature=079cd2623f0c9b2508243e689fac8f3fe43690508b815c77d2d2529dc2204c35&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


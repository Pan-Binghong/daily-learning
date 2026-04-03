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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLSO7RC4%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFm51rYbhw4iboMUnL74Z9CfE7XHj5Q0FQBEgXjy4ZNVAiBhj%2F65vUSqLUkms3OyItAQzj0oEbcthtGeDvO96VX0lyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMkVCzRCAQE%2FX9ZYdrKtwDPcZOkFDG76Ox73ahATpqKPwzbN4YfmKKXKSanGgP4bXkFvL3%2BD8B%2FcpeLzTYooZYEDV%2BXbA7i3QINMIqdI%2BeEkuCl9AdyP08CFJmfhSiifEf8ebxYIXPDD9a%2F%2FfwO3dbXxzI1L%2FCPDNN7CnCqZtWq3lv9EO6ty7kVUJVo%2Fla1Szo2b7xWweI3Rv9%2Bg6AG6xDEIjMSSA3Ht9hVnZs0rxHPA%2FmdCvYNmM71Qhl96%2FkckMzpZRVHaE3BRVz3ybCD%2FvxhuPRmY5Bljb3J3XWccdFPgW9Xy0mN9%2FEF132hP3b641KOeWWNvWpIYg%2BsfAbY%2Foc5d%2BGPygddTtkNyHr1Xp8AAmO9lfikOe66ZbSe%2FDrXFuf7iDb94XQl4hz%2BB7%2Fo%2FEGrZ8eZz4Qo0klwT97EmRsRi4SwM9iLRZ01N8M1lfHqSv3y8o2xO6Eed20eZzvYzmQKRxDGmjwrU7sRS6uf4Dv0Ey9iy4EUYil2lPfFQTpT7hrFzdlashp1c5rM6nIY6GNf%2BErbY2p5dpEwLscgRKxzrlyVPMD64%2FNhlQOlRA666wUUSgdyKbO5S%2FqPoxVu9hCfMdGwjuBqSSJWXz31Lbkd1IUWSOXpUfjViEP8yG6TtmfD5UF3%2BPdKAEJZ8YwqK69zgY6pgG%2F5b%2BHhDTns%2B0vp1PS%2BSnYrD3jlerzxjhC%2FpitKsDCnwWlQzaB6Tx93eQH1yuDVhPUaoGIGtF%2BF5pgW25rWUux7punDU3N4daNB6wa%2BwKPCxwhtZnBKjvJhWpTlZokBV0bVHxVS8dOGVQ9kXNyiuUo0KK6l8DAxbK7WdmgAhx3rO1E6zgo7OIDzefYKYIYfA5wNWYZFjcTy6%2FKYG6SCgr6VtfmXdZn&X-Amz-Signature=7bc9d6d736effe85e3d99984ab76e1e2a994403d1f9901b55ff1328d9ad54e80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLSO7RC4%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFm51rYbhw4iboMUnL74Z9CfE7XHj5Q0FQBEgXjy4ZNVAiBhj%2F65vUSqLUkms3OyItAQzj0oEbcthtGeDvO96VX0lyr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMkVCzRCAQE%2FX9ZYdrKtwDPcZOkFDG76Ox73ahATpqKPwzbN4YfmKKXKSanGgP4bXkFvL3%2BD8B%2FcpeLzTYooZYEDV%2BXbA7i3QINMIqdI%2BeEkuCl9AdyP08CFJmfhSiifEf8ebxYIXPDD9a%2F%2FfwO3dbXxzI1L%2FCPDNN7CnCqZtWq3lv9EO6ty7kVUJVo%2Fla1Szo2b7xWweI3Rv9%2Bg6AG6xDEIjMSSA3Ht9hVnZs0rxHPA%2FmdCvYNmM71Qhl96%2FkckMzpZRVHaE3BRVz3ybCD%2FvxhuPRmY5Bljb3J3XWccdFPgW9Xy0mN9%2FEF132hP3b641KOeWWNvWpIYg%2BsfAbY%2Foc5d%2BGPygddTtkNyHr1Xp8AAmO9lfikOe66ZbSe%2FDrXFuf7iDb94XQl4hz%2BB7%2Fo%2FEGrZ8eZz4Qo0klwT97EmRsRi4SwM9iLRZ01N8M1lfHqSv3y8o2xO6Eed20eZzvYzmQKRxDGmjwrU7sRS6uf4Dv0Ey9iy4EUYil2lPfFQTpT7hrFzdlashp1c5rM6nIY6GNf%2BErbY2p5dpEwLscgRKxzrlyVPMD64%2FNhlQOlRA666wUUSgdyKbO5S%2FqPoxVu9hCfMdGwjuBqSSJWXz31Lbkd1IUWSOXpUfjViEP8yG6TtmfD5UF3%2BPdKAEJZ8YwqK69zgY6pgG%2F5b%2BHhDTns%2B0vp1PS%2BSnYrD3jlerzxjhC%2FpitKsDCnwWlQzaB6Tx93eQH1yuDVhPUaoGIGtF%2BF5pgW25rWUux7punDU3N4daNB6wa%2BwKPCxwhtZnBKjvJhWpTlZokBV0bVHxVS8dOGVQ9kXNyiuUo0KK6l8DAxbK7WdmgAhx3rO1E6zgo7OIDzefYKYIYfA5wNWYZFjcTy6%2FKYG6SCgr6VtfmXdZn&X-Amz-Signature=682a8e6dd135ae24125466231a980ae166429b4da7caba5d1c3fa88ddcf3e0fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References


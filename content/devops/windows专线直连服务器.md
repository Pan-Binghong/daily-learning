---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667M737ZGW%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCICHNWuk155Xzim9yY%2BfonFG7A2QDZyUv9LoncN6hwU%2FWAiBRucxblS2iTui5ilo9I87DS6VDmnoxhiHVdOUZzP8neCqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbWUBY%2F0NBZ1InrZqKtwD5HqM8X11%2FqhwQzWoNJZr3RYcZI7%2F6MynVy8Zq5v5tKnQ09LpB6VNNlQv0g8U1OEhUiUWZPkBR%2FZrsVDlbBxAEie%2FgvHVy4FM%2F2Vk4wF4ckFCKNtBJLPXdDBLii2sVcqtrs3f0zbqDa2BNvJgPyzgoAKIYIXAnottJrJ1DdBSO1ttVKH6IgGgdqq%2BWQIuU6V67QYmgAdozs6hPGpl9Is2taCgiAYoCosJOEpoKit%2FhnSS5MVK3m26UrKrcpRWjY5xhW2qFZV0rr65gnnEcHcGLsZUuYfIdhSXdNWPEWw0O5MyREFcznYaTTPUgRPbZtA9wJqjTdj%2BB0hEhXS7%2BsVc9xkwFznCEKlls4OiuDRH9ftZWg8tte5eh%2FxTGSd%2B55wzRt8fj6LhtP18TKyWfjytbQNzykydPDpsrxT3APJkLMEirhZaM4EOj2bDjwQIjvJ1kHyekXyIZjeNbD0N6EW6otk%2FS6cszGsg%2F0rrLdHR8kKIA3RL80zVsn%2BfHmlVCkqmtYCkcYMoZV4qiMHPFufhD%2FfGoL7D%2Fom4sUAJfTU4T9il0GYPODJv5YlSYhsJuHLJndelWIU%2FN5oqQwt7ecrsKul8iYT5RoYmAiJ%2B1Iw7sSt%2FkTa%2Bkh8cDTr3ArowrejizQY6pgE5sOnZoNNFJ72d3YxUhPcpBcsiPRe8%2FoCklrh7KV91pZk%2F9LsHGXgUz%2FcAl4e8elsr0iSMpvb7%2FO1ia77NZnpSsSBtqhkSNHdGGZ6vd2V9OCb8Jyrb5TIr3ThjvuPJyGJQtFmBMkY1vQh1LYhhLoCEj%2F6FY%2FUz0maEx%2FUM7SQZeXYQ%2BvZ3dVE1B3odKthZ4dCbM9KxUM4GXy0bcoJatGsA8s8XzFZv&X-Amz-Signature=a30b8017087079d2755a5d3fdb50a2b03c8a677801d36d55dfbc6c857da6a81c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---


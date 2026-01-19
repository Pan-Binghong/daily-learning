---
title: 基于Huggingface镜像网站下载大模型及数据集
date: '2024-10-29T01:52:00.000Z'
lastmod: '2025-03-20T00:51:00.000Z'
draft: false
tags:
- LLMs
- HuggingFace
categories:
- AI
---

使用镜像网站下载大模型及数据集, 以及配置下载参数(本地路径等)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/dc82f140-d63c-44e4-bc53-0bc220caf11f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HDS5QDY%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2BKm6fhIhpjYi4jBoKAV6XA9mrRS8Y1zNMQUDwDdVkTAiEAvOO%2F%2Bner9RuyxKTgjuk7HvpS21AgSKPDngDFvaAS15IqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDJsbq0TDCHyrAJX0yrcA2tx5%2BaMA7u%2FmEsAWljbc8AojWJpN5sIN4%2FuankLnsM2zPIDpgAzubldp2r6To3RybORqKXLjpzDhhnwcLHogvWF3I%2BgzyFr6eSQNfBjwT%2FsMJJ91ABmew4w%2B2ZfzsaoSmA%2BXmgJxgr6c59kF%2BFXIwumNMeXJlyU7xCIb%2Fy9agPvv3zimMmVCh5IiZRl%2BKwXAVY9XBgdF6RUHZXNpmWoFEppuVw00uZPmg4Rf84do90GhWNWtMEyU8lWcGT%2F%2FXNBZGCF0faAl3tWMlRcJGvwWm0bOCBACYLqLfOGQ27183NbUVnCo9mw53DlvrqxyPEvsd30XG2vHhPF1wlqcQgwPzdyX5AyVgLuH8TxLYVRlsMKzKT%2FWZx%2FrRthUEr1Nn2CA%2FgyFR7JFUa9mXeWuY%2FAkHCf0Z7awrwQ9GFexliML2Ule%2FIckD8I69hZj9mmYUrNCj7795xbPl6FT6eWcxp33Er7KkMGkjsr7TAVWw3d7qeZzcOImhlTwds8CALs2jzL8xrcqFTgQe9WRJxoe%2FDLT1XEuTHqREigM7fmPR8Y9R8%2BOC7k5oxpN63p5Gg7LVXgOnmVpuRdLaD55xjgaU6G%2BgtUOb205JK%2FBypqqAWAkmcBhsyRgt7Xlzz1pXhqMPnctcsGOqUBV%2FK3udy1zlbldRqNLFXERYVteF3UXVh3LAowVpUvDK850xrN3ifG2Hy40%2BCTYxUbUuK%2BPaigrEmgYD6c9w4PHH3ISKcBRnzd6maNl0nJMQNwbFfDUbNIfnhtg%2BhEEq2RqRRCmXj2BYGiSJIbltWYEYm8BDrd25a%2BBMea9QS1KDylngVXTG%2BjLe74XCDFk2XrjhCKd%2FSiC9pwbm8b5nqVHt%2F2VB%2F2&X-Amz-Signature=5ee45c3abfa4aab1815806e9f78cb788b8a9b3abbb135f7c93be1cd63c4c80f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 基于HF镜像网站下载大模型&数据集

### 命令行下载

- 安装Huggingface依赖库
- 下载大模型命令
- 下载数据集命令
---

### 代码下载

- 首先获取Huggingface的Access Tokens
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/22b8dae9-3302-4380-a23f-5402b524f0a9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HDS5QDY%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2BKm6fhIhpjYi4jBoKAV6XA9mrRS8Y1zNMQUDwDdVkTAiEAvOO%2F%2Bner9RuyxKTgjuk7HvpS21AgSKPDngDFvaAS15IqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDJsbq0TDCHyrAJX0yrcA2tx5%2BaMA7u%2FmEsAWljbc8AojWJpN5sIN4%2FuankLnsM2zPIDpgAzubldp2r6To3RybORqKXLjpzDhhnwcLHogvWF3I%2BgzyFr6eSQNfBjwT%2FsMJJ91ABmew4w%2B2ZfzsaoSmA%2BXmgJxgr6c59kF%2BFXIwumNMeXJlyU7xCIb%2Fy9agPvv3zimMmVCh5IiZRl%2BKwXAVY9XBgdF6RUHZXNpmWoFEppuVw00uZPmg4Rf84do90GhWNWtMEyU8lWcGT%2F%2FXNBZGCF0faAl3tWMlRcJGvwWm0bOCBACYLqLfOGQ27183NbUVnCo9mw53DlvrqxyPEvsd30XG2vHhPF1wlqcQgwPzdyX5AyVgLuH8TxLYVRlsMKzKT%2FWZx%2FrRthUEr1Nn2CA%2FgyFR7JFUa9mXeWuY%2FAkHCf0Z7awrwQ9GFexliML2Ule%2FIckD8I69hZj9mmYUrNCj7795xbPl6FT6eWcxp33Er7KkMGkjsr7TAVWw3d7qeZzcOImhlTwds8CALs2jzL8xrcqFTgQe9WRJxoe%2FDLT1XEuTHqREigM7fmPR8Y9R8%2BOC7k5oxpN63p5Gg7LVXgOnmVpuRdLaD55xjgaU6G%2BgtUOb205JK%2FBypqqAWAkmcBhsyRgt7Xlzz1pXhqMPnctcsGOqUBV%2FK3udy1zlbldRqNLFXERYVteF3UXVh3LAowVpUvDK850xrN3ifG2Hy40%2BCTYxUbUuK%2BPaigrEmgYD6c9w4PHH3ISKcBRnzd6maNl0nJMQNwbFfDUbNIfnhtg%2BhEEq2RqRRCmXj2BYGiSJIbltWYEYm8BDrd25a%2BBMea9QS1KDylngVXTG%2BjLe74XCDFk2XrjhCKd%2FSiC9pwbm8b5nqVHt%2F2VB%2F2&X-Amz-Signature=b80240de00c97f098114250d394007f4c147e9df28f1c8adbe8dc59aefc2ded9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 下载代码如下:
- 下载数据集代码
---

> References




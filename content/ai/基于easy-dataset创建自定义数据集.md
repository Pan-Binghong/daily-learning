---
title: 基于Easy DataSet创建自定义数据集
date: '2025-03-27T03:06:00.000Z'
lastmod: '2025-03-27T05:53:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 前几天看视频发现一个开源的构建数据集项目，打算复现玩一下。这里记录全流程。

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNMOXDRI%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIAlORI9a50ND8e0ID0ky0xkfnvAjyNFIIWAuAH6fNcqjAiEAjxO%2FIjuKuFN0XTWMAWnM4o4DRJY1BE71NnnXu5ZvwGQq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDA7r6Mev2nsKUw8GxyrcA7wvf9SZPrkjffGQLh4Dfq1vYIizvHuwum25KimSONeDXDydkC9inWmojMd%2BsVXVTn1OsQJCwnjSuZUaTKwfE1JBV6pQvkcqBSf61s%2FV0R6gYwZbIMjtKWVxJpz9G4V8cf1oalycnfTbTq5TO0%2F4sor4y%2BG%2Bb46O3kdt4CvhqO6%2F7G31%2BsCtajHGcSPhwUFcd50f9seQ%2Fq%2BM5ecTKrjKPMX7zsuFFSuB4pUiU2fzgQtSZoWz50kmZsUC8LyRcS6IpIKotdGn%2Fr5hfUTIgyEe8g5%2Fwrr2c8rqdVLKKYbVda2gXdqEUOE%2FQejOEI3wHMICIvMgXdc07xCGscklPEP6yVqIsplmDBF5zH8kyVR6XpZA5cTF7qytQxNXHl%2FRraq80RHtzPfxYyrMvqz6TxVKtVzVwx6LFEucvLxLMNdnpsdCDx2hUJDXcbgM%2B6kk5dH38pVK3sJJ11299io6uTx2%2F8dU9QUaVKKtwp%2BDg8YeQU4LFVYOBWkGpWH7WFc082xS8RE2eCeXKmzAU%2Fe7hgo5OzWR8yocWGZf5Hu2MzcRCJWR%2Bn6OIf3xo%2FS3KAIMTDjIU6dlCBUwl9%2B7RLiKloaJo9R%2FwWjLsmZWwYI1OTUHZJRAU%2FLx4NgihEvZEpYLMICfxMwGOqUBOsS5TvvRiaL598vbO9o76jOMtrhRMPsUlr2G8acURpsAOaF16e5YPN0rwiYhOY3mFq5BtM2J7Dj9UMC5YJ46nOO3QUThFO9e5QHP770P2Szbkuqe44WIXGtx0PFNOttaebAEY%2B6CX84%2FTmzDhCywr0%2B%2BmaMb4F9kEHlew9C00ftE0e1AGqpHuTi9cXQupwLXM86y9NAQWnPmM4PweZnMQtXYOX3t&X-Amz-Signature=17632b177ae2e7ca0f31787d3492703ac94a7bb7aadf78af68dbb9be63af2f6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 环境安装

本人使用Ubuntu系统。首先安装node.js以及npm。

1. 使用nvm，安装nodejs以及npm
1. 安装pnpm
1. 检查安装是否正确
---

# Easy DataSet平台安装

1. 使用github下载源代码
1. 安装代码所需依赖包
> 使用pnpm的特点:

---

# Easy DataSet启动

1. 基于代码构建项目
1. 启动应用程序
---

# 怎么使用Easy DataSet

1. 新建项目
1. 配置大模型
1. 上传数据
1. 基于分割的文本，构建问题
1. 构建数据集
1. 导出数据集
---

> References


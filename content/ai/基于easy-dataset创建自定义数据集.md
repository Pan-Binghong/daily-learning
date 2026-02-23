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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVHINZ5F%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCICZ8QFupQNjrUI50xCHsaeoyHQSqAXfCMwlN6rvhx43TAiBiXVCaSHVUyvt2mjIMwMemI9GpdFdPqZANj%2B63OdxKJiqIBAjV%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLEbTT0beCb4wh6N9KtwDVE%2FOXaGMrDom8xW%2B%2FwR4TtTwufro0oFT4uIMo8VYpws9b9xIUI02ksVPzSTJ3HKns23gY9RBtHkI0E0oqOKqq5lEk8uk4SAfpTaeOa%2Fn4B6d%2F46eqGfgZcPXD1QsUjTz0pPV%2BEdkScPLCguGERq%2F5HIH6wlCCKXYOeSIxsE3YHHx3HFthrLFSxTsunjf23xXYFVm7yGschGjLAavDuqwYp6Hdfm01XmeVLh%2BPHoF5RCH9GNf%2FEOJeNveeYPqA%2B2yfFdJK3LgXNWhpklwn6HzYbRa6eA06QPZ0cPSfiQdDeGZZt27Rn2djRziGT7c7xEMoFsIZG%2FpD6rWDTG6NPH5wXdegnyL6GlTLSAWrNutaGggO8laHIOR%2FKsGaYiNUwBrCL8vj6zOoX9iLzB0E1nnZJxXgYks4bA3ZzeviAwOc9T0iXT%2FuqSvmhrFdPuVC%2BJa62q3YGrDbYP68KjwQ1jZ%2BKboq4i%2BpSx61hZNi3e3o%2FE1fkA09P5BMb7kRPnXih5Zkl8r7uYrN5Z9BngCAf0byb39wg6g6EULYe1okbG88UTdTIn4GOwmjdQh4YftL%2Bff2pQJkaO8zoOrfPGV7xwY1WwDsVaCcQpYQVXRdMTkgAW%2BH73r0%2FCucxbtCT4wgpTvzAY6pgFH7p58J339BlTxDt0BwN6j0Fpa6piw64tUpwH5TaF6JDSFtJa19JvbD7rKNCPiG66hOfZrkJRljHnOHQW7oZ9gjs36irgXJTOAyQa2RvpejfSN2QJSvYsh2hYKvO6R8n%2Frh8%2B03179rtYbmu6WBRpFWe%2BmXnkShFcrILvHzs%2Bi6NCFJIufrW0Bhv5ZRNP5V0HUuFD0Gk%2Ft9NzAd0fn6B6eqboRIYH3&X-Amz-Signature=d00e93467803c35394a3b02b018ccf2346bbaba22a78b037a2e4612626975660&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


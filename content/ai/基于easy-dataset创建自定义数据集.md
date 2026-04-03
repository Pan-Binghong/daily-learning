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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JU4L4KX%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCj7%2BYyOqBlnFajX%2BXlfnSCdz8Y3KhJOhbyKflsJHc%2FvwIhALzA5N3qxjIefCxAFduSLPxLgel3jP8r7RqlFQPTrSQRKv8DCH8QABoMNjM3NDIzMTgzODA1IgxEGRNTC2qV%2B7%2FGgI4q3AOOoE%2BvRbG43kNphSIKXrYHiXYiFMCKXrOIivFaLbdwvQVhiTmb78NmHVABVM9%2FozMjW2fU2NUv2Q20thLRdQTvcFxDyeztca2BfaPbKmQyf6qyfb096hoZ%2B6p8VSq9F1dz1wgl3SWiNMiOch9gPoLkk2GzNR2mHz3UPixnlK%2Bl7CxU%2F8buDm6Xtd4x05yfNQf1D%2BCC9Ttu%2B58dK9TPTMd1cWfmnppGCWnJUFiwFJBo8EGovfQiF6Aq%2ByCF522LIBM6mB052QnEQlbi6boft%2FDAsaV05NZ4V28WgxJrYz%2FVPJGjp6cYR3%2B8fffgxdJyiVhNyP7MsQ3M97AGeWxv63gto358N2t6Tbz1ZfCM6DOhNljxIDf%2FtnppowK881UqKj%2BOeGAEl11qb%2BBEV7Qn9N20etGNp2nE4ssRzGN7Rw%2FaTqdMDfxHNyl453GW0MoGHK6CzWLvbq5sojD%2Bgb3w7LJyjq5OmA5oXR1iQkX3MbGXJjXkrZ8C9drBfQqV5qtCOarQIj6OwzlTWpsZbv8%2F%2FJVwfrAyKlYbskR0hGY3MiWDmcxIdbseMP4TtlNHX%2B0z8FDLXaF1m1MYlTDAEfoMQkdnA7Ft6QeDwZehYpKPBwppD2zW4g4UGLE1AtWvRDDBrr3OBjqkAUPf3%2BdVLwx0vFMROziaHEJtx6Jw0DLg2M4swDOSHNv9S80FXJ7WIs%2BGlE1En%2FRaHznm%2Fil4eJKF%2FupgAT5qygH9RWqhtkGlRKpF7aJYwPq76iqfCFRAGYFmqU9kUyP7uTt3CosbLp9xey1M3CrDlTdltU4gyNDFoTk6Dd3B7iSY0sFF%2BoEbz8qq3nyX%2FYolKiskIVRLGpRuqBfRDRpwSOVAtqgB&X-Amz-Signature=537138d8a8f9431069bba80212a10cf705da08066265d273e00265ad19d9e2c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


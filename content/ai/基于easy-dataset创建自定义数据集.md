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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655JBHES4%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTox4EF98HYJTkd0AmJEVJxSv0nSUASJgKkJDgyvQ%2F2gIhAMYx9gcdvTZIXE2RLT1k81JrSbLNmVpuWhMwPvDfNi3AKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzVG68dJTatjhNd8%2B4q3APG67N%2F5camGAIfH2qtl7vhIJMCn%2F7nQ%2BOvJVz%2Fao6rJ2r%2Bqru9F87TwqDNG5iogijdVdQTKj2NRdIqFQT6dtpokiWdPZy67LENsSfbAdFSYDuZcDKvL6E0ZDEPCIUo257%2Fy9qdI1OC%2BaxyAfiG39lEH79NZmwn%2FOibJ%2BkPjLJcJyX6ihpNYJiWtTR%2BR%2FuJYk398MEOiV78OqhHJ8Jr9rET3%2FR%2BFE%2FcJSKruKHjv1eFpr%2BcvSHqKxUVuFtJZYb103oRUcjcBxoiB8Pnl4iMcbffjlFfGdSrUxtFwI4WhTxzt%2FAC6RaU2gEmVYFJggDmpn9mhFQ%2Bu8nPQcU9JsQnGlIZaQer3BbmM8cBi5c69NGo%2BitJ9WaIOCqZaZ7tmVn%2FT5oNFd9WHf2MiKcWE7TE%2FAnmSC5W4L6VceC7AaLlKv7wUw6YqRfic6m7P2uy3dfbsDT4%2BM7IrBs8RHGdOWdOrJXP3PuU99Hhh%2FajpjkM6ShCp16WswyvLR4DvTLO7C%2BaK2bszb0QBKDXscn%2B0dbIA93WQjk2OPKNA5x4ms6%2BnLW6C8wN%2BQlrZ8DU3sb1GSxFMTt2MiPYkkzkiqjhUJE9K1Vo4wZxdVyygyMwVLKssZxwkVR1heYZXvt5eSKfijCllPzOBjqkAegRZZlDVY8%2F6QMhS0ll3G3N94LNErXR585RZeKJWuj2gylt7OPA8pxbbPixcb9qoXvRtgkvxobjqJR0StZoUsAHsiXXV1WtP3HeRe8nA0ZB08zJ8gUXCzTh%2BWuP4NnwKQUAeU0q87%2FdwkwaiuZLPJPVA7x5ahTs6pMW0Y7N5BmjwSLWB9HP1HwmCQ8AIvqn5D%2BbxCsZOplzRMeKD0Bl1gd9emuI&X-Amz-Signature=7695fafa4f0008491010ab7d5a36816c991167c267be193ebacb73b4490fcf58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


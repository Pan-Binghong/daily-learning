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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIYTWZ3V%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFx6MPx5uLo%2BFgQH9jWefZXrw5Nm3juqM7u4kdHgeTvEAiByYP1CN3boBFAV6yVVl%2FfWnkezcbQp4SZS2hJsMVlIsSqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6ZjgOYCTVP733QmDKtwDQaNIF8DQ8OECaqPDoTjvVfFV3u0QAhQe%2FtAxO8FJlxbJueaCViyH3t6wNMjQBEUSKfw06KDwwsoNPTi2M1sCGM4%2BKwZcV7VuOBRDwmfjxS6oS8wOgDTKHw%2FKVWeIyog9QcQEgytfY%2BQwzQRUJzJKkCT%2FAofFLf6F7HkZWaWUdObVSy49wDenC%2FCXQDYTRsawYxjWLPDKgYXxGlqqrFSWkQb1YkU74ziPU8Q1QnWm6lwO%2BPqsGHakyb1l%2BdHS05z0MBgvD9qgWtdciUP7LnwdN8FRF2gmsrINJDxrk6XP8MZKrx4DsfYE%2F2%2B5YgU3t8Taerp6WtiA9VUkvBivKy4Z20gDxXq72cj0xAITeT%2FXXnBQUN8K5xtvCE%2BUJ8DVeQjIuAIzWc5ISwko%2BZVOJ%2FK8kQHuPASdKgoeXhuLU62IKv5vQSvuYBdcfqqDS9%2FX5c1la%2BKU%2BozpoOuiI4D1zKN1qpf%2Fzj0XydwTA%2BqpEG0U8KjEGJZZERWUdpZ1gpAwq93a2mftCARIA7HdD%2BEbm%2Ba7IRZh2nP9uIQ7BOGgTKlCHmLDzaTnh4%2BtLi7bAP6GUXTtF10Y1DUnfNsP0vdv9a%2Fp%2Bm7oIgWs4CwXTsmQm7iAnMScNBHhxel5beGccoAw9OPBzgY6pgEyKj4aZMb1vT1xTiAnzLHbfVaYGrDc9Rwxy8FlUNdpVjxABllOnsR59ZuV8dx5FBbVRnLJ4TS1BlxQeycZNMNY0S53%2FiHx1dOlxl3FGAw5QNdl6fP7%2FaA%2FsKA42lEgwbc%2FJQ2deHNT9W4L4js9Ohcu3DdPXMsAvbJB%2FMwy2uNRJcknnE3epA8B6s8bjJBCIW0q8QytUcL%2FjZa%2BlVosWWuUyBvjC9E8&X-Amz-Signature=f335c9408a87be05cfcc986645ba2ed6805647223b764cb2b7974cdf8c4e90c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


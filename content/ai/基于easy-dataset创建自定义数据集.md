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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7WHTUW3%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQCquRUqyH0A5qyH0W7v%2FA20EDJTurf8zmPO5tHbxoG5CwIgLMKQ9urJGcdu%2Fbd%2FADI28mUYf9WTv39RbA8GlirN9ckq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDKJy2eu8MLarOp4QOSrcA3nDgruVX%2B2E%2Bxqfthp5o1cjqvkXYNh8nzaE%2FQXFhnx0uvsx3ENqAzaSsgRgLHLDxVWbix7%2Bd06%2B%2Fv7OCh2O7nGYtkuenKDQkqPlPlLAEEX8Wlskh8VT%2FW%2F00MQKaov7KeT72tyhx6O26crGbT2hv%2BRi9GpKFV%2F0B1NriI42kLb2T3UvOg13Z4T3is5xzCmZUPUe%2FcQS0azJUawXkoV7BuajGVIzxAPNLdFj9%2BVluJ5OTctNmWe5Bpa1Y4mo62QRWq%2FAvel9sVzhgOnU3N6%2FHNZD6%2F1t0EVmPpJapAvEVf5NE%2BjdscT0z9xs1SnOsEH%2BV%2FM5jQatBmNjrxXbVgzn4AbiFkZt4HnWAVjGnrNLqyKyakjXd1CjMOetY2geAlBkJBCbyi8uWK51%2ByvzPI1lSRcREO%2FIs9No%2BMric2F0Qt8CqU4VbU6TEV14%2B%2BA92YolcgI6DIEekl8TmSVRpVY19mruC5qKhdzebw6Cq1O78QpWvVe6zAxPaupxBN%2BGR9ruZajno6Ak9ZhgbTXMGKH83HMeiW2SahEv%2F4VYiwMfpljYbtdoc%2Fz0a2S42%2BFjlFj9j7rfHPyz3qTtoZM2tYeKwGZTwRvH2xK660txjt%2B6b%2B32VVmD0CzQI2YjQ4QUMM%2Fw1MgGOqUBOAwKQTSnMUnRy5vML%2BLiRVC%2FaQnBIsv9FYglMm8EwfNL9WaJSlLBq3fqzwhY08zdL1e6H26tPTGHQhvhWzMw7R3E4qryH%2FS5CFe4AMr%2FRWN%2F8ILrtww%2FEo9WOX7j9Lk%2BBLgLSWYHAnGJ1m1ZbDqsdhRyI1eJ8J1zdhFnyU6RzDCYzcRzPiEyeGKAB7jXolWUm3lXUdi6P1Wck6WHf%2FRDqByiFxcW&X-Amz-Signature=6ec1a3ef18b7210e10e60978577ddae033d51e0eb7b5fc92a9740bbf0f42b9a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


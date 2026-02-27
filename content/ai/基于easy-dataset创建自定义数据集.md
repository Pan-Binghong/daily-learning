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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662K2S77SB%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQCGMnaJrEQaWgceabL%2B923QNz7ME0CUbiWINVCftpP4uwIhAI6Q5Okk041wYYZgkXe98mRv9CQYEa6BaHGo8NYXc8JoKv8DCDQQABoMNjM3NDIzMTgzODA1IgxW4p66mvUhvKqqDgcq3ANAuccZzRmniLqf%2B8Q3puCKtHuoDIUnbpdPw3ABwY%2FsLqaDCvmqpM72lzUt5E%2F8QYlIDwHQLx9SGrKpsTTuknlwcZUpnR20TMkbHENUXHRB0aWIDGDJZjK%2FFrF2bnJMCdeLl30seQLig2tTYBQHEGBM0uvjI64RVJUa1s87wnD%2B9x6gpd6WXNpxUymDzdNKKJg15GvEH3sVJKiRF7XuwqmlTvQzRhp47%2BhIEJxVAuDQe7LvjAxMoGauYbaJ%2FJJoJefT51lsavJlfwCnZJfRG9LS9MZGGNdQhGeign8WeEY1s4OxDU5xjouypnbifX2tnhah%2FeOsbaYjeeVZl48i7TWoHApF0BMVp6PI5DIgfx1Lg59Y6U15Y4A9Ckgnxizo%2FgeYyfyULl5zlpLRconGN5wEHhRh2%2FVx8MKn0gBApRIgplJwgd1x7zHRMbJKnWeFuZ%2BOAglQ3vggLPhYaT0MwfnDYrXiE8%2F8TkoWYxcYBwPJdigBRFgcEUoujW3634rmVT8pbRU4JhZdtgN3rUk3Y4b9e3%2FkTMeGZwObM0lb%2B1Oc6MqZGS3Ztp2TDQ%2B6mQgOsXlsW2E%2BtELqx288Ylc%2Fz%2BwE441faqoTrA6T3Ob%2FHfks2WwpiPNMFZnR1kbPyzCOh4TNBjqkAQOXeYHb8iKTxuM0OrESqq4FALpE%2BefH6%2FDkI%2B%2BZfGlXtt6czYKm%2BoFyBFjlzD%2BCcUWEGkSa%2Bp2PkaQRj0xGP34RMmER4BxGw5t2yoQLyJF3Ejuy7Y%2F5mrJ0gOvdAWCgzR2LwtgNp6Z6GtZc8CjvrTnuMdFqES0KCAAS%2F%2B7afoXITaioR%2BMLfRfilOM5VqvT43pYv5l%2FzoF%2B%2B0xlPO5HxRcOv71f&X-Amz-Signature=15d0c413e90dc0d919bd8cb3a1f63a3d1bc9386d421d0a57ff0e6d64778cb9a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


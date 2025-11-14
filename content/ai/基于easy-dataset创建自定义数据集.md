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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3EIPM2M%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCyCA5%2BmYSi1arTgEZ%2BLhUAlTypA95TCapMvXi%2F1t8IUQIhAKuE7AW8UwqJaYWioDzHTvjSohqH3rUJGXx2HQGZoOiGKv8DCFsQABoMNjM3NDIzMTgzODA1Igxrk4U%2B%2Fg2y5wTqMqcq3AMm5INKc0U0XjGjZpBVA06TnmLWHEQSEvN2dWvZrd6fMfVhmdp29L2WyO3N2JF4ncTrFlrzvFraNiQQUECLUqhbwjg4vgvLOBQc4m8SFk3tzp8OwOw5rYeGrEjHcowe2v%2FYn9AUhEQL5B4T9l9TqWoZDD2orQEUuHw3i%2BjIYomSsZlPNy1YhQkGowiZ5Lwg4ZcuRfotNtqtGb6zjQq5hN8aiT7nU00lTshqWhD5AmfV%2BXpjPYzEOY0wzsoU0KqPjH%2FtyEbQ2CWDakbIMJMuuiLIq9VPG34Xm3CgT12i96oIq%2B46ohUEu3xrqbzlCQOIqQCXWFWbmDdEiTMd5%2BcXJnqUcrQatrjVk7xubKNCm1btoi%2BMmXAgY9m5ffqzca%2F25qIsy8aSUTxXxfSA6AsHqR085s9qT5kjsAsLFS9PflJovoaxApeyGsubGrZra30eV%2FK6r201njs3YFcsEFFsXNNPubhaX9VQCAQeh53hKRDD2rPCfnqx1nm4Jy0T5mJ9zCscALUO1bUxSLXBAA8ABZ3H1QwKWvNr0tSbxA9ok%2FWriVs4t6uxoGaOstoguOPgjeJ7%2BAil%2Bo0wOgXZXf%2FkUpx4oYdxYO7zOyhjbq3fdkaQQG8Jh%2FqZ4dATXkioWzD0idrIBjqkASfg0MsdN7p2rsjXkseTQP3imfFuRibArnQZuNXLNlmJwWZ%2FewtyNNjIBIT94AGd0ZYbT9ZGLP4rp4Myo7jJltWFYYoWdFbYDIKIiAxUln3uSYKs%2B2ijI9H1TDLYkZCCtJA5fk9rUEE3UlzVxq4tTqA0QSRfV29SkSHPF6rv%2Fe91xKrg4HqPTDly7E97B2O9bk5Bv1SZ%2FBLo%2B48R58lng0b7QoEB&X-Amz-Signature=ec6a39753e4e7d1faa55fbee4947437212471bf8cec5f8ca111df654beacc437&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


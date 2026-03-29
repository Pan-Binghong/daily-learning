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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWIVBLSL%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQCI7vPXfCWq1QL%2Bu2kIIQV19gJ9%2FzYppzQx5g9eIGpEXwIhALJaHKaur8vfRro95YGkvxZTE98K7g0KlTrNEDpAbDETKv8DCAUQABoMNjM3NDIzMTgzODA1IgyEP8z9pewE4YaKONAq3AOU2NkKI1lrOkSFEz07YybkKRRUc%2BOdFToR3jRhHGSc0THXfxFDA4zvGlkDGpmE7ZpVYYMVYtxenT7rPAdJ%2BX0Ue%2FrdDvXNzbtfPASvXW7KBzab73iAA9ZpNMXlojqefQvcvqYxirof%2ByJ4l7fvDlmNsivfepw1kzSfRjLgeznVhJqqkCJieMSb39R%2FPJCKnoVeYZGSJ4CLeTXaTCH4qSNnJv6FxgZNGWlKwpMA8aHpozmSwPi24DJTaKbioNVfCf5qJZuRZBpJCsACi61v70MpTDYFu0XHlj9DKGVuzl3dyioWJqCJVBM8yOvhtDkZazBrBTwhkjMyTD87lbv%2FV4XtuKxqMu83JczsmRcsz9Uw%2BIUlyKAFAlxQ59HzOrjOlvtaIhW1oJIVtgSUPC%2Fx6%2BmuVqbw%2Fwf%2BClgkxUirmUjrDwsqmh6tUJ0LAs49c8g6mwEPU3W91sQ%2Bp4PoJUrnXH9Ns2TqXDuauTcQ39HlZU1w7p4gZ5Gx0DycecNvSX9kYV065yHH5QXZyk%2FljWRvhNpHnWalMl6poE%2BKR6%2BswLdceG1QbN0aDDkUDGBa7iClwzRBqNy6Tzt5VyV8qa4j0O8SCmBYi7olR7sh51anFTrh5QDYT7II6Bv7nQ9teTCJv6LOBjqkAeTPj6wr5dx5kYRPvqTC3m779X%2Fh%2FCGejbTR7Xmc5pLlZYBOiAlUDoWj5nadIICf8I5CQ9TuOnLjWGoh7P2MkFKgXOL1orAjDbhdgzFmKXrzek1Ob0AVnmWjLQRnHO%2B9UZypCvA9URObYcZc%2BetAI02sQX5Nf6jJDxKsoZMeNNO2TwFNdZ2lSyLBVALvo234macCKSKfiM1sgaJuUrh9GOJBD1YJ&X-Amz-Signature=f5be70eb22a5c079ab214f6b1a098ba4ff3dcc2890592617f2aacde6ca320dec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


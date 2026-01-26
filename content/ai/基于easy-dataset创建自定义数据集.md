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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VOVVJ3Y%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJGMEQCIBktmxTYWXEah0bw5ImN0Q6QckHYOPwsyE6182ZSIelAAiADLDSqkW%2BH6M%2FegVS3cqBZAgfqSwElWKqt8FJi1fwcyCr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMeGwyByaNHagmL7DYKtwD8Sy0yuKI4hib1gVZXBqn0YWBif%2BUOynj3xiGQZFfZU966Bjm7NKDYfr6Yz4BfuOqgjk4OAByt1puClfltf9SWFO%2B02ozjX3A6JAQ3tV4jgUH4aBxRUWUZ3g653kY33II%2FxGNkkaQ42ODc36DyowFNny9UmadGRcpDpC830b0uNA3eQHOQjGf2UWDQQnQ8hRu31t8Q0CpTX%2FBna7XrFqaNQjl6klPFnY1kkGyO12qS9djCfa1wDuJf8Oqt61%2F5VAhQq5MyT9dUKsaADOBMhXOhh0xB%2FkDr2xhjL3eWXxWZD7Z6xQPRFqgrHC4u6Nbg9tBzEroiDBbhHA2Ji5xhbiuKOc0DbJYD5%2BDh6DLNrvHd67mzw8n8ucym%2Bu7oDUc2iZ5StyLqPwpBBnHaUwwe13cINA8jvZvdCTWREqX83yNA1LomXFA5tx6jxYUTS966tC5%2F2U1j%2FShjJ7PdyHMHeXXtFYjTtZ9hZFXKT9v5V2bvIJSc2W3Crmr%2FC6ABsTPJGrsR3tn8q683NwilezOn3SJ1ytG34T%2BNa30U1MAgebkF1PGe2YPqco%2FcMkh%2BAZYTVlPcW%2BvuBCKH13Uj4RT5JKzSmiDxTaSKXRzYBOJrg9DpCZyFFxnsYorcqCtEr4w%2FrDaywY6pgFV3AyI%2F6G9eZilcZ8F0xQP9APlXAjHfH5M6grS78BYWJ%2Fh1%2FbDVts8NZjIwhk%2BpqdjZ8LIZIrOAs39l5tljh8gwPTQkCKw9z8PFbPTBjkgyrbnG%2F6fIQyyj11hNQ%2BwhJKlA%2BClui5Xt4xz9oBPIX5d29eTVuwDPeu9%2FBvwc0qfbLpsJvchlqVZ8lSx176hgrvJ6xgWdckcSCmRa3Q87Aa64nThyyDZ&X-Amz-Signature=b168b653907b309014aa54e85822bc1549a8d8cc66c5e4c42cc5ec8c651061b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


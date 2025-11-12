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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5FUQRCK%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIB2I10jq%2BQ27HWpUlTC1vgNJl%2B4%2BRhnbNZs1rcHEb8ELAiAI%2Fz2IgpBcdtHWz%2FbHNMCT1CM6JxxpxDR4pyUx%2FJeWDCr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMdy8pJOg3ahlIwytGKtwDtAB837Kk76BvkuG8gcHy8l1fviHOFVl5YulbD2oqf6MV7ZBJDuagYscaGm369kbV7Wg3y16TmQ%2Fnb5gQvOOF1NjVUV7e5BmQXyL0TOl78hTypH4yo92ogUcCtiryksoGyKgL3n98fcKjA3mEkx0iOv%2BgfE4etI29JuG9VCj1w0j3aVIUKxv%2F5q7jTqj8nuXinznTftVQThugU5Nqk7pWQUaAqPSmCrR7YYpWSIsiSN8aVlvQyuvwooAG9YR6mfXvadHm2z%2FvrTBWftNz7j%2FGQtpiSv0fJpnnYjqSM5cZzJNO%2BQ3G8slzrCA%2BmvQ31u73pahVMs54CgzipX7yOx8YbehtGiCYhqbwBiFJhtmV9fhRylEGyYE60mD0hQL%2FiHBMJHdjiZGgId8v9csObrlmItlz7DU7RqiF3wzSvs0n%2Bl9fHVQx1XQzWaNGrp5BPlOJfj85YV44MfmtMC%2BxXg9HBKMXseoq1fFv15mbRBk86JEhvF31pNmtF72nkptndDjXgWeg9asLn3CNi%2BSOSqMBxf1Qq1ZCZrKUCtzCA2KKGIfb6FCPpqYB0re3js%2FKe79kUyQUXNbVS0aTmuFntIecmyT0jMPUDC5AwKGagtIQGnZN6Go8R3FI7zi5EcEwo%2BPPyAY6pgE%2Fhu88omc1KhcGGaWkozzaBEiajEKWl4nbmoTsTOUORIyAU%2B1wVoFad6pD0g4mz5O5fSeDipOU0ed7o4yVqGldo8CPWQrBnm0DwGJFuKLrga5xt6d0MHb7a0NDd6l3sxgaLAbOglS%2BM3CmmHIeYdMXlsN9XjdTlWKOccUQdznDLYK04cUyll3UvWYnf8M28vZc2LMpLJ6AvF80jA4vHF15oUkq7gm8&X-Amz-Signature=7a6119f630ce243ba6e5772c56e29483e777c9492ce5c3359e34e5858bc1e44f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


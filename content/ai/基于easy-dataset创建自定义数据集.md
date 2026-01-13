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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YVU4B6N%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025827Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQDZ6Y7N%2B8xAFZ9fhnASM40EUH7RRkRQYnhdJp1tE87zrgIhAIZ16dulfcsLC8GqlTYYPlM0UguHlrKOqDf%2BUEAw%2FWLoKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzqJdZ2tTuD%2BTYSITQq3AOqqnr5%2B0gIJ5T0%2F%2F0GensycIBenhz3NpwqGgx8wXAE90EHmNa3X59Ae%2BwQY57SQd%2Biolv0sFGaF55Jav8wkxM%2BSVkrHJX4byuKfDvbQXBEATqyvi9GN%2Fm5oXw4YJTZdWDvZqZyIfB%2F8OjD3UEWGM1IaZOXJCz76V9qZUJ7x9TmFx7EDpnBWorDTmp2uvCCHdgprLY8dPLA015Q2GZ%2Bph3yCaSaKKFiFkYFYBJIZDYjM0txRavgbhiHQSAMFIyFNxuVR9jzzHS6KyOARS9MgbzbAmgq1w6A%2FBK2AUwOF1feAkKIs%2F5jRbDxN%2BWzAIBN4eJMWil38eYT3OpQYTwW84aer%2Fbp5viJc9Uzi2uzF2vXLbFW0Rb5BMwkV%2BThVohCkdxkHDWE9phV1sp3RWKMib8dH7rg92W6V24roGkfta48lUVsfyP9Gz6NC%2FuYFCZQnpvwGRbq8PHoEsjpA7aldToiMY4YIL6Z%2B3B2UDmh0pJEH%2BI5TqrwXKb4G2tG1hVE0APO2BxQAmxux4U2gEmJibcEi9ls6PK63lmsj5%2BiEFTw6DPIWdHET06uA1Th82BiT%2FQF7K4%2BnZ6gWOX5SLcB12GPiF6OvuIQYCHwBupS6I4kcoXtwM5retEKcwaBpTDT5pbLBjqkAd8pG8xqlbsmvML8BSjCDaw704i2kTPStzxX8lO8BlmXgYc0vThN80isjUFKcLsmNb0R%2FkJDM4G%2Bs5dtXbRw2zteKA4FgZUFxxcy%2BEk%2FY9rf9u9fxo3EalVXPSrd%2BqfHiUSSUBSkBFK%2Byo2dxHIbt6aVDxFEbnpktbQ%2B3N7O5DelAJg2JRwQnpsK9fOIxdCN1mhuvt7D691DmkaS0Ijozk0%2FAyUO&X-Amz-Signature=11662c1d8d09720e5560299855b03acaab7fdb2f69ce7d368d346473ce2bcff2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


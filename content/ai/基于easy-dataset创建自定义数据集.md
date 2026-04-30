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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466725LL7QA%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIEhnPino453sQHl0QpfOUiwFPOA%2BAoM1smt0ygCthvTmAiEA4D75yPKgNAdH4hEW%2F0Z8%2F%2Br8bPEeri89VlSh1wKWatgq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDA1CXPv0AQhT1diugCrcA0rRAlxuBIFXwma%2BI44iHc9jZ7iRxvS4ICrK05L5WfFZDrgCwLk%2FVYXuT0V5iKL35xc7V%2FM78KAqsjSw44Rn3OyfupsKokDDxBaBBII2wOJtfNzE%2FlfmcSl3tqfgZLfWEuauk9ok%2BA9w%2FO0iLYXcftCCccCWEO5TUBeFxw8bjhd4YC0W%2FF0AjScAT40f9z3IvEF4IKXXYCpjt3tyz4A%2FEqG%2Fck7eGIvCSA8%2F%2Fqqk5kc%2B%2BEIDGWNR0PEdyICnLsAO1AlwUVRQjpesbT30fR%2BNpq4QHaCVPSeXotKWGptK8TseQpmsqDFWMbmz7a%2FvhJvyzE5zrG4AYnc4lT2q2N7haD8yOHDy5ErlGHt90tZ4NgLKq1mZLoE73iLBn0AMKLi2Gisah59zTYaiHs5GRMBgj2uvFH55xkwv0bFnu4Xg3jFknZWNCoUfFoFUPlbGq7xzOitK1D2igq9oRy6yMsZlq2BOPCaHs2lI2K9822zOBvUzzdwENrLKAh8RRC3tTih2c2nemZ%2BerA0Vr%2BlsCy1FNSRQ%2FWAM%2FhmT5G17EdZ6mB4zNKGCYYe29E0Twr%2FlGowPnsqbu997Q%2FjGra5MB4VdsReh1%2BiQbswx2LxgBFyakDdOtALFPaoJs3%2Fa%2BpmHMKibzM8GOqUBij%2BXwXiBXAPhasXuaLGGiiYUQ48zyHaFnwW6Y8E4aErgWMs5IufVWYo2PxRbKsF2Yh%2FZISm8hTM1akOvPPDfqCKEFSB%2B8o2Bo6nDsW3Ymbr8%2BYLyQgyazr0ZCaVRTbZ77UBcAlHFEW7NZYZuPpOeEFBKUnU1QO3BJOJiB%2FfWRBk4kQla2e%2FxODkagoP8IUJ36Fw%2FZWr8sKMi1yrDWP9Kmed7i8VU&X-Amz-Signature=6166198cd79c179f3adff22d5568b10923f0441b3ee99e9164a5c432c4c6d4c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


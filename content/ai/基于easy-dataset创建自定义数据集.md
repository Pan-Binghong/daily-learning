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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MXAC6FX%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGx4zvrsSEGnvwa6SIVc3zjSsNsi4RvaExi3PXJKQ6wMAiEA73RvKRk%2B6jxO3xJHuysyim22dBE%2FLfEpbeS49rGeFIYqiAQIqf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMT2ZBtQ3lecSm%2FV8ircA9fjZutmLNdhB3zPVq1cMqAVtJ3mqMYQ%2FJbA38%2BUFxTKjwoA3z5JDJNxLjNmVTy2w3wgfOcoCBRpCdPTuXLRYMMZMh23crFqFEM3gEplmPZBqxYfOxfH7DGnzC2Z5M8Ff7H7%2F6a7te5Ph4SF%2BvWhope19cG11Ro5zac1IK3I651Tqd8157gZ4hqSL6vz%2FO24lc4eo35VstFOkoBzAX%2BkjnRe6v0LsiISe1PpxayEomTVWgCcjQltawPvqHmpfmZYSjG2%2B7Ve40y8xoWpiRWTZg8k1uWS0iGaEZa0jhwq06oEV5Hc%2FNv7rralAFFjj8NL%2F9uj0cnAYqZ6FdrZQm23NAcsUc6NANZimODFv8puAB%2BHiw9lPcT%2Ba%2Fu3mSyvr1w2CaV81l%2BhXPl9cGNSICDs8wv60HhfX1yRSC00pCZweAgEqWqJXfy4YLKgo92bWU89w2Z2IQNc%2FZzvJ80irwIWlS10powaTnHobh5I18cXZaB63ZT27Mct9315LiFpt1zF6Qw0fG6r5OyGAsIXI4%2FMIjagBwc6Z%2Br9eoZgqOta1u3oW1yPhAJOuM6DrzE6Qx3CP%2BhJ4%2FX6FE1loXXWOV3fNQ84rOPOB5wyQonjyO3VjijXCWl53eAwFpdKfZ3xMM%2FOo8kGOqUB%2BArTfOkiO9k9ragYK9zof3XW1ri6cXAldmuF8v4bLIsBZXRH1S9OLqix7Cx9tX%2BMs%2FHkIAZt3V0qTTgX57x1yjUJRYWJo3eeao1Tz55DXMq%2BisXpxvojkbkhSa8ksM8nXwjgRU5cexuSpqmpBJllNfegsa7hk8mU2SSQb2W2StJYTwBJmcKlaOtiAxy06rxDv%2B%2FiZEtYjGI8%2BkOhskl7ekMpN7RJ&X-Amz-Signature=43e361077322fa766cc426bbecac5d6b408611cabb365f6b5480bd9d422840a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


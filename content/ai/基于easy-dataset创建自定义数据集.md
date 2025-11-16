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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQ53HPTH%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTAJGh2xRefK%2Fu7yBsxYgDz2cpBiyLFw1Amj0DXV%2FgJQIgOGIu2rMqwV%2FJxzSvT4aBcMJ8R%2BMEzbM98lpcAEUH8L4qiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHP4t3jsZJdiC%2BdGqircAxinB8zWB1uvCbUY4qwGMgEPDOqjp%2FQtEIbb7EcIVC7LS1yrSW%2FR0KXx%2Fs7NrCO3AEsGwn0A%2FcXqKfrd0s7%2FEotPEmOGTWQPJZiYLw2SKLdNLedkq32atD%2Fw%2BQb6tu7Wh3Mbu0Lwo%2FfHo%2FkHWHX85Ha5nsQpXG4tTvq%2FBpCyddWMX9EgHJL0kP9LunjqfB4arIpoFr2fRJRCexzgFgsTIO7s7%2FZLeAL95NR7sdgKvnchrcubdVyM8scordCiMSk%2Bqc4j6T%2BwaQvzR7yLdUExdvewh2tCbKZZDoWH58%2FRTfT5y8K%2B7ykv%2Fm2qoKxmvN6ttoSDHepZl5KSlw7MjDXh7VJ%2BfKqBU1BZpzJEOZWR%2B%2BHp%2Ba5HFWwv8800kg0QuI8mdmpr0D5gbiqVW6btHQy8u%2FTW3lGPX7brVpXut1eq2jBol%2FbEet9HP%2F5gvtaNfqLoHobnxGPeXdYzkgISmM79U9UkpufaEhINVGVrvKf744hy%2FxpgJHRMdJ58TdK%2FMwnErc7CHtjWEb5%2BSewOBlsJ13FLiV5LMORiF5m36zODLCAvqSMzJDmXEMff0ylG9kG6JKMyrzjGuqi2vy%2BzFYanJ21Pr9p%2FBp0Rtvfu1KAcOYRNdYZsBXaRd3jRgeZ9MPbg5MgGOqUBML3vmhzBCBoo0ids4vHCRzBPYG17bc1IUN%2B0cCbzc3bgr%2FRZ8FoupDJ%2Bdus%2FKOFIdYeVPw%2FKAb%2FBfrkRwkBwTxTcpZI0OgR5mwrqnzl5wydnacYVQD%2FdOuD%2FQr2CLgvc8qhllNna%2FYL%2FWwyDoD%2B2Prbnjt7qgwe94FT1nB5oRCAO9awMhkU%2FvPrp7T94IPaHwp5xmJEz41umeLfqngxV6BTsDk0u&X-Amz-Signature=05c60448d1d85bd7b2dd45cff43cf620b0f5ba07bdf0fab7bb9e2175e725326d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WKHGTJM%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAPiqgxC1TQ7PB4ekM1M4ULUR51VhzfrPxanfuHpHFv4AiB30v2nYOPRuPWaNU2%2BUeI3HjySmHNh4qy9e%2BsLth5nmiqIBAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfR3WoZZlePnhje5IKtwDx0amgf%2BWnD966hQz4IWt04ujw5zmJ2hIMsK8gXyjyDz3G%2FLcM5EzxASlgcBXRAbFwiszmdI6u8sx9iUMlBt0sk%2B2fAsayQ%2B%2F4bWrCcX9PCxmxcDf3XPstTLRrFJKCwZfrTxZ2te08zLCxYi8vIczR8eio9nCxn2jSzOOXy4FeLSKk%2BFWFfTzIbYWKtrOIYOhJrYiOorYI6BRTGIMx8OWVRZ0j5plB%2BePnzJumDyuO0M%2BIhcZ3xNCb4TreZgPJfUr%2FBXyvcvysBli2%2B5rRg%2BDmoBlbbtzswTBkNQzQiwrdtCCCHPU%2BkbzmdRgEawlVJUehl0MbY3HTUhzWhWVWLMw2S2xHHtR1yAAWjx1CY2UU%2FsSrxESwOZWMtC4RHoiwB19JzSDP4KVNWaSe7wUQdeKvTpCtfMHNmRuLgx9%2FGYnHFfGH9OJpGyhsT4uCIVPglc8U3DoQjhV1wdUGSiY9S3CEMBnENV2VrQFJ8MViMkJDNjo%2Bo7E7PjV%2BDXFs5QRHGNmKLoqVVEXA4XdAzL2wDRtsJXcRhiIvsuKJ6C%2Fxrg2WgYtaBw0Z%2BGdZq4CQyIcwGJOYZZ0H82CtjsD6eVAsAzcvtVfmpmEuBixXR%2FPN5IRGJgp6PalaTCBhSsi70Aw2fS6ywY6pgGymaESYOdG%2BVVWFqylYnvttIvkeKY1eaQiJxbW60MZ4TpCfJADOIKX%2FPZgPe4pDn5LvEXC7YMVvckS53h39uUSfdyU1a7hrspc75i%2BVN4BJ4foUuHhua%2FKtVjo13vsxbvL0vUZXk4fnlkbLukE9%2Fpm2iz%2B64V%2BWQulroa7wavYNqLp7O6%2B4SsNoVEySiM%2F74fYq6YLHI3OepEm1LmX4mNUD19%2FRcZJ&X-Amz-Signature=1c48013e3a1a8b053289af01104a672cb74ea1b0dda2f910b54070aa1be52b17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


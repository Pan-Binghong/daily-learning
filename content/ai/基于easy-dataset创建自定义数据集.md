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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I45WWKT%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgtQtkb4bYHtkZMk0RKg7Yn%2F%2BB5K1NbyrbOgMMpbdx8AiEA%2BY%2FRzTL7vlSTQ3NP8ef8t3gBd%2BCW83hG%2FgReiKAmkY8q%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDCzQkt%2FAK8Okm34vpSrcA9%2Fyi1urGrvHj%2BtxGMTeqzeIU4Tt0YceCJhQeS5XEX%2BWXzDOPou5X1zpZ9K6cHS67Sy1PhbyVS95hD9S7AH6HRHBiYughk6rGtK%2BSP37t9W87CWqhUSj1FCroD%2BfAauidtY%2F65hBBszvrAy8GwDOkC%2F7pX49sR7zdwmBWTW7iXcjhJxkKbHnMLPs4s%2By8uxWqPx%2BFeNVQRY10Jtug5Vp0Dc3n6QbuHqQmAQF8EBx9HEw%2FB%2BqzYjzPFlq98NppxoGZbLepnWq3w001Zwt6IZTFufMLGS6jrunmd3zXMhpImz0WyLVEMRMGUWzcN87Dx9MlYn%2BiiEJdgopE9IEGh3n0wF8PLvXJtdN%2FurinTNqLRDdlS0%2BNW5X9zrtDNXtxME4TZRiz7byzMATQKiQX29Y9sUgCj9uYicW271u8Shf%2FNNDgztDsdCTES3%2FdbovOAu8xAaH7pvSGFNBvuSx%2Bx8%2F3Su4sD37En%2BVs4z%2Fjr%2FLLaTFepTyMa7s%2BEbtCA%2BaokipBsVfKs%2Bifg%2FXlqPK62yf0%2B6CtQImPQyoeiLHs%2BpIDxHnzKHtXZiWBcUf3BftKRaB%2BjqA4SNnzaqw%2BfjKWZ8SqYbab8Hn6ItET84thjY2uDKtQT%2FWsA7%2F7%2BoA6PzHMIOj68sGOqUB%2FukKqeqm6%2FAUE9SZuS9Hn0GX%2BZQ0cljn28nPJ4%2FsmUH0k9gbXW2DGh28IR7G7eV0TTNr%2B5d%2Fo7O868x7HlAg0y8J0I9ES%2Bu97K4FaLkrY3j3CHvuwU8y9Pgd%2FfISZwBHBsA2pLotkCBy9DA%2Fux4OdBmWUF2nkD3QB9y68JmDuMkp14XUSBPZcl2GkTAC5YdVmpFUZ8rZFU7wyHAN6rV8FZC%2FiSMY&X-Amz-Signature=8c07cac8abd8cc85aa7e64cb164797e4e912ded94fab8b8d1e6f4be247d2ae6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


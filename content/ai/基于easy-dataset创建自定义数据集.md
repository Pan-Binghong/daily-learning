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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLTW4ZH3%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIFbnxo%2B1456i0n1WVPiflCn7Q7FdPK6ELg27u%2FZqp52VAiBZQMiS84mogF%2Fnjm6IHtwKjt4h18BJ4h7qWjSpOZyIsCr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMemyKHdTO8%2B7h6qiQKtwDgRA0%2Bov6ukpkQcUFmuIMgkv3fqwGCMw2PNsWSGmAGGeuGN8Lq8ZergA4dFBBel9pmhO0nv2Yc%2BtTevAGN%2F4NiTmIFgWPApty2bQAyvF%2FFhpQfowG5ZG3d%2FZ%2FtRcweDrYLhLlx3jQFSXrX%2FfAuuIAFtdnHnDGu9eeQ3jVSuGC6a7IRfFpVcHsvMqDdsSwuEBPCvJTJPdvl7YE8GPcmf6%2FcEJVtV9ROYK4YPKdy9MLNjSV7LXRENhizxrlBjIgJX4CyoTm008K3wN8L4lec%2B2NcASRmDPhYK4wHJRLi5Ld2ANAb9xU%2F9lKzYdApjt8MumkY%2FRahwPNokW8bi3jBCcMJG0I7qP0Ef4Au5j0GBQJ%2BU5XNROcs1r36NA1TXXT1v7ChSgz7g2ICL%2BjLPXzpF2nyvstdP44WvyRruA0qsNP425s12zVPUoG%2BOsQ3dlg753V3cagBjzPQqTxZSLqpM2yaYdRc0BsXBEOuggxJe8vnTR3ohXtEroZ4VkDTsui6mjJnVYo7Ps9PjuWH7DMb9SvO2SW0YC5Tv92NE4Dh4ymOm3Nn0ofnnwS%2Fa3DHZvIB%2FdTT02Jl%2BVyb6GGjO%2FMuDvnsL9UKg3xaKUVdTFMxHZxU7%2F4QBNNUeYbqKHCzhww%2B5SWzwY6pgE7AdPeTIiFAotfx3HVtjqBUZRSesDGV20lUmlGDWl7qGH2hEEDVr9v58H6FQbHXAABXBavo%2FakZ7YSxRrCSkWEL%2FvdTy7jgZ%2FmHQ22OVLv9305Ee3OMHbxpDZ8CTlLhJQjU70fb3VGA0yeO5xyMLnZuT4Bg8xsmGvG7QiQcoLl5KtbQ2x9GiPobvcoR3KYLpHa7IeR6hGnRsFO2dj%2BaWC5VOQtURsb&X-Amz-Signature=de64418a27898641dff249c06e5563ff56bb2e892ea2e72208a4fff45ebe7800&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


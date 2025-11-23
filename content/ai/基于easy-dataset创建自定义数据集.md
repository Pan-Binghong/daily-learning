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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7LR3YSC%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIHK9bNjjCEHHY4aJ26%2BQS0DuxxiEAitZj2GJVdVa%2Fq49AiEAvGMVH7A2oiTrKnlEtbM7GRN%2BPpHVBY0t%2FrHb45TZSycq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDPiasFbsZT54ORi%2BmSrcA1rAHtmGiAXPtuKgvq6IYJ9TR1WmsjHH7LAn%2BUz0SngNwjUjQXBJRNnyA48AW63OCGVCkIfeivcz0co47Mjw5hxPSfgQ61yFtbn95giYhUw9PtSXS6wN%2Fy7k0Kf8UQsSA%2BPUv0shAEz3f%2B0BgoTV1RtdbA9hAP8zJIt1lUstDPJRNejBVDJIS4apHABrr6EuTusO%2BOUMs2NagW57OBCw39x8J54m%2FLvuRm0%2BuTN5qz5NSIH74%2BVPABDDAQIRR76k9Vl1%2BrqZR9lWpS5Cbt%2BjlxJ53som%2BK4tNrmjrx8UO2Dn3X2ksTo5jSrzZtWvAtK6BAcTEGEl9vn%2FKo0rHc88E7DUQymx2Vn3wiGPWKmFjT%2FZkh6AqSoBuGwDf3XQ%2BCoPoi3jTq%2BE%2BvWxTSUOSZd2z6uMqW3WDmMnwuoDm5FiDJzA79aRbOsyfzZC22%2FtPCpeFwap8kIB4fHHSPsnrRsumadZDBCqay1MGX6dc2ycx9OCZYHryWeH2Z8nK%2Fe82%2Bj9t89nghhr1ruU7Zk%2BRG%2BWXg8yvG0SwpFFLh4js%2FXDoBW2eJ1ufoVS4pIwzAqgITO4T5DhUEMQ%2Bb%2FrpkUyxgqYibv5uJEjZB63IAg2AQrDbakxCh9%2FICe%2FCkiwZaMHMO6wickGOqUBf8gDDtgnjZFyp%2B6ZJOdSiAT2KW5RqmwimGvO4o5aLR%2F4mBnQtnzF%2B49Bl2uM9lIml4C%2FxLd5srZBco1JzD07uTOVfJCO4hLbUD6YIm8tLNO1VAPgIEP7xzPPD%2BNcKTjDPaibLOH1lOa8OmTBnI8RGS1Qbr07TyT25ppuFglaU23lGbpkRNuZOBo6HVAroEB8K%2FdoFenxx53xbccTEWqg0Q4ZTC8C&X-Amz-Signature=2937125d5c2c1a713ce8e6c274a5305e914dcc5bf8234abc6d96a9196fa9d40e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


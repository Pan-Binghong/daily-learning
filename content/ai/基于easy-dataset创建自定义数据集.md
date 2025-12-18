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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4DKRFBK%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAPrgLkc9otXIgATVOKvy6wsHaffKSEoJiHk55Rt6Rg5AiBlnrjTsNW01a6DVamETNCrp10McrROXUe6%2FLsGlEB2dyqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrHuaiTJq6jNYEXa%2FKtwDEz5RzXzzdiKpR0OJzsp8C4dl1aIt0%2B3AG9uM26IWKlc6yADaMNDAbwQIhARraRvilgJoEVmP53XIZiQMTHL3OJP8stB%2BBlB5HrRD3f4rWrBgrA0fAsPn40HGQ2bme4r6mePY2ZSQd0grO8X12CwQ61nTXd6IJR%2FXT%2F8B%2BCMD%2B0nVsK0AQ7tvg%2BROgVYrDViNloNFs58PSujOHyRBEJGl17Ww49q4LVUsBlptXRZQ6M9YlddfGFJqs7V%2BMUR42x%2FXTIGjfUW5M29Q4NDhP%2F9BmujR8%2Fw1WRAYe6Tg6cB6gRN46c4OnEr8qCgdTmw0I62KoJJ8Stpm45MAW0hF0Qh%2BHQuFLxAiJ1U2X9gB28QmtSEqZTb6%2BbZFutwQpFoC0nmt97VAfNMURB3st7x6QTnLYEbqy1DmCp2VrTxTixP8%2FQd2i7h4pKUVSVjhR2jfvRvrVJzW%2BEYmscJYQ4GvFAF%2BtMu0hb2EPax7PG%2B5ehcxmbXmLCR%2FOb4TqAoG%2F6tkJqDd7HG9uzIZ8kuDSrmvnnKRB6%2Bo8psrQZ9NBZNItUtHoS%2FQhWdfMXGGuNQMRtLREPUkkPyfg6ptADSiSJdD3DMPzsHz8GKmR3Zv%2Ffo%2BkbTO5dwQllGueg2yoZmJhtswrsmNygY6pgEkldHHV87kZCkPk2ytmGhJ09omvbQWoLWaQNLAyFnj3EdrPj9Npv6waQUqdrcLSBUnrXHS9hI2JRGsG5ykFGsFbrh2VzKgB7GPT79eAi%2BjvLjAJOGXe8AWqDujyz38sRPqbJXDuSeM8sIB%2Fd%2FmtfzrZPLiVyoOG7lq%2BQ0uHapDT4oipWA1Gd64V3x9gjRN3PgfmR14y3t%2B%2BgzTpm2hdRwdHkiRAfzd&X-Amz-Signature=ae53b0e2c79703d6085389704beb1ed4bfeb437630799a7388a163a984b0eb8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


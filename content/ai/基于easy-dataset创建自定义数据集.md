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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YL3GNS3Q%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBQGLEBI%2BhojDwBHEjQdbX2Sbs2GNsA4adj9l9cQWvWiAiA0VYvnk9TYwO6FiRY7KW3ohHDsO3IFG2Us76BhmAIUBSr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMEf8mohndSrdZSb8IKtwDHHwfgrCIhWTsvualYRx2RTTrW%2BdiuahR79buAC2Qtujrrcd6WjYFuClJPtad%2B3gZohBFggSExIaRh4FVWxunzH2%2BIFQh1w97NPhMT4vAdfDW0ZXGTIEUTIo2vyenLANx9M%2FfGQIh9SwPuQYKZ%2BCCXVWNbzF%2FXQD%2F5jnr1RmjhC3xiiDtA%2BtCyuh8sbhvsWhf0F1A%2BLCB6C9bRRyfDhxHiHlQXOEUoTIF1wezF1Xb0hcleOC4zAGbvlEj3ZkWhxyDXF6my1YgLqGZdOtjzqIB0QmI7cqQ3aARU782mL8wypmstrDoJVvxwzKB2Ij2el5zgHftlMtiR0Pnvy4DlI3adpLEnZKlKfQ9Pqvo3wj7yjWkomKaKYniMJZWIcE6zarvLh7hAg49bumPECOfAeoEwjZh%2BIdTEgTxL2%2BsjBL2z4ehQ8zJhzhOT2xVM2alyP0Yap1K2ixQLq3OfYm7eWcqVgk65qv4thfBLpDrnkRalimyck3uaEyXYU9jO%2B4MZe%2FX2TaCV%2BqUcCLnayAJtUYFoHHmqLhVOP6TtOeaQb7evR1jTMXflPM2N7NJyvWcwTnOPrvrGSJWFAbj%2FgD2Bog6aKZEm40hlZ4D1QTQF6Bw%2FzFG6f4R%2FSlYTdDa%2FLAwmY%2BcywY6pgG9A1c%2FxkAF9Z5its76ruMQrhiM4HDMFv2SsB17WG0uz8dRH%2FvHyVYXBQ%2Bh8%2Bj9NeYqQ7FpmsJ4SttFrviqiB%2F2yDW6vVGOiGu2NxnEY9Eg446VKHg2cCcHWCB333%2FWJb3UsBtX2z6xw7%2FntFyl7dD9ynTOd8ImTgwsdCvrZdfOvMSSPHgZEZFdYxh4hINWRvj%2BWW6G7OT2e9otwdKA2cnfQI4ENyfW&X-Amz-Signature=11c1e494ca5927e0edb8e4720cd8def7a5e005a1074a9ef0266266d4a527ba78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


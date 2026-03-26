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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQKT22ZW%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID0i0AVymMewe2dA%2BBFF38pkRAxM%2FrYCoZZuv7JUpRPWAiEAxIaq5lxXOWvt6dREbwW3DMfMu9YtPM1I3f0XejJJzk4qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPtdnnM349u3QzkZ3yrcA79kb5nmvN%2FFy5Yp6mcelBEz9O6R4cI5Hc2pCMaBuGc%2FIqoDsNDhYcBWsqKKYhA4ugH1qPgoV3MWsutatVC%2B6V9omthR7hY%2BypcvYqq2mkWcWYlfmF6tbXMRzojMJlFU%2BzESejyI7lvYlnHqCwmlrzw6RRqSv8luGAKTibeahLlDLf%2BCMAMp4YMAQXp%2FDmmwUw6TEPMFo%2B0Qw8Q0zEYc5sgVixBKLUZhzEKItvhKTZiQDWIrTCuC4LHb%2BD6OxNdLIzKI%2Bh%2F7Hey8ClbAI50ioi2Zj7sxqCzNfSmGvHPFOzbXvXiI%2F9MybuafTfFAdRMw0ClC2VcOPwo75DL5WL%2ByM%2Fm79VdMDTUqw2cNhFaili62R3YWLB%2BmY2thJrsBonMSA1uNk0Icozq26MF8eWso0LYkH%2BZZeSbQPBekZcpwTa6IzzyqxLFSKKzUncMFZpiZXhLQYuTxfHIWDEDIn3AQMxJTkQ7fdqrz0OJGC24%2BtwAzMJ5KZwa6wVWXbB5Lpo7JPIAwS0nzeFL5jaz0v%2BqfRdHS9EkCOTggysVE%2FylNkialC3tAFNlV1jmXbxi1ZBG3KMaj%2B0TCr173nrfU3r8YuoNH%2B5jz0u5vIBjluT6AEpZaBlWgjllV8zEUauuGMNbIks4GOqUBpaNH2pHTQhdxpHZQ0pOQNbTKOhLroHbtCnAu7qH6RIu%2FfCEzjXc%2FkPtT4HXFPSS1oMWPSs1z9bstx2gEoKTTshHWYAVQSJASrn6GdRYOTVBQxUbZoOERkxao9jK%2F99MT4nYoxlPcNzYdqiRRJwOadMJKdRiLhqWaISp0%2BX5q5LchJfAiByYQzbXkHVzMjX1IAmCyf%2B%2Bawuw%2BcG5xVewI4mK2tBC0&X-Amz-Signature=08a8a9fbbd99ab0c02f0661e6dd4681311f73945c71d60389b0d5695fec24d4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


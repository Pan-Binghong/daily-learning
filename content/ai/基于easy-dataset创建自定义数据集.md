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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHL4ADU7%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDfPhI2zPaJLVvOjrcf1AAUarK39ifQESXb2vYKtUo%2BHgIgTJOH69QF4URXONHsl%2B6UjpHLBvSAFhP8zL53CZVLkFcqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPYZzm5Dm6yYVlm6ESrcAxHR9oIvzcexdQfSLtPevThukA3JixgocNMWctAgX4899xLnI4qLzAtPnaa5rhl1smn5Ovc247g%2FYAWx9SQowqArffI4bLicT38A99%2B9ahMW%2BwOQg2JmaD51CMJGFyUHvFCapn5PTmvJJLKIDmxmdzdFxbk7ppPx%2BqOCDgnGEbU52Rq8D8qbRSUQkQ4703MyZrOdOFU%2FgYoXo8Ge9Ao%2FD5aYGodQhsp5hy6JDKs3OGhxMY34lB47l9yNOuodCBq5U8uP7H3NcHxjQUAj2Hw5t4T%2BqaIbbtu9YsTi7nSHH2vh5RZYUtIHoMDCPUHfqgPshHsxVPVWBZnyz73n926bUPtix5iyc%2FJa2%2Ba1oI93BEYTtmjzd9TXqrY1PQYBBHGKQDq6mue0tft6IHCSXq8JX5JLoGs6nnyggkPsOFkEtnpeLhrCsu3rFYaqLFE4b9T9bbnGXH4hV0N6v3ALelTuswj5j9EtnDhKPxYra2L4G0vZhPVbLM7KVuEK%2FRwtBOvEZqjPww5k%2Bwk%2BuoXIP6WpOsLHH0JZqwjozIyiV173Wqq0SVm7VXut7j1tnWvQC2FjPNxFAL%2FTUHaAFrrS1aD8CHWGHkHffclp4r6ohPjVUQtlmAL7QHUINJpUEgl4MPeGgMwGOqUBRoB%2BGF5CqdQ%2Fe9QF5uOW3uTDAx3nnqvl4ryYjRPohLsrap7v27uWtbzSIvYOnki4QaAQf84zH8I%2FcqBiQU4fvrQNJ3zvHVZUq4PV2k2stZOn9KUMpn3nbfyupyNLXeHB30OPa9Wb9vBu5%2FU89eQlJCNHlhTs%2F%2BXrNEm%2BYqUvqv7S3gngQ2wY9twKxhwtHO8NRIPzCg49KI5t4TS4BbDMui2y55cm&X-Amz-Signature=a6528f4b96b7efcffe3dec1bc4a4a5090ad04f1030d74f62cec27ad91f8252c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


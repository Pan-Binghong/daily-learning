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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZVPFFWV%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCFRbAejEmMAvah%2BpnMeg9yCqcBt6mDBE9yoAkoLM076gIhAIYBxmhItHlxMaPjU%2FeEPt64ppj0bdYttiCDvokqPGhEKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxif7vyir5yFKtHyPQq3AOPSBkalkyMKCM3gYURuSCLeBZRJCm8FPq9oyTxsBe7hsgQA1WURt8jaqQvw3zIj736y4fJh7SnJOqb8qiHrf%2FOXMJqedUwn0LZGQ%2Bj8V3S5hu2%2FBDtSAd%2B9scrwnt0taX48%2BiFf7XXdmM4QkiR6IMXsVJLJz0QdOcR4fKgE0dJ%2BRb5mcAVCWliBz4WfuPuOOLyfQovHNsWDTYb7mnPulkMbNSRb2T1dg6%2F5WOuJ23Z48obULOfQu%2FXM4QjouPaJWC2xerlrcSR1oAJulRPFA%2B10FS%2BqXCWFFcGbFGRLe2YduHWSif5bAPnOJjHYaUZejexSd1Tl7o6NjQYrK%2B7OYb8NxsGzB5ToCsCLgxGselEMNkA5%2BkbxIbdVQDQWMfG67%2Ftz2%2FmVkoW1gllKo9Uoc78gCAXEiDQWz%2F%2BKCuS4MW40jXKRDYzKP9nH%2Bz9rggamklsJXp5wM9VbV8cA6DHugMqjYKE8%2FwKuMS44HOQzGhqlZVIXXOM65Pl6un0sLs2FctuP9OCJHCo8HLLXMF7XLqDDQPa3QVbpBTg50Q8A7wOcv2oLxuWS88I8Zo0T9%2B%2FeXFrU68yLCOKpAJ59kePTAGZWm0b0Z9oh4xYyePHm3woVjNWVNMpHHRzmzmEuzDxwqrMBjqkAWPc4PzYdmc8UQtvE3KrgoLzZottwgl%2FZlZtFjOFs290NyrW%2FZb4G%2FfZQbpn9Q1YpLzsb4QqpVdyodBz9zrXIjseUlM8YjacT06aXQxPEUUOh9ryt4Bm1nfcU6Kjx5%2FNzrRLOhdjkWkMuTWpGjG1vwgMzvTrK5TPyadhc2t%2B0f8SBhitlAVFbHKANJOI50GuXJVgJ3FBZ95WEavuWh6LGoB7%2F%2Fsi&X-Amz-Signature=7865786014d261ab4963dd69479b12b93b09f7099b433067cc4ec6e4b579b6fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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


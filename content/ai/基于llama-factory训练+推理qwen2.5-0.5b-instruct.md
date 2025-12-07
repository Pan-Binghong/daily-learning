---
title: 基于LLaMA Factory训练+推理Qwen2.5-0.5B-Instruct
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- LLamaFactory
categories:
- AI
---

## LLaMA-Factory框架总述

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626P6K7PL%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFzG1fYBG9dWIfDnN%2BXn0DxaLeFbWDte86tmAPp86RHrAiEA8hfUyYmVkWFIupx63nMqR7mJaXYGAGG7Fb9Pzh8HTc4qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAptGB6PJ7sjjzcwwircA8IhGILb5oKV7m8pKczcZiLNn5LQ810lSSeJJh13AzhjgnOlu999kA1o6%2F30WfuLxVM1neDVERqveGuvcT9SgLBXuoZ6h%2F6yCv1PFO25Ivsya8LIQPOWXUZ2A8vMd2docRg3A1OVYfWrZl2%2FiLR6CSqvepkRWbVHoJnAH9Dls%2BHQRIOfNvph6z2pkigDAjbPzUZo7sYZCsVniIumoZ9e8ve6At%2F6rGvoBcFJPPcXOqzwg526uHq1tGkZldsCGNMVGShbSf1FrZaEzFHpISl5b0UMoDVJbKQL7CiiSUXUrnAvYAIXJsDrumfBj4HUxT9Z1uoTt1k6XYOPTcOMUgwS8z9AhPuQIIlyMOhvDj94vO7myJ1BrjucwTpRSC1E%2BkbLXrpE1HDcke0Eu%2F%2FKzpT%2Bj3vOrDU5kFZCow7lCjgfBDz%2FlvT55PEIpOaGSSkP%2Fe09Eza3Z29qReuc%2FGUtVMU1DrbsIfCR0Zgtg0FY51D92PGG8bTmY7DX%2BLVKeqrbznkHMsuYG9aOCDb3rg6oesNLRtlqm5W15ZWCIFqa5iru2eRaZ8PO4yDVNVZDPOzFb3FgeFGfxwPM8qlId6K1BeP3T1ylq6jGsWF1ri2JnfudQ8r1oNHsAcWP76T2IebIMK%2F%2B0skGOqUBEe2yk7nEV5sYP%2B5FDCUQsvfgoswh2bUDsN0ALGaH1DsajlXjHLaCpTw6Vf3GgaT48ghFfZfsl9VxzpH9aiPcGbSZO%2BGL7sdfED8sCIZeEQdzKBk6MV%2Fc00uewq0AHNQxxC6U%2BbCCXkkDg%2B7G7xKVXM8uKgLe1ie094toO5WG4xrBJd6XkxWkw6EipcxuVsSVz4RpnS0lYOsqz42KOVp5iDt6EZV9&X-Amz-Signature=627e5c9d8f64e0ea9939787ae7700e8cc9c56c3d13fe476d62fde10fe744b79c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

前置条件: 环境，模型

- 模型路径 : /root/autodl-tmp/xinference/modelscope/hub/qwen/Qwen2___5-0___5B-Instruct
- 微调完成 : /root/saves/Qwen2-0.5B-Chat/lora/train_2024-10-10-19-48-53/checkpoint-62
- 融合完成 : /root/LLaMA-Factory/models/qwen2.5
## 数据

## 训练

## 推理

## Reference

> https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct

> https://llamafactory.readthedocs.io/zh-cn/latest/index.html

> https://inference.readthedocs.io/zh-cn/latest/




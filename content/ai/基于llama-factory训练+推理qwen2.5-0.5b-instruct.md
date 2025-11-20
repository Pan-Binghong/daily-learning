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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JQCDYOP%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIAOQBZ7e%2Fpq2507IiV7833ebW%2F5GqFg2AVk%2F9WTvg7b2AiB3H67%2F4Jmomdk6jDrEnh7SAQv13RT1eJezCYWUA6FVOCqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmylo%2BqS9jgSHR929KtwDgKIBqEDx0GQ%2BoYt9EpJHzMds3ZVVmE%2BhAHQgDDZkfBz9Gz82AqRjhFFTtaKTqth93Iiii9MowQktwKsHkX8iF0zUV3ViJ8Dg1O78VD6gFy8rHeuZqMvEgbZYX6pdpNiUlABY1yECm3mez9BY%2FzLArg0MkPDr9fMHTn3FJ9Wy4bmkN%2FFgM2Hzi6DmqTr31FTNmRnZlJdvVHAJYTUWiGeIw5a%2BuJEOYea2zxtCk6z9qs3yUIihqvysnmL4XiPHDgaYAvMLKkO2z52xA2RD4lsBIN52u8q%2BfqX7faGbnTC6y%2F35e6TVPe%2F%2F7oXSS5uHF4rLLi41IQy5sU4U7qvX7lvOPR7IerCRfeUGCTQ2CK3TztyDdGAIe6bBWw%2F7c13P2qLPscDMcF1EzKTVKa56%2F1Q6LO1cPeisGlLkq0F%2FujGID7E96F6N%2F2NdsGx2o9TI4xOtcbTyjlGWJqncBU3rwEtBdU0NkuoSgRHoWmVSpJK2qZemOz1bXHZu9ksE4TEarRRtUZ3U7RYbl%2FY8JB06W%2FDJQHGkUTMssNz8Kl9jSldVgWNynGmIyPNKNBWyjAtD5e3bepvsndKsMYFNhWQdXmYYTxfnkfnZLaR4z6kxmU%2FSBOxSVoUynSpyssv%2F%2FUwwter5yAY6pgGuuzNS6cONKn0eAW8EQiFgz3qeR1DPeCMRgVsAWcAdbPqvPMZV1kZj87pbbknqRJDBAVFsrCCX5biGygT0SN8yRQUJZYQtykk7TNnIrhsP3gYaTGqL%2FtEqDN6QFt72GcCCt%2B3BmkMuu76g%2FFTnkm61%2FrdIhDkXnTKc1twBOJ1uqmloXyKRCjeI%2BZb%2FW6bHuXYtV1hFbv2WaEbQKkXXD0wQ1%2BB9zWCt&X-Amz-Signature=c608a52b635a75a0de0edfa8fc60b90ab82af8406d42e14bfe032ef218d9a4c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




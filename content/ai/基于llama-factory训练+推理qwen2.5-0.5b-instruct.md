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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RU3I56Q%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHU%2F%2B0Lmm%2FSmDTt1P%2BuXgQVcqakTiRCJvtapUqYWUcrgAiAk9mqI7dVIYHwWaWADM7hVInqf4yPpsnrRW2Jyx%2B62ECqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0UzrCYCNLgkksbTxKtwDtjYnmi8AILa0RnYCOWxD6j6aEJQ%2Bc8IOmTMC5dtSiOkO7adL30qwSR7jcyAULRCuDQhPKMNE7S7Adw8tuZrtBV8hDjEVyPYBjKhjZnKeZ3rYEr3DmWjs4Zq0BSVF9%2FVkm1wa3J4bnJHJ4i8lM6CgSsBqfFqWx127fugiCM8sjwOw1aQJWllPkRKEoZ64qlZ8OSykIgMfSqv09TKZuJ1AiPo08nsw2I1xCHBUoqQkep5JLOi5Ro5aCdtXfJ8my%2B%2FIa7k2eN3yE6M%2FHxk3ISl2MVOj7DFsGwbGduXpxPh7vttBWwilhmO39YPZiRrpYyx676rRTyFLIA85ZkQ2GQVAi7%2BHkcJ0ke4b8z%2Bhmuqhuu6YyurdMmkyByHh4YlovDII6%2Ftj3cDizkpMyrpDWrNjQe4%2BEu1dPQ4MwPFOa%2BNs%2Bb2eNoYa0TRuqngzClp2qRUp6XswCBoXgyaC43XpSNQhPc2kU%2BLyXOJDFHUlr2f6gm%2FgDDHSzFE4PxbLNyzHXQvMupHtBp8Mt2JQPydwl03EegRQOhlVyaWVOcX3dI%2BVwm4GOQ7B%2BgxxdO7FI28g%2FW7WmEZ01wdLgjTidNOcGafBMQ6V77oLTbPMp%2BTeFxRc%2BXavo%2FuqwfHMM%2BUpLUAwp7jNzQY6pgHyS9SgZJam2QNJ39DLMHd0ZbFIiRhNxocSWLH9z1r7Zu9wMO03rgJTDM97xtvQTp12eUKRIPOkyScTlRG23tlBDfUqbO9VmtfoxAa0zClYDJBGfQtUa2ZMuPvQn%2B%2Bq8SGtfpvEfX6wdORZTDEBVZh%2FJMaqDFH%2FoUlceWUZFM4gZzPDkeHhsrIvbFT62SQcOhqyvf64ZdxEN8HCC2OmsLWxgBBbm9Yx&X-Amz-Signature=062504ce7be30cf032ac93acece730125f02797763101ac1df33f29276884d3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




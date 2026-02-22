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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7L4XGTZ%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICkDMmL%2FIu6fbccwRtDtKQMrimBVTpojM8RIgNpY5wOfAiEA1%2F5KM%2B3nYQOjfJuyxIU5YFSF0nBIyuUWmg3R505qOQMqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIu95kCEEky9EAF4UCrcA7Raq%2ByhaigDDbhzr3LH8wTuw2vBotj4Cm%2FH9V5ALGDH0lwIXzvxTxCtGUvFDPHDPtMEP9wfJRy3dRcgbQZ3NqmR1W0uW9HhytzDBCbTGgVLnWjK9mdiTfP7kxerRMRADZNL3v9XNzBNWg4vd5ZB240O%2BjIAOPAiwlTrvKkee61Jh%2BXn0Z2a%2FH9BNkvylpmiuXUu17tskipe%2F0YJzZsBJ4h5gXuO%2BCvlCEpBX9RB2T7Km%2FmBnwYn%2BHgfaFJ75cTJVMAxbwisSI7QvSTIrQ5R76y9RT7c6Sx6SG2O%2FtIizA9gn22OGJB2OyU51P88SI9kyYaHLhU7GSMr91aSOy6YcGpTgktdAg2vN04L645eHetAMNfHWyhq2LbGMdEVLP4Z2ojiB9Ed4Wzdwj19SDH1%2BbBFQqbxSF7lk%2BH0V%2FqjhNPk6J%2FOIwAF93jdOSbPvOmedGfZ0R4fpO7PbePwaGmewqYGfCPXwb2C1vmNCaz9qVHo946%2F4jrpDjVHMM8uWOLgmjc4A0xIm0b8vjfl6MlEUiFJBfHYMGkfOp9dDiP6vsdl8JpHhESiyPcOgLLoww3UlNIAy0A4MTgQTGkV3pJF0p%2FfAMsIQvAepI6h7v8kabjg3mFqj6mLv2%2FAYqYBML7M6cwGOqUBMKqPVyLS2YkQFr2Tsuh%2BSgmYGO%2FhKOkUu1rUMwxAi6cKKgvu5y%2BcKqzU4P%2F5k9u6YcMfVByNu6XCaPzO88sv5sAs16ONIwofBKjZm%2F0L47GTwMVzHECcwJibNuAG470KjwZGkD4RzqWwzFW2ZdEKxH6OPcQNUtdz0HG23iE1D9%2BR9tDlLmJn4CB5OXadj7DRikPy8LaaHE%2FJwApk60TwtWM%2F0CxT&X-Amz-Signature=6b84d45b9b24748e43c733efd8391a81ea4112df404ffe6bc4cc72be5f8bee4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




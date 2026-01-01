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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKV27FEX%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCICNOmVyJwNeWRXLO3pDl%2BZ9754oT4A1gC6nEItHSynN5AiEA3eaq8J2d%2BV0F4RyGfjKgl5rF9yBJLM0%2FpXw5%2FepIXwoqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCJGIEq8TXs3mETetCrcA2RyGIBYfzMv4%2B1ZWlI3XsMfLufLLj32LhJw%2FWLAa%2FxV5qrb%2BVmjoGlExU8mDBfgLRh7kiFfeQ%2By1Hx73B433lGkWbMt4KBXDuYbpNRJaZpCN5e7G0jxNNmOjK%2FvuX5MdJbtu7uiNYIQrrKAmvbHvhL0k10RKFYbw8UJFgSZXninWG3Y%2FVg7nuUVbRmneFkupE7oQFwhaLsCFRXoHQQtjEiNkkWWyRWbteyFRXj6Ge6oYgHHAhm2HC1oF%2FVw5vpbcAdQRihf490p6lUK9pJ0E5%2F3%2Fx8Otj6eUKg9l2fCJ2NeBjpzlADjSN8ZbNzmZjW4t8RfTdArkKVoFZgArDb5Bkx4i%2FaNfwPtoVDPBjDMVW2tiGXCu3FeK%2FMbPAMl5%2BSJF443au%2F9ZFNTd0dsIyguOZjxPnZonF5er1b8ZssilAMNksrjD3yiWbM2MxYeVR9LpTmkn6MvyGou9mkxampoWUoKaIbfhpk%2B7IJqZS0vKuyeWKyQJy3Y2WnTDByoKCa4SkLAJqD0KenKJ8w9zCh5gKmeG6xjfkYiurXnLNGA3%2BsTS84QCj%2FieRm3mMre3NetyvaJ2rwsWsKV8K%2F%2BljFrrPW0rBZw6DIZHDSYYioSgbw9i%2FnTytT2kws1HJMoMJKb18oGOqUBDjLlWFB2stMLVXYsiR9RClIawW48Bzs3MgDi%2F4PeUHT9VS5EX1zT%2FRcUgEEmzh5xMu2tPAbnB3EKEFt6Xwx%2FoPg51UiCgcieOXfhQeTwR3%2F88ks0lUrO63CzblKuJZ%2BQlH4jBr2ANvExOrcDeAEXttB%2FExiuRvccsf0P61X%2F15Vm%2FuPOi6ou5goL8pWvcAW%2BezFU2VkI%2FjayO1LUUQ9BH%2FwLbHaD&X-Amz-Signature=0e68bf2c1366ec41b9dfe922f3daed70174f0f5cb2d29f2848357afe534e141b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




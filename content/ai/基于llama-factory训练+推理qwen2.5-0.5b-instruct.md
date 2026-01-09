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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GLDOPH3%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T025955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9oCPup%2Fbjs7Ap2vH1RaKs1QUhs3Uuo9Ix%2Fe4n8b5bcAIgZwgEzRnrAqkA3pcSOrl18nNhzDdbdRTGZiCysQR4dVUqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNEYWw0kXQVEVjkNPSrcA%2BByN5RxnZ28QW0XzD1kgvB0yf1cxf61Fhub6g1Xr3cXBhGfFBDgycfDlYWTvjEHTgrIHQURa4kDsUdkp758rebvDec8EFP6sFYEiXq%2BHV5FKSSiNeM3x9a6kQswfw9trdx%2FKYdQpNaelfqMw7vsEUtOFELoSxkC06P%2FtUrklkUJAFpn%2BP%2FvezKr%2FjJFa%2BCqVcihBfW%2FX37S%2B6ow4Yykk%2FidPjMAvchXipmI1UcaXxaZWrZwaW4pIrZT5XM%2B8sRoKOdulde5UG9Z8P588thC4wCIK00gFQU0cg5quvoyqfa1VoriRo6kKcLQKwuWdwv%2FYRA3KP5YTrp35roqShLBdhtkNIHVZpFWHJFMBoEGwWuiXfbPVGp9z83ZJWSZs2YvCwB%2ByFUyMC%2BQWm2uzLLJBiV4fbNNxrX9uVqMmlAPVK5T2olMb%2FTHSEhRnRP3AiuBt7qRAvh7mb0kKTf6nKKIhLLUcXPmS57danwnLVUNo8SSUhqO2Xmb5Qw5c%2FS13P69I35ZKqU6fKl5DeNTD2FQGyvHlsSK9dGiHCmNlemPXrgh6sQANhdPwdWcc0HUSvqCwSzBV%2FnOzeS2i5I5L07vasM1yDhpu1yOa1X%2Fi8LkhF6GA4hnpepxPPSFfjoTMOfDgcsGOqUBRNF8a%2BCD3tE%2FUZAaPftGZDhIarhLHBggJwKQPyd60XGw7HvwrxhTAsWgpdkVWz3xIUuuSRwOqXsuUMk6WYeQb3ivdxv0%2BBCCmoPTY3lXbPz2fgmMCoJiyQhIJIGSG3vw1bojJNgzVhcyle%2BBaGAeiAAftwB%2ByFz7Lb7nvdEW3JqInR%2BDgqyJ4lYZvuiFZsp9TuKvmTOx%2BXuJ4zBgV2EN7Yu3%2BAN1&X-Amz-Signature=9128b96645de84472a0d6712c9087a886469b283ae8d4d7559023ff4505a1311&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




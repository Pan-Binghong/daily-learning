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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZE6VCO4O%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2WbQ5y9eFb8Tf1NHZZpA9zE3EgGj2kXlEUQX%2FhWkPBgIgTPXU0BJScvvixk1ySybxNEf6yxdjKOmNf32Brw2XiiMqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPjdGbqW7XRdfCfMAircA0YWSI1TKDDcBJ4H0rk8DCZc6fmcbmqNEwbyUTRPsPhRqDUup6eM7T%2F9lK07VOacbpRt5PMtT6Zrf6JVCt19YeKyWtO3IC8uF1RU2LB50nJDjlb2OLSYKJz98QR4ETWX%2F0wcGCV7fG8u%2FaSyuU%2Be13xr2hsnwDH6ol3EaQI%2BV1LN0QYlfYWv2W8erv1eOCkPL770FMCpTCmCl%2Fr4WeZBQ7CJZjxwQZP59j4FF72Lz3DPvhxXS5hgf3MRVlAQJeD5GNTQ30%2BYt%2BzZ80CsU78rFz1Dv%2B7jCPYQZhkTeny4XhK0eXWanDYP0Su%2FYACK0GOyOSbR2bbCc9ssnAlev%2FQVKpJsC2RVhUr49XvqSm9DO17AGyiNu23Xg0dOIyyG%2F0cpTGRYsZ37a9yJQN5LGyNFLSMaGKTPHxePLIKLAWSJ4A9UsS7k0zTXORIHQn2EBb4Dm6mEbT%2BUV7%2B3JBG9kj7R%2BRcGDi0a7kRQIWa3DZEmem0wv%2FDv8G2ps4vsKPpEFlqxBe%2BQ0QZspORADnxA48Zakg248WbU3iANRKlzb4aNnfPvLtVMcqQ4BlNb0Ylux6Tk6y%2BDf0lO9huqd7hfJjpkgKM21hAeklbrSMAbWc4zE9Y2VFuRytz7fZVSEEf5MI%2F1ussGOqUBlhf8dB9vpf2OSq3hDuw%2BTVWuPr9COxsL34StjIVfpiSqIoMkdE2uzEdyGaz%2FEOkmFsvegOs5NHXAQ5Ttumaw%2B937R8oYbXec4aqkiv8cmdwoBxNPm9sOrkmznKyrx4XG9HP0AoYiDyvdVdCcGTaTtcNrb3CzqUkzkFtfg%2BJxXxK55Yb77F7cpjDp0Fa3tNXOjjMvSCvy7qotnVGwL9uOaGjA2Gt3&X-Amz-Signature=d2a1eec81c800deadd28bbf11b39919b7c4b25981fc78d570cf65786295fb0d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




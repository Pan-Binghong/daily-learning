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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSHXL4ML%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1Dxmgl60kNtnMVCESRbW0itA2hks6t2ohNl1a%2F4lS0AIhAKzz70WkPqd5fCBWmpVYrSXPETBSrWZY%2BiEBvnr4pLp6Kv8DCFMQABoMNjM3NDIzMTgzODA1IgySY40lRJaX%2BmWs0MIq3AN6i01BmfWyiqR1vCU1oyvr6UB%2BWHcRL56t9JnLo45yr%2Bbuezh2Oob3mAyvTevjiP45l%2BP9k0dsnLTYn9eTqsoNAYQvSIE93MsFsVBLDsARdFPqr%2BNKp2JiKbLR2hYnKbJE6Rz%2Bont56wmTNekrotVxlifAC70Qp3W%2Bug392lqQrPo3wAb9TCvGGLQz5mTaf2qiwna%2FxTaWreiX%2FuUGetGzbcTIFB8Xi2Qft82vrN80YxsrdCOGgWG4ggEeQ7O%2Bd16SswVmGCXuvUCoZVKlmd5e1AY%2BRZnMFjQpomD9MUtszEARWH%2Fy51%2FEzabE7KOnZOy6%2B6hD8UFnOwbjCz1s%2BdijcQ7WKQhXp4VSzslgGhMy%2FLygkm2z0pMhzfUs3%2FP38z6W9w96PxPTa3fLh%2FB%2Fr3TtTH2k%2Byn%2F8V%2BhgciMg1ret9ynQPrxvkLCSKGEO5P2QDsPviF1MVp6NI47%2Ff7qj8vMH%2BxdL4wBfbVpH4oxxf02t%2Bp%2B6Ca6d%2FUz07ag6DKEeVuQ2%2FEHCwaX3w69IUE2Fj%2FHAIa8LLfwSxr7RmYyaOaU3ePOou4iu%2BsMStSo1hEdmCBClEwHbl%2Bg9BttCYM%2FgJ3GOhtvE64JxjO5KCghe3e3vxengPedYrc%2Fra37qDCkxJrMBjqkAZoi%2BG5zGx1SLyJuObowGEc4G%2BFmCfiJOoEPfbA5QZH8ep6wufDNhKy0hLoeHOwza%2BeUyJ%2FIFqO154oJrg3BZUbCWAOlBVqq5Hd6W%2B4v4LhCZUqpzgnvheFxCGnoxZRAP%2FIrVM5XwqJbDMBh2kQtG2yayk0olrSSHcJUzbG8xS7%2F0JD4H2GP8sFhM3dmscCkrbHtZZdpA9vpfTKw5yDxkWxI3qha&X-Amz-Signature=93f52e531070a31a6ac79f00d3cae820ce6d4867f82187c90d2f790cdb458fc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




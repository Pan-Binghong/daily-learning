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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKXZZRL7%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDH%2F0%2FyQ9gFNHy5bwf8SLEaFWL8vpQF%2BKktACJrAfDLpAiEA53uip0KMXu7dOmKl77Ai4bL0sGr70tE8eoAL%2F0sQUDkq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDGRjnD99B0dr34USGCrcA8mPh%2FaKgbZBZMQqJrpsjQ8uDyk6eOoebYrZPqvSfaHdLR%2B34HVr05o4RuE0VLA4v6RHKz9GbvuZ70qLk9Ah0oi%2FXmeWnPbD9Xf%2FTUB5a0PJHyUkYufRcVasn2sPV4ZilDjzg7YJPjfWE9JKOn5lw89cFjiCB%2B2xEG02XJWHMHT5kt2%2Fjqfefglmx%2Fg%2FYHyJRH5klKWaI3Q64zefudI2qbWTxuk%2FWmQjkJUcHwFl8imISkdLRvEuXRtT3l8Alo2xgQ7JbGc5Yty6N4xvZzRXb7z4f%2BfUtLLBeIZKfAVyvtIczux0%2BRw6QYdrpuoA5Nd8w7i%2B7B7TyOjIlCGhq4W7DgBu3aN%2Bzqs5NPC%2Fsmy9R5DgTK3PdgqWPRDnSTPK4fteUj%2FiIXcuFFm940EhTo6aNwK2CW3ON6ujj25IWlWR2q7p8Ci1ww5UfQLZo7yBTFge64%2FsNx9EgRJ%2FkEQpb3xh7sha3uhdXKER4KAUD5bcq8zBRcYl4zQkadYUoz3gYmUCxyyXWhw6jesNy810ImdN6GwC67zrCOBPw%2F3zqnexkO4xgY01kXuziDoc1gtOfwXKP59lVbdNRpiHtNjJU0PCxe8Cv2hbSx8SV%2FoZcSAqGYnarmw6QyyEvTDTK9nrMP3rvM4GOqUBmgqjL5CfAUYn%2BqeP%2FEbNwdgipnXmuohaCxhliMRpCm7%2B%2FJmASn%2FSUDUoVyZyVWI6N2h1x8MTJQVdkq93%2F%2F2Lwe%2FJRpg%2FNgvtWTlsBx8Y3TzDSmPX2x1wTD78mM3rgZ%2FQPUPUg2stMS%2F084Vpox27MXxCKdmWlUgcxvGx7%2FP0m0C5DAmDly4FjLOM6z1LFWPyHpM%2BncHReN0b%2FpEzZY%2BQBqX4nhmN&X-Amz-Signature=ca4c6801dd16db0821abf36d1ea033344b22b4c12467545a4f6371170feda01e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




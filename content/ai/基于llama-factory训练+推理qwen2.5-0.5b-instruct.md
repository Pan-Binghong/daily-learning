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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TK5PHRTV%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040841Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGDflnV%2BMqKxuMGY89rgId7GAn9eQux%2F0Get00YC0QR%2BAiEAtvyLvANrIsUxDv5tyTT%2FIqzndHbIc%2FT2DuDt4Wq%2BZ1IqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLzVKtfh0iBPuDBjICrcAyRoQL9IPB%2B1PEniF56%2By%2BetCTwbiev46BpyYUzsMUQ5Vrbw4qgYPW0TMxS3gXtdfAys6jNGgVeAbTY6eo0SFVZWSE1NlYVbRPbWvQiDkKA4ifMzVlJcjDWH0EamzYINjtEVQLC3mA0SjjehdEiWVM2g2Fn4cbaJGQSmiJkejXBsiDffkJzME%2BOR3VOfpM9XTqxm4CnPVDYEZPAmU%2FUg211ve7O3I2iNrXdiXOB0Fc%2BBaJMzEv%2F%2FRoTge6bo4nqKx834O04SKSvOZ44GAsimEr0HgJN%2FGFjDrTZimSfOv9Awct7%2BzoItPVBG6SITEMmW9e8k964f28NF%2BWgicrwl2swZe7o1JdCsgYVKrolUkHX0OnwLX%2FfaiFATywv2T0buvXYseYL6oD6AxA8eUSG7cFpnpGM6UyBAkAcYnsplmU4TBcHnpYwjfOYZQRsBYIdADngE%2BvmkHbyuuAF5PRUtYj3yLbSX3YxPRVhvlZ6qbSOGGrHDlgq5Ap%2FkWCANLEsJkt9%2BO2ER%2F%2BLaxpj0TTMn30UcXcCc6SBEiGOz5NBnrgUz1x3o%2FCLY%2BLfzefx2Ua6I8DBNaSfLK11cJern7CspuPSxuBKWauV7SZXZnHIJAphS6NfU3mh7JzHRfvxKMOuvzM4GOqUBOb22nFc4dPfHA1n8vSlgsszWX%2Fjdy65mRm5OPRJFt7pphAw43RDaUecqiGHIm8iq1JY5fuQyEQyKF8LhoCU8WSTTBeJ54G5NcFclPbYrpF0i70jXH%2FBxVBiysD73wK4K1Jq0clQWUCkUQYgzW%2Bj1YBh08v6MHTtp8cT8Ljo0M73Wx0xZGuavFE93AUNc%2F9BK1r3HzKZ5xG94MTmF8YdIFOAIyrci&X-Amz-Signature=e0c2ef1b63cf28eb96f7a896d275dd9c4364968103b0953644a0cdfaac5000cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




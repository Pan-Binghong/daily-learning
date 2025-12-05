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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIMLWZF5%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T024947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHNBl7FAM8kDXtonCbnSb0Ae%2Fnnuns65HggxheM4E1rOAiEAtw5mdsw%2Fvm0cPEvWm0kQQ%2BmxSdBYhXuVqtO%2B1PYAwEIq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDGHjzcBQ6N7N9HgyTCrcA4pneZ60Mj0m7AUpewCJAkiWLAAaGJ9ni93h7FQ3F1SDLdM4GYCObjP7u7IpgEap0T360eIHD6m2%2FmZTrsJoBCiWb%2FP5rhjLMZwfef66JoqW%2Ffbkkve%2FrUsC5sqC9E2gpKAk1HlR2s3nVRQAYWl9P9Kb%2BfW5MeMrE7juV5GgmGTCbyIyev9LusBqqUNvbkNC%2FACdGcSueZlOfBFgvWdBad0F4vfMPT3p%2FmYb%2BQEbUu3PLNEfWnprUlHuXZkO7jWxf0CyKpKwYCAU8p9ex%2BR5Nzlsytu5KIVyHENHvbDJhcBCHuI68z5JbwiwPEKAG0XL%2BD%2FuAIz0zuYcdvPY2TByR1NJJu0sjJRbpp71SwGjnv%2BxxYCjCvRgXcxusztLFaI1%2BehdpTFC3FrOACffN2%2FEj5Nkr5VUAgt0%2BcGxlmHySmdA7iqNE1okNleX4BasLrJbKwTJ6%2BaTEjCDcRuMHk3lm6X6vBi4S%2B%2FXZ7f%2BW1mTpSCOPzN5aDjfvbiM1T0mIFmkKB9u09JglvNkarFog83rbLKwAKkztEiHH%2B5iYSnP%2B%2BH7BqlM2skH5ECvQfcGiZs9K8UTPBH8eX3rMckRaFu3B4s4Bm84eaGqG7Xhxo%2FUqmFTG8EEQGk3toHAHZcrMPiLyMkGOqUBw%2BkuaqZizhDhMiP0133Vg6WFiBZ7W6oXMcbb5iVG9nR0zQ2e4f1vfmEN7zug2gsIYbZmqZHdO6Xn0vJ1Lq4BbxN7VgFLua6yf684nuaZ5MfZOYutsL4itOaIIKl5R8f6jX%2BiWwLwm2K0COTtv8soYCHDBq7h%2BWYie64t4LHoxWCX3xpHShTXKMtjuBkM%2FuEo4OvrxYqSwVvCCr7ubx2iGfrLlAxX&X-Amz-Signature=0bb219c8c21c1adddef9297b94bceae11520347a5dd62e3aec70463c0f94847a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGY4EBUL%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T033949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvPOpYcvl28MZMaZ5we8OrtitKf78eQ%2BcO%2BUnPkix0WgIgPrDPGrs8MSW80oQvlgpm2vItiYb%2BYkVNPzGR4HUgQIgq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDEmIKR2Gqlny3SW%2BOircA5NWh0%2BXoQM2yN8oR0GLDrhy74dIHvW3qddAh6ETRAemRTnT%2Fz20LqtcYZNbySfpwgf74swaU4BlAxzcfvRl%2Fk2zS%2F5BtQoXSxYt0EOOcRZ%2FUy18W%2BtQ1yh5athc1SY5q3ljTV6TDp8HGJOPoB7A%2BIRwIDjB9ardZlKXVU%2BVcDx36rdlwKY3I783K6gKLfGjjktPcQujWQ%2FvMOoGaS0Rwz2cyMXUo%2FtuBSKg3uk8cJRrtPHeLoMT%2B13%2B%2BwJo1PD%2Fiy1Pi9m7Oj2U65QDCFO9fk2ZhWD%2FSpaqqiaWzZGiJW9xoXOtfyMG7xYwviNPSjAYb%2BOjnei10vcwRHGw04LB1%2BtISegzL%2BRWRHC8B500PKJHQBvgHuzw2ec6Zf6vXVuvjXfacD8%2BqUHLO4lf28egklCP7efSgouUDg0He7FscA5q2DaG3xFGU2c%2BPxZbdsYplei9zGUa4SRjdRAkD7HeUJKAK%2Bx5Ta8R5zOe9FsRyQVcoDV3e9p76ra5MnMHnsVmQMCVORN9ZP%2BOjJTWFAJ1qkWeYMzhUWhJYecBTnFoSNfJotbzN3%2BlZ4cDc1aqD%2B%2FMX2gQMh1mAKEOTLKN2Qf%2Fr3nXMvU6Yv0lhXvTSx2%2Bsgcvj%2BNpBc3YfQrBk0oDMJqf1MwGOqUBOCJ0QmLBEw7dLpfagV0omt4PeBGCCzpZ7p2p%2FjzYM%2B1V1LImHjmIMCkyQ4BOH8GO7xCymvCHRFfHrS7TB0pe6xp986WTagj9iqb0L1MysKcc%2FhZTx4sQ5qxI1iOD1lSkqT0w3qh9A1RLHI9yB0y9HM%2Bc%2Bj2yEc3dxRo7Rn8cXjtMEp6fl%2F9LZbOufVir3QsvuuTBgSr4KrYOR%2B3TpxNQ%2FLGfzlUj&X-Amz-Signature=977bdd981f009853f7ffbf0143b219067ef268ce107cb360eeba19604fe041dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDE2UHWS%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAoQfpjKukDWAdy6i8dc%2B6mC5U%2FoxU1GBYMZwTn6SpcDAiBQP0FjMS7fc09H67s9CHeF63PYp74nmn%2BqJZhDs83KYSqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0BqXWbqkDmSuhsBkKtwDcGdK7I5fOaZb3nX%2BI16aGL3bWFlSALdOZwpKUAYwQqx4UR2LHBrWLXvAoZi62tNOvV3M%2Bn61c13VdY2xDcpdJptz9IhIC47qp%2FxcFc%2B8JMp%2BPiMArfSSpGJunpKQm1i1XftEMVF%2B3KO4x3j3%2FG4TzgVrYcl2TTWl6IFgakL1Z7JpoTt%2F2%2FF1Xk3P9FF%2Blvu2vi%2B7litv%2F8pAOl7L7LrUaiJ%2B0FU6W49kBgt0Wawh8ojUJE4PYetiHOnbWn6wObVmF9nMh434gNFCEYYzRE7kWHtJ7bXPy%2B63W5CGYfiPLF%2BSK6e88Aw0a4vtnMj2irabcy5tCVmolggTQMlD4ixWbYw%2FEU0tY2dA3m290sr2OkSvv2FoBMEOEI0Ni4NSfuiB4roCCPdWja%2FnM4ZFWXJXsHIP3VJ0hbh6%2BZlfLr7iL01CG8Zvua6yhuq0uxeVhTP3lPf7hUez6f85KtY4Jw5giRU241HBBqatkuXyYn55ZnxO6jH1yZIzanSkypi%2Bh1QDPv9eTgjZ18%2FMMDgpR3yKP%2BiawYuHFgRmqBolpT9jLe%2BZmAcwIo7EJuE3SOjYTSx1p9SE%2BuR9FHP5SINto8UXuo20LgqN7JUpLe3NOoi01tbEkelYaBhHh6Dhil4w3PXRygY6pgF2mPHaHO3u%2BoDOqFrxb9BSMlWRs3ED3wtnuLnklIGL3%2BeTFTviWIEbwv9Z4EWI8s42lz%2BA5kLInY%2Bz%2FOy9Q2HYJSNcaUm0%2BOp2ihR54fu0xSGpOg8arv6cwL1%2B8qowMoJFaZ6%2FfgbQzHhL1q58o8gB%2B5rFCENzUlDBdgFyQcUY3Uq9YDuvGD%2FSujdCnR4JZr%2F423BwtIEBStBqu3rlqu6Zj446ZXoj&X-Amz-Signature=68e31c24224f9fb244755011c79a730b144dd4f98992a352c0e3ec0f3634ab4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




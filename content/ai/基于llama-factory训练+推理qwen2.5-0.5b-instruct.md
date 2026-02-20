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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHD6NJ5W%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOQ%2BxuuURVf8IIkD5khPxXo4ERerDxI9xWCZSRbcRSZwIhAJxVOLt%2FJrSCrnwnSRmg%2BCWAW11CBSzHlauHUkg0CRDsKogECIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwK6JPAE%2FawHe9jLDYq3ANYCR6pIKIdIwn%2F6OnwbDx9XtN42%2Bh7sHTr%2F6EISkc70WgxQyXfPANXIJksXtR3Zi2G145lAPsqxSPQZ6G019Ph6%2FZOixD%2F%2B8UROYS78f4T8wMwPH3hNIMhQ8pStII1NNAILezFQSGNlCXEldIs7qhH6PwEWXumnl0pbSxlfiiGAy8epbOQuvDaqOmJkmOU2MQU8be%2FoAquwv1hSNmC0G40pm6vE%2BCtnVysRsVgpuBUeHpRkYf4pvWH0ad3OBrXCXWhJC%2B035FxeB%2Bru1gAh0mYZlDGzNUGhGOZRVU4HrcA1LFHOtDOvMW0BGdzhJ5DFZaepYi8Yeq8N4t5US4EfjIKInJ7ze4bnW9%2B0xoU3y%2Fnn1B7YdvA2PWxnCGEYrWeaR%2Bgyg6DjQ4eF%2Bo1oDr8vXme%2FbSOtPhcVd6g8LJNbsFT6xMSO4AUaYxnKZLtvHIOgH%2BDOKc4PxySh72lpgm5YOhd8NT6TwzNHPRkwKHA%2F%2BRKPcZlgwPINgy1DVKVum8hWIt3BpvFyd73784ashiFMydPYoyEYYs4TIVxIn61J5yfE3f6IF3YiFCgENIWVVI6MkDSxL%2BwlPpmXggSKRMgAotFAfl%2FbmzVNM9V4d0uO8LVwNQTao8KEoHGl%2F5rBDDUkd%2FMBjqkAZLC8Ad2cQP1CtGaCGuvL42PlEQQPrugdkn4l61g10SzJUP8N1dMs0VK9QPMAMp0TJooKuz96%2FDKs8V6WkNmCEdgU7JIq3dYFbwiFcpLT7aHnVD4t9CpM2Lz8IgUCVEoTo684hyAcc%2BYTmPDaZvYKezVZuFL3TIeWvuZbkEkXxf5dPJ3AL%2Bqh6LQo4zx%2BJ6dKxZjBCO%2B5EqP0dslzNAAKFAo5ztT&X-Amz-Signature=a144033753fc3005e2b083adf85fd0d627cdb7f22cf330c463a647503206ec20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




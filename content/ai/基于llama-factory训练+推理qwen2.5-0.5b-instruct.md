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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNSP4KRQ%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034036Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5nHslzJmda41p2tomWMVj06PGafyiKS6tsbu7zkH%2FCgIhANZDqPi2M7jyU2KyVCvOPAfy%2B8N%2Fk6L4wxtBn04kD9M6Kv8DCFwQABoMNjM3NDIzMTgzODA1IgyL%2FZeEnXeejjjkzkIq3APBMBcaENEEX%2F9XcsIvCo3XWFTNG8fbGyzL4xeoaq1fHxV82i9BcNKbh97M5IobPaWVMWk%2Fn74GAvRd4i%2FYIZxt7cdEpyYFJJ%2BCV3d9rI33aEIoBDDUhagKPSHq2ClsquDP7%2FLiJy1cYf4M0Uyy6WTDO%2FURAPw1pLkEIWkNwY%2F7j4IiN0Kk5XJY8SqE3AGZWpaSoJMmRr1c9%2Fhck71YbOkXMLn0LSdXlbh%2FssCKNTwLjMd4f4MXQnikm6zLqCLW6aO2NVYN73xWC6oczFLPJYH2WuiVWADL8O0iwtdyQnPTc7M2D763E%2FCe%2BTew1SblmNaVfrcl4D2c2M4AchYwN4ehjTyfmkA%2B0Dk%2B1ojHYYkzo2JonczHy1E9tPzEuNdzWhQ2KcFgqXxNwsHINT01CHm%2BXI%2BXF4%2FVrejNdbVZ%2F9AmTfRwWoN6GYJpBQKmLIANsUUwBFrKA8YEq5Jh%2BhuUfIsAa7UtyxkBT2FzKjiu%2BbpGBPdq9JPFPLVANdPSfjjLj8bHwxs%2B0d%2FezDiaJvpe7IzgH2iH3yAYFVoGFQdSXSONI1AQnAg3B%2B%2BFiSs8sqZv15J8vmNDWTMoSCb%2F3qujVLOn6%2BhxcRPPZwOIVwxwUfeHTHZUi%2BvdLwHdezI31TDhrP3NBjqkAYmS9L3B%2FZVQNsk%2BxIkowbSXIIzO4f6ZKSnPYzRGiPMMzROuEvG1xqaFuZjN55b6n7W9CJIYuHLTw4Kis5EKSIvCLJjQqL3SoB7VL%2Bt7Hc%2FTjv9u3SYGopYrN77KYvts%2Fgemh9bZyhu6NjMp4QHehAm7Rm7DEb0I1%2Be1jeawLKdDxOz7A4%2F%2BRR4f%2FtUee7Eqb%2BLydsK%2B5ZnhMGp1%2FhM%2Ftzx63MKb&X-Amz-Signature=6745c4b10da3873c692eef8dc1b432dea91654c65fcd02aada836825776019f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




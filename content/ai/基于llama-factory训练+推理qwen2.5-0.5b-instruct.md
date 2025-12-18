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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675DPHBIK%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAY1NYlrtmMNZzAAgnP7C2EjKCgIeZ%2FeaRUR2PAEFJGgIgBcwsIUrTIVx8DHteiVGxib0aHLaK0XAW6lZMCsGpXfQqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLdbm%2B28p28C3GMVHircA6DaUT1YTJAUVnhjwmkPAS7EUmhcyz0ESByiNzpsRKQQ6Bmuzesby43W2IuxNOSVpM5rCYkp%2F2yTNXCSxkuitPKaUFcQzvA4jNp%2F%2ByIKASYjp4sJkHIux4f%2Bou2SAhVk6OFzgT%2BjNtVpSEkoKCWKgtBIs3HSszGxLBk0%2B6cbEUaARGkWlXJihZ3tV6njGg7lq%2BQjGQnBZQ8UU4JrOLg1xDd3dJJJa2v4PIBeE7lu%2FEW2uGSP0fJ3KVimMeZljze8tYSUkZ136oMPdoEY7HuWxPMOyr2%2BYuH9zK5DMNhLfR9igZyQHrtSByV02usFXiymJnolYUg%2BNe0FP0miqUTwMScsnGqsuWPzcgglglUZNYVQS%2Fct4F8PP4rzMMD%2F6RBSb%2BF%2FmO3VZtHFmMviNMH988sOOGHLyLqGVWiQR3lngBuPYkUQw5P%2BZ%2FjREBVLj20LUDPnPm%2BGC3VBc78gPM1iL7AlIvm0jNbBBjZWgj138fNXgNzsHScVZmpJgv6bebKiaAyNwtujNtNd4mpweRENNtrjkTtP2GV3m71k0056sfKudWTYfRFVDnfQiLmXYy%2FbucECo67bZagpBLIkoHd9iSHsQwfnpdcXajkpjp29BZm9iv1WAYS4QcNIugM5MKPJjcoGOqUBxpF1qG0HU6Eof0A2hf5ExZ6moKsVA81ZnFnS29SwfluMSaA0QoSiG5BxLezsGtZqqTogLdN5U1Rw3NDmMWuYlqNSHkyxjxeHt%2B5TFiw5S4yBynpQsxmzAACWMY9ZtomQ2RY%2F9aJ9%2BEErrq52zIwcqHrwrmAbtrfX6LC6k97XKuKX9R0kiOWf%2B05vLxuJ%2BExbMWKuRVCZzNQTPMm40OQrzmY6guN4&X-Amz-Signature=5ace5f14b6a9d2486a67ed55a30577c9cb2716422591d5e2508b6476d807ed7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




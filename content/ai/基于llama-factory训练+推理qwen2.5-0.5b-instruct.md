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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YO6C73M%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHXw%2FHNvgWjHqLvO2lU6gIQVVuxjpCg3AfvMgMGnQq7gIgGJyTbd5fODPd2yN8IZSBvBHgn0rTRyUt66NNNdTBQhIqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGahvI9HGT41EGOCaircAyWeZyQOJfSIF3EQikL6m2nBInWGyhgL1Uml6VMJjnalnelfddttCCT%2B%2BlryRabCFvLjWWc3X9dB6gBl3z4Smn0wOL9cvrZfNuqG%2FoTljx6a6cpUZj0rZIsUYmpMax8WrfTl%2FZECrKQPX%2F5lC%2BqWCPb2nZmnpQCPxapSDwoXDFNcIrgTWjVB4zlcs8frPCW19p%2B4GcPoH6Eo0c8q5uTY7eUXw%2BX3wfBvQ6xM%2B1hqDpwVTDGeD4sKJm1tQOhGV0foFUxHHITu16wXIG1e8OvVdc4RGutcc0SIZmy0wskCRk%2FfBMYVIUG0vzQsaCt3ZHbRXpWv7W1lwFhwv4OOK4qY%2FcxNZcgQ0A7oN%2F2K8G7FpbIMqdU2H1GLnUOSQfru%2FxhAS6E8nyodznHWYau%2BWc46waR4L%2BfC0ddWMnV3X77WgWX9rjbEDwtTjd4WXGHpBdKFV3XOVnkPfDqldJ%2Bi6E9qvsLf3Qf%2B0s8dkc6DLCtvyE%2F4zdyZUgLBoyFT5owWzHvS6IJahUndsfm%2BLsKcWFA5MyPg%2FCkmhMwNRnn0JnnnodcUf17LcpNbDDB0U0ICBwQP6pQCERT1DwkpqnhPUnV7WL1MtR67HrRbpCqsrTgdVGc7aKiWBesZ2nCBhwoeMNC85MwGOqUBrA89pS58YfeO7opu1Yat5kW4sxuDtvyhW3eL15X8F152Lyfx0%2FodjbY8VmP6NHs7HPncezLZ9HgnOIgM9fAo1rig1qjAGZY31OJbboHlsRkh93bKiQC7b5NYIi%2Bkrl9%2FpGMuL48FDVrzA4BLBFXGbM0p6500p5LLPQEE8hnKZbqKvs5tYXJcoTsENIvWwBSfGvxcBimtk%2FOLkAEgN7eYQz58cxKt&X-Amz-Signature=ba1630a4cbd664a79066304ec121f0b77679657db4fe8a5f4b24735e668054e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




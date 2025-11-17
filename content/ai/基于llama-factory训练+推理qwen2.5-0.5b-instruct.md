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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VP6N5TG6%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVzfpoiPy9f6cKxbW%2Bywu6ACtNniJP6o9v8T4SByoSnQIgF5UFZG6Sh6VkJVsfudwZYgUgoR%2BP%2FVkdkDES6U7bmR4qiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE26BsjGs5nZ5a4b7CrcA7RGtEmMMadDYm2vFK9oWcTOBsh9ov%2BboKX3XvxLq86P2lOCOmwIpn1Oyn5cep7fPU7TtNtKXF1kx%2BFZHQuMhLGLNnASwGyUQtgSa5OqaPrn9B3UFOnvT766XUVYn6IjUB5ybfV7q4lM3iWWFSM5Puv0g1EXkEa2JBB29Bb2XFk%2BNAnO57oeJU5qwOCo6tEh3qYSJfxh5R%2FB0FShSuM8Z4Z63GE3MjGc3xGOX%2BP4U8fackwOFNA8AlSr48RAUFHzuf%2BQ4XyZRTLPDYsVoqoGzbFqLMit6PFOwCQWX0%2Bj5wJpPIGTXZxQ3XgdbDGbySu2TsBn4IikOKfFw79ijBby%2FNHkYxpqHIFbDzgfX6%2BkPARKK52yZvazqTIhUYI9eZOUovtDKqZQma4FMh809F95UHII5U2%2BlryK7Dos4WQ2nIwjUGl9X89ZSP0xQwY3n%2F3rb2aOTt%2FzDLDB0XT7DgjQO%2BR4fQ2vVrIi2mhxTsUEEDdLCOI%2B4TBkCSqtS%2F%2FIIduLXjYkbvxaJ8Y9R2Bi1droOCCJ3r6yP2x0n1QAeDOhLj60gXapFwUAtxPvMnSDmMKp5%2FTRxxPrJ3oQy7foEZP4VpWTATPz3YUPpnv5l2nnUdO0X1CWH2RcOfZ1FknKMJSH6sgGOqUBuZUEK9bdcXSzgsgsebFgHsDLgSfmT9krZHimoCFQy8ZsNY4GkpDuH12eJvUrmmBWuHT4n7M%2B1GcO4UEo83rTDTqnmUbk7MYOBWCkrC9cgYzam%2FBlilvwRpntB%2FrjP%2FDgO5f%2F5XUP%2BdaWohFyDKmbb7vEHJrJ4cjI24YG2ukxQezYauPUu3QpMotGnf10jW8zP5dRiNdgVqftGk%2FhGhryiVOkDowX&X-Amz-Signature=0425729eb8334f65034d1a55618304cd0d688b06868a7bbd31846a282ee9bbdb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




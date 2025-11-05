---
title: 基于LLaMA Factory训练+推理Qwen2.5-0.5B-Instruct
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
标签:
- LLMs
- LLamaFactory
categories:
- AI
---

## LLaMA-Factory框架总述

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXMNTK2X%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDiqLDcRC9UwECAgLpWovnHU3mspgW3VuX3NPmB4Gcb%2BgIgJVu%2B2NonF1CYgEmQu1wfs%2BtBy2OEn6w199GUQmYC6MwqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC0Z9bMvI%2B16XQGK4SrcAxa8GVMY8G7DwjiNlI36cio6vO8r9FvGL30wIvI1R39PF7vLCGgsaJgFeqRnG5jxsyFB9K1%2BonCEvQjQ3EAXiNzJlmOYZ7xgWTnPLKFVGbX0BkTzK6qMcMKHR31TO6NeZZhGwoLOwTzrzTRBwtngIOHLzSoDQaeTLcCDOqAodDhiomEPZWIuod1AI63yqit3PtnbxInI%2BB%2FSRar2Jnjg1i9p7039JaRT4%2FqFUPXfYcjRyU1aZHj5CUgDSpse5oIs7Iw2BCsf34r7CBZbOKcj6AG3LaWqj2%2BZfjASmIYfak74K1ZxTfsLVHCM0QP%2BEGYj%2BWcaovlMIKVkJuvqbkdIs7jqrqe4X6dAOf8SVErwNnS2jRDo8tG%2BRIwH3jUAJkC5pxI4d42WOA9MoIawD6LrYzsjfXmZ2AG7NBzOLmRZlLWFCw1T80PI8wvTPcrmb6gGFICTtlB4tsc9zulQhGkOeijulNDlx04YwoTLuLTdhuhjgZf20O0tqR0X7n7fzYuASm5oXz4UYy0y34JW8HH84e3R4zM6pPtA5YSBo5R3uCR2j9IqZuec683%2FBtSEjEeyxRQ%2BX1jY2o6iM9Z7XS9HC6hc7SnM%2Fu5%2FUyhXS66qGCAu8j8mNeftuibL3ZbZMPKirMgGOqUByTx3MUaXtm8yKW7cLRlx6yGV0nwNsSMu8ldCkbHygME62y1B3v7dLmPbk9m71pNgs%2BmHWJ8JGsaVEFvHAXkbCx%2F5Wv2IrLzJlT0s%2FJKQt6ijiJ2kV7P%2BtG0EBmMWcvd10oxpyq5XeQXLcnwXO2%2BDklfXAZqAWsqZ11epr0rYI8n2ACCdqx%2BVqjSWiYqcJRPg93J%2BXXOpPJh8uPBghYbMqUe9ceTQ&X-Amz-Signature=0f147ce757f504d156843ef96885a29ee861661eeecb897439bfbe8280e0454a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




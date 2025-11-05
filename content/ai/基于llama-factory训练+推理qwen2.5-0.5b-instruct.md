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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MJVPSW2%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCAfMbx0sKG61N2gEXb9saYlkEBSrSUAK47XpIQo9IpaAIgAb08jow%2BQ6qZuTY%2Bn2ARaJghA3sNY8njMZLp%2FB2FcE8qiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEdSNpGe8rWBso4HjCrcA%2F5wnPCpgRhWi84%2FC%2BPZpEGiFpH0VV8px0%2BzQ7HlG1uUt47GsI%2FEi5BRP%2Bbbu%2B%2BX2Lf6gVumRIjVpjFksXQ3NZ5fniaCRBgFzqacFYRjF9AxkUMlQUoVvmfbhMNKFWR2lnBoWbzwoKt%2FpoLI54jLTfriLIy1awUzDCn5UV%2FH9pApIZz7QizzrZnIV1kxZSiTXKvHmk7b8Zw5NyuYzy0%2B%2B2DJhX0rVQYXih%2FSDZaAulYaSuxhYKhXkltRtvk0weuCVQ%2Brj6UUoF7VBhT3EGLRBkqnJuCHneD6PRVmrkMV64CKCR2JcvIvI5OrJKdPMxAuak5PJ6B4foc6TMyhQ5RLV9pbC3nc3%2BLQSLlQ8sLyuw7GY25ofl18GzpSCNRKTsvlb2wplC2utMLqdv0331hS0VK5KYhCk2FhoL%2BvrS9V3ceW%2B%2FmfgnNm2vIFU5s2eskftvv%2Fnk%2BdVKmGHshbENP40JU4ZuMryoUsiplhfanctyT8lixPpZmAJ5DHO1l1XHwAF8zALGSjr%2F7FKdoa0fL2L5GhozJh6Dix1IJyfpq6rzdZwjz4z8LAZDevvcjOUwlrd8bu3xnw07HVJBDJFD8Tgu2iPRph0CoxDgzv0nLl0Ig7dSIuHIcSA6nwN%2BrbMP%2BirMgGOqUBLe14JFPkjwheGvKGuP19cevcXUzg2Sg47fdb9LMGnaQ4d1abm4QQ0%2F8CpE336eFkuHAx2Nx1LH3bdBunjnKLeHu75HuwHv7Jv2t2FjOkYdehqvRTSvxLk1LUo9LQ8WhflysB%2FUxAD0FhmL0dF6boDEJk894PBbi7Kqf5xWPEmnwS5xkEskhfSt1uzTQO4jSnjNU08jox%2FyH88YQ0Y1XBwWnOTMKs&X-Amz-Signature=d78c7686de47daeb05d079ee6dcf29fe6d6c44353a5421242394082b9fd3f23a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




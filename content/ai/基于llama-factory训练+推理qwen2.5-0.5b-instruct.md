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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT5QWSVK%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAg6jeKfZTKBtndjXO0Z6fj2n7esjnogBjxWWvs%2BSWcgIgUDYXXf7rLvDX1ZwC3sYMQ2rev%2B32NBjGXH3MdUWdoy0qiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDErXtvJI%2FIiN7fc0WyrcAxgrzI119XU3oTT91dWqWq5dz6IbaE3quwkJO43zcdMUJCNOjddVUuYPh8Ah7WI9QID8mRTyKgBjU7RGFy894qeMa%2F%2BndPZTpEXq3OQf2N2ro%2FRyOlpmxC3UfUZO%2FY9aokKJ6T%2BaIrAFn0JJB3A6KSBJ5dVEUZaM9xBHvehAlQinYU91dNzYAWzM9csc46YfrvW5vR%2FNwNAUWul5r%2FlVE5U0JNUrldpkEYEqnenRPcc7flaGYyr5BIfT9K4FABgSjeS1q2BugYPL1mXi5xLczjQU0MLJ6FHwWn%2B2%2Bb5oNxBH%2F9K1UkNgJ5tFtotPThm2Z%2BzHbfhiZIZ%2FL2YKDtv5WTtokqlSIelTX1W2UCDs0KfmlYwm45tfUuEUVJJ%2F0IvHW429nPcr6OecuRF4FZ8YyJ8hxR037P0kd%2F8abPl%2FfXL9t3NQrqDor8q90nGnEj25zOcnClNhrAihfD7YVMoKiq%2B5%2FTPDwdWPZYjBmAfgdDKf3iyLF8Dt1M%2FdOTU8YF%2BtMh%2Fhxo4bpxMaa41WwTGf6Vg5goOqkZP2NLR6ptwtl2FbuRuOrw9S4tJduhIYYeTXGyNI5KvAi6kJpanwzSNlRprezB%2BDTIO7LKyaw%2B8Ceqlr437DYxaTB9frM%2FJlMJfiksoGOqUBEHXtGsghsX3e2dMjB64Yct9IDijv%2B688Xw76TjIvdoQV5G%2BJJvIshSnqXk0Wx38Sm6ha0yL94KJnrJO5e7EdHy3IJz0bskkn6kyxTBDI3yxvF%2B1A3HIhZiXrL6knhCmosYlaYIdoxcmCUPBGHFuSulzKhsCOfiW%2FuUqgHFIc6BSFVR9g3eT6C1pGLlsYR4mB1%2BtFobidr7dYVnfvX7%2FCsQ9q2h4t&X-Amz-Signature=1982292aa1079c4ca302b104ea6f2a8fbb41ec0ae49a59d460484db16fd22a43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




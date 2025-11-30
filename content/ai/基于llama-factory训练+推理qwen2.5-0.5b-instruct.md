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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJP5SDRT%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQDXAjbkcutVEmAYudJ%2B3oldmCjGWyL9Wl7M%2B8pr%2F8AoJQIhAPJYVD7xNfXInDRdGR4MD7WQfxYhrRa9KPxJZ8rdPhWiKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwIjIA%2FZA%2BLNkP6TR4q3AMZiniTe%2B2B0WibZqZZG%2FUVUkUk%2FVFGCWKU7k8Cryv20P%2BUudc5yaQlJo1fJumVz72Qew9sSPhok%2BdO0qhPkejOhdAAqYXYtkA6nvhXd8da%2BBz9nIEYm0N996zjD3I4zKhJWXIMJleie1hM8ZsmnxO7dXgZWxdrGlDuqnHk%2FetY6nJHoqFyo%2BKd3RS5qq%2FaPAEOXfZkmqqlekkr2BAYu%2F5v9nHap1FBxTbAEjxpU2fOeLBgC9i1dbZyjH7DaSJZRMtX4oMkeSfSp4MGv5TPmHkWJkRsmkypGJQ2fFn4O7EpAiqIhXMzR4ZvBS8tt70cqK9NK3yxVG0QFHgJ5EnXF%2BPe%2F16i0GdqOW8c2dbWatjdn4Diq5JQy8zuikHXhgxwUyPHaY%2F6ILNobSX3KJrbVZcMSaWhnbqO9daSM4HN%2Bz7i7%2B1MEXlJVh0DX6huyxER3gQVxZMlnEV4w7URi5oeT5iCCYDbrTeBowmOCEtNe5PpyuNJrlZiy2%2FP0v0lhI%2BAj2A9XpueH10sqsQ%2Bv%2Fkc7zqyks0BpxgOYpuQk2UiSSRU5%2FWgzNeEI%2FaP1WWBzbdWX3jBAS8kOJ3rmiQC%2F37g89XP4vDwLwMsJB3tDG01osy3ErRxuVnZEl%2FAzAZmPzCu1K3JBjqkAUBG0d1dk%2B14trr6xd7D%2BKAd1OR4VUpcZEytRY3CKB1SCRKS6gx%2BjlRPTs3pfov7F1hO%2BoImZIuIZ7mAATJ4j7YAw67sIiXmKTKDmov9cL8o54WwXhqyw9KGzG%2Fy6rBIxU83y%2BHDUXRCprHsFZb4vmWvdDv3ib7WXDFiiNMVtuOdsZdvdWN91PRaZqFhWGe4%2FG5noGam0vdx9xxYztSdlHLmOAzV&X-Amz-Signature=e1dab1feacb61e767d84118ced108db718b77b4e4aa64bd4df5c6bb861ad66f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




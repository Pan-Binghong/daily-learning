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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSYOLCLF%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOGF6e4Gr8koB%2FWs8NKWstuLrebKNhRcoarC3DjDjXzwIgQDqk7OLojpkvrXxxNeLWiLYaMvgAwgDngLFHH3EkCTsqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBDC3Xde9TuYIMrekyrcA6pWS97zT20uw%2FNnR8j%2BMLpRMmDL4V5JkO%2FaEioUdZ2kPmIcSxAh%2B8Sn9SHM3g%2BoIJUkmTxwsJwlGI6QJn3avdQM08bzS9hIlnxqPKcU1eguIj5%2F604ErurgV0w6PgXHo32%2F9tJ3%2B%2BGdhFdba018sZm1YikQ4eDG9DUuTxUWtAApBBk4oG7GyzefDgPHmFZn0lUTKOLFmpB0sIhIfOIbGJ57VY8xSFTeOC4A9Qnmbp6UrdYzSes0hgc6OeyBoGwfrRuTO0zZiLYRqkMZKrF5y6%2Fn4iOUQrf1Iq9frNCjhrejYI6lGPrC3WIFzhg0Ro5aypQrehH%2FDahx5fgn8NtDUuQCZ3Pou%2F3LMnVxzOJMvV5%2FMtBejnvwCc6DwBlBaovINgqriRnpmRr0FX%2BpJ4%2F5Ot5HnG5LLqjkZpxiqDIKIdBB4iFP%2FKDRsSdroNsZS%2BYzsLT7VZqbeNz5s396YkvTb%2FkQACE0fY5PIW4%2FwFDb1JcdnaOTe3nOH4%2F6HPiaU%2FQwvznJnZY5YCwj1Sid6wDtn2YTNskEvAygOnQHawUS9EnuiYVS09StUdcX2Bafxs3wjIjhfr3iSx31LyI4TdRP20gYoNNyTXnJ8giTIIN0Rop74fIFvCeSZkO06j7OMMjdtcsGOqUBtFNjhpKNe6Bi%2BrPy2rksmJo1VwQE5d0G%2FRlOWIfV1Sie4YlknjsDcUgD9hrDq0JOD8jxOqoO0YPaVkNVa96zQUj7pKFF7vryC2tL27%2BY3QjxAnmUK27F%2BFuB6X0wFGKpYjn1v1aeWoZJHhnNUlcnNCG%2FAlRQR7zsIVZ6cWTBrzbwW84HYr%2FCH2o0eJuOsHOloy9UaNMfHkeU%2FEB2UbIxdCaEgBYX&X-Amz-Signature=ef917c6a826e492ebf3d95c8d1fcfb23cd9f0e98c8ceb25ccf2c1a021150efc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




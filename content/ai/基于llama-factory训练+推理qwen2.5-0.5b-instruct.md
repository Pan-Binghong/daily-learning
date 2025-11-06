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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676CB7ASD%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFEE2hzLjNSz7FJEpmbRDXFwa8feMtA2H4RgcuosCayJAiASg2%2B35nDF1tSyEIAgv6%2BvIgs%2FfpQSZwEGBjtENyPLGiqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNL17e%2FS1yQ6tjywAKtwDzNj%2FHqJurrnToMCtTdDSH846K3vxWE%2FQQDFfFzktytL4LNJQ%2FwxVmTJNPjuJkk4A1OrKioUWGCaA3ba1xPsj0z0XM66%2Fd1DYhCh1OPDYTvh3usXdSboXaPbyAGarADs9HAKfNcq8t%2FowXEnCBJi%2Bh2%2FPgvSqVRXHJOku7oaRI72ZKqqJd%2F1eucFzdLAMnI04%2Bl3wluAvoDEW30jZwoTOsymAM%2F7kNuF1mXVzbh5izhCYrQMxRWpG7RYOYIibeJ1nXWu9rULrapqltD7KxNtAqnHTCOeCYEcA0B8MfODe%2FqDCPZT3dpvR9IzZV2j9dekBMr1FEk9LPDEG1g6Q1%2FXGc8RpsMs3H3rLynDWcINe8BvjhhoWI72bTa%2BAb4NIM3nWseEgVqYyjlCDF3khKE3k9jVgI8Q0xfdRU5nfeq0QJy3WBi1L28McaxkvkLvv119aGpBOqLOJTuSFn22CynQaqskHwa%2FeE2zl3ktaS8716MvqvbiCp7NeC69AoABnG7Tfi7AXVaVmHL3CWALq1C%2FE7ZxBeWBTFLdDqpsDSnH%2Fp17%2B1ENW2ljZN5wI5KimyYkaaMSksMjUWxYckUldziR7qKpMjzyEiHqDhqVVuEfGys0KT%2Bmja0%2FG40iYuCsw3fGvyAY6pgEPys2X4VFeiNeP22EvGvW86QO8Vu4XoJYrnCzjmeJBlRuwvlqqAcATtCD%2FHDbaoqtq3KqwmmhmDxk9Z8FofR5DXI%2BiyZ3MEQnTeqZSSLhRMaVEXdz%2FJSg5rwPw3YTcKIvlSlZLIgXRqzkgP%2BDKDCp%2B%2BqzA%2FXONAlFfHWIJAfdZLpc53bV1kfeIp2YOmNuuI8h%2BzCZLuflhHwwf%2FUX0JRUOYM1zsp2P&X-Amz-Signature=29570a183d91b07fc4da0ee8939ab0446305089fc1f26e9409e38ccb473db040&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




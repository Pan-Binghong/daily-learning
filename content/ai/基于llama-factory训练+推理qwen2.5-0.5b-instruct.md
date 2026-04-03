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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEGWMUAN%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB92ZKJXBfjMuuKAiQdRQ4ut8w7kTGwxcYqGXp%2FoIZa1AiBXWrkgu7gTpK5B9oOyHGFCU98MSvhuzEiERWGJBNIXHir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMYqRxojKXohIcegjbKtwDsOHwOkcgVN6oZliEdCoDzYAKd8tpjacCaC2ATr%2FyQdNBCFJyqV13%2BFp7gTrufBxkXbJyC1zy3k6k6kuULGSTRvgrGLlkeooRRXrAdqj7TIMlFVqQ8DR%2FPFgSnXYjHW5XRgzP%2ByCJfMTlDHjIpir7DgZGY69%2FNh0PjbKs3qRl8Oi93Z3Nz5WvKyi8PNMGt9UTZsSNhCIA9hSsec%2BR2Amg7W17hjWlNKeMHfWFRmgvxX%2B7TBGlZPJpCHqmzpBGQeGa1CkVcixvWd7rOrLm0ad%2B6Rd6%2FXSO0jqHapvdNSxsnNSjKvzeO%2Bw2d6hjMOSfPl%2B914FW5aYBPNowtw27wyWEna%2FhTXgvur7jF5k19Vjk9fSBj8YJ5SDHZkCURhR4sekpNf8bJDL4TEbu8msfFnBNVJ5ZcqGcGJdXC5%2F1hSnpkCvuuie5wVOMrNPqKrt8K6QcIfudQ%2BygLqTj%2FZ%2FxO5AdX93PQJ1w6Pc4wzmYyevO%2FeenRA8oD8lKarnU%2FTjJh4E4gtKe%2Fynvg8IM%2FpZvwcd%2B2kcEnvNwmj8KYXT0Hx9pEpIe56jr4RoZKmhdqat0QBAf34sFZDZNPwzK5CqqhrW7tbAA8HzfGfHfXb5T0PNTH9akUE7s3D9%2BxmFMwWowp669zgY6pgFURw%2BYS1RWh0J8JgEScCX0fF0GlZPXwJU3moIUU5ISFrgRvR%2FrY7fKyg86dFfQ4dOQbhVPUXLjyeKz%2Fg1U7EogrGV%2FG277k3AswQ4Qr%2BlGB6POpEdov4wtIbDwKXioCfMkCfL61BL%2FbHtWpkPs07lfFD4qv1YzW9RBjIGHlW0%2BgBrcC6E%2Bn1NFJ82QbsXaWqoS3xw%2Bwt4xIZdHxQw0xKqbGar%2F09qu&X-Amz-Signature=f171ca8d68ae283cfe0bd4e1ef35381d18d49430a34b353d145296bb00fc18dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




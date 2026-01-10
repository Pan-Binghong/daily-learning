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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIVMNQVB%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FsICWXv5Q4c0FMSqsKOy5KzaQIBTzqjYNCFFy7SsFJQIhAJsjmWbkwFBS4lU3Y0LN5UQdxvmAhYblXrmegL6hT7vSKogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igymu59xLio8Y0TuEJYq3AOvT8JVzIpovJL3jyO2WuzeQSsiO7j99mib53ySofLReDRbNmGhScuqgbc46sGTclyopGYVCRemzwqghYA%2BDA%2B7Pv5Y80n6zB4WyfEHEysiFLrjiLvncLzxkxpKiwE%2FeXeEbpb8ByO%2Bbnq%2BclTkEw7q00SgROJMDHYslT0AK9ei6F6hRLS8E3zbL58gnymo66PABM9iQR%2FVzRtTYSBmKlpbVj9AFZgPTlSFn9xVOYPnQJf4PkzRgC%2F%2Fz6zrg91FAZYErJ6%2FY3WsDeU6RPASAhubWRIsu9Q40SmpAGgGOaH6WKIIExHsU6d6cybP%2FU5HQHcO2PUjBWsh45qTOI2syqiQkudw3LDclGI%2FAjO6XgAQURAVTCK1klqwGxhnZBhC5pJLk8y7Q8YZM970nWpxkGuAw1W9IQi0KiRH7%2BpEjXbfFYdFiLcvjbGhrzXBPaB9Pvaojgt%2FuN72RZCxMBLIrlqZ5fPAZkQqU65yCJjLcheaHk5YR1tRKNCGAQizw4cykge9VTcnLyrsi6ZU3lyaJkYO%2FdrxRV62VlJk3pvb%2FyI4oad4ie7jqub8pold3NCwaoFB%2Buj2FgqKDt7l4WlH9MT6s3LmgiltkCgn2%2BuTpqUENN9nfarCIjjoAhQnqzCr%2BYbLBjqkAW8E1NVt9i0nvK5u6eIlwSFHJ83PdQzVWXbE88jHzAY3VXyu7LBJVT00ZtyJ66O3Hmpz6JwTxxIy01SGiaNGf0UO5qVaL1m5CTolDqLHCX4kU2xGUNYU3xkuHHiJGbtg%2FI%2FVaQzrPLk3bvMKSDW9H3ZdNj3zbtd159PpHJjJDpsmTsJAehuj82RsRAEzI%2FJOvD5%2BNDlddD5H6PmrnYyHOR%2BV3WfQ&X-Amz-Signature=afb64f6859e5389f5f9049f40979ecf5afbdc2792bfcda3d2f15a41fa7bce537&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OUDT5HS%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEZ2xh9CuaTQez8ibb6kOvqijWOTXtkKHH868ojfiocJAiBKdN3U9rEM5T8n7co1kWE732mtPvoGd%2Bjq3t9x4wFROCqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMW002aQIFzX9hz7HxKtwDHNnGBIxMeXcZFFuPicvQCU1tosbRjSTkk808eI%2Fck4YWgk8fxH7UgaHmizDxipLPdSCAWy9CEHwRLYl3WSXlFM0Aq06%2F7XqkYYAVnmNaf1ky6%2BS9SSul6QDIEWFYmxfJ7FYixq0KBuO6UmZBt%2BtbkqLtCJYfFDfAFfY8lbqocWkx%2BTZdFZhZ9xfNMZCKzmLBq5pmIXc%2FzvDYF9nkJ997Eh3H9jR0mCZIDwBmIWNEgVcU9s14in5qzV4Jp1fudx7Km2rrtnZEqC0Ou9KOjvkH%2BLDXZddbzTVajXT7SJbmnGjQrnR02h6FNgvguXOY7hBh9LoELhj96JnSilzpG7f0iaaBWCjtiHK8yVKqC7NtD28UbN%2Fg7I86lLf39%2B6naT91MZJRKETB32T5xqiAvIBkanlcqoKSg3QahZRy7cZPCJlTKTDYjObtjE5zv%2Fm2kxBMy%2BtCgawKo5MdOusp%2F48%2Fr7UrVER%2FojmhWZpQYHjF%2Fq2RQKAvgyFHFj4XimxjxivL6vxhRboeuGaivv4Fo%2BFXhZQoBoga2uCAwr6H%2FC6NtHKFTR4q5ey6%2Fy1sWmYEwjqagLPW9kmJdhbIvBjsOGghU5I6bot5T4gbxTUdNCWDt0iJ20BsYwZDfG4C1cMwz8uvzAY6pgH7Dyad7mCBK37BoRBXXwEfjaBIzYSI%2BSxV1J6hfEsx4FVjKc45f0xkyRq%2F2nrqHfXLcyfn6GWs2TWs9Z5NN77RJ6JnzEna7ZJ1rK7rvXafG48ExxkIWX4EbSPsZRMcSsXG1duqYIua9nGUxkYepxAGwxzcycmn1NA64CkvFPI1nt8NeRO1EZpn%2Bkov9X%2BIZAOUvdZAXw7p1JrEvl0T0kxNFKfRUfze&X-Amz-Signature=3c08f4d34e9c73758436da56f1526c0664c2791171a2fa0ed081a6b488c37f96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




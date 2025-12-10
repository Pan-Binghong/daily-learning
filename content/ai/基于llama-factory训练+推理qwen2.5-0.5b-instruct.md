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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQSW2KBX%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA2W0Whl3290NwNj7j%2BIWqo6qwuMftXOT1qMm1E4crZoAiEAtNEXtV6a4i6BXYkEiPd6FPeAeF%2FrzyXh8IfpBvqz5MkqiAQIyP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKElqxE71r7023jrqircA12%2FrbzpLlVmmCMgUZhb32iWSVbMYEo1pEq4h1VRCL%2F8h6sJKBi3mz15ris7dm%2BJPEIqOHD%2BDKl1lna%2FFlbYJdFkVrGfWdKYVZ2JmQ5c2WWjOeZhlGoAtsqSQSeXnXhYDJLst3VJxva9%2B6h1dw0IyNHc6zV1TLFuVitwSUzuzSKMtbTr8Z9nYewpcAYtVzGMw68elaCU8pgOxE9Ra99U9rUPfV%2FFE2phf2q%2BDnRXh8s0Ofi2%2FPbtFjak77PL%2FUiFpr0Fb7%2FalXPtrZpiFsoU0dBodcx%2FE6fPKYdtHfi5TLHE2IA0A%2BU6uXtYXvSrsVnY5QqLxTJEpmEW7I89%2F%2BCExcbMJFe8NMcMgtihoiiJa2SOOVfHY8PkzSJXfGQ9JGzk%2BqmDIdMZ2iW%2BZ0gq1c0CswXi2UvEmh0GTgL%2FE93yVIA4kszQWqAZc22vqGjhqX4qn7hz1kfwqBvrHnODHjmjgUVmzbGyXgeGjmbwYJ8habKJ9U4hmW58ezcjBSyR2aba4epM7gizNvyvmpFe7R79Z1ThNFJUhHYXW3Vktg%2B8l7jRybq1wCgfqD9KM5kWpgfbFmbT15tw0UwPhvKPWm3GzlFcDZNojhaXN8p7JzkzgNGW4fi8Z%2ByVve6qeWY8MJPE4skGOqUBUxkf%2FhphFOVgj60BKBn2Fhrv9Iepoeaaeqd4m2eUXXTPW0nN7q5Dt0pIy4dym6CfQ1nCRvLI1DvfycnRvcYLf3ywD8n9IMbnXDKye4xAbXMjET74VHv18Yneh6KC12byXgWrCLIzGNu6aXBXazn1KN6ahOPgqf7EcUp1jhFXg3UZQ7ocnRRsh%2FUqQ%2BSuMycgCKiD2Hqc28wIMo6WZt7QWlh%2BfVoG&X-Amz-Signature=1d86fdde1c10736637a5cefa3cb1c2e6e622d2ab03d95846e0e7e05c24a0bd63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




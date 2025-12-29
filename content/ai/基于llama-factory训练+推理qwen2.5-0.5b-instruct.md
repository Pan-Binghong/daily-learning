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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DXWV3N3%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBzj1DekdkirWNFqxlTqOvYgYPTELdIVLe5SAADTajBtAiAEkiLjlD3bWybbIU5RTk63birTJL6AvRtP9gKj9EyJ8yqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMl0qB0zhnBs0s74wmKtwDgh%2BVq4WMYhu1KJP4D07j%2BIwMhVNUPIpklQZUfR%2FoheUxoQ%2FBXfRaoNJ5QNsb0jANCbPNYii4ItvXD%2Fo0aqDv%2FmTY4TCLYaeo9ABgYKjhdHUy56LolHwmr2pweBNucC8QwYEirnkhk9ZcX%2F%2BR9Hg3YogvPWZJa3U7316p5ReasabhLZBRyPn6Y0yR6z%2B0atzC%2Fp4rMH9i1oDDLr66O9FyxSnrSOgqr%2FmdIOLdhzIQW0drtFuout4zKnb%2FtjhDCIVDoMF9j6vukco8WFCbJcDnNELbJhSuZR1eVhxXL6a0Qplr290tVkskFjWCe8URCKYXLXItMMMh5fzRmA2ONvpz3v9J1fwgCAD%2Bo3t1Ts2LzX1Dn%2FnVYEoyZnoHe8WnEQajpS83BfdBBLtQKx3uWye1Y9g%2F1%2FcnapHZO6kRWazOgCZqNZnJn2sIWdnfISCRjvv19hiscN%2Bh7%2BGFlXxfjtqrU7kKPBRQ4U2CjjxgPXTD4W%2FkxUuu8mLHY6s%2Fu4flz13lBEdARpaxeJhX4HDkkBIPH6KYIG9%2BWPnlRKoALGGq4AmlO7qfSzeS4z1FXEN2mVWFtOlxdP6q0goDQjauwVKhd6CzUdeMY7OOp8trzjGyybZk%2BWg8CXvRJk1VIcQwsKDHygY6pgFZkuW6Lx1j3MvNJYRD6N6rnD1XdmzGktcwzQB5ul5mxok4XQW6v8GVbj5%2BFAFgoiFqWlF4mZhju%2BbQdqV8Dp4O6%2Bxca5DMCc1rgSccjosphzaTc2OXYGdzT1rbwRVI0Tsm9Ejv%2BCCLrhV5VXGLeWyPqgXND4Eweo9Z9Ht%2F9ZAtjI%2F3hoXhKlLVuEKHzl83c%2BzTovAIQgIQREWaGrcRew1Bceyc%2FXlK&X-Amz-Signature=e3e458989e228a9bf1d871723c85818c42609fb5f1af69068b61afd402c99241&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5DOJR7N%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTLgrKJjb8ii8iPIJWpy8i3xRf13%2B8jY3fc0WDggF%2B%2FgIgGcrDf0pnywWZ5cmEZucKif6mliKUE6z6KQvlYvvRbw4qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCDdJqxUG2zAApAlaSrcA2i2Ile3Sr%2BBOj3cv49ZOA21lVhlm3yUNJEFC2JV%2BxwCFvJ0u8vbV6J3X%2FXS4LTgFzIG660iktck8OGB8ZdUILqvvfdQFz3zzTa73qqWtcHfWUmKAH2rfgpWWJI0WEEBYbkKGa79PWGQGf2dOl2WAG2pIh9hvpXwVvO3rMMQNRApkvAVpiWRrgI1x%2FuESniIirudp225tHFgTDfe4ZPD2ZlSq1SOp20%2FENqulfTqoLGpsWGOpkrMYwxBZ37NbjjInwrEs3DFHmnJUk9jWRX9fueuiT%2ButQu81ep1kknMCsipIgWEADESehpGzI6yh6bQD3BRpuuLlswmQMJk7ZgiT%2BYtwIvZ5xkNwL4b5lrzfFyqtyDMrRVf1AJZERIiPA2TkjvRllOK7%2BVA9s5xHavJJlYLs%2FM41y0pJVpOlzuSav0NUxJdH%2BdPAOgyMunoyId%2FayE23fbj88XO2UP5Tqz1WWy0tBhCiX0bpC8ovUPSrsAjtnGFgLpKi8DhB6cET%2F7dpfMOkNkrYMazCXrDODyuo5NOw4fz9Qr9jRtZJalZ7owfp7j0ZsxE2hheBQYqKghaTKBmNCsK4AxFP1VMByWGzlf8E9660%2FRnL464aFFLz%2FzOhC%2FVa1bqpLg6NcRjMN%2BY78gGOqUB0PlYA032ngzNzACjw0xO%2FuGM6Iv4DQkUsbuR9%2FsGWGk3HcEKy%2B5yT8%2BsplPUqSTkhhqz8qjKTzBdyTjVIUYsL6r1PChDNaEzO%2BiYDJZkCqoqL2ApZpoujsKljAH8lvXqtuWzn%2BfiMd6UMveGVkOwHDGH5B%2F3SSLQ8G54ylIu6SGbGJna561pp3iKW7EWnViaMUNZDt65sdS%2BuLCQZdO76ldW59q5&X-Amz-Signature=01b95f7d89851e2f719785cc3310feca1a6f43c2604fc4836b04bb9b76ea63bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




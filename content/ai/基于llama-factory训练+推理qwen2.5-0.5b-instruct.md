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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G56ZG47%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC8ygQOZcIJpk3oN9bTiKwo%2BiJCFgfcH1n%2F4idhoVjSZAiAuAKHrQ7diSZIPzm9q8xr67i2MdWj5ilodZDwqBmC4kyqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7KDlEBi7Unlt%2BG8jKtwDC%2FERptY4MDxBv7%2BoFXbYCWh7YiLTxePGBpfKMHKV8KUwCTgSGstqhofjfBa9J5lIT1F%2BTnwUvmkkqCYJz9xhYmW0%2FURmg8a1TyKtob4QtD6OF9CXqNHAycZm8wqu05VbnydgqMtngY2Iq4blG0aQczyKxqpFHPuoP%2F2qZTTkofw4jnCf2OrzrkFxKcLqm3GQQxDT65xlmHdapMll9CNyMZZn5CRjvzBMVf83XgpdUm4O3A%2Fn%2FxNmIGtmj4oHrZQJX7DB3FW6CodGpwfgerNYgv07o76a3JYIiZjYsLCWf0rR7qWtPSd%2Fk%2B6B85oaLcdXJljOsTbaQgArrjOGR68SFpLOzGD%2FhWjlc30C4aWwQFZPhulVvYcnV8G1szFZz1skJ%2FG7VrhkzREG9XlGUXhLGhpNiyWb7k6eWGGlPMHGkbtSFu13aC1Y3GwYjdkgl9cE8pMmneRFNqfvlmYGXeHvhIVtgqP5U9AYOmnQ5VAFljZ%2B9garU8LbzLI8vkfzPFW%2B3bsZItwNfbDkaFLe0xhW4xaGYm%2B8APTMzkA360JuP8RR2B1EwhO47%2FOFd3i6U8pfaJPs7ipgEY%2BHq2RwNMaTDJwG43LOGpl9NXlUlJUxIBGLa%2BiMFZ6XHhnYgKMw2vCvyAY6pgFPcWqjdgNhHAZXl9%2FHcB2Dbab9m6tzysE6j4a9%2FFnmOQChx29riqJGOLxcJT4tYGZbSJ%2BFzn5d8%2BXNWI4BAJclpFaUXwDfchqS3WpVXCHjjY2QZVS4UCVHQq9Gf1I5Xn5bMrisiKI67dr2EC58igAgOuOhIGmJ2saaZACnGvoXTDmJy%2BwQPPVErcm3Thm9aVbIpiVl6qjJU%2FD24kk5xOnULqKLEkXy&X-Amz-Signature=51c58f915a3124a7d53e25bee9ff34d5c99f3e299fd40fa254a439d3c04b4bdd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




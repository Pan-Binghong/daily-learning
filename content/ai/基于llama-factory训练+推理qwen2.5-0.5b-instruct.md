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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJYCN2R2%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025853Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDakpg%2Bzq%2BDpCI%2B%2Bfn0yd%2FIwLP%2B31OOvkyh2ontA14gQIhANHfDkp2%2F5DvwlzTlSS93QeQ1awxi5vX3hK6rtAAtLS9Kv8DCFQQABoMNjM3NDIzMTgzODA1IgxrY%2Fvy1g8zIiVsXNEq3ANtq0c5oYi4gS7IOs21qxP3zHF2T9EqRGud80RSC0rxFjuk6Qerfjm8AkVsekHK8B2KyarDXGkr9Yo%2BuQ47eZO3oHmsrGgfnIl2WHpeD%2BC4UYjviu%2FZ0xj9fH3lhdoDDgUThxfOsyrPl%2B0jQeff8Dl7g41qNRPSxYOG6jvf%2FdTfqNprN3Y9GFxVUItXNOrScdd0PV1phdxQt8%2FfyiBFnwwRvizcAjy7XqmfuXLOqx1mSLfur%2BYlW9KGR6hq0tXLF%2F0i2nyafNVUIHsRSk2V6D3VRQwSmpFYOZU1rDJPIeh03hGxvtikIbiE%2BZBhc%2F55lm2MzUTjU9aP8u5ohleJU1fg7np5Rzj%2BY4BjpOFWUljGvMpMH0XAWApylcF%2BcCPJv91TF43IakdlL%2Fux9jIW%2BtUHrHDOdj8jp1ym%2Fub4AI%2F2gkws2N7C4%2BwkCEGyb86FoCrRS6BpSQJiA0LqBJmy%2BwqFzHJF7tEvesQd2oSMIIaUCX82ec0%2BaxJ1hc%2Fyqy1XsA7YyxWjcHi9PU3JYXa3EZ1Z%2BSoy1GSFWP1ycYG0C9os%2FKHPkvycGiWzcy86JCu%2FBiYg2uoQ1LGWjTyxBkGqGrrWFNFFweU1V0uIx9TsCIaSN3w3hMGzVALAiJyMpjDK5fHKBjqkAd2kMg547vw2M34MeDzAV133LEcqxqhXKEb0aSJ3HteQWFPQOoQISjElBQNn%2FPDTQ48kNdDuiuoveeBTzWzG3jlAkAYTwAarQx121rlCP2YLF%2FRljl5%2Fybz2OFyySq6paESngrSzLbo5hDZdxBx7BoxicM5YYCdE65IP0LgLyuHWYCYUnwAXdNe3MeWSBUG94O6a4KSvjM8dOdNmCRmWoUrkCH7X&X-Amz-Signature=a067e6cb13f73992ce4e9d2ed18a2b1576581ce1c7f6a283272f952f0ff81708&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663V7JT3YM%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIB0cZjyrcbELWm5VN5yEoANusD7L2GjXVpbr7iFTV8DNAiEAt%2BcD9nh6zQSSNpkGK%2Bv2ODM4xUFRcL1W8ohH%2Bh8DXf8qiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFYFJC%2Bjw3HQkhAGoircA0Nu1R%2F5TU8DxagkJjb0cWOHkXPxnD22Zmuz%2FAh4gtKlQ1dxwml%2Bq9uqoa37B4O3sVFTKjnDqSrM5cuk%2Fbh7CrZ7g4Xr7URWDC%2BFk9Wc5n2E%2F%2Fptq914mfZSK809OjHdg0e3n8XzGgQwO8sXZXCW4%2BOmKsBM1HW2ahGx0w4K3x7zjpl7RQ3G3S7eiLpJ3vrmPwXMdWIrERmk17RKIgWV8hnBye1SfJSfZ2dXLWbHk5MCH9h%2BuOox%2BWD5MS7GLYG%2BKjMJpPbUgXYssu5zoH%2Fal2ltiYvQf311MlQ5iSiTU7XpY1Uao3Wr8iXxM9KR8J3r4gHKScl6nRUQrxmy2Ffm5fgdzNWSy8Hsw5UI%2BAkwjRNIbo1jiLCYSxZakaBjzY3Ma%2BESVSqDMRrSu1MmP%2Fwg8mp4qwVieQQGIRB9a275VjqAJe2xOm6CqcSbiyy3Ed5d7UUlT8WXWWVj02PqoEkrNc51amoUWccarMoQSubF3gm0xN4SV9vLKXtPk8ZOpuEWiJHBMk4JsuMxYwASun4Gl2QSzgUKnGHRNYmTFl29IV5K6s869yfR8EoXVwx1poVyu9Cb1sdVPdV5rII7dDKvvM85%2BoQ29BDgY930hngUZm%2FXICHoWrBmG1exToGiMObXhcwGOqUBuHJR63MuI5FcITWdwu2Vir7HjXwvGwzNcvJ3WPCQmyMYB9q5m5HQW9AF4r%2BqsxkpaWs7hOxTz%2B2i1K%2FCEX6CCazO5LXAl3D63GdovU7y565rPXw1bw3XFaMqQlDB6TZO0agxO5ITF7pqkBtlv0DYvOjXKWiFe0%2BT0V4yMrkM%2BRFZ0A6Onea%2BmQ76RVqIoHIYw0m%2Bx1ufMZrDn0KK%2B%2B0%2FYteb6uDj&X-Amz-Signature=999c2ab4202fb87c1d69982ee19e1feadfd7ee340246e667c89e4cb80abf6664&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




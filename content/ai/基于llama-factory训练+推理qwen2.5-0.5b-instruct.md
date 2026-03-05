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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TU27VXYR%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC4CJoGEUwnMKSgcD%2FQCBVT4i58t1VHTxcSjAHhNtwvXAiAGeH%2FZeREHRBUwtVj0XiaQIgTsuTuxp2pI9bfgbyE6oyqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIML0tKJBe2dV%2FPP1uhKtwDFRyHwLQZ9PTEQdYdLAxSHu1Vd9VGBDESnt87ZfziMVnA8Zg7HDCaUR5ys7FuEbUapUE0nY%2FI0%2BmZe5GpNWny7bO9i68lyinfQyDwl9Lgin6NvyTYFZjcxDFPocNohQhH%2B8zeDLk%2FeqcSK7AccgdxWqwRc4XKEutXcDdAidsw2R9nzGSfEyCAHWyjRBw0KFe2OGtfdwBbQI45F80%2FTHw98PQYwnhZX0zPhvI9DAjUjlXfrvgHYd4Yt5qACiJTsEXFWB9I5ix9%2FJt2I0Aq%2BUAT868ZXTNIcbn5EKvEc3ybYJboiuXqASTGAjPN7iE2lgGW%2BDidfwpAUelItdNP3zW23wWWPc5kwxUnXkFwXC%2BHiNznolNS%2FQGDlRIFZGVo1a%2F%2FTliuzdbCW1py9NQSC0i0K4r8DU%2BA3lUvGbT3tkTDl%2F6%2B%2Bh8lLpzeyEG3shHFJ5mjBeU0zD7lmm0kypOjGM2jAwGA8AmNb8CnmevEy7t%2BKQSnbDOxiAZNoQiZUDeIA4J8PdcgeDDNTEowM1zT870XtKvPrraVBlyiEAjALofLiVx%2Fke6RC5MR0jaUynm6XcwdPVoseg3kW1vZloACIYTj4c9moE3r90NMf3LOi8UsDEmqjuT%2F07YHSItJ4AEwxuCjzQY6pgF%2FSdPcYdjXBWjY5TAnIWUS5o5qLTzVR%2BJrmrnmclYdwVIT5%2FE3V%2BZpuBUKRZHgEXsAQTODYoZsu8X9tM65DP3SI7udJANRXjwLdt4XPL6xmDL%2FsoG7iR7cYyiyo%2BrE6HbKYuLfLO4mQxZuTvC9sRpQYrW9Knq3KhE4iFHmXdlvwKPj0018b0fv7vl3NWQ5p3IDAg86uk8NCT0UPoQR7zJCZIxbKwAQ&X-Amz-Signature=a6c61aa8cb11e904678f0dcca090235f9340dcf61831a6287868a720a6314ef2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




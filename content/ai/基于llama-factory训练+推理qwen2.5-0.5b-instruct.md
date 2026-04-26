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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3I5FY2V%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH1aw3MlbcVsR8YKGP12I0tlIDtfF0Q62FaPFLXwGA74AiEA8ROT3W%2B652uaDgSnU6xA5boh7cMrc3vaNh81o6lzTF4qiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD0kPjPYWjg45i2amyrcA8ssU1OF5U64HkLmpD9xUAIy96JYrgp2ZyjCr5%2BEUvMOeZ9C5sWaIx%2Baf8oyxEzBqxrFVT9%2F%2FdTL3oQgkMLCdQzhMIpDe00AdpesjcjPJd1iFFTDovpF5RKQrjEUktHphyCp9QOdZNE6V9fe1FlndmjpFhsy1K%2FCCHdnr%2FhHyLip%2FpTMKg0HxGHTl6OUCYSqLnCsB%2B%2FuQhGxW%2FgkmVv4ANZJblHfHJhTDOQL2F33IL4BKtmD1vwvaODPzT9bQ%2FnuiCI2ojMg5aXzHEMXWSUZociZV04yL1OWG32EuAhm4vSN6hi91ysU%2FiYWhPxHIq6aHdXlQXp3HEOaQjJC5yQp3WGxUxDjAq7eVE%2BpTqaPBOVo3RqAkK0iTzzhEchBQbAH%2B52e46%2F%2BgbgJjf5Rxv4GO8rKnJZsgIOAuuC%2F05YXIr1Vo8%2F0SpyFJatgrLXXE9XjcKhEu8LtX7FuRdcmX7yzF1iH3WA5S9eO85LgD0CvTsgs0upFBMGugnu4HHpmqLzbxrvwHpBaGHmvV3M4uvysrCnCO8sBLQPs%2FADGQSh8lg0tMYq0u6V57B86dEhKBjuQLpYF%2BWONUAps3ofR9zP%2FEo9MkwOXT0aBfZE675mA2Klxl%2ByvlBvaiw54ECehMJCPts8GOqUBFAYb8icFCOkTG9QJyzqsaCsiId87CJHJdqYgQZtaAupaoYpn8R8GzutmxXcQZSScMw1bg4PGSU9kpbhL1ahoG5J%2FY2swL2blFxPtmdlSvuywE1Glg%2FJXpNJEYv6yBIkI6uwhtYB7oIx4lNsp%2B%2BoeFlKErpBn%2Ffh%2FpyeNk%2BafCvy%2FD1h3z9nhmsaNKjvgEGlVVB%2BV0X5VUoOH1JCiu4XcDEczkXNO&X-Amz-Signature=dc7d1f4afa43b8a19c7d04a086f284ddbecfdbfab06d513fdb23892e6bef2d71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNFMWOVH%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T025943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQCzXOP53s1WGdUQ94TKQ83BlwazulLT5zthanNoBHsrIQIgPY3xDuj%2FIo6Ozdej72FYnJ0fsPWl%2FMJsofpksh36dTsqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHpFj%2BDT%2FueSLn185yrcAx1fy2ilkCFZiNpytg%2BZDLPUmI8xrZLwD8eeYF7IEAQOa6cgU9AAdRYF5omVB52%2BvXh2uzaryX%2FB6ZuGQ6bIBYxWlajpHchKkw2EiS3NZ3ebdrXXwAZit%2B7vNJgRi0fCbV88mTPO44Rc2Z56bACd7VqldParVdPwKEA7EaKRgNv5Yabw2WPLpm906wIldMh6IiBq6P8FFeuD4uicNiWJFuDTbCF9uJcvJr7t1WddQQUOYKpM8Lu%2FY6c4Cx%2Bz%2FupD4oG1WR9ZIPj7nqgN3Uv2pQU%2BoD9dUSQpWiJO%2BNl%2BROAfQpEqvAeAIvaKleDR3OXqSmeELsT78SfNiCchuadbiYmVYAjNTuiws%2BEaWyUH%2Bilawy9oe1KLFiCkEbf6OUjJXmEavXq17F5zRxrdo5ZqeUJxpGa3%2BGzewhaeNH05jCCuetvIwQkkbI%2BtlNdVc3BusPaQjnY9m%2BrwTnlLYEDdwH%2F3K5oCjoYzIvrV3Ne%2FxPDLPlqAqZFe%2BdZAeVH4tu%2FTxWzKlOiQE4mJWGtb3WORSse%2BYCJTRw7hRUwvmOOetVy1iZr1zLHrJrUVj0mrl3e2WyriXEeKG3dqZKxpyp%2FPa1oDauxSgMRKyKYz6nB%2F%2BKOMAGfBDCNw5RIzRhJVMIb5nMoGOqUBFreks%2Buza6lGuD6bqAgMHNia6QDG2%2B5TyNhkxqYT4I3n5E6VM7ivX0IhbLMuDb0GoP7YONKanjZrMJUdLewKpxeZRjTYm%2BLbCsVNXtTrUK5bgUH0gkwsUpcFAwgh6ouyCqJ2WwS%2BEDLkB4RGfgx7BsS3GsCUZVU57L7HeuLhYi%2Bm%2FvgbOQSMCZ4n1ivkD8OBUfAfzSX1ecWS%2FA69cqGdPmEjMAh1&X-Amz-Signature=e62ec0b0bdf999171cebdc9e3d8efd82126250b56df5491b9d2aab98e25f5731&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




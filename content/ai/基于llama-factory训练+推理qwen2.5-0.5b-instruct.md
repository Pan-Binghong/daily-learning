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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSYTH2I6%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICy35p3RKX9%2Bv2WTKGb%2FJBX6gVsxCb7CmnmXfGGpNUqJAiEAq4%2FviYC%2FXt%2FPMV80HORZkMjPwBudFbmGIjAA0wk3JtAqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOfe0TImzGlgIQuvOircA%2B2FcKVQ6X3U5irqhvHcmxd3pI3bebA2HHkFhjb7ns5PK536H3fbut0Sxj68SU2b5l8Vzki1D6gMdU2JXFlCvCCYQHSstZOk6ph0XmcRfkyi4IHZAaS65bzq2BwkCIyVO%2FwjlAnVAR9JKi12QKvS8byu5Z0DZnlatZhkRzDC%2FkLjBhfeQd0IrfrqByihj8tFwbvlV1dvBiM%2FhVBsYWZ72jwAENgWsTOncLHFvUJv6M78hDHVjHKwE38Z4MwtQY2kZeAiwOq6slCY08%2BIi5dwOtdxG8sThEEh3wxEv8RmPQZiWa2TnAOyFrjN9pGHC45Z4gFAZ0NBBVjPkgL0K0yKnRxUEFjpHk796cI0%2FXd2TgwxBRePPeROqUX58umf3SF%2BIbrC9wno4LtqR2a09Kj4QewCQ7pBOxSNSbIy2nIYDgtN0lSbJKgKYmVV%2F6PWEs1n8a0SH1fSueQZstA%2FzXmocE5mmJTrGWQm20LhC4J7qO9%2BY5kT%2BqZ7EIg7cyzLafwkmACLUgefGJHJmi%2BYKSnDwywwEEdwZSsuMIb9BNIWMh55sx16IjSaDDWUVkg42xd4ux0z5CfKpJYRp%2BWW6cBYeuSDUrTUmyirJfohgLkRuNkQVF6ACEzluUzr9Q%2BiMPKdx84GOqUBOpwoqvTD8USTeAWILtaUOYnjeKzTIkMB1DzuvdZxh5jDAB4T6thLB0ZuMG0zmi%2FLIFMgeO%2Bw1jbXtWVsa4mqdrRRDPL76QZX%2B%2BzznNZ9xS93ce54ATWbNmMNg0tU2DylmnUpMfIF3cNnTBkugCVEIR%2Bk4S6tNwJqCXdqNFyy04L4IInT7cq39QD7X9KLNVMTUMczr2AVp0d%2FNCQG05DKi%2FBXlAQr&X-Amz-Signature=150e2c8ba6ca04dd7d3cf5946574d03d19868254ab3ccee4a907fa62ff379cdc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




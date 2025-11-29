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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YP2HVYHQ%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQhNMJFXtoK2dEgOf8XNOFojLpkxKlgoHYVIh7i4y45wIgIuiZDhM6JfDLsQJe41%2BvjAB5a8ZQtbdGneMbFZVgQuIqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhOqWChH0hrjJNxKircAzu9j8U3UlcjMuKRHVYpVP6mN4lplOwWfrytO8HBk43tN%2Bd40qhsgDoJLH07DntVpZHosGyYtQ2PDG5ks4QDw8VLQtdLSZvd%2Bf%2B7UrM59OPDZyDH%2BbvGq6Z%2FxIGODqs2LJFXaiWTqv7VHAJk8KjzL%2F61abx2f6nvZM7jRFGydlBhugqZFqahx3m8F2lwDrmRHQIs9shhXxIZPLgNWpppAwTF7jGJHg9IG0Gmt%2BXFgSfzmDXHI2xcG6Ld%2BBrovhNBUBG12oi%2BjuGJmfvElKoX6vBo7150W%2FuDYktX9x1C4GkCf5l83XiyRZTMFspxazNaG2Ih60oH161flnJRB13NqyHTqpMRcFaNjMl91Wr47ZtSVOtV16MfLiJWOGp%2Fk9LqTxc5G2j63IrCTetf5%2FaayE7KWM%2Bhv8l1hL8ycGawjygm01z7orYqhJwEuOvbeOcIczuyryIC6LatY2A9EaqSluOG2%2F8jQpYYbpzDMNbiRNkccmVQjtyYDRq22po5sNsxxwJ6EXn7FpWeLkgx1XqYsvSkWuTkDJJ8I5n9XcnLSXtCmj6fm5bNixKds0KIyysDtSb%2F3ZXj7bDZo%2B0J8VKo0CFlrOxLASe5nRWMciRLo68MNMkJQ4Lo%2B7NCLl1tMPCbqckGOqUBFJomPLfbCJsuqQOMK29InNm4OGxoQeXVwiCADi0srnKj%2B%2BouQV1dS7AORsBPPvuGtQLwjTVoKvMliylt9xCBkmJMS15qaR3rDuzBbnTwIDGblzgxNANtMOZZO4x9hwoWcszyNcUnqCorzGwXFRjgxmKfMUeTXcsZoqRTndB%2Bybgc2ijE%2B2LCkBwyu7smL2%2BK2KYmBNdvzDBx9sGSFyqF0K8QJov3&X-Amz-Signature=b511386886d9176db08a8624dc9cf5a18adb2c0db91051135813153c6e0d2dc2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




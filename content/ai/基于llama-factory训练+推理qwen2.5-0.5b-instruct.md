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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PRAJBRA%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICC1bQtNd3eBG57rtysxCSZHpI8VWNryQv7EQ1Uk4TJkAiAuGNEDjnsWRLasDrNYkTm6MOD3u1DcsCJ6ANmj5iH68yqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLPapYtpd7mWL0uAEKtwDiZmf2TEfeDjUIL8l3lK1as3Qo4aRtjgBAsMI8R%2B5FbP0zodX4tKkTHBOOkssJ9noKacQxgKG2BIcmN2vEf9ABOtNZ3xV%2FiaWKw6rCiFzyesGvGoLFmGzPg1VX9gM3ner8%2F57xv36gEjRmSXsQ8H0kalOmvF7XwT5YxrnHDHJjoH0Bz4%2BoeRW8JZ0kZm8DQCSxrWvpli%2Fv%2FPQG25s7b0LQt9cMUwUdOK80GFeOyXnjBfPVqc11CePwdqu8%2FLD6Sc9Yd7%2FH%2Fw55m9c3lNGUlxPZ5PRrfKQNARyMGDQLwkJzud41Xgoo8VxMG7qLE6Ny3CJXV4jzLvjNQOGV2LnxOQe04q0yXLYyTzN1d0Z8oKdJzo0E%2BaPH3MH9c1wLg0jkmVKyqN3rq1foihUICK%2BG79I%2F8YXX5hPMfdhaxQ3Jn4nlWZyS%2BT4EhY3o870XqDU7CcJWaNHsHz2ezj6j9s2LYiQQ6AUkP8pdQIdoXkhaFVbW9dtX1UDvnqf3SHNlY6kz5P%2BhpuAhUVkmHc2dV8rQmwmVT7XdNFK%2B6TDRyV3ty30JG8SZdkbFHOZZ2xVMXhrLr5knoujbacdJhprcH8MKocAhULx3%2Be8oKsuxxFECJF5Z7QLdL3%2Fj5sJ1HpFmfAwsILTzQY6pgGqs5%2Fo0PS%2FUAsGNHpzuJMNsElrnBXNRvGvd%2FnXSlQZ4WNbB%2BODhWvuslN7RaRRaMFUe%2FyHNQVv8wmQgBpK5wWDuD0b4%2BpCg%2Bl5AP58cCje4wdC43AJO1UE%2BeOIG%2BAnfxjoCVairO4LiL4hQhscs%2FD%2Ft8M7ptA00N5Z9u2DMj0pch9I0o2fqyNLObdMN6fPf0Gbm1ilAvDwQrdE8B21EXAPQitlWVDe&X-Amz-Signature=363252159662bc28ee22ed39c79227a33e7c9df1294401a6b783c27bb4f5fec8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




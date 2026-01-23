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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAR4GCYJ%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQCbMlKW3udzNYp8eF1%2F8qtKIAhB80R4GgGlY7cJQiBESAIgV%2BMmBHl5%2FR9s8pqSx7Mk7Mxa1ULxpQW4Tc6ANjpM%2F%2FEqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOdK4odRptFk%2BoP5dCrcA1a%2F4g%2FUM%2BJfIKbvRTZPiGyphNInRFiGfPyqQLGjYy4kglr%2B9ZY2RxY4rLxWWoqQswcng%2BkaiV%2FfvdMq%2FdUYy%2F1FmSqJnqf9BvAMUk5gIvMtYkMnldvdTYUIYQJ7ClcZmjPVkxEyyk5sIsn3KXzoapo2NQOBWGLF%2BtRNHNo%2FYr2ddGcg%2FWsjXXQ0AshKb8nHuQB5N9PnPsQJZtpK6xPCW7XdC48e7R2smIihEtT%2FMnV32Cn%2BLd5qYvIAp4riORaF%2BHc5DIV0M9ESjIBUT2qfmCOvRckgwbKlxLbanyXJeAoD%2FWMOk%2BEVMhrVogvsKipWru9PNIriBVNrVp9otfy%2Fmab4Az4cwa%2FKqMUQE8J%2B2%2BMbMon74YmXzEOgf5dBGP7A2p%2B70j%2B4WH7EViUdLouC0dgMnBrtXxsm8arHd5Suqdn1D9jshS%2BKHyLiwLuatgoDfeXmh3dG3xYdqoojBvsnKEpBLadIs4Riy7PxxYOY%2Big%2BGf2iVFBx%2BbDwxGCyb6t2fmqNTj%2Fo3J3sBOcGnqABf9JRQWVTPeZTUSNqkEqQ4CyrMpnmmmjzKDjRlwFt2jvA51AGQ1viIZUgzBy0sTgf92YDL4Sp38UebalZe9zcajliNeZns2YNj4PbC701MMWvy8sGOqUBq3qQkL1ZbXkdExbCfXSNKynEMAvLEdwEYLTLiD%2BKB7dJ56CPPwjbcF9ogTBOjkboSh4FupZoiiwLwtiVJygeOJER4AGb%2Fh5UqGtPXHQDpja96g9biW3USgTjYDrI57AhiU5Ycn4aG%2FlmLjIJ2FWaaFKr%2FwEPc7Jqt2glgQFMMb381pfuYegXK2yPaEFUFKltSvYRPm3dlUfv3hh%2Bc3s8v9me5H2w&X-Amz-Signature=d5a93653938ac96165da16738f6be0e0e9564786456874ef5ceb150c2f792196&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




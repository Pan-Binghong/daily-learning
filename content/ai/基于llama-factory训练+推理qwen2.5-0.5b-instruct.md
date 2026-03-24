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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWZC7SGG%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHSP9qLAID3mXudD2As6pLil7clHPUl%2BFXDcpxcqOxZwIgZ1mB5l838UIfPvPTuMvTMUiKqYjb3025ctVM4Gzgd5EqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhsvZG3WEVa5br9AircA3RGcQDGPcc7QgCz9wrJibWpeEkRsn8LkrByPth2zAbMBwMpfcskxruxM5d27aBK8M5BqgAlMWlPTNIZJ54Y1%2BPexjiMPBvpXDdec5IwF4BTeIKDW%2BkJ29t0jtyASOnDr2I%2FvOb1fJuarlawtKDopzNld8vHF%2B%2F45M%2BopY3K5T6I78GIcKVEVhbjoi%2B4HwAb411DtdTWE5Pk%2Bx%2F8rywaS%2FC%2FHAInV6q8SubNqq1ASe%2FQm3e2bwRN8YLc%2BwVkHZGOPB9JRPGLUjKlwKJNbScCcEaFwUU1FxwuegcoA6OcYd6SWplcsaevlW7MYMznSfBrAMIWl%2BqhsTywjf84p%2FcSfNVnHIDKffntpJeo180ODM8mCVY%2Fn0GypAOUf8RW5PvtKwfj%2BJL9DBp0QCwcWAbFsThDe3OqVIqOL2j4Wma59mQzAPN7AbFua2V1Z3ucYziaXue6l7%2B400cN9Qovc1N%2Fu%2FUBFHR7TXJVUgNHQWiwTm41z36O%2F44HS5ht75Kgtsq2t4ejdj1q9inZAxp617pqyBFC9n%2BBI4x1OPYMly6oYZP%2BtmIQNu756gFqYqNOA7gDmmwW7fqdRBIHhspUGvE2yH2dHAWZYs1Z4yBiIiUJPEzjt08nO5pUL3F74hJlMJvzh84GOqUBfpHB1z2lWns78FYnBj%2FhCyRVN71qQHybeQ72IDiEZ%2FU4Hga9fqw11CAogbqAsn7IxecKvUeWzmWCPYts0Np0FjK%2Fzzb0pGi0vMjquWachz%2B58f%2FKsYRtK7MHaBpG8J33u9v9iqr0foWZl3y2tmcw%2BG1CNEBSrrF6ficAcQzgpGXuRpLTdwUnSsE8xuud%2BoVR67G2%2FZarBzazOpatT0QClF4Wk6kD&X-Amz-Signature=ebe25c69cc0aaeb7a801b0b56e596811741594e3c791a3d8b2505ec2e941b872&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




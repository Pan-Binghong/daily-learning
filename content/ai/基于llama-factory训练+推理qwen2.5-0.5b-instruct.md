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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZY5UDY2Z%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDSwED%2F9SFmB6QjMH6aW6%2FIAupjHbr62bBN49csG1CqiAiEA4%2Frj2zDmFMSwfscwT12ZvZdVj%2BDCwcIUxxbJUXGKli8q%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDK12Hlm1nSaJt0Fd%2FSrcA2onurG577%2B9xwLUbC4DYk9U%2Ft2pQGdkz2o3Gd4GxGKhJQuxw8irMs9YU9wZVlZNPbrNkXVZ0cqnonAbPjwFDo3GBY%2BWQbtsRTkO4sgYZoFX7X9ujw6Xsdkj1wjnWSwpJFfKS%2FpquwbiUzO8diQ90Kfg7RYm%2FDpoLc8LTJLoa3NvEoXwfAVBILnmEZpRYqHVeuq6%2FlOw4bOcN8k7uKsqeostM9rMVr2EFCzOmO2YugaTucBxZ%2Bh4ADVduV2hi32xo9Ul6G2J5tSqc0HoqSLict5EJ9hQ66uEaYA2oGypsOxctWzIV%2BWLVivWF0va73u5%2BA21LQAkgDvC5ldf%2FaYJaBrFYKu9ea%2F0RArvO3Z5ZZggp%2FkX17BgrXsbnMM%2BSwGR3dEvtWjzV8u7b6JzM9On1U%2FiTkWQ5eSAyBAz2fDQ9v24v%2FKAsG%2BIfJx3FTw%2BN9EekxoP40mJp9DIViIkMhIsZ%2BdGkMAYPqRyZfwjVV4k2wG3GtLouqoQWzdddisuoyk0waAZ22HkZVMTwtjHrDcSXI6e8gVrrPD7gZ3eT7Vus%2FYstcJ1zZkuVndAGmFsOPfw04rLCrRBTFaz%2BHWZiFRzksSX8TBXHTLN8o8LZKWa5bZJpWnuE%2Bnuxp2OS1p5MOKV5csGOqUBrl9h%2Fn7CZ8Ejt0BO6MltS1ePFrqjCCMhMpaA0N%2FsE8kPer3ji3K5y%2FujQIINs5qV3XWuEkxfW7NwxkU8oAoN8Pn0bih4a99OUmJ0xoIHEa8uwTtSrBHT%2BnUObtJVaiYsp%2Bsw%2BwTfqqwi3%2FbIb0D6RQplDT%2FEbTjXXowGMShJbTOSiH3jq3WgD2ENNUDsH%2Ftmx04mK8KJ2FOVniON7HgTe4uvkISV&X-Amz-Signature=5bffd8ff684b73d0d1c3918e13419bbbd9ab13c2f25b6b883abc5ed709860606&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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




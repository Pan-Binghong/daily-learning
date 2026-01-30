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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VW3REKN%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCX3kaKrN2p23k7mzal%2BwwflT%2FoXZc6pY%2FiscvK5ZOlqgIhALAIAd2G3IAvwmbF5eST1V1%2FYT3Bt%2BhmObrSTFa8BcTHKogECJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwgh0F6p0PbkXy%2BPDIq3AP10srxhXLAwRWFVga7slduIuafNH%2Fy%2BWzedWfwvBSuXUSwyCMFmREAPR%2FGJy0xknYdEUfPHMD85RexFtuEhtKEbWQh7tYFv%2BvXtwF6GZkOcIghdm6GZYVX6S8B01%2BLpBB5FCeYrdBMIKamHS6W3DGp2V%2FBPppcFPcsqHHl8Op6EPrwXjZfo0jWmzZUZr%2BkPaHqeKOebIE8tkHiQl5YGxd18c4t3gRR38U0x0G4SiLHIPVrabltYI%2FfuTXHAoljFhIE1fgO27eGErNhtYTrEPBOxG3ePwoQZac3lpdCMxQHniAjrLv8upQo9qP6AShFh4Zpnw5NJuxBA4MkMUb3HVzEZYPv4tpoM4UyC9IBqRkCXP8JgsRG8CUJi%2FA0I9cpyKCtgdOBbh4KfHOvXLtyLBCEjnKoic5%2F0yzD0mwxSbrvemzCxljU%2FbnqVVNjOEYoTSyICzH3wnONuUpEc9BA0HsyOKzvB5CeqkMDr1mJpZQMGVYPcgDehz9C7zpbOVDh%2Ftyz%2BThXul8KE%2FVBA6%2Bc8KKD8LoqcXEnN2B6UbCPMQaSjFJlaL2%2F2sclkqLb7MHEV7FHS9l%2FiUvbyLEVAzPhUtpUQPGnhaLooMouGdvPPrOCDUTTt%2FFYOq7OZnpdETDGyPDLBjqkAX5PYMEFVRIFL8Wu14SDMlYadqgZYUQB6b%2BIdTV6CdSpCxy95qejZy51A1jweF2ovq4fNsoG5woeTMtHN%2B1VUkVt9W1T2uemQItbKMwqvb0Mcwx6lm8P8i8S16nbWEp1I60tO0NSS%2BKzyOqtKrKFc3id3ne7bd6YmCBsaFq3LLEsQXCFJqZCoeqXXXdZcjqXfUM3cojuvKdOh904ImQlP7S2EL%2BW&X-Amz-Signature=c0ea29e21ddf713f58ea15007a08948c2d51aa48a4a5ead805b4c2bdd46b63ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



